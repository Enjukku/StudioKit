"""Audit a Roblox stage's structure from a Studio probe: floating, buried, out-of-bounds parts,
per-zone counts and the ambience map against the place. Measures and lists; never invents a budget.

Kit tool: universal (Studio Kit). Python 3.11+ standard library only; runs offline and in the gate.
Two parts:
  1. tools/env/scene_probe.luau, a read-only Luau probe the agent runs through Studio MCP
     execute_luau (Edit). It prints one JSON document ("SCENE_PROBE k/n <slice>" lines).
     `python tools/env/scene_audit.py probe ...` prints the probe source with its config filled in.
  2. The pure checks below read that JSON (and the stage's ambience map) and write audit JSON + Markdown.

Sources:
  - knowledge/reference/environment/03-pipeline-performance-review.md: RC10 contact and placement
    (:229), H11/RP07 scene report, unknown fields reported as unknown (:61, :278), RA03 no PASS
    without a contract or measurement (:214), RP06 observe-change-verify (:277).
  - templates/environment/ambience-map.md: §B "- zone: <id>", §C "- id: <id>" + "kind:" in yaml blocks.
  - fact-check-lighting.md LF10, LF31 (light classes; no documented light-count limit);
    fact-check-audio.md AU01-AU03 (AudioEmitter, AudioPlayer, legacy Sound).
  - Every Roblox API the probe uses is cited in scene_probe.luau's header with mirror file:line.

Verdicts: MEASURED unless the caller passes a tolerance or budget (CLI flags or --budgets JSON);
then PASS / FAIL, or UNVERIFIED when a needed field is unknown (RA03). map_vs_place is a contract
check: any mismatch or duplicate is FAIL without a tolerance. Lead decisions 2026-10-21 (J008-T08b):
several zone volumes may share one ZoneId (the zone is the union of their boxes; the id is matched
once against the map; duplicate AmbienceId anchors stay FAIL); audio with no AmbienceId outside the
stage root (probe scope Lighting / SoundService) is listed as global_audio, MEASURED, never FAIL,
while audio with no AmbienceId under the root (or with no scope recorded) is an unlisted source, FAIL. Triangles are UNKNOWN: the API mirror
documents no MeshPart triangle count. Never invent a tolerance (no source gives stage budgets for phones).

Method limits (also written into the audit):
  - floating: ray down from the part's centre; a part whose bounding box touches another part's box
    counts as supported. A part resting on a rotated neighbour's box may be missed; the lowest part of
    a stack with nothing under it (a baseplate over the void) is listed.
  - buried: first terrain surface met by a ray from above at the part's centre (caves and overhangs
    above a part read as buried), plus enclosure: all 8 corners of the part inside one opaque part's
    box (bounding-box estimate; wrong for spheres, cylinders, meshes and unions as enclosers).
  - zones: a part or object counts once in every zone whose boxes (one or more volumes per ZoneId)
    contain its centre / position.

Usage:
  python tools/env/scene_audit.py probe --root Workspace/Stages/Falls [--ray-length 5000] \
      [--chunk-size 60000 --chunk 1]
  python tools/env/scene_audit.py audit --probe probe.txt [probe2.txt ...] \
      --map content/stages/<stage>/ambience-map.md --budgets budgets.json \
      --floating-tol 0.05 --buried-tol 0.1 --oob-tol 0 --out content/stages/<stage>/review/audit.json

budgets.json (every key optional; a missing key means MEASURED):
  {"floating_tolerance": 0.05, "buried_tolerance": 0.1, "out_of_bounds_tolerance": 0,
   "zones": {"*": {"lights_with_shadows": 2}, "Z-FALLS": {"parts": 800}}, "unzoned": {"parts": 0}}
"""

from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROBE_FILE = HERE / "scene_probe.luau"
# Geometric epsilon (studs), same as the probe: float32 spacing is <= 0.002 studs up to 16,384 studs
# from the origin, so 0.01 absorbs rounding but no gap a player can see. Not a tolerance.
EPS = 0.01
NO_HIT = "NO_HIT"
UNKNOWN = "UNKNOWN"
BUDGET_KEYS = ("parts", "mesh_parts", "lights", "lights_with_shadows", "cast_shadow_parts",
               "audio_sources", "particle_emitters", "triangles")
# which unknown field leaves a budgeted count unproven
UNKNOWN_FIELD = {"cast_shadow_parts": "cast_shadow", "lights_with_shadows": "shadows"}
CHUNK_RE = re.compile(r"SCENE_PROBE (\d+)/(\d+) (.*)$")
ROOT_RE = re.compile(r"[A-Za-z0-9_ ./-]+")


# ---------------------------------------------------------------- probe source and output

def probe_source(root: str = "Workspace", ray_length: float = 5000, chunk_size: int = 0, chunk: int = 0) -> str:
    """The Luau probe with its config lines set. root is a '/' path from game, e.g. Workspace/Stages/Falls."""
    if not ROOT_RE.fullmatch(root):
        raise ValueError(f"root path has characters the probe config cannot hold: {root!r}")
    if ray_length <= 0 or chunk_size < 0 or chunk < 0:
        raise ValueError("ray_length > 0, chunk_size >= 0, chunk >= 0")
    src = PROBE_FILE.read_text(encoding="utf-8")
    for name, value in (("ROOT_PATH", f'"{root}"'), ("RAY_LENGTH", repr(ray_length)),
                        ("CHUNK_SIZE", str(chunk_size)), ("CHUNK_INDEX", str(chunk))):
        src, n = re.subn(rf"^local {name} = .*$", f"local {name} = {value}", src, count=1, flags=re.M)
        if n != 1:
            raise RuntimeError(f"config line {name} missing in {PROBE_FILE}")
    return src


def load_probe(texts: list[str]) -> dict:
    """Join SCENE_PROBE slices from one or more captured outputs (any order, repeats allowed),
    or read a plain JSON document."""
    slices: dict[int, str] = {}
    total = None
    for text in texts:
        for line in text.splitlines():
            m = CHUNK_RE.search(line)
            if not m:
                continue
            k, n, body = int(m.group(1)), int(m.group(2)), m.group(3)
            if total not in (None, n) or (k in slices and slices[k] != body):
                raise ValueError("probe slices come from different runs")
            total, slices[k] = n, body
    if total is None:
        doc = json.loads("\n".join(texts))
    else:
        missing = [k for k in range(1, total + 1) if k not in slices]
        if missing:
            raise ValueError(f"probe slices missing: {missing} of {total}")
        doc = json.loads("".join(slices[k] for k in range(1, total + 1)))
    if not isinstance(doc, dict):
        raise ValueError("probe output is not a JSON object")
    if "error" in doc:
        raise ValueError(f"probe error: {doc['error']}")
    return doc


def parse_ambience_map(text: str) -> dict:
    """Zone ids from §B and source ids + kind from §C (yaml code blocks), in file order."""
    zones: list[str] = []
    sources: list[dict] = []
    section, fence, is_yaml, cur = "", False, False, None
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:4]
        stripped = line.strip()
        if stripped.startswith("```"):
            fence, is_yaml = (False, False) if fence else (True, stripped.startswith("```yaml"))
            cur = None
            continue
        if not (fence and is_yaml):
            continue
        if section == "B" and (m := re.match(r"- zone:\s*([^\s#]+)", line)):
            zones.append(m.group(1).strip("'\""))
        elif section == "C":
            if m := re.match(r"- id:\s*([^\s#]+)", line):
                cur = {"id": m.group(1).strip("'\""), "kind": None}
                sources.append(cur)
            elif cur is not None and (m := re.match(r"  kind:\s*([^#]*)", line)):
                cur["kind"] = m.group(1).strip().strip("'\"") or None
    return {"zones": zones, "sources": sources}


# ---------------------------------------------------------------- geometry (CFrame = x,y,z,R00..R22)

def _frame(rec: dict):
    cf, size = rec.get("cf"), rec.get("size")
    if not (isinstance(cf, list) and len(cf) == 12 and isinstance(size, list) and len(size) == 3):
        return None
    return cf[:3], [cf[3:6], cf[6:9], cf[9:12]], size


def half_extents(rot, size) -> list[float]:
    """Half sizes of the world axis-aligned box around a rotated box."""
    return [sum(abs(rot[i][j]) * size[j] / 2 for j in range(3)) for i in range(3)]


def corners(pos, rot, size) -> list[list[float]]:
    out = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            for sz in (-1, 1):
                local = (sx * size[0] / 2, sy * size[1] / 2, sz * size[2] / 2)
                out.append([pos[i] + sum(rot[i][j] * local[j] for j in range(3)) for i in range(3)])
    return out


def distance_outside(box, point) -> float:
    """0 inside the box (pos, rot, size), else the distance from the point to the box."""
    pos, rot, size = box
    d = [point[i] - pos[i] for i in range(3)]
    local = [sum(rot[i][j] * d[i] for i in range(3)) for j in range(3)]
    return math.sqrt(sum(max(0.0, abs(local[j]) - size[j] / 2) ** 2 for j in range(3)))


# ---------------------------------------------------------------- checks

def judge(values: list[float | None], tol: float | None, unknown: int = 0) -> str:
    """values: listed measurements (None = no hit, always over). MEASURED without a tolerance."""
    if tol is None:
        return "MEASURED"
    if any(v is None or v > tol for v in values):
        return "FAIL"
    return "UNVERIFIED" if unknown else "PASS"


def _unknown(rec: dict, *keys: str) -> list[str]:
    return [k for k in keys if rec.get(k) is None]


def check_floating(parts: list[dict], tol: float | None = None) -> dict:
    listed, unknown, skipped = [], [], 0
    for p in parts:
        miss = _unknown(p, "anchored", "transparency")
        if not miss and (not p["anchored"] or p["transparency"] >= 1):
            skipped += 1
            continue
        frame = _frame(p)
        miss += _unknown(p, "contacts", "down_hit") + ([] if frame else ["cf/size"])
        if p.get("down_hit") not in (None, NO_HIT) and p.get("down_dist") is None:
            miss.append("down_dist")
        if miss:
            unknown.append({"path": p.get("path"), "unknown": miss})
            continue
        if p["contacts"] > 0:
            continue
        gap = None if p["down_hit"] == NO_HIT else p["down_dist"] - half_extents(frame[1], frame[2])[1]
        if gap is None or gap > EPS:
            listed.append({"path": p["path"], "gap": NO_HIT if gap is None else round(gap, 4),
                           "over_tolerance": None if tol is None else (gap is None or gap > tol)})
    return {"tolerance": tol, "listed": listed, "unknown": unknown, "skipped_unanchored_or_invisible": skipped,
            "verdict": judge([None if i["gap"] == NO_HIT else i["gap"] for i in listed], tol, len(unknown)),
            "method": "ray down from the centre, gap = hit distance - world half-height; parts whose "
                      "bounding box touches another part count as supported (bounding-box estimate)"}


def check_buried(parts: list[dict], tol: float | None = None) -> dict:
    listed, unknown = [], []
    for p in parts:
        if p.get("transparency") is None:
            unknown.append({"path": p.get("path"), "unknown": ["transparency"]})
            continue
        if p["transparency"] >= 1:
            continue
        frame = _frame(p)
        if p.get("enclosed_by"):
            listed.append({"path": p["path"], "method": "enclosed_box", "enclosed_by": p["enclosed_by"],
                           "over_tolerance": None if tol is None else True})
            continue
        ty = p.get("terrain_y")
        if ty is None or frame is None:
            unknown.append({"path": p.get("path"), "unknown": ["terrain_y" if ty is None else "cf/size"]})
            continue
        if ty == NO_HIT:
            continue
        depth = ty - (frame[0][1] + half_extents(frame[1], frame[2])[1])
        if depth > EPS:
            listed.append({"path": p["path"], "method": "terrain_ray", "depth": round(depth, 4),
                           "over_tolerance": None if tol is None else depth > tol})
    values = [math.inf if i["method"] == "enclosed_box" else i["depth"] for i in listed]
    return {"tolerance": tol, "listed": listed, "unknown": unknown, "verdict": judge(values, tol, len(unknown)),
            "method": "terrain_ray: top of the part's world bounding box below the first terrain surface hit "
                      "from above at its centre (caves and overhangs read as buried); enclosed_box: all 8 "
                      "corners inside one opaque part's box (bounding-box estimate). Enclosed parts fail any tolerance."}


def check_out_of_bounds(parts: list[dict], areas: list[dict], tol: float | None = None) -> dict:
    boxes = [f for f in (_frame(a) for a in areas) if f]
    if not boxes:
        return {"verdict": "NOT_CHECKED", "reason": "no BasePart tagged PlayArea in the stage"}
    listed, unknown = [], []
    for p in parts:
        frame = _frame(p)
        if frame is None:
            unknown.append({"path": p.get("path"), "unknown": ["cf/size"]})
            continue
        over = max(min(distance_outside(b, c) for b in boxes) for c in corners(*frame))
        if over > EPS:
            listed.append({"path": p["path"], "overshoot": round(over, 4),
                           "over_tolerance": None if tol is None else over > tol})
    return {"tolerance": tol, "play_areas": [a.get("path") for a in areas], "listed": listed, "unknown": unknown,
            "verdict": judge([i["overshoot"] for i in listed], tol, len(unknown)),
            "method": "largest distance of any part corner outside the union of PlayArea boxes"}


def _empty_counts() -> dict:
    return {"parts": 0, "mesh_parts": 0, "lights": 0, "lights_by_class": Counter(), "lights_with_shadows": 0,
            "cast_shadow_parts": 0, "audio_sources": 0, "audio_by_class": Counter(), "particle_emitters": 0,
            "effects_by_class": Counter(), "triangles": UNKNOWN, "unknown": Counter()}


def _add(c: dict, rec: dict, kind: str) -> None:
    cls = rec.get("class")
    if kind == "part":
        c["parts"] += 1
        c["mesh_parts"] += cls == "MeshPart"
        if rec.get("cast_shadow") is None:
            c["unknown"]["cast_shadow"] += 1
        c["cast_shadow_parts"] += rec.get("cast_shadow") is True
    elif kind == "light":
        c["lights"] += 1
        c["lights_by_class"][cls] += 1
        if rec.get("shadows") is None:
            c["unknown"]["shadows"] += 1
        c["lights_with_shadows"] += rec.get("shadows") is True
    elif kind == "audio":
        c["audio_sources"] += 1
        c["audio_by_class"][cls] += 1
    elif kind == "effect":
        c["effects_by_class"][cls] += 1
        c["particle_emitters"] += cls == "ParticleEmitter"


def _judge_counts(c: dict, budget: dict) -> dict:
    verdicts = {}
    for key, limit in budget.items():
        value = c[key]
        if value == UNKNOWN:
            verdicts[key] = "UNVERIFIED"
        elif value > limit:
            verdicts[key] = "FAIL"
        else:
            verdicts[key] = "UNVERIFIED" if c["unknown"].get(UNKNOWN_FIELD.get(key, ""), 0) else "PASS"
    return verdicts


def zone_counts(probe: dict, budgets: dict | None = None) -> dict:
    budgets = budgets or {}
    zone_boxes = []
    for z in probe.get("zones", []):
        frame = _frame(z)
        if frame:
            zone_boxes.append((z.get("zone_id") or z.get("path"), frame))
    buckets: dict[str, dict] = {key: _empty_counts() for key, _ in zone_boxes}
    buckets["unzoned"] = _empty_counts()
    buckets["unpositioned"] = _empty_counts()
    multi = 0
    items = [(p, "part", (_frame(p) or [None])[0]) for p in probe.get("parts", [])]
    items += [(o, o.get("kind"), o.get("pos") if o.get("positioned") else None) for o in probe.get("objects", [])]
    for rec, kind, point in items:
        if point is None:
            keys = ["unpositioned"]
        else:
            keys = sorted({k for k, box in zone_boxes if distance_outside(box, point) <= EPS}) or ["unzoned"]
            multi += len(keys) > 1
        for k in keys:
            _add(buckets[k], rec, kind)
    out = {}
    for name, c in buckets.items():
        if name in ("unzoned", "unpositioned"):
            budget = dict(budgets.get(name, {}))
        else:
            budget = {**budgets.get("zones", {}).get("*", {}), **budgets.get("zones", {}).get(name, {})}
        verdicts = _judge_counts(c, budget)
        c = {k: dict(v) if isinstance(v, Counter) else v for k, v in c.items()}
        c["budget"] = budget
        c["verdicts"] = verdicts
        c["verdict"] = _worst(verdicts.values()) if verdicts else "MEASURED"
        out[name] = c
    return {"zones": out, "items_in_multiple_zones": multi,
            "triangles_note": "UNKNOWN: the API mirror documents no MeshPart triangle count",
            "verdict": _worst(z["verdict"] for z in out.values())}


def _dupes(values: list[str]) -> list[str]:
    return sorted(v for v, n in Counter(values).items() if n > 1)


def _global(obj: dict) -> bool:
    """Audio found outside the stage root (probe scope Lighting or SoundService)."""
    return isinstance(obj.get("scope"), str) and obj["scope"] != "stage"


def map_vs_place(probe: dict, amap: dict | None) -> dict:
    if amap is None:
        return {"verdict": "NOT_CHECKED", "reason": "no ambience map given (--map)"}
    zones = probe.get("zones", [])
    place_zones = [z["zone_id"] for z in zones if z.get("zone_id")]
    place_sources = [a["ambience_id"] for a in probe.get("anchors", []) if a.get("ambience_id")]
    map_zones, map_sources = amap["zones"], [s["id"] for s in amap["sources"]]
    objects = probe.get("objects", [])
    audio_ids = {o.get("anchor_id") for o in objects if o.get("kind") == "audio"}
    effect_ids = {o.get("anchor_id") for o in objects if o.get("kind") == "effect"}
    unanchored = [o for o in objects if o.get("kind") == "audio" and not o.get("anchor_id")]
    kind_mismatch = []
    seen = set(place_sources)
    for s in amap["sources"]:
        kinds = set(re.split(r"[+\s,/]+", (s["kind"] or "").lower()))
        if s["id"] not in seen:
            continue
        if "sound" in kinds and s["id"] not in audio_ids:
            kind_mismatch.append({"id": s["id"], "kind": s["kind"], "missing": "audio object at or under the anchor"})
        if "effect" in kinds and s["id"] not in effect_ids:
            kind_mismatch.append({"id": s["id"], "kind": s["kind"], "missing": "effect object at or under the anchor"})
    r = {
        "map_zones_missing_in_place": sorted(set(map_zones) - set(place_zones)),
        "place_zones_missing_in_map": sorted(set(place_zones) - set(map_zones)),
        "zone_volumes_without_zone_id": [z.get("path") for z in zones if not z.get("zone_id")],
        "map_sources_missing_in_place": sorted(set(map_sources) - set(place_sources)),
        "place_sources_missing_in_map": sorted(set(place_sources) - set(map_sources)),
        "unlisted_audio": [o.get("path") for o in unanchored if not _global(o)],
        "global_audio": {"listed": [o.get("path") for o in unanchored if _global(o)], "verdict": "MEASURED"},
        "kind_mismatch": kind_mismatch,
        "duplicates": {"map_zone_ids": _dupes(map_zones), "map_source_ids": _dupes(map_sources),
                       "place_source_ids": _dupes(place_sources)},  # place zone ids may repeat (multi-volume zones)
    }
    bad = any(v for k, v in r.items() if k not in ("duplicates", "global_audio")) or any(r["duplicates"].values())
    r["verdict"] = "FAIL" if bad else "PASS"
    return r


ORDER = ("FAIL", "UNVERIFIED", "MEASURED", "PASS")


def _worst(verdicts) -> str:
    vs = [v for v in verdicts if v in ORDER]
    return min(vs, key=ORDER.index) if vs else "MEASURED"


def audit(probe: dict, amap: dict | None = None, budgets: dict | None = None,
          floating_tol: float | None = None, buried_tol: float | None = None, oob_tol: float | None = None) -> dict:
    budgets = budgets or {}
    unknown_keys = set(budgets) - {"floating_tolerance", "buried_tolerance", "out_of_bounds_tolerance", "zones", "unzoned", "unpositioned"}
    for b in [*budgets.get("zones", {}).values(), budgets.get("unzoned", {}), budgets.get("unpositioned", {})]:
        unknown_keys |= set(b) - set(BUDGET_KEYS)
    if unknown_keys:
        raise ValueError(f"unknown budget keys: {sorted(unknown_keys)} (allowed counts: {BUDGET_KEYS})")
    pick = lambda flag, key: flag if flag is not None else budgets.get(key)  # noqa: E731
    parts = probe.get("parts", [])
    report = {
        "probe": {k: probe.get(k) for k in ("probe", "version", "root", "ray_length", "eps")},
        "floating": check_floating(parts, pick(floating_tol, "floating_tolerance")),
        "buried": check_buried(parts, pick(buried_tol, "buried_tolerance")),
        "out_of_bounds": check_out_of_bounds(parts, probe.get("play_areas", []), pick(oob_tol, "out_of_bounds_tolerance")),
        "per_zone_counts": zone_counts(probe, budgets),
        "triangles": UNKNOWN,
        "map_vs_place": map_vs_place(probe, amap),
    }
    report["verdict"] = _worst(report[k]["verdict"] for k in ("floating", "buried", "out_of_bounds", "per_zone_counts", "map_vs_place"))
    return report


def to_markdown(report: dict) -> str:
    root = report["probe"].get("root") or UNKNOWN
    lines = [f"# Scene audit: {root}", "", f"Overall: **{report['verdict']}** (structure only; not a visual or listening review)", "",
             "| Check | Verdict | Listed | Unknown |", "| --- | --- | --- | --- |"]
    for k in ("floating", "buried", "out_of_bounds"):
        r = report[k]
        lines.append(f"| {k} | {r['verdict']} | {len(r.get('listed', []))} | {len(r.get('unknown', []))} |")
    m = report["map_vs_place"]
    n = sum(len(v) for k, v in m.items() if isinstance(v, list)) + sum(len(v) for v in m.get("duplicates", {}).values())
    g = len(m.get("global_audio", {}).get("listed", []))
    lines += [f"| map_vs_place | {m['verdict']} | {n} | - |", f"| global_audio | MEASURED | {g} | - |", "| triangles | UNKNOWN | - | - |", "",
              "| Zone | Parts | MeshParts | Lights | Shadow lights | CastShadow parts | Audio | Particles | Triangles | Verdict |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for name, c in report["per_zone_counts"]["zones"].items():
        lines.append(f"| {name} | {c['parts']} | {c['mesh_parts']} | {c['lights']} | {c['lights_with_shadows']} | "
                     f"{c['cast_shadow_parts']} | {c['audio_sources']} | {c['particle_emitters']} | {c['triangles']} | {c['verdict']} |")
    lines += ["", "Full lists, methods and limits: the JSON next to this file."]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- CLI

def main(argv: list[str]) -> int:
    import argparse  # noqa: PLC0415

    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("probe", help="print the Luau probe source for execute_luau")
    pr.add_argument("--root", default="Workspace", help="'/' path from game, e.g. Workspace/Stages/Falls")
    pr.add_argument("--ray-length", type=float, default=5000, help="search distance in studs (not a threshold)")
    pr.add_argument("--chunk-size", type=int, default=0, help="characters per printed slice; 0 = one slice")
    pr.add_argument("--chunk", type=int, default=0, help="print only slice k (1-based); 0 = all")
    au = sub.add_parser("audit", help="audit saved probe output")
    au.add_argument("--probe", nargs="+", required=True, help="file(s) holding the probe output")
    au.add_argument("--map", help="the stage's ambience-map.md")
    au.add_argument("--budgets", help="JSON budgets and tolerances from the approved stage contract")
    au.add_argument("--floating-tol", type=float, help="max gap under a part, studs")
    au.add_argument("--buried-tol", type=float, help="max depth below terrain, studs")
    au.add_argument("--oob-tol", type=float, help="max overshoot outside PlayArea, studs")
    au.add_argument("--out", required=True, help="audit JSON path; Markdown is written beside it (.md)")
    a = p.parse_args(argv)
    if a.cmd == "probe":
        sys.stdout.write(probe_source(a.root, a.ray_length, a.chunk_size, a.chunk))
        return 0
    probe = load_probe([Path(f).read_text(encoding="utf-8") for f in a.probe])
    amap = parse_ambience_map(Path(a.map).read_text(encoding="utf-8")) if a.map else None
    budgets = json.loads(Path(a.budgets).read_text(encoding="utf-8")) if a.budgets else None
    report = audit(probe, amap, budgets, a.floating_tol, a.buried_tol, a.oob_tol)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    out.with_suffix(".md").write_text(to_markdown(report), encoding="utf-8")
    print(f"RESULT: {report['verdict']} -> {out}")
    return 1 if report["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
