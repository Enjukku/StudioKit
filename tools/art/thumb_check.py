#!/usr/bin/env python3
"""Measure a Roblox game icon or Home thumbnail at the size players see it - without AI taste.

Kit tool (universal). A thin marketing wrapper over tools/art/look_check.py: it imports look_check's pure
functions (subject mask, WCAG luminance, components, resampling, records) and adds the Roblox surfaces, the
master-file checks the Roblox docs state, the "one clear moment" measures and one contact sheet.
Input: a PNG/JPG icon or thumbnail master (ChatGPT image, Figma export, render). Output: one JSON (stdout and
--out) plus one contact sheet PNG next to the input or in --out-dir. The input is never overwritten.

What it measures (the owner's three questions, J012 2026-10-21):
  master checks   icon: square, at least 512x512 (experience-icons.md:55). thumbnail: 16:9 (thumbnails.md:54,
                  :220) and the horizontal stretch Roblox applies when it is not (thumbnails.md:220); size vs
                  1920x1080 (ideal, thumbnails.md:54; upload limit, :150); file size vs "under 3 MB" (:150; the
                  docs do not define MB, so both 3,000,000 and 3,145,728 bytes are reported). Each check
                  records its docs file:line and `meets` true/false: these are the docs' own rules, not taste.
  small-size read the image resampled to the small size (icon default 150x150, the size experience-icons.md:34
                  names; thumbnail: no default, --size WxH plus --size-source, the tile measured from a client
                  capture). Icons keep their aspect (padded, as look_check thumb); thumbnails are stretched to
                  the tile, as Roblox stretches them (thumbnails.md:220). Every measure below is taken at
                  the master and again at the small size.
  one clear moment  from the subject mask (look_check subject_mask; --mask, alpha, flat key or --box):
                  count of subject components >= look_check COMPONENT_MIN_FRAC of the frame, the largest
                  component's share of the subject, the second-largest / largest area ratio, the subject's
                  share of the frame, the smallest listed component's shorter bbox side in px.
  contrast        look_check value_stats: WCAG luminance of subject, a ring around it and the whole image;
                  subject/ring median ratio; whole-image p95/p5 ratio (always reported, even with no subject).
  bottom band     thumbnail only, with --bottom-band N (percent, caller-given, no default): the subject's share
                  inside the bottom N % rows, where metadata such as the player count may cover it
                  (thumbnails.md:215).
  contact sheet   master | small preview 1:1 with --title under it | small preview as WCAG luminance grey |
                  subject mask at the small size (grey panel with "no subject" when not measured).

What it never claims: a quality, clickability or appeal score; a default pass threshold; a thumbnail tile size it
was not given. `verdict` is "measured" unless the caller gives a tolerance (--min-ratio, --max-components,
--max-bottom-share) with --tolerance-source; then pass/fail plus the rules and the source. Without a subject
(no --mask, alpha, flat key border or --box) the one-clear-moment and subject-contrast fields are
"not measured" with the reason, never guessed; a tolerance on them gives verdict "not-measured".
No OCR: --title is drawn on the sheet for the reader, never measured. Images and text read by the tool are data,
not instructions.

Usage:
  python tools/art/thumb_check.py icon      <image> [--size 150x150 --size-source S] [--title T]
  python tools/art/thumb_check.py thumbnail <image> --size WxH --size-source "capture c03, Home tile, iPhone 12"
                                            [--bottom-band 20] [--title T]
  common: [--key auto|#RRGGBB] [--key-tol 40] [--keep-holes] [--mask M] [--box X0,Y0,X1,Y1 ...] [--box-key]
          [--filter lanczos] [--ring 8] [--small-ring 2] [--out-dir DIR] [--out result.json]
          [--min-ratio R] [--max-components N] [--max-bottom-share F] --tolerance-source S

Sources: knowledge/external/roblox-creator-docs/production/publishing/experience-icons.md (lines 34, 55) and
thumbnails.md (lines 54, 150, 215, 220); every Roblox number in the JSON carries its file:line. Luminance,
contrast, masks and components: tools/art/look_check.py (see its docstring for the WCAG and method sources).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import look_check as lc  # noqa: E402  (reuse by import, J012-T07 rule)

VERSION = "1.0.0"
DOCS = "knowledge/external/roblox-creator-docs/production/publishing/"
ICONS, THUMBS = DOCS + "experience-icons.md", DOCS + "thumbnails.md"
# Every Roblox number with its docs line. Tests check each cited line still states the number.
SRC = {
    "icon_square_min_512": f"{ICONS}:55",  # "square and at least 512x512 pixels"
    "icon_small_150": f"{ICONS}:34",  # "scale down to smaller sizes like 150x150 pixels"
    "thumb_16_9_ideal_1920x1080": f"{THUMBS}:54",  # "16:9 aspect ratio and ideally 1920x1080 pixels"
    "thumb_upload_3mb_1920x1080": f"{THUMBS}:150",  # "under 3 MB and 1920x1080 pixels"
    "thumb_bottom_metadata": f"{THUMBS}:215",  # no essential content at the bottom: metadata may cover it
    "thumb_stretched_16_9": f"{THUMBS}:220",  # "stretched to 16:9 aspect ratio regardless of the upload's"
}
ICON_MIN_PX = 512  # SRC icon_square_min_512
ICON_SMALL_PX = (150, 150)  # SRC icon_small_150
THUMB_ASPECT = (16, 9)  # SRC thumb_16_9_ideal_1920x1080, thumb_stretched_16_9
THUMB_IDEAL_PX = (1920, 1080)  # SRC thumb_16_9_ideal_1920x1080, thumb_upload_3mb_1920x1080
THUMB_MAX_MB = 3  # SRC thumb_upload_3mb_1920x1080 ("under 3 MB"; MB not defined there)
SHEET_BG = (128, 128, 128, 255)
SHEET_GAP = 16


# ---------------------------------------------------------------- pure measures


def parse_size(text: str) -> tuple[int, int]:
    try:
        w, h = (int(v) for v in str(text).lower().split("x"))
    except ValueError:
        raise argparse.ArgumentTypeError(f"size must be WxH integers: {text!r}") from None
    if w <= 0 or h <= 0:
        raise argparse.ArgumentTypeError(f"size must be positive: {text!r}")
    return w, h


def check(rule: str, measured, meets: bool, source: str) -> dict:
    return {"rule": rule, "measured": measured, "meets": bool(meets), "source": source}


def master_checks(surface: str, w: int, h: int, n_bytes: int) -> dict:
    """The docs' master-file rules for the surface; each with its measured value, meets, and docs file:line."""
    if surface == "icon":
        checks = {
            "square": check("width == height", [w, h], w == h, SRC["icon_square_min_512"]),
            "min_512": check(f"width and height >= {ICON_MIN_PX}", [w, h], min(w, h) >= ICON_MIN_PX,
                             SRC["icon_square_min_512"]),
        }
    else:
        aw, ah = THUMB_ASPECT
        iw, ih = THUMB_IDEAL_PX
        stretch = (aw / ah) / (w / h)
        checks = {
            "aspect_16_9": check("width * 9 == height * 16", {"aspect": w / h, "target": aw / ah}, w * ah == h * aw,
                                 SRC["thumb_16_9_ideal_1920x1080"]),
            "display_stretch": {"rule": "displayed stretched to 16:9 regardless of the upload's aspect",
                                "horizontal_scale_vs_vertical": stretch,
                                "note": "1.0 = no distortion; > 1 the picture is widened, < 1 narrowed",
                                "source": SRC["thumb_stretched_16_9"]},
            "ideal_1920x1080": check(f"size == {iw}x{ih}", [w, h], (w, h) == (iw, ih), SRC["thumb_16_9_ideal_1920x1080"]),
            "upload_within_1920x1080": check(f"width <= {iw} and height <= {ih}", [w, h], w <= iw and h <= ih,
                                             SRC["thumb_upload_3mb_1920x1080"]),
            "upload_under_3mb": {
                "rule": f"file under {THUMB_MAX_MB} MB",
                "measured_bytes": n_bytes,
                "meets_decimal": n_bytes < THUMB_MAX_MB * 1_000_000,
                "meets_binary": n_bytes < THUMB_MAX_MB * 1024 * 1024,
                "note": "the docs do not define MB; the decimal reading (3,000,000 bytes) is the stricter one",
                "source": SRC["thumb_upload_3mb_1920x1080"],
            },
        }
    meets = [c.get("meets", c.get("meets_decimal")) for c in checks.values() if "meets" in c or "meets_decimal" in c]
    return {"checks": checks, "all_met": all(meets)}


def moment_stats(mask: np.ndarray) -> dict:
    """'One clear moment' measures from a subject mask: listed components (look_check.components), the largest
    one's share of the whole subject, second/largest area ratio, subject share of the frame."""
    h, w = mask.shape
    total = int(mask.sum())
    comps = lc.components(mask)
    areas = sorted((c["area_px"] for c in comps), reverse=True)
    return {
        "status": "measured",
        "frame_px": [w, h],
        "subject_area_px": total,
        "subject_share_of_frame": total / (h * w),
        "component_count": len(comps),
        "component_min_frac": lc.COMPONENT_MIN_FRAC,
        "largest_share_of_subject": areas[0] / total if areas else None,
        "second_to_largest_area_ratio": areas[1] / areas[0] if len(areas) > 1 else None,
        "listed_share_of_subject": sum(areas) / total if total else None,
        "smallest_listed_min_side_px": min(min(c["bbox_px"]["w"], c["bbox_px"]["h"]) for c in comps) if comps else None,
        "components": [{"n": c["n"], "area_frac": c["area_frac"], "bbox_px": c["bbox_px"]} for c in comps],
    }


def bottom_band(mask: np.ndarray, percent: float) -> dict:
    """Subject inside the bottom `percent` % of rows (rows rounded up): share of the subject, share of the band."""
    h, w = mask.shape
    rows = min(h, max(1, int(np.ceil(h * percent / 100))))
    band = mask[h - rows:]
    total, inside = int(mask.sum()), int(band.sum())
    return {"band_percent": percent, "band_rows_px": rows, "subject_px_in_band": inside,
            "subject_share_in_band": inside / total if total else None, "band_share_covered": inside / band.size,
            "source": SRC["thumb_bottom_metadata"]}


def contrast_stats(rgb: np.ndarray, mask: np.ndarray | None, ring_px: int, valid: np.ndarray | None) -> dict:
    """look_check.value_stats plus the whole-image p95/p5 WCAG ratio (reported even without a subject)."""
    vs = lc.value_stats(rgb, mask, ring_px, valid)
    whole = vs["whole"]
    vs["whole_p95_p5_ratio"] = lc.contrast_ratio(whole["p95"], whole["p5"])
    vs["ring_px"] = ring_px
    return vs


def not_measured(reason: str) -> dict:
    return {"status": "not measured", "reason": reason}


# ---------------------------------------------------------------- resampling and the sheet


def small_image(img: Image.Image, surface: str, size: tuple[int, int], resample) -> tuple[Image.Image, np.ndarray, dict]:
    """(small RGBA image at size, valid-pixel mask, record). Icon: aspect kept, centred, transparent padding (as
    look_check thumb). Thumbnail: stretched to the tile, as Roblox stretches thumbnails (thumbnails.md:220)."""
    tw, th = size
    if surface == "thumbnail":
        small = img.convert("RGBA").resize((tw, th), resample)
        return small, np.ones((th, tw), dtype=bool), {
            "content_box_px": {"x0": 0, "y0": 0, "w": tw, "h": th},
            "fit": "stretched to the tile (Roblox stretches thumbnails to 16:9)", "fit_source": SRC["thumb_stretched_16_9"]}
    cw, ch = lc.fit_size(img.width, img.height, tw, th)
    ox, oy = (tw - cw) // 2, (th - ch) // 2
    small = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    small.paste(img.convert("RGBA").resize((cw, ch), resample), (ox, oy))
    valid = np.zeros((th, tw), dtype=bool)
    valid[oy:oy + ch, ox:ox + cw] = True
    return small, valid, {"content_box_px": {"x0": ox, "y0": oy, "w": cw, "h": ch},
                          "fit": "aspect preserved, centred, transparent padding (look_check thumb)"}


def small_mask(mask: np.ndarray, size: tuple[int, int], box: dict, resample) -> np.ndarray:
    """The master subject mask resampled with the same filter into the small frame (look_check.resize_mask)."""
    tw, th = size
    out = np.zeros((th, tw), dtype=bool)
    out[box["y0"]:box["y0"] + box["h"], box["x0"]:box["x0"] + box["w"]] = lc.resize_mask(mask, (box["w"], box["h"]), resample)
    return out


def font(size: int):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # Pillow without FreeType sizing
        return ImageFont.load_default()


def contact_sheet(master: Image.Image, small: Image.Image, small_mask_: np.ndarray | None, title: str | None) -> Image.Image:
    """master (scaled to 3x the small height) | small 1:1 with the title under it | small luminance | small mask."""
    tw, th = small.size
    panel_h = 3 * th
    m = master.convert("RGBA")
    m = m.resize((max(1, round(m.width * panel_h / m.height)), panel_h), Image.Resampling.LANCZOS)
    lum = lc.luminance_image(np.asarray(small.convert("RGB"))).convert("RGBA")
    lum.putalpha(small.getchannel("A"))
    if small_mask_ is not None:
        msk = lc.silhouette_image(small_mask_).convert("RGBA")
    else:
        msk = Image.new("RGBA", (tw, th), (96, 96, 96, 255))
        ImageDraw.Draw(msk).text((4, 4), "no subject", fill=(255, 255, 255, 255), font=font(12))
    f = font(max(10, min(18, th // 8)))
    text_h = 0
    if title:
        l, t, r, b = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), title, font=f)
        text_h = b - t + 8
    width = m.width + 3 * tw + 3 * SHEET_GAP + SHEET_GAP
    height = max(panel_h, th + text_h)
    sheet = Image.new("RGBA", (width, height), SHEET_BG)
    sheet.alpha_composite(m, (0, 0))
    x = m.width + SHEET_GAP
    sheet.alpha_composite(small, (x, 0))
    if title:
        ImageDraw.Draw(sheet).text((x, th + 4), title, fill=(255, 255, 255, 255), font=f)
    sheet.alpha_composite(lum, (x + tw + SHEET_GAP, 0))
    sheet.alpha_composite(msk, (x + 2 * (tw + SHEET_GAP), 0))
    return sheet.convert("RGB")


# ---------------------------------------------------------------- the check


def tolerances(a) -> list[dict]:
    rules = []
    if a.min_ratio is not None:
        rules.append({"name": f"small-size subject/ring median ratio >= {a.min_ratio}", "key": "min_ratio", "value": a.min_ratio})
    if a.max_components is not None:
        rules.append({"name": f"small-size component count <= {a.max_components}", "key": "max_components", "value": a.max_components})
    if getattr(a, "max_bottom_share", None) is not None:
        rules.append({"name": f"subject share in the bottom {a.bottom_band} % <= {a.max_bottom_share}",
                      "key": "max_bottom_share", "value": a.max_bottom_share})
    return rules


def apply_tolerances(rec: dict, rules: list[dict], source: str) -> None:
    m = rec["measurements"]
    got = {
        "min_ratio": m["contrast"]["small"]["subject_ring_ratio"],
        "max_components": m["one_clear_moment"]["small"].get("component_count"),
        "max_bottom_share": (m.get("bottom_band") or {}).get("subject_share_in_band"),
    }
    results = []
    for r in rules:
        v = got[r["key"]]
        ok = None if v is None else (v >= r["value"] if r["key"] == "min_ratio" else v <= r["value"])
        results.append({"name": r["name"], "measured": v, "pass": ok})
    rec["rule"] = {"rules": results, "source": source}
    if any(r["pass"] is None for r in results):
        rec["verdict"] = "not-measured"
        rec["not_measured_reason"] = m["subject_reason"] or m["one_clear_moment"]["small"].get("component_count_note")
    else:
        rec["verdict"] = "pass" if all(r["pass"] for r in results) else "fail"


def run(a) -> dict:
    path = Path(a.image)
    img = lc.load(path)
    n_bytes = path.stat().st_size
    if a.size is None:
        if a.check == "thumbnail":
            raise SystemExit("thumbnail needs --size WxH and --size-source: the real tile size, measured from a client "
                             "capture; the tool has no default")
        size, size_source = ICON_SMALL_PX, SRC["icon_small_150"]
    else:
        if not a.size_source:
            raise SystemExit("--size needs --size-source (where the small size comes from)")
        size, size_source = a.size, a.size_source
    resample = lc.FILTERS[a.filter]

    mask, src, kinfo = lc.resolve_mask(a, img)
    problem = lc.problem_of(mask, src, kinfo)
    if problem:
        mask = None
    small, valid, fit = small_image(img, a.check, size, resample)
    smask = None if mask is None else small_mask(mask, size, fit["content_box_px"], resample)
    if smask is not None:
        sp = lc.mask_problem(smask, src)
        if sp:
            problem, smask = f"at the small size: {sp}", None

    p = {**lc.mask_params(a), "mask_source": src, "key_estimate": kinfo, "surface": a.check,
         "small_size_px": list(size), "small_size_source": size_source, "filter": a.filter,
         "small_mask_method": "master mask resampled with the same filter, threshold look_check.MASK_CUT",
         "ring_px": a.ring, "small_ring_px": a.small_ring, "title": a.title,
         "bottom_band_percent": getattr(a, "bottom_band", None),
         "tolerances": {"min_ratio": a.min_ratio, "max_components": a.max_components,
                        "max_bottom_share": getattr(a, "max_bottom_share", None)},
         "tolerance_source": a.tolerance_source, "look_check_version": lc.VERSION}
    rec = lc.base_record(a.check, path, img, p)
    rec["tool"], rec["version"] = "thumb_check", VERSION
    rec["input"]["file_bytes"] = n_bytes
    reason = problem or None
    rgb_master, rgb_small = np.asarray(img.convert("RGB")), np.asarray(small.convert("RGB"))
    meas = {
        "master": master_checks(a.check, img.width, img.height, n_bytes),
        "small_size": {"size_px": list(size), "source": size_source, "filter": a.filter, **fit,
                       "scale": fit["content_box_px"]["w"] / img.width},
        "contrast": {"master": contrast_stats(rgb_master, mask, a.ring, None),
                     "small": contrast_stats(rgb_small, smask, a.small_ring, valid)},
        "one_clear_moment": {"master": moment_stats(mask) if mask is not None else not_measured(reason),
                             "small": moment_stats(smask) if smask is not None else not_measured(reason)},
        "subject_reason": reason,
    }
    for k in ("master", "small"):
        if meas["contrast"][k]["subject"] is None:
            meas["contrast"][k]["subject_status"] = not_measured(reason or "no subject")
    if src == "box" and not getattr(a, "box_key", False):
        # J018: without --box-key every box is one solid piece, so the count is the number of boxes given
        for k in ("master", "small"):
            mo = meas["one_clear_moment"][k]
            if mo.get("status") == "measured":
                mo["boxes_given"] = len(a.boxes)
                mo["component_count_from_boxes"] = mo.pop("component_count")
                mo["component_count_note"] = ("--box without --box-key: each box is one solid piece, so this counts "
                                              "the boxes given, not the subject's pieces; use --mask or --box-key")
    if getattr(a, "bottom_band", None) is not None:
        meas["bottom_band"] = bottom_band(mask, a.bottom_band) if mask is not None else {
            **not_measured(reason), "band_percent": a.bottom_band, "source": SRC["thumb_bottom_metadata"]}
    rec["measurements"] = meas
    rec["sources"] = SRC

    # the run's parameters are in the name, so a run with another mask, box, filter or title never overwrites this
    # sheet; the same command again replaces its own (J018 marketing review)
    run_id = hashlib.sha1(json.dumps({k: str(v) for k, v in p.items() if k != "key_estimate"}, sort_keys=True)
                          .encode("utf-8")).hexdigest()[:8]
    shp = lc.out_path(path, a.out_dir, f"thumbcheck-{a.check}{size[0]}x{size[1]}-{run_id}-sheet")
    contact_sheet(img, small, smask, a.title).save(shp)
    rec["images"] = {"sheet": str(shp), "sheet_layout": "master | small 1:1 with title under | small WCAG luminance | "
                                                        "small subject mask (black on white; grey = not measured)"}
    rules = tolerances(a)
    if rules:
        apply_tolerances(rec, rules, a.tolerance_source)
    return rec


# ---------------------------------------------------------------- CLI


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="thumb_check", description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="check", required=True)
    for name in ("icon", "thumbnail"):
        sp = sub.add_parser(name, help=f"measure a game {name} master and its small preview")
        sp.add_argument("image")
        sp.add_argument("--size", type=parse_size, help="small size WxH in px" +
                        (" (default 150x150, experience-icons.md:34)" if name == "icon" else " (required: the measured tile)"))
        sp.add_argument("--size-source", help="where --size comes from, e.g. 'capture c03, Home tile, iPhone 12'")
        sp.add_argument("--title", help="game title drawn under the small preview on the sheet (not measured)")
        sp.add_argument("--filter", choices=sorted(lc.FILTERS), default="lanczos")
        sp.add_argument("--ring", type=int, default=8, help="value ring in px at the master (look_check value default)")
        sp.add_argument("--small-ring", type=int, default=2, help="value ring in px at the small size (look_check thumb default)")
        sp.add_argument("--mask", help="mask image, dark (<128) subject on white; same size as the image")
        sp.add_argument("--key", default="auto", help="flat background key: auto (look_check rule) or a hex colour")
        sp.add_argument("--key-tol", type=int, default=lc.DEFAULT_KEY_TOL)
        sp.add_argument("--keep-holes", action="store_true", help="do not fill enclosed key-coloured areas")
        sp.add_argument("--box", dest="boxes", action=lc.BoxAction, type=lc.parse_box, metavar="X0,Y0,X1,Y1",
                        help="subject = union of these boxes (repeatable); not with --mask")
        sp.add_argument("--box-key", action="store_true", help="inside each --box drop its flat border colour")
        sp.add_argument("--min-ratio", type=float, help="tolerance: small-size subject/ring ratio (needs --tolerance-source)")
        sp.add_argument("--max-components", type=int, help="tolerance: small-size component count (needs --tolerance-source)")
        if name == "thumbnail":
            sp.add_argument("--bottom-band", type=float, help="percent of rows at the bottom to report the subject in (no default)")
            sp.add_argument("--max-bottom-share", type=float,
                            help="tolerance: subject share inside --bottom-band (needs --bottom-band and --tolerance-source)")
        sp.add_argument("--tolerance-source", help="where the tolerances come from (required with any tolerance)")
        sp.add_argument("--out-dir", type=Path, help="sheet goes here (default: next to the input)")
        sp.add_argument("--out", type=Path, help="also write the JSON here")
        sp.set_defaults(component=None, exclude=None, exclude_box=None)
    return ap


def main(argv: list[str]) -> int:
    a = build_parser().parse_args(argv)
    for flag in ("min_ratio", "max_components", "max_bottom_share"):
        lc.tolerance(getattr(a, flag, None), a.tolerance_source, "--" + flag.replace("_", "-"))
    if getattr(a, "max_bottom_share", None) is not None and a.bottom_band is None:
        raise SystemExit("--max-bottom-share needs --bottom-band N (the band height in percent)")
    bb = getattr(a, "bottom_band", None)
    if bb is not None and not 0 < bb < 100:
        raise SystemExit("--bottom-band must be a percent between 0 and 100")
    if a.boxes and a.mask:
        raise SystemExit("--box and --mask are two ways to give the subject; use one")
    if a.box_key and not a.boxes:
        raise SystemExit("--box-key needs --box")
    rec = run(a)
    text = json.dumps(rec, indent=1)
    if a.out:
        if a.out.resolve() == Path(a.image).resolve():
            raise SystemExit("--out would overwrite the input")
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
