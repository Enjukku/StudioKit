"""Measured egg masks and brightness ranking for the J009-T13 direction test (diagnostics, not verdicts).

Mask method (recorded so anyone can repeat it):
  1. WCAG relative luminance Y per pixel (sRGB linearised, 0.2126 R + 0.7152 G + 0.0722 B).
  2. Seed: threshold at the image's own 98th percentile of Y; the seed = the largest 8-connected component.
  3. Grow: pixels with Y >= the image's own GROW percentile (argument, default 90) that are 8-connected to the seed.
  4. Holes inside the grown region are filled (cracks, shading on the shell).
  The script never uses hand-drawn boxes. Check the overlay image before trusting a number.

Also written: share of the frame's brightest 1 % and 0.2 % of pixels that fall inside the mask, the 5 largest
bright components (area, centroid, median Y) so the egg can be ranked against torches, snow and lanterns.

  python egg_masks.py <image> <out_dir> [grow_percentile]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def luminance(rgb: np.ndarray) -> np.ndarray:
    c = rgb.astype(np.float64) / 255.0
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return lin[..., 0] * 0.2126 + lin[..., 1] * 0.7152 + lin[..., 2] * 0.0722


def components(mask: np.ndarray) -> tuple[np.ndarray, int]:
    """8-connected labelling with an iterative flood fill (numpy only)."""
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    n = 0
    ys, xs = np.nonzero(mask)
    for y0, x0 in zip(ys, xs):
        if labels[y0, x0]:
            continue
        n += 1
        stack = [(y0, x0)]
        labels[y0, x0] = n
        while stack:
            y, x = stack.pop()
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < h and 0 <= xx < w and mask[yy, xx] and not labels[yy, xx]:
                        labels[yy, xx] = n
                        stack.append((yy, xx))
    return labels, n


def fill_holes(mask: np.ndarray) -> np.ndarray:
    """Background = pixels not in the mask connected to the border (4-connected); the rest is filled."""
    h, w = mask.shape
    outside = np.zeros((h, w), dtype=bool)
    stack = [(y, x) for y in range(h) for x in (0, w - 1) if not mask[y, x]]
    stack += [(y, x) for x in range(w) for y in (0, h - 1) if not mask[y, x]]
    for y, x in stack:
        outside[y, x] = True
    while stack:
        y, x = stack.pop()
        for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= yy < h and 0 <= xx < w and not mask[yy, xx] and not outside[yy, xx]:
                outside[yy, xx] = True
                stack.append((yy, xx))
    return ~outside


def main() -> int:
    img_path, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    rgb = np.asarray(Image.open(img_path).convert("RGB"))
    y = luminance(rgb)
    t98 = float(np.percentile(y, 98))
    bright = y >= t98
    labels, n = components(bright)
    sizes = np.bincount(labels.ravel())[1:]
    order = np.argsort(sizes)[::-1]
    egg_label = int(order[0]) + 1
    grow_pct = float(sys.argv[3]) if len(sys.argv) > 3 else 90.0
    t_grow = float(np.percentile(y, grow_pct))
    glabels, _ = components(y >= t_grow)
    seed_hits = np.unique(glabels[labels == egg_label])
    egg = fill_holes(np.isin(glabels, seed_hits[seed_hits > 0]))

    top = []
    for idx in order[:5]:
        lab = int(idx) + 1
        m = labels == lab
        yy, xx = np.nonzero(m)
        top.append({"label": lab, "area_px": int(m.sum()), "centroid_xy": [round(float(xx.mean())), round(float(yy.mean()))],
                    "bbox_xyxy": [int(xx.min()), int(yy.min()), int(xx.max()) + 1, int(yy.max()) + 1],
                    "median_Y": round(float(np.median(y[m])), 4)})

    def share_in_egg(pct: float) -> float:
        thr = np.percentile(y, 100 - pct)
        sel = y >= thr
        return round(float((sel & egg).sum() / sel.sum()), 4)

    ey, ex = np.nonzero(egg)
    rec = {
        "image": str(img_path).replace("\\", "/"),
        "size_px": [rgb.shape[1], rgb.shape[0]],
        "method": f"seed = largest 8-connected component of WCAG Y >= p98; grown into connected Y >= p{grow_pct:g}; holes filled",
        "threshold_Y_p98": round(t98, 4),
        "grow_percentile": grow_pct,
        "threshold_Y_grow": round(t_grow, 4),
        "bright_components": int(n),
        "egg_mask": {"area_px": int(egg.sum()), "area_frac": round(float(egg.mean()), 4),
                     "bbox_xyxy": [int(ex.min()), int(ey.min()), int(ex.max()) + 1, int(ey.max()) + 1],
                     "median_Y": round(float(np.median(y[egg])), 4)},
        "share_of_brightest_1pct_inside_egg": share_in_egg(1.0),
        "share_of_brightest_0.2pct_inside_egg": share_in_egg(0.2),
        "largest_bright_components": top,
        "image_median_Y": round(float(np.median(y)), 4),
        "verdict": "measured (diagnostic; no project tolerance exists)",
    }
    stem = f"{img_path.stem}-p{grow_pct:g}"
    mask_img = Image.fromarray(np.where(egg, 0, 255).astype(np.uint8))  # dark subject on white (look_check --mask)
    mask_img.save(out_dir / f"{stem}-eggmask.png")
    over = rgb.copy()
    over[bright & ~egg] = (0.5 * over[bright & ~egg] + 0.5 * np.array([0, 160, 255])).astype(np.uint8)
    over[egg] = (0.55 * over[egg] + 0.45 * np.array([255, 0, 255])).astype(np.uint8)
    Image.fromarray(over).save(out_dir / f"{stem}-eggmask-overlay.png")
    (out_dir / f"{stem}-eggmask.json").write_text(json.dumps(rec, indent=2), encoding="utf-8")
    print(json.dumps(rec, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
