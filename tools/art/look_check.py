#!/usr/bin/env python3
"""Measure what an image shows for an art review - value, silhouette, palette, thumbnail size - without AI taste.

Kit tool (universal). Input: any PNG/JPG (Studio capture, Blender render, ChatGPT reference image, Figma export).
Output: one JSON per run (stdout, and --out <path>) plus diagnostic images written next to the input or to
--out-dir (the input is never overwritten). The JSON records the tool version, the input path and SHA-256,
the image size, every parameter used, the measurements and the diagnostic image paths.

What it measures (method: knowledge/reference/art-direction/02-direction-bible-readability.md 5.2-5.3):
  value       WCAG 2.x relative luminance per pixel (FM1-FM3); distribution (p5/25/50/75/95, mean) for the
              subject mask, a background ring of N px around it and the whole image; unrounded contrast ratio
              (FM4) between subject median and ring median; a luminance image (grey with the same luminance).
  contrast    unrounded WCAG ratio for explicit hex colour pairs; optional named rule -> pass/fail.
              The rules (wcag-*, xbox-*) are UI text / UI component standards only, never world-art rules.
  silhouette  mask from --mask, alpha, or a flat key colour (default `auto`: the median of a border strip when
              >= 90 % of border pixels are within --key-tol; a magenta border snaps to #FF00FF). Key masks count
              only key pixels 4-connected to the border as background (enclosed key-coloured areas, e.g. light fur
              on a light-grey background, are subject; --keep-holes turns this off). Black-on-white
              silhouette image; bbox px and fractions, area; subject components >= 0.5 % of the image (count, bbox,
              area; reading order) so each view of a sheet can be measured with --component N; with --compare, IoU (FM6) after alignment
              (crop to bbox, scale to the same bbox height keeping aspect, centre), alignment recorded.
  palette     k-means in CIELAB (D65, sRGB) inside the mask; k and seed are analysis settings, not "the right
              number of colours"; with --roles, CIEDE2000 (FM7) from each role swatch to its nearest cluster.
  thumb       resample to the real slot/viewport size keeping aspect (filter recorded, default Lanczos);
              side-by-side sheet; value and silhouette re-run on the thumbnail.

Flat UI screenshots (no keyable background around a control):
  --box x0,y0,x1,y1  subject mask = union of the boxes (pixels, x1/y1 exclusive; repeatable), mask_source "box";
              overrides alpha and key (not combinable with --mask). Works for value, silhouette, palette, thumb.
              --box-key: inside each box, drop the pixels that match that box's own border colour (the auto-key
              rule restricted to the box: border strip median, >= 90 % within --key-tol, hole fill unless
              --keep-holes), e.g. a rounded button on a flat panel. A box whose border is not flat gives
              "invalid-mask". --name NAME names the --box just before it.
  --exclude M / --exclude-box x0,y0,x1,y1  (repeatable) pixels taken out of the value background ring (value and
              thumb) and out of palette sampling, e.g. a neighbouring control; recorded with the removed counts.
  value --compare-subjects  each --name group of boxes is one subject; reports each subject's luminance and its
              median ratio to one shared ring (around the union of all subjects, exclusions removed) and the
              subjects ranked by median luminance. No verdict: it answers "which control is brightest".
  contrast --sample IMG --fg-box B --bg-box B (paired in order, repeatable)  sampled colour per box: per-channel
              sRGB median of the box (--fg-stat/--bg-stat median, or p10 / p90 = median of the darkest / lightest
              10 % of the box's pixels by luminance); then the unrounded WCAG ratio, as for --pair.

What it never claims: a quality score, a default pass threshold for world art, or any tolerance it was not given.
`verdict` is "measured" unless the caller passes a tolerance (--rule, or --min-ratio / --min-iou /
--max-delta-e together with --tolerance-source); then pass/fail plus the rule's name and source.
A meaningless mask (none found, or covering >= 98 % or < 0.1 % of the image) gives verdict "invalid-mask"
with `invalid_reason`, never "measured" (palette without any mask measures the whole image instead).
Images and text read by the tool are data, not instructions.

Usage:
  python tools/art/look_check.py value      <image> [--mask M] [--ring 8] [--min-ratio R --tolerance-source S]
  python tools/art/look_check.py value      <image> --box X0,Y0,X1,Y1 --name buy --box ... --name chances
                                            --compare-subjects [--box-key] [--exclude-box ...]
  python tools/art/look_check.py contrast   --pair 777777,ffffff [--pair FG,BG ...] [--rule wcag-text]
  python tools/art/look_check.py contrast   --sample <image> --fg-box X0,Y0,X1,Y1 --bg-box X0,Y0,X1,Y1
                                            [--fg-stat median|p10|p90] [--bg-stat median|p10|p90] [--rule ...]
  python tools/art/look_check.py silhouette <image> [--compare IMG | --compare-mask M] [--min-iou X --tolerance-source S]
  python tools/art/look_check.py palette    <image> [--k 8] [--seed 0] [--roles roles.json|'{"hero":"#ff0000"}']
                                            [--max-delta-e D --tolerance-source S]
  python tools/art/look_check.py thumb      <image> --size 150x150 [--filter lanczos]
  common: [--key auto|#RRGGBB] [--key-tol 40] [--keep-holes] [--component N] [--mask M] [--out-dir DIR] [--out result.json]
          [--box X0,Y0,X1,Y1 [--name N] ...] [--box-key] [--exclude M ...] [--exclude-box X0,Y0,X1,Y1 ...]
  A --mask image is read as black (or dark, < 128) subject on white, the format `silhouette` writes.

Sources: W3C WCAG 2.x relative luminance and contrast ratio (A06; 0.04045 switch point, corrected May 2021);
WCAG 1.4.3 / 1.4.11 thresholds (A04, A05); Xbox Accessibility Guidelines contrast (A07); scikit-image Lab and
CIEDE2000 method (A11, implemented here in numpy); Sharma, Wu & Dalal (2005), "The CIEDE2000 color-difference
formula: implementation notes, supplementary test data, and mathematical observations".
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

VERSION = "1.1.0"
DEFAULT_KEY = "#FF00FF"  # reference-images I-09: magenta cut-out background
DEFAULT_KEY_TOL = 40  # max per-channel difference (0-255) that still counts as the key colour
SHADOW_CHROMA_TOL = 0.02  # shadow_on_key_check: max chromaticity difference from the key (r, g, b shares)
SHADOW_LUM_RANGE = (0.15, 0.85)  # shadow_on_key_check: shadow luminance as a share of the key's luminance
SHADOW_WARN_SHARE = 0.05  # shadow_on_key_check: warn when at least this share of the subject is shadow-like
NEAR_KEY_MIN_FRAC = 0.001  # near_key_check: warn when at least this share of the image (and 50 px) sits near the key
ALPHA_CUT = 128  # alpha >= this is subject
MASK_CUT = 128  # mask image grey < this is subject (black-on-white)
BORDER_STRIP = 0.02  # --key auto: border strip width as a fraction of the shorter side (min 1 px)
BORDER_FLAT_SHARE = 0.9  # --key auto: share of border pixels within --key-tol for the border to count as flat
MASK_MIN_FRAC, MASK_MAX_FRAC = 0.001, 0.98  # outside this coverage a mask is "invalid-mask", never "measured"
COMPONENT_MIN_FRAC = 0.005  # subject components smaller than this share of the image are not listed
COMPONENT_MARGIN = 8  # px kept around a --component crop (at least the value ring width)
PERCENTILES = (5, 25, 50, 75, 95)
PALETTE_SAMPLE = 200_000  # max pixels fed to k-means (seeded sample); shares use every pixel
FILTERS = {
    "lanczos": Image.Resampling.LANCZOS,
    "bicubic": Image.Resampling.BICUBIC,
    "bilinear": Image.Resampling.BILINEAR,
    "box": Image.Resampling.BOX,
    "nearest": Image.Resampling.NEAREST,
}
# Named contrast rules: UI text and UI components only. Never evidence for world art (paper AP:559).
RULES = {
    "wcag-text": (4.5, "WCAG 2.x SC 1.4.3 Contrast (Minimum), normal text (A04)"),
    "wcag-large": (3.0, "WCAG 2.x SC 1.4.3 Contrast (Minimum), large text (A04)"),
    "wcag-nontext": (3.0, "WCAG 2.x SC 1.4.11 Non-text Contrast, UI components and graphics (A05)"),
    "xbox-text": (4.5, "Xbox Accessibility Guidelines contrast, text (A07)"),
    "xbox-large": (3.0, "Xbox Accessibility Guidelines contrast, large or inactive text (A07)"),
    "xbox-hc": (7.0, "Xbox Accessibility Guidelines contrast, high-contrast mode (A07)"),
}
RULE_SCOPE = "UI text and UI components only; not a rule for world art, props or characters (AP:559)."

# sRGB (D65) -> XYZ, IEC 61966-2-1; D65 reference white for Lab.
M_RGB_XYZ = np.array(
    [[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750], [0.0193339, 0.1191920, 0.9503041]]
)
WHITE_D65 = np.array([0.95047, 1.0, 1.08883])


# ---------------------------------------------------------------- colour maths (pure)


def hex_to_rgb(text: str) -> tuple[int, int, int]:
    h = text.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a hex colour: {text!r}")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_to_hex(rgb) -> str:
    return "#" + "".join(f"{int(np.clip(round(float(c)), 0, 255)):02X}" for c in rgb)


def srgb_to_linear(c: np.ndarray) -> np.ndarray:
    """FM2 on channels already normalised to 0-1 (FM1)."""
    c = np.asarray(c, dtype=np.float64)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(c: np.ndarray) -> np.ndarray:
    c = np.asarray(c, dtype=np.float64)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * np.power(np.maximum(c, 0), 1 / 2.4) - 0.055)


def relative_luminance(rgb) -> np.ndarray:
    """FM1-FM3: 8-bit sRGB (..., 3) -> WCAG relative luminance 0..1."""
    lin = srgb_to_linear(np.asarray(rgb, dtype=np.float64) / 255.0)
    return 0.2126 * lin[..., 0] + 0.7152 * lin[..., 1] + 0.0722 * lin[..., 2]


def contrast_ratio(l1: float, l2: float) -> float:
    """FM4, unrounded."""
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def srgb_to_lab(rgb) -> np.ndarray:
    """8-bit sRGB (..., 3) -> CIELAB (D65, 2 degree)."""
    lin = srgb_to_linear(np.asarray(rgb, dtype=np.float64) / 255.0)
    xyz = lin @ M_RGB_XYZ.T / WHITE_D65
    eps, kappa = 216 / 24389, 24389 / 27
    f = np.where(xyz > eps, np.cbrt(xyz), (kappa * xyz + 16) / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], axis=-1)


def lab_to_srgb(lab) -> np.ndarray:
    lab = np.asarray(lab, dtype=np.float64)
    fy = (lab[..., 0] + 16) / 116
    fx, fz = fy + lab[..., 1] / 500, fy - lab[..., 2] / 200
    eps, kappa = 216 / 24389, 24389 / 27
    f = np.stack([fx, fy, fz], axis=-1)
    xyz = np.where(f**3 > eps, f**3, (116 * f - 16) / kappa)
    xyz[..., 1] = np.where(lab[..., 0] > kappa * eps, fy**3, lab[..., 0] / kappa)
    lin = (xyz * WHITE_D65) @ np.linalg.inv(M_RGB_XYZ).T
    return np.clip(linear_to_srgb(np.clip(lin, 0, 1)) * 255, 0, 255)


def ciede2000(lab1, lab2, kl: float = 1.0, kc: float = 1.0, kh: float = 1.0) -> np.ndarray:
    """CIEDE2000 colour difference (Sharma, Wu & Dalal 2005), vectorised over the leading axes."""
    lab1, lab2 = np.asarray(lab1, dtype=np.float64), np.asarray(lab2, dtype=np.float64)
    l1, a1, b1 = lab1[..., 0], lab1[..., 1], lab1[..., 2]
    l2, a2, b2 = lab2[..., 0], lab2[..., 1], lab2[..., 2]
    c_bar = (np.hypot(a1, b1) + np.hypot(a2, b2)) / 2
    g = 0.5 * (1 - np.sqrt(c_bar**7 / (c_bar**7 + 25.0**7)))
    a1p, a2p = (1 + g) * a1, (1 + g) * a2
    c1p, c2p = np.hypot(a1p, b1), np.hypot(a2p, b2)
    h1p = np.where((a1p == 0) & (b1 == 0), 0.0, np.degrees(np.arctan2(b1, a1p)) % 360)
    h2p = np.where((a2p == 0) & (b2 == 0), 0.0, np.degrees(np.arctan2(b2, a2p)) % 360)
    zero = (c1p * c2p) == 0
    dh = h2p - h1p
    dh = np.where(dh > 180, dh - 360, np.where(dh < -180, dh + 360, dh))
    dh = np.where(zero, 0.0, dh)
    d_lp, d_cp = l2 - l1, c2p - c1p
    d_hp = 2 * np.sqrt(c1p * c2p) * np.sin(np.radians(dh / 2))
    l_bar, cp_bar = (l1 + l2) / 2, (c1p + c2p) / 2
    hsum, hdiff = h1p + h2p, np.abs(h1p - h2p)
    h_bar = np.where(hdiff <= 180, hsum / 2, np.where(hsum < 360, (hsum + 360) / 2, (hsum - 360) / 2))
    h_bar = np.where(zero, hsum, h_bar)
    t = (
        1
        - 0.17 * np.cos(np.radians(h_bar - 30))
        + 0.24 * np.cos(np.radians(2 * h_bar))
        + 0.32 * np.cos(np.radians(3 * h_bar + 6))
        - 0.20 * np.cos(np.radians(4 * h_bar - 63))
    )
    d_theta = 30 * np.exp(-(((h_bar - 275) / 25) ** 2))
    rc = 2 * np.sqrt(cp_bar**7 / (cp_bar**7 + 25.0**7))
    sl = 1 + 0.015 * (l_bar - 50) ** 2 / np.sqrt(20 + (l_bar - 50) ** 2)
    sc = 1 + 0.045 * cp_bar
    sh = 1 + 0.015 * cp_bar * t
    rt = -np.sin(np.radians(2 * d_theta)) * rc
    tl, tc, th = d_lp / (kl * sl), d_cp / (kc * sc), d_hp / (kh * sh)
    return np.sqrt(tl**2 + tc**2 + th**2 + rt * tc * th)


# ---------------------------------------------------------------- masks and geometry (pure)


def key_mask(rgb: np.ndarray, key: tuple[int, int, int], tol: int) -> np.ndarray:
    """True = subject: pixels whose max channel difference from the key colour exceeds tol."""
    diff = np.abs(rgb[..., :3].astype(np.int16) - np.array(key, dtype=np.int16)).max(axis=-1)
    return diff > tol


def mask_from_mask_image(img: Image.Image) -> np.ndarray:
    """Black-on-white mask image (the silhouette output format): dark = subject; transparent = background."""
    if "A" in img.getbands():
        rgba = np.asarray(img.convert("RGBA"))
        return (rgba[..., 3] >= ALPHA_CUT) & (np.asarray(img.convert("L")) < MASK_CUT)
    return np.asarray(img.convert("L")) < MASK_CUT


def estimate_border_key(rgb: np.ndarray, key_tol: int) -> dict:
    """Flat-background estimate from the image border: median colour of a border strip and the share of border
    pixels within key_tol of it. `flat` = share >= BORDER_FLAT_SHARE. A border near magenta snaps to #FF00FF."""
    h, w = rgb.shape[:2]
    s = max(1, round(BORDER_STRIP * min(h, w)))
    border = np.concatenate(
        [rgb[:s].reshape(-1, 3), rgb[-s:].reshape(-1, 3), rgb[s:-s, :s].reshape(-1, 3), rgb[s:-s, -s:].reshape(-1, 3)]
    ).astype(np.int16)
    med = np.median(border, axis=0)
    key = tuple(int(round(float(c))) for c in med)
    if (np.abs(np.array(key) - np.array(hex_to_rgb(DEFAULT_KEY))) <= key_tol).all():
        key = hex_to_rgb(DEFAULT_KEY)
    share = float((np.abs(border - np.array(key, dtype=np.int16)).max(axis=1) <= key_tol).mean())
    return {"estimated_key": rgb_to_hex(key), "border_strip_px": s, "border_share_within_tol": share,
            "flat_share_needed": BORDER_FLAT_SHARE, "flat": share >= BORDER_FLAT_SHARE}


def label(mask: np.ndarray, eight: bool = False) -> tuple[np.ndarray, int]:
    """Connected-component labels (0 = outside the mask, 1..n), 4- or 8-connected. Run-length union-find, numpy only."""
    h, w = mask.shape
    d = np.diff(np.pad(mask.astype(np.int8), ((0, 0), (1, 1))), axis=1)
    parent: list[int] = []

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    ys, ss, es = [], [], []
    prev: list[tuple[int, int, int]] = []
    for y in range(h):
        starts, ends = np.flatnonzero(d[y] == 1).tolist(), np.flatnonzero(d[y] == -1).tolist()
        cur, j = [], 0
        for s, e in zip(starts, ends):
            rid = len(parent)
            parent.append(rid)
            lo, hi = (s - 1, e + 1) if eight else (s, e)
            while j < len(prev) and prev[j][1] <= lo:
                j += 1
            k = j
            while k < len(prev) and prev[k][0] < hi:
                ra, rb = find(rid), find(prev[k][2])
                if ra != rb:
                    parent[max(ra, rb)] = min(ra, rb)
                k += 1
            cur.append((s, e, rid))
            ys.append(y), ss.append(s), es.append(e)
        prev = cur
    labels = np.zeros((h, w), dtype=np.int32)
    if not parent:
        return labels, 0
    roots = np.array([find(i) for i in range(len(parent))])
    _, compact = np.unique(roots, return_inverse=True)
    ys_a, ss_a, es_a = np.array(ys), np.array(ss), np.array(es)
    lengths = es_a - ss_a
    run_of_px = np.repeat(np.arange(len(lengths)), lengths)
    xs = ss_a[run_of_px] + (np.arange(lengths.sum()) - np.repeat(np.cumsum(lengths) - lengths, lengths))
    labels[ys_a[run_of_px], xs] = compact[run_of_px] + 1
    return labels, int(compact.max()) + 1


def fill_key_holes(subject: np.ndarray) -> tuple[np.ndarray, dict]:
    """Background = key-matched pixels 4-connected to the image border; enclosed key regions become subject."""
    lab, _ = label(~subject, eight=False)
    edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    background = np.isin(lab, edge[edge > 0])
    filled = ~background
    holes = filled & ~subject
    return filled, {"hole_fill": True, "filled_holes": int(len(np.unique(lab[holes]))), "filled_area_px": int(holes.sum())}


def components(mask: np.ndarray, min_frac: float = COMPONENT_MIN_FRAC) -> list[dict]:
    """8-connected subject components with area >= min_frac of the image, in reading order: rows top to bottom
    (a component starts a new row when its top is at or below the highest bottom edge in the current row), then left to right."""
    h, w = mask.shape
    lab, n = label(mask, eight=True)
    if n == 0:
        return []
    areas = np.bincount(lab.ravel(), minlength=n + 1)
    out = []
    for i in np.flatnonzero(areas >= min_frac * h * w):
        if i == 0:
            continue
        x0, y0, x1, y1 = bbox(lab == i)
        out.append({"label": int(i), "area_px": int(areas[i]), "area_frac": float(areas[i] / (h * w)),
                    "bbox_px": {"x0": x0, "y0": y0, "x1": x1, "y1": y1, "w": x1 - x0, "h": y1 - y0}})
    out.sort(key=lambda c: c["bbox_px"]["y0"])
    rows: list[list[dict]] = []
    for c in out:
        if rows and c["bbox_px"]["y0"] < min(r["bbox_px"]["y1"] for r in rows[-1]):
            rows[-1].append(c)
        else:
            rows.append([c])
    ordered = [c for r in rows for c in sorted(r, key=lambda c: c["bbox_px"]["x0"])]
    for n_, c in enumerate(ordered, 1):
        c["n"] = n_
    return ordered


def key_subject(rgb: np.ndarray, key, tol: int, fill_holes: bool) -> tuple[np.ndarray, dict]:
    m = key_mask(rgb, key, tol)
    if fill_holes and not m.all():
        return fill_key_holes(m)
    return m, {"hole_fill": False, "filled_holes": 0, "filled_area_px": 0}


def inverted_mask_check(m: np.ndarray) -> dict:
    """Warn when a --mask image looks inverted: its border strip is nearly all subject.

    Mask images are read dark = subject (the silhouette output format). A white-subject-on-black mask makes the
    background the subject and every number describes the background, with no error (J018 marketing review).
    Never changes the mask.
    """
    h, w = m.shape
    s = max(1, round(BORDER_STRIP * min(h, w)))
    border = np.concatenate([m[:s].ravel(), m[-s:].ravel(), m[s:-s, :s].ravel(), m[s:-s, -s:].ravel()])
    share = float(border.mean())
    out = {"mask_border_subject_share": round(share, 4)}
    if share >= BORDER_FLAT_SHARE:
        out["mask_warning"] = (f"{share:.0%} of the mask's border is subject: the mask may be inverted (mask images "
                               "are read dark = subject, white = background); check it on an overlay")
    return out


def shadow_on_key_check(rgb: np.ndarray, m: np.ndarray, key) -> dict:
    """Warn when part of the subject looks like a shadow on the backdrop: the key's own colour, only darker.

    A cast shadow on a flat key falls outside --key-tol and is counted as subject with no error (J018 game-designer
    and level-design reviews: a valid mask with the wrong area). Shadow-like = chromaticity within SHADOW_CHROMA_TOL
    of the key and luminance SHADOW_LUM_RANGE of the key's. A grey subject on a grey key also matches, so this is a
    warning to check on an overlay, never a mask change.
    """
    if not m.any():
        return {}
    px = rgb[..., :3][m].astype(np.float64)
    kk = np.array(key, dtype=np.float64)
    if kk.sum() < 30:  # a near-black key has no darker shadow to find
        return {}
    chroma = px / np.maximum(px.sum(axis=1, keepdims=True), 1.0)
    kchroma = kk / kk.sum()
    lum = relative_luminance(px.reshape(-1, 1, 3)).ravel()
    klum = float(relative_luminance(kk.reshape(1, 1, 3)).ravel()[0])
    lo, hi = SHADOW_LUM_RANGE
    like = (np.abs(chroma - kchroma).max(axis=1) <= SHADOW_CHROMA_TOL) & (lum >= lo * klum) & (lum <= hi * klum)
    share = float(like.mean())
    out = {"shadow_like_share_of_subject": round(share, 4)}
    if share >= SHADOW_WARN_SHARE:
        out["shadow_warning"] = (f"{share:.0%} of the subject has the key's colour, only darker: a cast shadow or "
                                 "ambient occlusion on the backdrop may be counted as subject; check the mask on an "
                                 "overlay, or render without the shadow (shadow catcher off) or mask the subject")
    return out


def near_key_check(rgb: np.ndarray, key, key_tol: int) -> dict:
    """Warn when pixels counted as background differ from a very flat border by more than the border's own spread.

    On a flat render background (one exact colour) the default --key-tol 40 also removes subject pixels close to the
    key, such as a lit head on a grey backdrop, with no error (J018 modeler review: the box was 768 px high, the
    true height 932 px). Reports the count and a suggested tighter --key-tol; never changes the mask.
    """
    h, w = rgb.shape[:2]
    s = max(1, round(BORDER_STRIP * min(h, w)))
    border = np.concatenate(
        [rgb[:s].reshape(-1, 3), rgb[-s:].reshape(-1, 3), rgb[s:-s, :s].reshape(-1, 3), rgb[s:-s, -s:].reshape(-1, 3)]
    ).astype(np.int16)
    kk = np.array(key, dtype=np.int16)
    spread = int(np.percentile(np.abs(border - kk).max(axis=1), 99))
    tight = spread + 2
    if tight >= key_tol:
        return {"border_spread_p99": spread}
    diff = np.abs(rgb[..., :3].astype(np.int16) - kk).max(axis=-1)
    near = int(((diff > tight) & (diff <= key_tol)).sum())
    out = {"border_spread_p99": spread, "near_key_px": near}
    if near >= max(50, int(NEAR_KEY_MIN_FRAC * h * w)):
        out["near_key_warning"] = (f"{near} px differ from the flat key by {tight + 1}-{key_tol}: they are counted as "
                                   f"background, but the border itself varies by only {spread}; a subject near the key "
                                   f"colour may be cut. Re-run with --key-tol {spread + 4} and compare the mask")
        out["suggested_key_tol"] = spread + 4
    return out


def subject_mask(img: Image.Image, key: str = "auto", key_tol: int = DEFAULT_KEY_TOL, mask_img=None, fill_holes: bool = True):
    """(mask or None, source, info): --mask image > alpha channel (if any pixel is not opaque) > key colour > none.
    key "auto" estimates a flat background from the border (estimate_border_key); a hex key is used as given.
    Key masks fill enclosed key-coloured regions (fill_key_holes) unless fill_holes is False."""
    if mask_img is not None:
        m = mask_from_mask_image(mask_img)
        if m.shape != (img.height, img.width):
            raise ValueError(f"mask size {m.shape[::-1]} differs from image size {img.size}")
        return m, "mask-image", inverted_mask_check(m)
    if "A" in img.getbands():
        alpha = np.asarray(img.getchannel("A"))
        if alpha.min() < 255:
            return alpha >= ALPHA_CUT, "alpha", {}
    rgb = np.asarray(img.convert("RGB"))
    if str(key).lower() == "auto":
        info = estimate_border_key(rgb, key_tol)
        if not info["flat"]:
            return None, "none", info
        m, holes = key_subject(rgb, hex_to_rgb(info["estimated_key"]), key_tol, fill_holes)
        k = hex_to_rgb(info["estimated_key"])
        return m, "key-auto", {**info, **holes, **near_key_check(rgb, k, key_tol), **shadow_on_key_check(rgb, m, k)}
    m, holes = key_subject(rgb, hex_to_rgb(key), key_tol, fill_holes)
    if not m.all():
        return m, "key-colour", {"key": rgb_to_hex(hex_to_rgb(key)), **holes}
    return None, "none", {"key": rgb_to_hex(hex_to_rgb(key))}


def mask_problem(mask: np.ndarray | None, source: str) -> str | None:
    """Reason the mask is meaningless (no mask, near-full or near-empty), else None."""
    if mask is None or source == "none":
        return "no subject mask found (no --mask, no alpha, no flat key-colour border)"
    frac = float(mask.mean())
    if frac >= MASK_MAX_FRAC:
        return f"mask covers {frac:.4f} of the image (>= {MASK_MAX_FRAC}): background not separated"
    if frac < MASK_MIN_FRAC:
        return f"mask covers {frac:.6f} of the image (< {MASK_MIN_FRAC}): subject not found"
    return None


def problem_of(mask: np.ndarray | None, source: str, info: dict) -> str | None:
    """mask_problem, with a --box-key failure (recorded in info) taking precedence."""
    return info.get("box_problem") or mask_problem(mask, source)


def parse_box(text: str) -> tuple[int, int, int, int]:
    """'x0,y0,x1,y1' (pixels, x1/y1 exclusive) -> tuple; argparse type."""
    try:
        x0, y0, x1, y1 = (int(v) for v in str(text).split(","))
    except ValueError:
        raise argparse.ArgumentTypeError(f"box must be x0,y0,x1,y1 integers: {text!r}") from None
    if x1 <= x0 or y1 <= y0:
        raise argparse.ArgumentTypeError(f"box needs x1 > x0 and y1 > y0: {text!r}")
    return x0, y0, x1, y1


def check_box(box, shape) -> None:
    h, w = shape[:2]
    x0, y0, x1, y1 = box
    if x0 < 0 or y0 < 0 or x1 > w or y1 > h:
        raise SystemExit(f"box {list(box)} lies outside the image ({w}x{h})")


def box_masks(rgb: np.ndarray, boxes: list[dict], key_tol: int = DEFAULT_KEY_TOL, fill_holes: bool = True,
              box_key: bool = False) -> tuple[list[np.ndarray], list[dict], str | None]:
    """One full-size mask per box entry ({"box": (x0,y0,x1,y1), "name": str|None}); with box_key the pixels inside
    the box that match the box's own border colour (estimate_border_key on the crop) are dropped, enclosed
    key-coloured areas kept unless fill_holes is False. Returns (masks, per-box records, problem or None)."""
    h, w = rgb.shape[:2]
    masks, recs, problem = [], [], None
    for i, b in enumerate(boxes, 1):
        check_box(b["box"], rgb.shape)
        x0, y0, x1, y1 = b["box"]
        m = np.zeros((h, w), dtype=bool)
        rec = {"n": i, "name": b.get("name"), "box_px": list(b["box"]), "box_area_px": (x1 - x0) * (y1 - y0)}
        if box_key:
            crop = rgb[y0:y1, x0:x1, :3]
            est = estimate_border_key(crop, key_tol)
            rec["box_key"] = est
            if not est["flat"]:
                problem = problem or (f"--box-key: box {i} {list(b['box'])} border is not flat "
                                      f"({est['border_share_within_tol']:.3f} within --key-tol, need {BORDER_FLAT_SHARE})")
            else:
                sub, holes = key_subject(crop, hex_to_rgb(est["estimated_key"]), key_tol, fill_holes)
                m[y0:y1, x0:x1] = sub
                rec["box_key"].update(holes)
        else:
            m[y0:y1, x0:x1] = True
        rec["area_px"] = int(m.sum())
        masks.append(m)
        recs.append(rec)
    return masks, recs, problem


def exclusion_mask(shape, boxes=(), mask_imgs=()) -> np.ndarray:
    """Union of --exclude-box boxes and --exclude mask images (dark = excluded), full image size."""
    h, w = shape[:2]
    out = np.zeros((h, w), dtype=bool)
    for b in boxes:
        check_box(b, shape)
        x0, y0, x1, y1 = b
        out[y0:y1, x0:x1] = True
    for mi in mask_imgs:
        m = mask_from_mask_image(mi)
        if m.shape != (h, w):
            raise ValueError(f"exclude mask size {m.shape[::-1]} differs from image size {(w, h)}")
        out |= m
    return out


def sample_colour(rgb: np.ndarray, box, stat: str = "median") -> dict:
    """Rendered colour of an image box: per-channel sRGB median of the box (stat "median"), or of the darkest
    ("p10") / lightest ("p90") 10 % of its pixels by WCAG luminance (ties at the percentile included)."""
    check_box(box, rgb.shape)
    x0, y0, x1, y1 = box
    px = rgb[y0:y1, x0:x1, :3].reshape(-1, 3).astype(np.float64)
    sel = px
    if stat in ("p10", "p90"):
        lum = relative_luminance(px)
        thr = float(np.percentile(lum, 10 if stat == "p10" else 90))
        sel = px[lum <= thr] if stat == "p10" else px[lum >= thr]
    elif stat != "median":
        raise ValueError(f"unknown stat {stat!r}")
    colour = np.median(sel, axis=0)
    return {"box_px": list(box), "stat": stat, "rgb": [float(c) for c in colour], "hex": rgb_to_hex(colour),
            "n_px_box": int(len(px)), "n_px_used": int(len(sel)), "luminance": float(relative_luminance(colour))}


def resize_mask(mask: np.ndarray, size: tuple[int, int], resample) -> np.ndarray:
    """Bool mask -> bool mask at size (w, h), via the black-on-white image and the MASK_CUT threshold."""
    return mask_from_mask_image(silhouette_image(mask).resize(size, resample))


def bbox(mask: np.ndarray):
    """(x0, y0, x1, y1) with x1/y1 exclusive, or None for an empty mask."""
    ys, xs = np.nonzero(mask)
    if len(xs) == 0:
        return None
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def dilate(mask: np.ndarray, n: int) -> np.ndarray:
    """Chessboard (8-neighbour) dilation by n px."""
    out = mask.copy()
    h, w = mask.shape
    for _ in range(n):
        p = np.pad(out, 1)
        nxt = np.zeros_like(out)
        for dy in (0, 1, 2):
            for dx in (0, 1, 2):
                nxt |= p[dy : dy + h, dx : dx + w]
        out = nxt
    return out


def ring_mask(mask: np.ndarray, n: int) -> np.ndarray:
    return dilate(mask, n) & ~mask


def align_mask(mask: np.ndarray, height: int, width: int) -> np.ndarray:
    """Crop to bbox, scale to `height` keeping aspect (bilinear, threshold 0.5), centre on a height x width canvas."""
    box = bbox(mask)
    if box is None:
        return np.zeros((height, width), dtype=bool)
    x0, y0, x1, y1 = box
    crop = Image.fromarray((mask[y0:y1, x0:x1] * 255).astype(np.uint8))
    new_w = max(1, round(crop.width * height / crop.height))
    scaled = np.asarray(crop.resize((new_w, height), Image.Resampling.BILINEAR)) >= 128
    canvas = np.zeros((height, max(width, new_w)), dtype=bool)
    ox = (canvas.shape[1] - new_w) // 2
    canvas[:, ox : ox + new_w] = scaled
    return canvas


def aligned_iou(a: np.ndarray, b: np.ndarray) -> tuple[float, dict]:
    """FM6 IoU after aligning both masks to the larger bbox height, centred; returns (iou, alignment record)."""
    ba, bb = bbox(a), bbox(b)
    if ba is None or bb is None:
        return 0.0, {"method": "empty mask"}
    ha, hb = ba[3] - ba[1], bb[3] - bb[1]
    height = max(ha, hb)
    wa = round((ba[2] - ba[0]) * height / ha)
    wb = round((bb[2] - bb[0]) * height / hb)
    width = max(wa, wb)
    ma, mb = align_mask(a, height, width), align_mask(b, height, width)
    inter, union = int((ma & mb).sum()), int((ma | mb).sum())
    rec = {
        "method": "crop to bbox, scale to common bbox height keeping aspect (bilinear, threshold 0.5), centre",
        "canvas_px": [width, height],
        "scale_a": round(height / ha, 6),
        "scale_b": round(height / hb, 6),
        "bbox_a_px": list(ba),
        "bbox_b_px": list(bb),
    }
    return (inter / union if union else 0.0), rec


def silhouette_stats(mask: np.ndarray) -> dict:
    h, w = mask.shape
    box = bbox(mask)
    area = int(mask.sum())
    out = {"area_px": area, "area_frac": area / (h * w), "bbox_px": None, "bbox_frac": None}
    if box:
        x0, y0, x1, y1 = box
        out["bbox_px"] = {"x0": x0, "y0": y0, "x1": x1, "y1": y1, "w": x1 - x0, "h": y1 - y0}
        out["bbox_frac"] = {"x0": x0 / w, "y0": y0 / h, "w": (x1 - x0) / w, "h": (y1 - y0) / h}
    return out


def distribution(values: np.ndarray) -> dict | None:
    if values.size == 0:
        return None
    pct = np.percentile(values, PERCENTILES)
    return {"n_px": int(values.size), "mean": float(values.mean()), **{f"p{p}": float(v) for p, v in zip(PERCENTILES, pct)}}


def value_stats(rgb: np.ndarray, mask: np.ndarray | None, ring_px: int, valid: np.ndarray | None = None,
                exclude: np.ndarray | None = None) -> dict:
    """Luminance distributions for whole image, subject and ring; unrounded subject/ring median ratio.
    `exclude` pixels are taken out of the ring only (count recorded as ring_excluded_px)."""
    lum = relative_luminance(rgb[..., :3])
    valid = np.ones(lum.shape, dtype=bool) if valid is None else valid
    out = {"whole": distribution(lum[valid]), "subject": None, "ring": None, "subject_ring_ratio": None}
    if mask is not None:
        m = mask & valid
        ring = ring_mask(m, ring_px) & valid
        if exclude is not None:
            out["ring_excluded_px"] = int((ring & exclude).sum())
            ring &= ~exclude
        out["subject"], out["ring"] = distribution(lum[m]), distribution(lum[ring])
        if out["subject"] and out["ring"]:
            out["subject_ring_ratio"] = contrast_ratio(out["subject"]["p50"], out["ring"]["p50"])
            # the ratio is symmetric: say which side is brighter (J018 reviews: a dark subject on a light ring and
            # a light subject on a dark ring gave the same number)
            s50, r50 = out["subject"]["p50"], out["ring"]["p50"]
            out["brighter_side"] = "subject" if s50 > r50 else "ring" if r50 > s50 else "equal"
    return out


def compare_subjects(rgb: np.ndarray, subjects: dict, ring_px: int, exclude: np.ndarray | None = None) -> dict:
    """subjects: {name: bool mask}. One shared ring around the union of all subjects (exclusions removed); per
    subject its luminance distribution and the unrounded ratio of its median to the ring median; names ranked by
    subject median luminance, highest first. A measurement, never a verdict."""
    lum = relative_luminance(rgb[..., :3])
    union = np.zeros(lum.shape, dtype=bool)
    for m in subjects.values():
        union |= m
    ring = ring_mask(union, ring_px)
    excluded = 0
    if exclude is not None:
        excluded = int((ring & exclude).sum())
        ring &= ~exclude
    rd = distribution(lum[ring])
    out = {"ring": rd, "ring_basis": f"{ring_px} px chessboard ring around the union of all subjects, exclusions removed",
           "ring_excluded_px": excluded, "subjects": {}}
    for name, m in subjects.items():
        d = distribution(lum[m])
        out["subjects"][name] = {"luminance": d,
                                 "ratio_to_ring": contrast_ratio(d["p50"], rd["p50"]) if d and rd else None,
                                 "brighter_than_ring": bool(d and rd and d["p50"] > rd["p50"])}
    ranked = [n for n in subjects if out["subjects"][n]["luminance"]]
    out["rank_by_median"] = sorted(ranked, key=lambda n: -out["subjects"][n]["luminance"]["p50"])
    return out


def kmeans(points: np.ndarray, k: int, seed: int, iters: int = 50) -> np.ndarray:
    """k-means++ init then Lloyd iterations; deterministic for a seed. Distinct points <= k: they are the centres."""
    rng = np.random.default_rng(seed)
    uniq = np.unique(points, axis=0)
    if len(uniq) <= k:
        return uniq
    centres = [points[rng.integers(len(points))]]
    d2 = ((points - centres[0]) ** 2).sum(axis=1)
    for _ in range(1, k):
        centres.append(points[rng.choice(len(points), p=d2 / d2.sum())])
        d2 = np.minimum(d2, ((points - centres[-1]) ** 2).sum(axis=1))
    c = np.array(centres)
    for _ in range(iters):
        lab = assign(points, c)
        new = np.array([points[lab == i].mean(axis=0) if (lab == i).any() else c[i] for i in range(len(c))])
        if np.allclose(new, c, atol=1e-6):
            break
        c = new
    return c


def assign(points: np.ndarray, centres: np.ndarray, chunk: int = 250_000) -> np.ndarray:
    out = np.empty(len(points), dtype=np.int64)
    for s in range(0, len(points), chunk):
        p = points[s : s + chunk]
        out[s : s + chunk] = ((p[:, None, :] - centres[None, :, :]) ** 2).sum(axis=2).argmin(axis=1)
    return out


def palette_stats(rgb: np.ndarray, mask: np.ndarray | None, k: int, seed: int, roles: dict | None = None,
                  exclude: np.ndarray | None = None) -> dict:
    if exclude is not None:
        mask = (np.ones(rgb.shape[:2], dtype=bool) if mask is None else mask) & ~exclude
    px = rgb[..., :3].reshape(-1, 3) if mask is None else rgb[..., :3][mask]
    lab = srgb_to_lab(px.astype(np.float64))
    rng = np.random.default_rng(seed)
    sample = lab if len(lab) <= PALETTE_SAMPLE else lab[rng.choice(len(lab), PALETTE_SAMPLE, replace=False)]
    centres = kmeans(sample, k, seed)
    counts = np.bincount(assign(lab, centres), minlength=len(centres))
    order = np.argsort(-counts, kind="stable")
    clusters = []
    for i in order:
        c = centres[i]
        clusters.append(
            {"lab": [float(v) for v in c], "hex": rgb_to_hex(lab_to_srgb(c)), "share": float(counts[i] / len(lab))}
        )
    out = {"n_px": int(len(lab)), "k_requested": k, "k_effective": len(centres), "clusters": clusters, "roles": None}
    if roles:
        cl = np.array([c["lab"] for c in clusters])
        out["roles"] = {}
        for name, hx in roles.items():
            rl = srgb_to_lab(np.array(hex_to_rgb(hx), dtype=np.float64))
            de = ciede2000(np.broadcast_to(rl, cl.shape), cl)
            j = int(de.argmin())
            out["roles"][name] = {"hex": rgb_to_hex(hex_to_rgb(hx)), "nearest_cluster": j, "cluster_hex": clusters[j]["hex"], "delta_e2000": float(de[j])}
    return out


def fit_size(w: int, h: int, tw: int, th: int) -> tuple[int, int]:
    s = min(tw / w, th / h)
    return max(1, min(tw, round(w * s))), max(1, min(th, round(h * s)))


# ---------------------------------------------------------------- images and records


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def out_path(src: Path, out_dir: Path | None, suffix: str) -> Path:
    d = out_dir or src.parent
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{src.stem}.{suffix}.png"
    if p.resolve() == src.resolve():
        raise ValueError("diagnostic image would overwrite the input")
    return p


def luminance_image(rgb: np.ndarray) -> Image.Image:
    """Grey image whose every pixel has the same WCAG luminance as the source pixel (sRGB-encoded for viewing)."""
    lum = relative_luminance(rgb[..., :3])
    return Image.fromarray(np.round(linear_to_srgb(lum) * 255).astype(np.uint8), "L")


def silhouette_image(mask: np.ndarray) -> Image.Image:
    return Image.fromarray(np.where(mask, 0, 255).astype(np.uint8), "L")


def swatch_image(clusters: list[dict], roles: dict | None, width: int = 600, height: int = 60) -> Image.Image:
    rows = 2 if roles else 1
    img = Image.new("RGB", (width, height * rows), (255, 255, 255))
    x = 0
    for i, c in enumerate(clusters):
        w = width - x if i == len(clusters) - 1 else round(c["share"] * width)
        img.paste(hex_to_rgb(c["hex"]), (x, 0, x + w, height))
        x += w
    if roles:
        n = len(roles)
        for i, r in enumerate(roles.values()):
            x0, x1 = i * width // n, (i + 1) * width // n
            mid = (x0 + x1) // 2
            img.paste(hex_to_rgb(r["hex"]), (x0, height, mid, 2 * height))
            img.paste(hex_to_rgb(r["cluster_hex"]), (mid, height, x1, 2 * height))
    return img


def tolerance(value: float | None, source: str | None, flag: str) -> None:
    if value is not None and not source:
        raise SystemExit(f"{flag} needs --tolerance-source (where the tolerance comes from); the tool never invents one")


def base_record(check: str, path: Path, img: Image.Image, params: dict) -> dict:
    return {
        "tool": "look_check",
        "version": VERSION,
        "check": check,
        "input": {"path": str(path), "sha256": sha256(path), "size_px": [img.width, img.height], "mode": img.mode},
        "params": params,
        "measurements": {},
        "images": {},
        "verdict": "measured",
    }


def load(path: Path) -> Image.Image:
    img = Image.open(path)
    img.load()
    return img.convert("RGBA") if "A" in img.getbands() or img.mode == "P" else img.convert("RGB")


def mask_params(a) -> dict:
    return {"key": a.key.upper(), "key_tol": a.key_tol, "alpha_cut": ALPHA_CUT, "mask": a.mask,
            "key_order": "--mask | --box > alpha > key (auto = flat border estimate) > none",
            "valid_mask_frac": [MASK_MIN_FRAC, MASK_MAX_FRAC], "hole_fill": not a.keep_holes,
            "component": a.component, "component_min_frac": COMPONENT_MIN_FRAC,
            "boxes": [{"box_px": list(b["box"]), "name": b["name"]} for b in a.boxes] if a.boxes else None,
            "box_key": a.box_key, "box_coords": "pixels [x0, y0, x1, y1), x1/y1 exclusive",
            "exclude": {"boxes": [list(b) for b in a.exclude_box or []], "masks": a.exclude or [],
                        "applies_to": "value background ring and palette sampling"}
            if a.exclude or a.exclude_box else None}


def resolve_mask(a, img: Image.Image):
    """subject_mask for the CLI args; returns (mask, source, key info). --box: union of the box masks."""
    if a.boxes:
        masks, recs, problem = box_masks(np.asarray(img.convert("RGB")), a.boxes, a.key_tol, not a.keep_holes, a.box_key)
        info = {"boxes": recs}
        if problem:
            return None, "box", {**info, "box_problem": problem}
        return np.logical_or.reduce(masks), "box", info
    return subject_mask(img, a.key, a.key_tol, load(Path(a.mask)) if a.mask else None, not a.keep_holes)


def resolve_exclude(a, img: Image.Image) -> np.ndarray | None:
    if not (a.exclude or a.exclude_box):
        return None
    return exclusion_mask((img.height, img.width), a.exclude_box or [], [load(Path(p)) for p in a.exclude or []])


def prepare(a, img: Image.Image):
    """(image to measure, mask, source, info, exclude mask or None). With --component N the image is that
    component's crop (margin COMPONENT_MARGIN or the ring width), as RGBA whose alpha is the component mask;
    source "component"; the exclude mask is cropped the same way."""
    mask, src, info = resolve_mask(a, img)
    excl = resolve_exclude(a, img)
    if not a.component:
        return img, mask, src, info, excl
    comps = components(mask) if mask is not None and not problem_of(mask, src, info) else []
    if not 1 <= a.component <= len(comps):
        raise SystemExit(f"--component {a.component}: the image has {len(comps)} components above {COMPONENT_MIN_FRAC} of its area")
    c = comps[a.component - 1]
    lab, _ = label(mask, eight=True)
    m = max(COMPONENT_MARGIN, getattr(a, "ring", 0) or 0)
    b = c["bbox_px"]
    x0, y0 = max(0, b["x0"] - m), max(0, b["y0"] - m)
    x1, y1 = min(img.width, b["x1"] + m), min(img.height, b["y1"] + m)
    cmask = lab[y0:y1, x0:x1] == c["label"]
    rgba = np.array(img.convert("RGBA"))[y0:y1, x0:x1]
    rgba[..., 3] = np.where(cmask, 255, 0)
    info = {**info, "base_mask_source": src, "component": {**c, "crop_px": {"x0": x0, "y0": y0, "x1": x1, "y1": y1}, "margin_px": m},
            "components_found": len(comps)}
    return Image.fromarray(rgba, "RGBA"), cmask, "component", info, None if excl is None else excl[y0:y1, x0:x1]


def tag(a, name: str) -> str:
    return f"c{a.component}.{name}" if a.component else name


def invalidate(rec: dict, reason: str) -> None:
    rec["verdict"] = "invalid-mask"
    rec["invalid_reason"] = reason
    rec.pop("rule", None)


# ---------------------------------------------------------------- checks (thin over the pure functions)


def run_value(a) -> dict:
    path = Path(a.image)
    orig = load(path)
    if a.compare_subjects:
        if not a.boxes or a.component:
            raise SystemExit("--compare-subjects needs --box groups named with --name, and no --component")
        if any(b["name"] is None for b in a.boxes):
            raise SystemExit("--compare-subjects: every --box needs a --name after it (boxes with one name form one subject)")
    img, mask, src, kinfo, excl = prepare(a, orig)
    problem = problem_of(mask, src, kinfo)
    rgb = np.asarray(img)
    p = {**mask_params(a), "mask_source": src, "key_estimate": kinfo, "ring_px": a.ring, "ring_metric": "chessboard dilation",
         "luminance": "WCAG 2.x relative luminance (FM1-FM3, switch 0.04045)", "percentiles": list(PERCENTILES),
         "min_ratio": a.min_ratio, "tolerance_source": a.tolerance_source, "compare_subjects": a.compare_subjects}
    rec = base_record("value", path, orig, p)
    rec["measurements"] = value_stats(rgb, None if problem else mask, a.ring, exclude=excl)
    lp = out_path(path, a.out_dir, tag(a, "luminance"))
    luminance_image(rgb).save(lp)
    rec["images"]["luminance"] = str(lp)
    if problem:
        invalidate(rec, problem + "; subject/ring not measured, whole-image distribution only")
        return rec
    if a.compare_subjects:
        masks, recs, _ = box_masks(rgb, a.boxes, a.key_tol, not a.keep_holes, a.box_key)
        subjects: dict[str, np.ndarray] = {}
        for b, m in zip(a.boxes, masks):
            subjects[b["name"]] = subjects.get(b["name"], np.zeros(m.shape, dtype=bool)) | m
        cs = compare_subjects(rgb, subjects, a.ring, excl)
        for name in cs["subjects"]:
            cs["subjects"][name]["boxes_px"] = [r["box_px"] for r in recs if r["name"] == name]
            cs["subjects"][name]["area_px"] = int(subjects[name].sum())
        rec["measurements"]["compare_subjects"] = cs
    ratio = rec["measurements"]["subject_ring_ratio"]
    if a.min_ratio is not None:
        rec["verdict"] = "pass" if ratio is not None and ratio >= a.min_ratio else "fail"
        rec["rule"] = {"name": f"subject/ring median ratio >= {a.min_ratio}", "source": a.tolerance_source}
    return rec


def run_contrast(a) -> dict:
    if not a.pair and not a.sample:
        raise SystemExit("contrast needs --pair FG,BG or --sample IMAGE with --fg-box/--bg-box")
    fgb, bgb = a.fg_box or [], a.bg_box or []
    if a.sample and (not fgb or len(fgb) != len(bgb)):
        raise SystemExit(f"--sample needs as many --fg-box as --bg-box (paired in order); got {len(fgb)} and {len(bgb)}")
    if (fgb or bgb) and not a.sample:
        raise SystemExit("--fg-box/--bg-box need --sample IMAGE")
    pairs = []
    for pr in a.pair or []:
        fg, bg = (s.strip() for s in pr.split(","))
        lf, lb = (float(relative_luminance(np.array(hex_to_rgb(c)))) for c in (fg, bg))
        pairs.append({"fg": rgb_to_hex(hex_to_rgb(fg)), "bg": rgb_to_hex(hex_to_rgb(bg)), "l_fg": lf, "l_bg": lb, "ratio": contrast_ratio(lf, lb)})
    inp = None
    if a.sample:
        sp = Path(a.sample)
        simg = load(sp)
        srgb = np.asarray(simg.convert("RGB"))
        inp = {"path": str(sp), "sha256": sha256(sp), "size_px": [simg.width, simg.height], "mode": simg.mode}
        for fb, bb in zip(fgb, bgb):
            f, b = sample_colour(srgb, fb, a.fg_stat), sample_colour(srgb, bb, a.bg_stat)
            pairs.append({"fg": f["hex"], "bg": b["hex"], "l_fg": f["luminance"], "l_bg": b["luminance"],
                          "ratio": contrast_ratio(f["luminance"], b["luminance"]), "source": "sample",
                          "fg_sample": f, "bg_sample": b})
    rec = {"tool": "look_check", "version": VERSION, "check": "contrast", "input": inp,
           "params": {"pairs": a.pair, "rule": a.rule, "min_ratio": a.min_ratio, "tolerance_source": a.tolerance_source,
                      "rounding": "none (a failing ratio is never rounded up, A04)",
                      "sample": a.sample, "fg_boxes": [list(b) for b in fgb], "bg_boxes": [list(b) for b in bgb],
                      "fg_stat": a.fg_stat, "bg_stat": a.bg_stat,
                      "sample_method": "per-channel sRGB median of the box (median) or of its darkest / lightest 10 % "
                                       "of pixels by WCAG luminance (p10 / p90); luminance from the unrounded median; "
                                       "box pixels [x0, y0, x1, y1)"},
           "scope": RULE_SCOPE, "measurements": {"pairs": pairs}, "images": {}, "verdict": "measured"}
    if a.rule:
        need, src = RULES[a.rule]
        rec["rule"] = {"name": a.rule, "min_ratio": need, "source": src}
    elif a.min_ratio is not None:
        need = a.min_ratio
        rec["rule"] = {"name": f"ratio >= {need}", "min_ratio": need, "source": a.tolerance_source}
    else:
        return rec
    for q in pairs:
        q["pass"] = q["ratio"] >= need
    rec["verdict"] = "pass" if all(q["pass"] for q in pairs) else "fail"
    return rec


def run_silhouette(a) -> dict:
    path = Path(a.image)
    orig = load(path)
    img, mask, src, kinfo, _ = prepare(a, orig)
    problem = problem_of(mask, src, kinfo)
    if mask is None:
        mask = np.ones((img.height, img.width), dtype=bool)
    p = {**mask_params(a), "mask_source": src, "key_estimate": kinfo, "compare": a.compare, "compare_mask": a.compare_mask,
         "min_iou": a.min_iou, "tolerance_source": a.tolerance_source}
    rec = base_record("silhouette", path, orig, p)
    rec["measurements"] = silhouette_stats(mask)
    rec["measurements"]["components"] = [] if problem else components(mask)
    rec["measurements"]["component_count"] = len(rec["measurements"]["components"])
    sp = out_path(path, a.out_dir, tag(a, "silhouette"))
    silhouette_image(mask).save(sp)
    rec["images"]["silhouette"] = str(sp)
    other = a.compare_mask or a.compare
    if other:
        op = Path(other)
        oimg = load(op)
        if a.compare_mask:
            om, osrc, oinfo = mask_from_mask_image(oimg), "mask-image", {}
        else:
            om, osrc, oinfo = subject_mask(oimg, a.key, a.key_tol, None, not a.keep_holes)
        oproblem = mask_problem(om, osrc)
        om = np.ones((oimg.height, oimg.width), dtype=bool) if om is None else om
        rec["input"]["compare"] = {"path": str(op), "sha256": sha256(op), "size_px": [oimg.width, oimg.height],
                                   "mask_source": osrc, "key_estimate": oinfo}
        if oproblem and not problem:
            problem = "compare image: " + oproblem
        if not problem:
            iou, align = aligned_iou(mask, om)
            rec["measurements"]["compare"] = {"iou": iou, "alignment": align}
            if a.min_iou is not None:
                rec["verdict"] = "pass" if iou >= a.min_iou else "fail"
                rec["rule"] = {"name": f"aligned IoU >= {a.min_iou}", "source": a.tolerance_source}
    if problem:
        invalidate(rec, problem)
    return rec


def parse_roles(text: str | None) -> dict | None:
    if not text:
        return None
    p = Path(text)
    data = json.loads(p.read_text(encoding="utf-8") if not text.lstrip().startswith("{") and p.exists() else text)
    return {str(k): str(v) for k, v in data.items()}


def run_palette(a) -> dict:
    path = Path(a.image)
    orig = load(path)
    img, mask, src, kinfo, excl = prepare(a, orig)
    # No mask at all = whole-image palette (valid); a mask that was found but is near-full/empty is invalid.
    problem = problem_of(mask, src, kinfo) if mask is not None or src == "box" else None
    if not problem and excl is not None:
        left = int(((np.ones(excl.shape, dtype=bool) if mask is None else mask) & ~excl).sum())
        if left == 0:
            problem = "--exclude removes every sampled pixel"
    roles = parse_roles(a.roles)
    p = {**mask_params(a), "mask_source": src, "key_estimate": kinfo, "region": "whole image" if mask is None else "mask",
         "k": a.k, "seed": a.seed, "k_note": "analysis setting, not the right number of colours",
         "algorithm": "k-means++ init, Lloyd, Euclidean in CIELAB", "colour_space": "CIELAB D65 2deg from sRGB",
         "difference": "CIEDE2000 (kL=kC=kH=1)", "sample_max_px": PALETTE_SAMPLE, "roles": roles,
         "max_delta_e": a.max_delta_e, "tolerance_source": a.tolerance_source}
    rec = base_record("palette", path, orig, p)
    if problem:
        invalidate(rec, problem)
        return rec
    rec["measurements"] = palette_stats(np.asarray(img), mask, a.k, a.seed, roles, excl)
    if excl is not None:
        rec["measurements"]["excluded_px"] = int(((np.ones(excl.shape, dtype=bool) if mask is None else mask) & excl).sum())
    wp = out_path(path, a.out_dir, tag(a, "palette"))
    swatch_image(rec["measurements"]["clusters"], rec["measurements"]["roles"]).save(wp)
    rec["images"]["swatches"] = str(wp)
    if a.max_delta_e is not None and rec["measurements"]["roles"]:
        ok = all(r["delta_e2000"] <= a.max_delta_e for r in rec["measurements"]["roles"].values())
        rec["verdict"] = "pass" if ok else "fail"
        rec["rule"] = {"name": f"every role CIEDE2000 <= {a.max_delta_e}", "source": a.tolerance_source}
    return rec


def run_thumb(a) -> dict:
    path = Path(a.image)
    orig = load(path)
    # the mask method is decided on the original (or the component crop), then applied to the resampled content
    img, omask, osrc, kinfo, excl = prepare(a, orig)
    tw, th = (int(v) for v in a.size.lower().split("x"))
    cw, ch = fit_size(img.width, img.height, tw, th)
    small = img.convert("RGBA").resize((cw, ch), FILTERS[a.filter])
    thumb = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    ox, oy = (tw - cw) // 2, (th - ch) // 2
    thumb.paste(small, (ox, oy))
    valid = np.zeros((th, tw), dtype=bool)
    valid[oy : oy + ch, ox : ox + cw] = True
    p = {**mask_params(a), "mask_source": osrc, "key_estimate": kinfo, "target_px": [tw, th], "filter": a.filter,
         "aspect": "preserved, centred, transparent padding", "ring_px": a.ring}
    rec = base_record("thumb", path, orig, p)
    tp = out_path(path, a.out_dir, tag(a, f"thumb{tw}x{th}"))
    thumb.save(tp)
    content = np.asarray(thumb)[oy : oy + ch, ox : ox + cw]
    if osrc == "mask-image":
        cmask = mask_from_mask_image(load(Path(a.mask)).convert("L").resize((cw, ch), FILTERS[a.filter]))
    elif osrc == "box":
        cmask = None if omask is None else resize_mask(omask, (cw, ch), FILTERS[a.filter])
    elif osrc in ("alpha", "component"):
        cmask = content[..., 3] >= ALPHA_CUT
    elif osrc == "key-auto":
        cmask, _ = key_subject(content, hex_to_rgb(kinfo["estimated_key"]), a.key_tol, not a.keep_holes)
    elif osrc == "key-colour":
        cmask, _ = key_subject(content, hex_to_rgb(a.key), a.key_tol, not a.keep_holes)
    else:
        cmask = None
    full = None
    if cmask is not None:
        full = np.zeros((th, tw), dtype=bool)
        full[oy : oy + ch, ox : ox + cw] = cmask
    problem = kinfo.get("box_problem") or mask_problem(cmask, osrc)
    tex = None
    if excl is not None:
        tex = np.zeros((th, tw), dtype=bool)
        tex[oy : oy + ch, ox : ox + cw] = resize_mask(excl, (cw, ch), FILTERS[a.filter])
    rgb = np.asarray(thumb.convert("RGB"))
    rec["measurements"] = {
        "thumb_size_px": [tw, th],
        "content_box_px": {"x0": ox, "y0": oy, "w": cw, "h": ch},
        "scale": cw / img.width,
        "mask_source": osrc,
        "value": value_stats(rgb, None if problem else full, a.ring, valid, tex),
        "silhouette": None if problem else silhouette_stats(full),
    }
    if problem:
        rec["measurements"]["value"]["verdict"] = "invalid-mask"
        invalidate(rec, problem + "; thumbnail value subject/ring and silhouette not measured")
    sheet_h = 4 * th
    bg = (128, 128, 128, 255)
    orig = img.convert("RGBA").resize((max(1, round(img.width * sheet_h / img.height)), sheet_h), Image.Resampling.LANCZOS)
    big = thumb.resize((4 * tw, 4 * th), Image.Resampling.NEAREST)
    gap = 16
    sheet = Image.new("RGBA", (orig.width + tw + big.width + 2 * gap, sheet_h), bg)
    sheet.alpha_composite(orig, (0, 0))
    sheet.alpha_composite(thumb, (orig.width + gap, 0))
    sheet.alpha_composite(big, (orig.width + tw + 2 * gap, 0))
    shp = out_path(path, a.out_dir, tag(a, f"thumb{tw}x{th}-sheet"))
    sheet.convert("RGB").save(shp)
    rec["images"].update(thumb=str(tp), sheet=str(shp))
    rec["images"]["sheet_layout"] = "original at 4x thumb height | thumbnail 1:1 | thumbnail nearest x4 (grey = padding)"
    return rec


# ---------------------------------------------------------------- CLI


class BoxAction(argparse.Action):
    """--box: append {"box": (x0, y0, x1, y1), "name": None} to a.boxes, in command-line order."""

    def __call__(self, parser, ns, values, option_string=None):
        setattr(ns, self.dest, list(getattr(ns, self.dest) or []) + [{"box": tuple(values), "name": None}])


class NameAction(argparse.Action):
    """--name: names the --box given just before it."""

    def __call__(self, parser, ns, values, option_string=None):
        boxes = getattr(ns, "boxes", None)
        if not boxes or boxes[-1]["name"] is not None:
            parser.error("--name must follow the --box it names (one --name per --box)")
        boxes[-1]["name"] = values


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="look_check", description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="check", required=True)

    def common(sp, image=True):
        if image:
            sp.add_argument("image")
            sp.add_argument("--mask", help="mask image, dark (<128) subject on white; same size as the image")
            sp.add_argument("--key", default="auto", help="flat background key: auto (default; median of a border strip, used only if >= 90%% of border pixels are within --key-tol; a magenta border snaps to #FF00FF) or a hex colour")
            sp.add_argument("--key-tol", type=int, default=DEFAULT_KEY_TOL, help="max per-channel difference counted as key")
            sp.add_argument("--out-dir", type=Path, help="diagnostic images go here (default: next to the input)")
            sp.add_argument("--keep-holes", action="store_true",
                            help="per-pixel keying: do not fill key-coloured regions that are not connected to the border. "
                            "By default they become subject, which also fills a true enclosed negative space (e.g. a "
                            "closed handle loop); use --keep-holes or a supplied --mask when that matters")
            sp.add_argument("--component", type=int,
                            help="measure only subject component N (1-based, reading order; listed by silhouette) on its crop")
            sp.add_argument("--box", dest="boxes", action=BoxAction, type=parse_box, metavar="X0,Y0,X1,Y1",
                            help="subject = union of these boxes (repeatable; pixels, x1/y1 exclusive); mask_source 'box'; "
                            "for flat UI screenshots where no background can be keyed; not with --mask")
            sp.add_argument("--name", action=NameAction, help="name for the --box just before it (value --compare-subjects groups by name)")
            sp.add_argument("--box-key", action="store_true",
                            help="inside each --box drop pixels matching that box's own border colour (auto-key limited to the "
                            "box; border must be flat), e.g. a rounded button on a flat panel")
            sp.add_argument("--exclude", action="append", metavar="MASK",
                            help="mask image (dark = excluded, same size): removed from the value ring and palette sampling (repeatable)")
            sp.add_argument("--exclude-box", action="append", type=parse_box, metavar="X0,Y0,X1,Y1",
                            help="box removed from the value ring and palette sampling, e.g. a neighbouring control (repeatable)")
        sp.add_argument("--out", type=Path, help="also write the JSON here")
        sp.add_argument("--tolerance-source", help="where a given tolerance comes from (required with any tolerance)")

    v = sub.add_parser("value", help="WCAG luminance distributions: subject, ring, whole image")
    common(v)
    v.add_argument("--ring", type=int, default=8, help="background ring width in px around the subject edge (recorded)")
    v.add_argument("--min-ratio", type=float, help="tolerance for the subject/ring median ratio (needs --tolerance-source)")
    v.add_argument("--compare-subjects", action="store_true",
                   help="each --name group of --box is one subject: luminance per subject, ratio of each median to one shared "
                   "ring around all subjects, subjects ranked by median (no verdict)")
    c = sub.add_parser("contrast", help="WCAG ratio for hex pairs or sampled image boxes. Rules are for UI text/components only, never world art.")
    common(c, image=False)
    c.add_argument("--pair", action="append", help="FG,BG hex colours, e.g. 777777,ffffff")
    c.add_argument("--sample", help="image to sample rendered colours from (with --fg-box/--bg-box)")
    c.add_argument("--fg-box", action="append", type=parse_box, metavar="X0,Y0,X1,Y1", help="foreground box in --sample (repeatable, paired in order with --bg-box)")
    c.add_argument("--bg-box", action="append", type=parse_box, metavar="X0,Y0,X1,Y1", help="background box in --sample")
    c.add_argument("--fg-stat", choices=("median", "p10", "p90"), default="median",
                   help="median of the box, or of its darkest (p10) / lightest (p90) 10 %% by luminance")
    c.add_argument("--bg-stat", choices=("median", "p10", "p90"), default="median")
    c.add_argument("--rule", choices=sorted(RULES), help="named UI standard: " + "; ".join(f"{k} {v[0]}" for k, v in RULES.items()))
    c.add_argument("--min-ratio", type=float, help="custom tolerance (needs --tolerance-source)")
    s = sub.add_parser("silhouette", help="subject mask, bbox, area; aligned IoU with --compare")
    common(s)
    s.add_argument("--compare", help="other image; its mask is found the same way")
    s.add_argument("--compare-mask", help="other mask image (dark subject on white)")
    s.add_argument("--min-iou", type=float, help="tolerance for the aligned IoU (needs --tolerance-source)")
    p = sub.add_parser("palette", help="k-means clusters in CIELAB; CIEDE2000 to role swatches")
    common(p)
    p.add_argument("--k", type=int, default=8, help="cluster count: an analysis setting (recorded)")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--roles", help='JSON file or inline JSON: {"role": "#hex", ...}')
    p.add_argument("--max-delta-e", type=float, help="tolerance per role (needs --tolerance-source)")
    t = sub.add_parser("thumb", help="resample to the real slot size; re-run value and silhouette")
    common(t)
    t.add_argument("--size", required=True, help="target WxH in px, e.g. 150x150 or 1170x2532")
    t.add_argument("--filter", choices=sorted(FILTERS), default="lanczos")
    t.add_argument("--ring", type=int, default=2, help="ring width in px for the value re-run")
    r = sub.add_parser("reserved", help="share of pixels within a CIEDE2000 distance of reserved colour swatches (J018 G3-P8)")
    r.add_argument("image")
    r.add_argument("--swatch", action="append", required=True, help="reserved colour #RRGGBB (repeatable; add the colour as rendered too)")
    r.add_argument("--max-de", type=float, required=True, help="CIEDE2000 distance that counts as the reserved colour (the art bible's value)")
    r.add_argument("--exclude", action="append", metavar="MASK", help="mask image (dark = excluded): gameplay objects that may wear the colour")
    r.add_argument("--box", dest="boxes", action=BoxAction, type=parse_box, metavar="X0,Y0,X1,Y1", help="measure only inside this box")
    r.add_argument("--out-dir", type=Path)
    r.add_argument("--out", type=Path, help="also write the JSON here")
    x = sub.add_parser("extremes", help="near-black and clipped-white pixel counts in a box (J018 G3-P8)")
    x.add_argument("image")
    x.add_argument("--box", dest="boxes", action=BoxAction, type=parse_box, metavar="X0,Y0,X1,Y1", required=True,
                   help="the play-area box (repeatable: union)")
    x.add_argument("--exclude", action="append", metavar="MASK", help="mask image (dark = excluded): named accents allowed to be white")
    x.add_argument("--near-black", type=float, default=0.004, help="relative luminance below this counts as near-black")
    x.add_argument("--clipped", type=float, default=0.98, help="relative luminance at or above this counts as clipped white")
    x.add_argument("--out-dir", type=Path)
    x.add_argument("--out", type=Path, help="also write the JSON here")
    h = sub.add_parser("hue-spread", help="spread of the CIELAB hue angle over 4x4 blocks inside one material box (J018 G3-P8)")
    h.add_argument("image")
    h.add_argument("--box", dest="boxes", action=BoxAction, type=parse_box, metavar="X0,Y0,X1,Y1", required=True,
                   help="one box fully inside one material on its lit side")
    h.add_argument("--out", type=Path, help="also write the JSON here")
    return ap


RESERVED_IMAGE_SUFFIX = "reserved"
HUE_BLOCK = 4  # px: hue-spread block size
HUE_MIN_CHROMA = 5.0  # CIELAB chroma under which a block has no usable hue angle
HUE_VALID_CHROMA = 15.0  # hue-spread is valid only with a median chroma about this or more
HUE_VALID_BLOCKS = 0.9  # ... and this share of blocks with a usable hue


def run_reserved(a) -> dict:
    """Pixels within --max-de (CIEDE2000) of any reserved swatch, outside the exclusions: share and count.

    The kit form of the art-review look-check recipe CL1 (a k-means palette merged a 0.072 % reserved accent into a
    brown cluster, J018). A screening aid: a frame that still holds characters, effects or the HUD counts their
    reserved colours as decoration, and the lit colour drifts from the authored swatch (add it as rendered)."""
    path = Path(a.image)
    img = load(path)
    rgb = np.asarray(img.convert("RGB"))
    lab = srgb_to_lab(rgb)
    region = np.ones(rgb.shape[:2], dtype=bool)
    if a.boxes:
        region[:] = False
        for b in a.boxes:
            check_box(b["box"], rgb.shape)
            x0, y0, x1, y1 = b["box"]
            region[y0:y1, x0:x1] = True
    for e in a.exclude or []:
        m = np.asarray(Image.open(e).convert("L"))
        if m.shape != region.shape:
            raise SystemExit(f"--exclude {e}: size {m.shape[::-1]} differs from the image {rgb.shape[1::-1]}")
        region &= m >= 128
    n = int(region.sum())
    if n == 0:
        raise SystemExit("nothing left to measure: the box and exclusions cover the whole image")
    hit_any = np.zeros(region.shape, dtype=bool)
    per = []
    for sw in a.swatch:
        sl = srgb_to_lab(np.array(hex_to_rgb(sw)))
        hit = (ciede2000(lab, sl) <= a.max_de) & region
        hit_any |= hit
        per.append({"swatch": rgb_to_hex(hex_to_rgb(sw)), "px": int(hit.sum()), "share": round(float(hit.sum()) / n, 6)})
    rec = base_record("reserved", path, img, {"swatches": [p["swatch"] for p in per], "max_de": a.max_de,
                                             "metric": "CIEDE2000", "exclude": a.exclude, "boxes": a.boxes})
    rec["measurements"] = {"measured_px": n, "per_swatch": per, "px": int(hit_any.sum()),
                           "share": round(float(hit_any.sum()) / n, 6)}
    marked = np.where(hit_any, 0, 255).astype(np.uint8)
    out = out_path(path, a.out_dir, RESERVED_IMAGE_SUFFIX)
    Image.fromarray(marked).save(out)
    rec["images"]["marked"] = str(out)
    return rec


def run_extremes(a) -> dict:
    """Near-black (luminance < --near-black) and clipped-white (>= --clipped) counts inside the box, outside the
    exclusions. p5 and p95 cannot see a small black or white patch (J018: a 30x30 pure-black patch left p5 at 0.069).
    A screening aid: a JPEG capture lifts or crushes the extremes (use PNG); the HUD, sky or characters in the box count."""
    path = Path(a.image)
    img = load(path)
    rgb = np.asarray(img.convert("RGB"))
    lum = relative_luminance(rgb)
    region = np.zeros(lum.shape, dtype=bool)
    for b in a.boxes:
        check_box(b["box"], rgb.shape)
        x0, y0, x1, y1 = b["box"]
        region[y0:y1, x0:x1] = True
    for e in a.exclude or []:
        m = np.asarray(Image.open(e).convert("L"))
        if m.shape != region.shape:
            raise SystemExit(f"--exclude {e}: size {m.shape[::-1]} differs from the image {rgb.shape[1::-1]}")
        region &= m >= 128
    n = int(region.sum())
    if n == 0:
        raise SystemExit("nothing left to measure: the exclusions cover the whole box")
    black = region & (lum < a.near_black)
    white = region & (lum >= a.clipped)
    rec = base_record("extremes", path, img, {"boxes": a.boxes, "exclude": a.exclude, "near_black_below": a.near_black,
                                             "clipped_at_or_above": a.clipped, "metric": "WCAG relative luminance"})
    rec["measurements"] = {"measured_px": n, "near_black_px": int(black.sum()), "near_black_share": round(float(black.sum()) / n, 6),
                           "clipped_px": int(white.sum()), "clipped_share": round(float(white.sum()) / n, 6)}
    if path.suffix.lower() in (".jpg", ".jpeg"):
        rec["input_warning"] = "JPEG: compression lifts or crushes the extremes; measure a PNG capture"
    marked = np.full(rgb.shape, 255, dtype=np.uint8)
    marked[black] = (0, 0, 255)
    marked[white] = (255, 0, 0)
    out = out_path(path, a.out_dir, "extremes")
    Image.fromarray(marked).save(out)
    rec["images"]["marked"] = str(out)
    return rec


def run_hue_spread(a) -> dict:
    """Standard deviation of the CIELAB hue angle over 4x4 blocks inside one box (a flat or one-hue material reads low).

    The kit's one flat-fill measure (J018: a linear-RGB chromaticity spread passed one-hue materials on renders with
    a studio highlight, 19.7 and 36.3 against a limit of 8). Valid only when valid is true (median chroma about 15 or
    more, nearly all blocks with a hue); a coloured light pool or bounce in the box reads as a hue change."""
    path = Path(a.image)
    img = load(path)
    rgb = np.asarray(img.convert("RGB")).astype(np.float64)
    if len(a.boxes) != 1:
        raise SystemExit("hue-spread takes exactly one --box")
    check_box(a.boxes[0]["box"], rgb.shape)
    x0, y0, x1, y1 = a.boxes[0]["box"]
    lin = srgb_to_linear(rgb[y0:y1, x0:x1] / 255)
    hb, wb = lin.shape[0] // HUE_BLOCK, lin.shape[1] // HUE_BLOCK
    if hb == 0 or wb == 0:
        raise SystemExit(f"the box is smaller than one {HUE_BLOCK}x{HUE_BLOCK} block")
    blocks = lin[:hb * HUE_BLOCK, :wb * HUE_BLOCK].reshape(hb, HUE_BLOCK, wb, HUE_BLOCK, 3).mean((1, 3))
    lab = srgb_to_lab(linear_to_srgb(blocks) * 255).reshape(-1, 3)
    chroma = np.hypot(lab[:, 1], lab[:, 2])
    use = chroma > HUE_MIN_CHROMA
    rec = base_record("hue-spread", path, img, {"box": [x0, y0, x1, y1], "block_px": HUE_BLOCK, "min_chroma": HUE_MIN_CHROMA})
    med = float(np.median(chroma))
    share = float(use.mean())
    if use.any():
        z = np.exp(1j * np.arctan2(lab[use, 2], lab[use, 1]))
        sd = float(np.degrees(np.angle(z / z.mean())).std())
    else:
        sd = None
    rec["measurements"] = {"hue_sd_deg": None if sd is None else round(sd, 2), "median_chroma": round(med, 1),
                           "blocks_used": round(share, 3), "blocks": int(len(chroma)),
                           "valid": bool(sd is not None and med >= HUE_VALID_CHROMA and share >= HUE_VALID_BLOCKS)}
    if not rec["measurements"]["valid"]:
        rec["verdict"] = "not-measured"
        rec["not_measured_reason"] = ("near-neutral or low-chroma material: the hue angle swings with noise; judge by eye "
                                      f"(median chroma {med:.1f}, blocks with a hue {share:.0%})")
    return rec


RUNNERS = {"value": run_value, "contrast": run_contrast, "silhouette": run_silhouette, "palette": run_palette, "thumb": run_thumb,
           "reserved": run_reserved, "hue-spread": run_hue_spread, "extremes": run_extremes}


def main(argv: list[str]) -> int:
    a = build_parser().parse_args(argv)
    for flag in ("min_ratio", "min_iou", "max_delta_e"):
        tolerance(getattr(a, flag, None), getattr(a, "tolerance_source", None), "--" + flag.replace("_", "-"))
    if getattr(a, "boxes", None) and getattr(a, "mask", None):
        raise SystemExit("--box and --mask are two ways to give the subject; use one")
    if getattr(a, "box_key", False) and not getattr(a, "boxes", None):
        raise SystemExit("--box-key needs --box")
    rec = RUNNERS[a.check](a)
    text = json.dumps(rec, indent=1)
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
