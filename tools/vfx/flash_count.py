"""Count large-area flashes per rolling second in a folder of frames, and a pulse rate in a box - without AI taste.

Kit tool (universal). The studio's one flash counter (owner decision J018-D7, G3-P1): it replaces the script that
`vfx-craft/references/measure.md` section 6 printed by hand; cinematics (`film-craft`) and marketing videos
(`marketing-craft`) run the same tool on their own frame folders. A screening aid, not a photosensitivity analyser:
its known false readings are listed in measure.md section 6, and every count at or over the cap, and every count
under it on a scene with a listed too-low case, is checked on the frames by eye before a fix note.

Input: a folder of frames of one image type (.jpg or .png): Studio captures `f###_<ms>ms.jpg`, the marketing frame
command's `f####_<ms>ms.jpg`, Blender renders `0001.png`. Frames go in the order of the numbers in their names;
times come from `_<ms>ms` in the names, else from the frame numbers at <fps> (a Blender frame_step keeps true times).
It stops with a message on fewer than 2 frames, two image types, a name that is not a frame name, names of more
than one pattern, times that do not rise, a 16-bit or float grey frame, or a box not given in fractions.

Method (PROPOSAL thresholds, record them): relative luminance (WCAG); a flash is a net rise of STEP or more from
each pixel's lowest value since the region was armed, over the share of the frame (or 9 x that share of one of nine
blocks). After a flash the region waits; a net fall over the share re-arms it (waiting or not); while it waits and
almost nothing falls, the trough follows the frame. Two counts: over 10 % of the frame (cinematics, marketing) and
over 3 % (effects); "most in any 1 s" is the largest number of onsets in a rolling second.

Usage:
  python tools/vfx/flash_count.py <frames folder> <fps> [--box x0,y0,x1,y1] [--json]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

STEP = 0.1  # PROPOSAL: net relative-luminance rise that counts as a flash
AREAS = (0.10, 0.03)  # PROPOSAL: share of the frame: large (cinematic, marketing) and mid (effects)
GRID = 3  # local flashes: G x G blocks, each needing G*G x the share
NAME_RE = re.compile(r"[A-Za-z]*_?\d+(_\d+ms)?\.(jpe?g|png)", re.IGNORECASE)


class FlashError(Exception):
    pass


def frames(folder: Path, fps: float) -> tuple[list[Path], list[int], str]:
    """Frame paths in frame-number order, their times in ms, and where the times came from."""
    if not folder.is_dir():
        raise FlashError(f"not a folder: {folder}")
    fs = sorted((p for p in folder.iterdir() if p.suffix.lower() in (".jpg", ".jpeg", ".png")),
                key=lambda p: [int(v) for v in re.findall(r"\d+", p.name)])
    ext = {p.suffix.lower() for p in fs}
    if len(fs) < 2 or len(ext) > 1:
        raise FlashError(f"need 2 or more frames of one image type in {folder}: found {len(fs)}, types {sorted(ext)}")
    odd = [p.name for p in fs if not NAME_RE.fullmatch(p.name)]
    if odd:
        raise FlashError(f"not frame names (number, or f###_<ms>ms): {odd[:3]}: move them out of {folder}")
    if len({re.sub(r"\d", "", p.name) for p in fs}) > 1:
        raise FlashError("more than one name pattern (per-shot renders?): renumber into one sequence in edit order")
    ms = [re.search(r"_(\d+)ms\.", p.name) for p in fs]
    fn = [int(re.findall(r"\d+", p.name)[0]) for p in fs]
    if all(ms):
        t, src = [int(m.group(1)) for m in ms], "the names (ms)"
    else:
        t, src = [round((k - fn[0]) * 1000 / fps) for k in fn], f"{fps:g} fps"
    if any(b <= a for a, b in zip(t, t[1:])):
        raise FlashError("frame times do not increase in frame-number order: check the names")
    return fs, t, src


def luminance(path: Path) -> np.ndarray:
    im = Image.open(path)
    if im.mode[0] in "IF":
        raise FlashError(f"{path.name} is a 16-bit or float grey image ({im.mode}): it reads as white; save 8-bit RGB")
    c = np.asarray(im.convert("RGB"), float) / 255
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4) @ [0.2126, 0.7152, 0.0722]


def most_in_1s(onsets: list[int], t: list[int]) -> int:
    return max((sum(t[s] <= t[o] < t[s] + 1000 for o in onsets) for s in onsets), default=0)


def count(fs: list[Path], t: list[int], box: list[float] | None = None) -> dict:
    """Flash onsets per area (the region with the most in any 1 s) and, with a box, its pulse rate."""
    regions = {a: None for a in AREAS}
    box_means = []
    for i, f in enumerate(fs):
        lum = luminance(f)
        h, w = lum.shape
        if box:
            box_means.append(float(lum[int(box[1] * h):int(box[3] * h), int(box[0] * w):int(box[2] * w)].mean()))
        for a in AREAS:
            if regions[a] is None:  # region: [slice, share, lo, hi, armed, onsets]; the whole frame, then G x G blocks
                regions[a] = [[np.s_[:, :], a]] + [
                    [np.s_[h * y // GRID:h * (y + 1) // GRID, w * x // GRID:w * (x + 1) // GRID], min(1, a * GRID * GRID)]
                    for y in range(GRID) for x in range(GRID)]
                for r in regions[a]:
                    r += [lum[r[0]], lum[r[0]], True, []]
                continue
            for r in regions[a]:
                x = lum[r[0]]
                lo, hi = np.minimum(r[2], x), np.maximum(r[3], x)
                net = ((x - lo) >= STEP).mean() - ((hi - x) >= STEP).mean()  # rising share minus falling share
                if r[4] and net >= r[1]:  # a flash: wait for a fall
                    r[5].append(i)
                    lo, hi, r[4] = x, x, False
                elif -net >= r[1]:  # a net fall over the share, waiting or not: count rises from here
                    lo, hi, r[4] = x, x, True
                elif not r[4] and ((hi - x) >= STEP).mean() < r[1] / 2:  # waiting, almost nothing falls: trough follows
                    lo = x
                r[2], r[3] = lo, hi
    out = {"counts": {}}
    for a in AREAS:
        best = max(regions[a], key=lambda r: most_in_1s(r[5], t))
        out["counts"][f"{a:.0%}"] = {"area_share": a, "onsets": [fs[i].name for i in best[5]],
                                    "most_in_any_1s": most_in_1s(best[5], t)}
    if box:
        b = np.array(box_means)
        lo, hi = float(b.min()), float(b.max())
        mid, k = (lo + hi) / 2, 0.1 * (hi - lo)
        up, rises = b[0] > mid, []
        for i, v in enumerate(b):
            if not up and v > mid + k:
                rises.append(i)
                up = True
            elif up and v < mid - k:
                up = False
        if hi - lo < 0.005:
            hz = "no pulse (swing under 0.005)"
        elif len(rises) > 1:
            hz = round((len(rises) - 1) * 1000 / (t[rises[-1]] - t[rises[0]]), 2)
        else:
            hz = "n/a (fewer than 2 rises)"
        out["box"] = {"box": box, "luminance_min": round(lo, 3), "luminance_max": round(hi, 3), "rises": len(rises), "hz": hz}
    return out


def run(folder: Path, fps: float, box: list[float] | None = None) -> dict:
    if box and not (len(box) == 4 and 0 <= box[0] < box[2] <= 1 and 0 <= box[1] < box[3] <= 1):
        raise FlashError("box: x0,y0,x1,y1 as fractions of the frame, x0 < x1 and y0 < y1")
    fs, t, src = frames(folder, fps)
    rec = {"tool": "flash_count", "folder": str(folder), "frames": len(fs), "first": fs[0].name, "last": fs[-1].name,
           "times_from": src, "step": STEP, "grid": GRID, "verdict": "measured (screening aid: check onsets on the frames)"}
    rec.update(count(fs, t, box))
    return rec


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("folder", type=Path)
    ap.add_argument("fps", type=float)
    ap.add_argument("--box", help="x0,y0,x1,y1 as fractions of the frame: pulse rate inside this box")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        box = [float(v) for v in a.box.split(",")] if a.box else None
        rec = run(a.folder, a.fps, box)
    except (FlashError, ValueError) as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(rec, indent=2))
        return 0
    print(rec["frames"], "frames,", rec["first"], "to", rec["last"], "| times from", rec["times_from"])
    for k, c in rec["counts"].items():
        print(f"flashes over {k} of the frame: onsets {c['onsets']} | most in any 1 s: {c['most_in_any_1s']}")
    if "box" in rec:
        b = rec["box"]
        print("box luminance", b["luminance_min"], "-", b["luminance_max"], "| rises", b["rises"], "| Hz", b["hz"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
