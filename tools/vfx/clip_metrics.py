"""Measure what a recorded VFX clip shows, frame by frame, without AI taste.

Input: a capture folder of `f###_<ms>.jpg` frames (tools: the Studio capture rig).
Output: `metrics.json` in that folder: per frame screen coverage, bright coverage, box, centre,
mean colour and peak brightness of the pixels that differ from the background, plus a clip summary
(onset, peak, how long it stays visible). Used for frame scripts and the similarity score
(knowledge/reference/vfx/training/benchmark.md).

Background = per-pixel median of all frames, so it suits fixed-camera clips. Clips whose camera
moves (`_follow`) are measured anyway and flagged `moving_camera` in the summary.

Usage:
  python tools/vfx/clip_metrics.py <capture_dir> [<capture_dir> ...]
  python tools/vfx/clip_metrics.py --all output/vfx/training-captures
  python tools/vfx/clip_metrics.py [--background-first] --press-ms <press ms> <press folder>   (the UI lag line)
  python tools/vfx/clip_metrics.py diff <folder A> <folder B> X0,Y0,X1,Y1   (per-frame difference in one box)
  python tools/vfx/clip_metrics.py --background-first <capture_dir>   (an idle first frame as the background: use it
      when the effect stays on screen in more than half the frames, where the median background inverts every number)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

WORK_WIDTH = 256  # frames are downscaled to this width before measuring
DIFF_THRESHOLD = 40  # max channel difference from the background that counts as "effect"
BRIGHT_LUMA = 230  # luminance (0-255) that counts as near-white
UI_MASK = (0.10, 0.07)  # top-left Roblox menu buttons: (width, height) fraction ignored
FRAME_RE = re.compile(r"^f(\d+)_(\d+)ms\.jpg$")


def load_frames(folder: Path) -> tuple[list[int], np.ndarray]:
    # numeric order: a name sort puts f1000 before f101 (J018 vfx repair round 3)
    names = sorted((p for p in folder.iterdir() if FRAME_RE.match(p.name)),
                   key=lambda p: int(FRAME_RE.match(p.name).group(1)))
    if not names:
        raise ValueError(f"no f###_<ms>ms.jpg frames in {folder}")
    times, frames = [], []
    for p in names:
        m = FRAME_RE.match(p.name)
        assert m
        times.append(int(m.group(2)))
        img = Image.open(p).convert("RGB")
        h = round(img.height * WORK_WIDTH / img.width)
        frames.append(np.asarray(img.resize((WORK_WIDTH, h), Image.BILINEAR), dtype=np.int16))
    return times, np.stack(frames)


def luma(rgb: np.ndarray) -> np.ndarray:
    return 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]


def effect_mask(frame: np.ndarray, background: np.ndarray) -> np.ndarray:
    mask = np.abs(frame - background).max(axis=-1) > DIFF_THRESHOLD
    h, w = mask.shape
    mask[: int(h * UI_MASK[1]), : int(w * UI_MASK[0])] = False
    return mask


def frame_metrics(frame: np.ndarray, background: np.ndarray) -> dict:
    mask = effect_mask(frame, background)
    h, w = mask.shape
    n = int(mask.sum())
    out: dict = {"coverage_pct": round(100 * n / (h * w), 3)}
    lum = luma(frame)
    out["bright_pct"] = round(100 * float((mask & (lum >= BRIGHT_LUMA)).sum()) / (h * w), 3)
    if n == 0:
        out.update(box=None, centre=None, mean_rgb=None, peak_luma=None)
        return out
    ys, xs = np.nonzero(mask)
    out["box"] = [round(xs.min() / w, 3), round(ys.min() / h, 3), round((xs.max() + 1) / w, 3), round((ys.max() + 1) / h, 3)]
    out["centre"] = [round(float(xs.mean()) / w, 3), round(float(ys.mean()) / h, 3)]
    out["mean_rgb"] = [int(c) for c in frame[mask].mean(axis=0)]
    out["peak_luma"] = int(lum[mask].max())
    return out


def summarise(times: list[int], rows: list[dict], moving_camera: bool) -> dict:
    cov = np.array([r["coverage_pct"] for r in rows])
    peak_i = int(cov.argmax())
    peak = float(cov[peak_i])
    visible = cov >= max(0.2, 0.1 * peak)
    onset = next((times[i] for i, v in enumerate(visible) if v), None)
    last = next((times[i] for i in range(len(times) - 1, -1, -1) if visible[i]), None)
    bright = np.array([r["bright_pct"] for r in rows])
    return {
        "frames": len(times),
        "moving_camera": moving_camera,
        "onset_ms": onset,
        "peak_ms": times[peak_i],
        "peak_coverage_pct": round(peak, 3),
        "peak_bright_pct": round(float(bright.max()), 3),
        "visible_ms": None if onset is None or last is None else last - onset,
        "mean_coverage_pct": round(float(cov.mean()), 3),
    }


def measure(folder: Path, background_from: str = "median") -> dict:
    """background_from: "median" (per-pixel median of all frames, the default) or "first" (the first frame, an idle
    frame before the effect). The median inverts every number when the effect stays in more than half the frames
    (J018 vfx review: an effect in 70 % of the frames); record an idle frame first and use "first" then."""
    times, frames = load_frames(folder)
    if background_from == "first":
        background = frames[0].astype(np.int16)
    elif background_from == "median":
        background = np.median(frames, axis=0).astype(np.int16)
    else:
        raise ValueError(f"background_from must be median or first, got {background_from!r}")
    rows = [{"ms": t, **frame_metrics(f, background)} for t, f in zip(times, frames)]
    result = {
        "clip": folder.name,
        "summary": summarise(times, rows, "_follow" in folder.name),
        "frames": rows,
        "settings": {"work_width": WORK_WIDTH, "diff_threshold": DIFF_THRESHOLD, "bright_luma": BRIGHT_LUMA,
                     "background": "first frame (idle)" if background_from == "first" else "median of all frames"},
    }
    (folder / "metrics.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
    return result


def press_lag(rows: list[dict], press_ms: int) -> dict:
    """The UI lag line (ui-design S-33): the highest coverage before the press, the first frame from the press on
    whose coverage rises above it, and the lag. summary.onset_ms is never the lag (a bigger later change hides a
    small press cue). The pre-press maximum must be 0; cue None is UNVERIFIED, not a pass."""
    base = max([r["coverage_pct"] for r in rows if r["ms"] < press_ms] + [0])
    cue = next((r["ms"] for r in rows if r["ms"] >= press_ms and r["coverage_pct"] > base), None)
    return {"press_ms": press_ms, "pre_press_max_pct": base, "cue_ms": cue, "lag_ms": None if cue is None else cue - press_ms,
            "valid": base == 0 and cue is not None}


def frame_diff(folder_a: Path, folder_b: Path, box: tuple[int, int, int, int], level: int = DIFF_THRESHOLD) -> list[dict]:
    """The reveal difference (ui-design S-44): per frame pair, in one box, the mean difference and the count of pixels
    that differ by more than `level` in a channel. Folders are paired in frame-number order; both start on the press."""
    def frames_of(folder):
        return sorted((p for p in folder.iterdir() if FRAME_RE.match(p.name)), key=lambda p: int(FRAME_RE.match(p.name).group(1)))
    fa, fb = frames_of(folder_a), frames_of(folder_b)
    if not fa or not fb:
        raise ValueError("both folders need f###_<ms>ms.jpg frames")
    out = []
    for pa, pb in zip(fa, fb):
        a = np.asarray(Image.open(pa).convert("RGB").crop(box), float)
        b = np.asarray(Image.open(pb).convert("RGB").crop(box), float)
        d = np.abs(a - b)
        out.append({"a": pa.name, "b": pb.name, "mean_diff": round(float(d.mean()), 2), "changed_px": int((d.max(-1) > level).sum())})
    return out


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "diff":  # diff <folder A> <folder B> X0,Y0,X1,Y1
        box = tuple(int(v) for v in argv[3].split(","))
        for row in frame_diff(Path(argv[1]), Path(argv[2]), box):
            print(json.dumps(row))
        return 0
    bg, press = "median", None
    if argv[0] == "--background-first":  # the first frame is an idle frame before the effect
        bg, argv = "first", argv[1:]
    if argv[0] == "--press-ms":  # the UI lag line on one press folder
        press, argv = int(argv[1]), argv[2:]
    if argv[0] == "--all":
        root = Path(argv[1])
        folders = sorted(p for p in root.iterdir() if p.is_dir() and any(FRAME_RE.match(x.name) for x in p.iterdir()))
    else:
        folders = [Path(a) for a in argv]
    for f in folders:
        res = measure(f, bg)
        if press is not None:
            print(json.dumps({"clip": f.name, **press_lag(res["frames"], press)}))
            continue
        s = res["summary"]
        print(f"{f.name}: peak {s['peak_coverage_pct']}% at {s['peak_ms']} ms, visible {s['visible_ms']} ms")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
