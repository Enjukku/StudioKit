"""VFX texture library catalog: see a library of Roblox image IDs, tag it by eye, pick the best texture per layer.

Source list: the VFX Studio plugin's public library (github.com/Sytranom/VFXStudio, VFXData.json), shape
{"<assetId>": {"Name": str, "Keywords": [group, ...], "Grid"?: 2|4|8, "Resolution"?: int, "Credits"?: str}}.
Method: knowledge/design/vfx-workflow-proposal.md section 4b. Images live in output/vfx/library/ (git-ignored);
the tagged catalog is content/vfx/library/catalog.json.

  python tools/vfx/vfxlib_catalog.py fetch       # list + 150 px thumbnails (resumable)
  python tools/vfx/vfxlib_catalog.py features    # dead / duplicate / coverage / hardness / colour per thumbnail
  python tools/vfx/vfxlib_catalog.py sheets      # numbered sheets of 48 per group + sheets.json manifest
  python tools/vfx/vfxlib_catalog.py flipsheets  # 4x4/8x8 flipbooks: 420 px, 4 frames per cell (FB_###.jpg)
  python tools/vfx/vfxlib_catalog.py merge       # tags/*.json + features -> content/vfx/library/catalog.json
  python tools/vfx/vfxlib_catalog.py shortlist --group Flare --style anime --shape star --min-quality B --n 16

Pure helpers (codes, hashes, dedupe, merge, filter) need only the standard library; PIL is imported where images are read.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import io
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "output" / "vfx" / "library"
CATALOG = ROOT / "content" / "vfx" / "library" / "catalog.json"
DATA_URL = "https://raw.githubusercontent.com/Sytranom/VFXStudio/refs/heads/main/VFXData.json"
THUMB_API = "https://thumbnails.roblox.com/v1/assets?assetIds=%s&size=150x150&format=Png&isCircular=false"
CELL, COLS, PER_SHEET = 150, 8, 48

# Two-letter code prefix per library group; tag files and sheets use codes like "FL-0042".
GROUP_PREFIX = {
    "Form": "FO", "Flare": "FL", "Other": "OT", "Impact": "IM", "Beam": "BE", "Circle": "CI", "Smoke": "SM",
    "Slashes": "SL", "Text": "TX", "Spec": "SP", "Lightning": "LI", "Fire": "FI", "Swirl": "SW", "Energy": "EN",
    "Grid": "GR", "Ground": "GD", "Water": "WA", "Star": "ST",
}
STYLES = ("anime", "soft", "realistic", "pixel", "other")
QUALITY_RANK = {"A": 3, "B": 2, "C": 1}


# ---------- pure helpers ----------
def primary_group(entry: dict) -> str:
    kws = entry.get("Keywords") or ["Other"]
    return kws[0] if kws[0] in GROUP_PREFIX else "Other"


def assign_codes(data: dict) -> dict:
    """Stable codes: per group, asset IDs sorted numerically, numbered from 1. Returns {assetId: code}."""
    by_group: dict[str, list[str]] = {}
    for aid, entry in data.items():
        by_group.setdefault(primary_group(entry), []).append(aid)
    codes = {}
    for group, ids in by_group.items():
        for n, aid in enumerate(sorted(ids, key=int), 1):
            codes[aid] = "%s-%04d" % (GROUP_PREFIX[group], n)
    return codes


def dhash_bits(gray: list[list[int]]) -> int:
    """Difference hash of a 9x8 grayscale grid (rows of 9 ints): 64 bits."""
    bits = 0
    for row in gray:
        for x in range(8):
            bits = (bits << 1) | (1 if row[x] > row[x + 1] else 0)
    return bits


def hamming(a: int, b: int) -> int:
    return bin(a ^ b).count("1")


def visible_diff(a: bytes, b: bytes, floor: int = 25) -> float:
    """Mean abs difference over pixels visible in either image. A plain mean is diluted by black
    background: faint different sparkles scored as duplicates (2026-10-16 calibration, 32 labelled pairs:
    threshold 8 caught 14/20 true pairs and 0/12 false ones)."""
    idx = [i for i in range(min(len(a), len(b))) if a[i] > floor or b[i] > floor]
    return sum(abs(a[i] - b[i]) for i in idx) / len(idx) if idx else 0.0


def find_duplicates(items: list[tuple[str, int, int]], max_dist: int = 3, confirm=None) -> dict:
    """items: (code, hash, grid) in keep-first order. Same grid + hash within max_dist makes a candidate;
    confirm(code, kept_code) -> bool, when given, must also agree (the 64-bit hash alone is too coarse:
    2026-10-16 sample, about half the hash matches were different sparkles). Returns {dup_code: kept_code}.
    Blank images (hash 0) are never matched."""
    kept: list[tuple[str, int, int]] = []
    dups = {}
    for code, h, grid in items:
        if h == 0:
            kept.append((code, h, grid))
            continue
        match = next((k for k, kh, kg in kept if kg == grid and kh != 0 and hamming(h, kh) <= max_dist
                      and (confirm is None or confirm(code, k))), None)
        if match:
            dups[code] = match
        else:
            kept.append((code, h, grid))
    return dups


def merge_rows(data: dict, codes: dict, features: dict, tags: dict) -> list[dict]:
    """One catalog row per live, non-duplicate asset. features/tags are keyed by code."""
    rows = []
    for aid, entry in data.items():
        code = codes[aid]
        f = features.get(code, {})
        if f.get("dead") or f.get("dup_of"):
            continue
        t = tags.get(code, {})
        row = {
            "code": code, "id": int(aid), "group": primary_group(entry), "keywords": entry.get("Keywords", []),
            "grid": entry.get("Grid", 1), "name": entry.get("Name", ""),
            "style": t.get("style", ""), "shape": t.get("shape", ""), "quality": t.get("quality", ""),
            "note": t.get("note", ""),
            "coverage": f.get("coverage"), "hardness": f.get("hardness"), "saturation": f.get("saturation"),
        }
        if entry.get("Credits"):
            row["credits"] = entry["Credits"]
        # keep the file small (~8k rows): drop fields that carry nothing
        if row["keywords"] == [row["group"]]:
            del row["keywords"]
        if row["name"].split("/")[-1].isdigit() or row["name"].startswith("Images/Untitled"):
            del row["name"]
        rows.append(row)
    rows.sort(key=lambda r: r["code"])
    return rows


def filter_rows(rows: list[dict], group=None, style=None, shape=None, min_quality=None, grid=None) -> list[dict]:
    """Shortlist filter; best first (quality, then hardness for anime picks)."""
    out = []
    for r in rows:
        if group and r["group"] != group and group not in r.get("keywords", ()):
            continue
        if style and r["style"] != style:
            continue
        if shape and shape.lower() not in (r["shape"] + " " + r["note"]).lower():
            continue
        if min_quality and QUALITY_RANK.get(r["quality"], 0) < QUALITY_RANK[min_quality]:
            continue
        if grid is not None and r["grid"] != grid:
            continue
        out.append(r)
    out.sort(key=lambda r: (-QUALITY_RANK.get(r["quality"], 0), -(r["hardness"] or 0)))
    return out


def validate_tag(code: str, t: dict) -> list[str]:
    errs = []
    if t.get("style") not in STYLES:
        errs.append("%s: style %r not in %s" % (code, t.get("style"), STYLES))
    if t.get("quality") not in QUALITY_RANK:
        errs.append("%s: quality %r not A/B/C" % (code, t.get("quality")))
    if not t.get("shape"):
        errs.append("%s: empty shape" % code)
    return errs


# ---------- IO ----------
def _get(url: str, tries: int = 4) -> bytes:
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            return urllib.request.urlopen(req, timeout=30).read()
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(1.5 * (k + 1))
    return b""


def load_data() -> dict:
    return json.loads((WORK / "VFXData.json").read_text(encoding="utf-8"))


def _fetch_thumbs(ids: list[str], size: int, folder: Path, states: dict) -> int:
    """Roblox thumbnails for asset IDs into folder/<id>.png (skips files that exist). Updates states."""
    folder.mkdir(parents=True, exist_ok=True)
    todo = [a for a in ids if not (folder / ("%s.png" % a)).exists() and states.get(a) not in ("Blocked", "Error")]
    api = THUMB_API.replace("150x150", "%dx%d" % (size, size))
    urls = {}
    for i in range(0, len(todo), 100):
        batch = todo[i:i + 100]
        for _attempt in range(3):
            pending = []
            for e in json.loads(_get(api % ",".join(batch)))["data"]:
                aid = str(e["targetId"])
                states[aid] = e["state"]
                if e["state"] == "Completed" and e.get("imageUrl"):
                    urls[aid] = e["imageUrl"]
                elif e["state"] == "Pending":
                    pending.append(aid)
            if not pending:
                break
            batch = pending
            time.sleep(2)
        time.sleep(0.25)

    def dl(item):
        aid, url = item
        (folder / ("%s.png" % aid)).write_bytes(_get(url))

    with cf.ThreadPoolExecutor(8) as ex:
        list(ex.map(dl, urls.items()))
    return len(urls)


def cmd_fetch(_args) -> None:
    (WORK / "VFXData.json").write_bytes(_get(DATA_URL))
    data = load_data()
    states_path = WORK / "thumb_states.json"
    states = json.loads(states_path.read_text()) if states_path.exists() else {}
    n = _fetch_thumbs(list(data), 150, WORK / "thumbs", states)
    states_path.write_text(json.dumps(states))
    print("list", len(data), "downloaded", n, "states", {s: list(states.values()).count(s) for s in set(states.values())})


def flip_frames(grid: int, picks: int = 4) -> list[int]:
    """Evenly spaced frame indices across a grid x grid flipbook, first and last included."""
    total = grid * grid
    return [round(k * (total - 1) / (picks - 1)) for k in range(picks)]


def cmd_flipsheets(_args) -> None:
    """Flipbooks are unreadable on the 150 px sheets (2026-10-16 tagging pass graded them C as "tiny frames").
    Here: 420 px thumbnails, each cell shows 4 evenly spaced frames, 2x2, at 100 px each. Sheets FB_###.jpg."""
    from PIL import Image, ImageDraw, ImageOps
    data = load_data()
    codes = assign_codes(data)
    feats = json.loads((WORK / "features.json").read_text())
    ids = sorted((a for a in data if data[a].get("Grid", 1) > 2 and not feats[codes[a]]["dead"]
                  and not feats[codes[a]].get("dup_of")), key=lambda a: codes[a])
    states: dict = {}
    _fetch_thumbs(ids, 420, WORK / "thumbs420", states)
    ids = [a for a in ids if (WORK / "thumbs420" / ("%s.png" % a)).exists()]
    out = WORK / "sheets"
    fcell, cols, per = 100, 6, 30
    cell = fcell * 2
    manifest = []
    for s in range(0, len(ids), per):
        chunk = ids[s:s + per]
        rows = (len(chunk) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * (cell + 6), rows * (cell + 18)), (28, 28, 32))
        dr = ImageDraw.Draw(sheet)
        for k, aid in enumerate(chunk):
            x, y = (k % cols) * (cell + 6), (k // cols) * (cell + 18)
            im = Image.open(WORK / "thumbs420" / ("%s.png" % aid)).convert("RGBA").resize((420, 420))
            flat = Image.new("RGB", im.size, (0, 0, 0))
            flat.paste(im, mask=im.split()[3])
            if feats[codes[aid]].get("faint"):
                flat = ImageOps.autocontrast(flat)
            g = data[aid]["Grid"]
            fw = 420 / g
            for j, fr in enumerate(flip_frames(g)):
                fx, fy = (fr % g) * fw, (fr // g) * fw
                tile = flat.crop((round(fx), round(fy), round(fx + fw), round(fy + fw))).resize((fcell, fcell))
                sheet.paste(tile, (x + (j % 2) * fcell, y + (j // 2) * fcell))
            dr.text((x + 3, y + cell + 3), "%s  G%d  frames %s" % (codes[aid], g, ",".join(str(f + 1) for f in flip_frames(g))),
                    fill=(235, 235, 235))
        name = "FB_%03d.jpg" % (s // per + 1)
        sheet.save(out / name, quality=88)
        manifest.append({"sheet": "sheets/" + name, "group": "Flipbook", "codes": [codes[a] for a in chunk]})
    (WORK / "flipsheets.json").write_text(json.dumps(manifest, indent=0))
    print("flip sheets", len(manifest), "flipbooks", len(ids))


def _measure(path: Path) -> dict:
    from PIL import Image
    im = Image.open(path).convert("RGBA").resize((CELL, CELL))
    rgb = Image.new("RGB", im.size, (0, 0, 0))
    rgb.paste(im, mask=im.split()[3])  # composite on black, as an additive particle reads
    gray = rgb.convert("L")
    px = list(gray.tobytes())
    vis = [p for p in px if p > 25]
    small = list(gray.resize((9, 8)).tobytes())
    sats = rgb.convert("HSV").tobytes()[1::3]
    sat = [s for s, p in zip(sats, px) if p > 25]
    return {
        "coverage": round(len(vis) / len(px), 3),
        # share of visible pixels that are near full intensity: hard cel shapes score high, soft glows low
        "hardness": round(sum(1 for p in vis if p > 200) / len(vis), 3) if vis else 0.0,
        "saturation": round(sum(sat) / len(sat) / 255, 3) if sat else 0.0,
        "g32": rgb.convert("L").resize((32, 32)).tobytes().hex(),
        "hash": dhash_bits([small[r * 9:(r + 1) * 9] for r in range(8)]) if vis else 0,
        "placeholder": _is_placeholder(rgb),
        "peak": max(px),
    }


def _is_placeholder(rgb) -> bool:
    """Roblox 'no image' tile: a near-white square with a grey icon."""
    corner = [rgb.getpixel((x, y)) for x, y in ((2, 2), (CELL - 3, 2), (2, CELL - 3), (CELL - 3, CELL - 3))]
    return all(min(c) > 235 for c in corner)


def cmd_features(_args) -> None:
    data = load_data()
    codes = assign_codes(data)
    states = json.loads((WORK / "thumb_states.json").read_text())
    feats = {}
    paths = {aid: WORK / "thumbs" / ("%s.png" % aid) for aid in data}
    live = [aid for aid, p in paths.items() if p.exists()]
    with cf.ThreadPoolExecutor(8) as ex:
        measured = dict(zip(live, ex.map(lambda a: _measure(paths[a]), live)))
    for aid in data:
        m = measured.get(aid)
        # faint or dark-red textures are real (2026-10-16 check): only blocked, placeholder or fully black is dead
        dead = m is None or m["placeholder"] or m["peak"] == 0
        faint = m is not None and (m["peak"] < 128 or m["coverage"] < 0.002)
        feats[codes[aid]] = {"id": aid, "state": states.get(aid, "missing"), "dead": dead, "faint": faint, **(m or {})}
    order = sorted((c for c in feats if not feats[c]["dead"]), key=lambda c: (c[:2], c))
    grids = {codes[a]: data[a].get("Grid", 1) for a in data}
    g32 = {c: bytes.fromhex(feats[c]["g32"]) for c in order}

    def same(a: str, b: str) -> bool:  # near-identical at 32 px, colour ignored (Roblox tints anyway)
        return visible_diff(g32[a], g32[b]) <= 8

    for dup, kept in find_duplicates([(c, feats[c]["hash"], grids[c]) for c in order], confirm=same).items():
        feats[dup]["dup_of"] = kept
    for f in feats.values():
        f.pop("g32", None)
    (WORK / "features.json").write_text(json.dumps(feats))
    n_dead = sum(f["dead"] for f in feats.values())
    n_dup = sum(1 for f in feats.values() if f.get("dup_of"))
    print("total", len(feats), "dead", n_dead, "duplicates", n_dup, "live", len(feats) - n_dead - n_dup)


def cmd_sheets(_args) -> None:
    from PIL import Image, ImageDraw, ImageOps
    data = load_data()
    codes = assign_codes(data)
    feats = json.loads((WORK / "features.json").read_text())
    by_code = {c: a for a, c in codes.items()}
    live = sorted(c for c, f in feats.items() if not f["dead"] and not f.get("dup_of"))
    out = WORK / "sheets"
    out.mkdir(parents=True, exist_ok=True)
    manifest = []
    groups: dict[str, list[str]] = {}
    for c in live:
        groups.setdefault(c[:2], []).append(c)
    for prefix, cs in sorted(groups.items()):
        for s in range(0, len(cs), PER_SHEET):
            chunk = cs[s:s + PER_SHEET]
            rows = (len(chunk) + COLS - 1) // COLS
            sheet = Image.new("RGB", (COLS * CELL, rows * (CELL + 18)), (28, 28, 32))
            dr = ImageDraw.Draw(sheet)
            for k, c in enumerate(chunk):
                x, y = (k % COLS) * CELL, (k // COLS) * (CELL + 18)
                im = Image.open(WORK / "thumbs" / ("%s.png" % by_code[c])).convert("RGBA").resize((CELL, CELL))
                tile = Image.new("RGB", (CELL, CELL), (0, 0, 0))  # on black, as an additive particle reads
                tile.paste(im, mask=im.split()[3])
                if feats[c].get("faint"):
                    tile = ImageOps.autocontrast(tile)  # brightened so it can be judged; label marked *
                sheet.paste(tile, (x, y))
                grid = data[by_code[c]].get("Grid")
                label = c + ("*" if feats[c].get("faint") else "") + ("  G%d" % grid if grid else "")
                dr.text((x + 3, y + CELL + 3), label, fill=(235, 235, 235))
            name = "%s_%03d.jpg" % (prefix, s // PER_SHEET + 1)
            sheet.save(out / name, quality=88)
            manifest.append({"sheet": "sheets/" + name, "group": primary_group(data[by_code[chunk[0]]]), "codes": chunk})
    (WORK / "sheets.json").write_text(json.dumps(manifest, indent=0))
    print("sheets", len(manifest), "cells", len(live))


def load_tags() -> tuple[dict, list[str]]:
    tags, errs = {}, []
    for p in sorted((WORK / "tags").glob("*.json")):
        for code, t in json.loads(p.read_text(encoding="utf-8")).items():
            errs += validate_tag(code, t)
            tags[code] = t
    return tags, errs


def cmd_merge(_args) -> None:
    data = load_data()
    codes = assign_codes(data)
    feats = json.loads((WORK / "features.json").read_text())
    tags, errs = load_tags()
    rows = merge_rows(data, codes, feats, tags)
    untagged = [r["code"] for r in rows if not r["style"]]
    CATALOG.parent.mkdir(parents=True, exist_ok=True)
    body = ",\n".join(json.dumps(r, ensure_ascii=False) for r in rows)
    CATALOG.write_text('{"source": "%s",\n"rows": [\n%s\n]}\n' % (DATA_URL, body), encoding="utf-8")
    print("rows", len(rows), "tagged", len(rows) - len(untagged), "untagged", len(untagged), "tag errors", len(errs))
    for e in errs[:20]:
        print("  ", e)


def cmd_shortlist(a) -> None:
    from PIL import Image, ImageDraw
    rows = json.loads(CATALOG.read_text(encoding="utf-8"))["rows"]
    pick = filter_rows(rows, a.group, a.style, a.shape, a.min_quality, a.grid)[: a.n]
    if not pick:
        print("no match")
        return
    cols = min(COLS, len(pick))
    sheet = Image.new("RGB", (cols * CELL, ((len(pick) + cols - 1) // cols) * (CELL + 30)), (28, 28, 32))  # grey shows the cell edge
    dr = ImageDraw.Draw(sheet)
    for k, r in enumerate(pick):
        x, y = (k % cols) * CELL, (k // cols) * (CELL + 30)
        im = Image.open(WORK / "thumbs" / ("%d.png" % r["id"])).convert("RGBA").resize((CELL, CELL))
        sheet.paste(im, (x, y), im)
        dr.text((x + 3, y + CELL + 2), "%s %s %s" % (r["code"], r["quality"], r["style"]), fill=(235, 235, 235))
        dr.text((x + 3, y + CELL + 15), r["shape"][:24], fill=(170, 170, 170))
    out = Path(a.out) if a.out else WORK / "picks" / ("%s_%s.jpg" % (a.group or "all", a.shape or "any"))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=88)
    for r in pick:
        print(r["code"], "rbxassetid://%d" % r["id"], r["quality"], r["style"], r["shape"], "|", r["note"])
    print("sheet", out)


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("fetch", "features", "sheets", "flipsheets", "merge"):
        sub.add_parser(name)
    s = sub.add_parser("shortlist")
    s.add_argument("--group")
    s.add_argument("--style", choices=STYLES)
    s.add_argument("--shape")
    s.add_argument("--min-quality", choices=list(QUALITY_RANK))
    s.add_argument("--grid", type=int)
    s.add_argument("--n", type=int, default=16)
    s.add_argument("--out")
    a = ap.parse_args(argv)
    {"fetch": cmd_fetch, "features": cmd_features, "sheets": cmd_sheets, "flipsheets": cmd_flipsheets, "merge": cmd_merge, "shortlist": cmd_shortlist}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
