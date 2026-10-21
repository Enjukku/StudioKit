"""J009-T09 art-director helper (review evidence only, not a kit tool).

Finds control bounding boxes by colour predicate inside a search window
(largest connected component), writes subject masks for look_check
(dark subject on white, same size as the screen) and a JSON of boxes.
Search windows are coarse seeds; every reported coordinate is measured
from pixels. Run from the repo root:
  python knowledge/jobs/J009-art-director/art/test-b/diag/measure_boxes.py
"""
import json
import os

import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = "knowledge/jobs/J009-art-director/art/test-b"
EGG = "content/ui/egg-shop/screens/"
ANI = "content/ui/anime-summon/screens/"


def rgb(path):
    return np.asarray(Image.open(path).convert("RGB")).astype(int)


def P_green(a):  # egg primary green face (#7CF05A -> #2FB52A) incl. light bars
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (g > r + 40) & (g > b + 40) & (g > 140)


def P_white_btn(a):  # egg utility button face (#FFFFFF -> #D3DAE4), low saturation
    mx, mn = a.max(2), a.min(2)
    return (mn > 195) & (mx - mn < 40)


def P_red(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (r > 180) & (r > g + 70) & (r > b + 60)


def P_cyan(a):  # anime crystal face (#9CF4FF -> #1A8FD6), excludes the glow halo
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (b > 200) & (g > 130) & (b > r + 50)


def P_glass_stroke(a):  # light violet stroke around anime glass buttons / panels
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (b > 200) & (r > 90) & (r < 200) & (g > 80) & (g < 190) & (b > r + 40)


def P_grey_btn(a):  # anime disabled face (#8A8AA0 -> #4A4A5E) incl. shine
    mx, mn = a.max(2), a.min(2)
    return (mn > 60) & (mx - mn < 30) & (mx < 235)


def comp(a, win, pred, fill=True):
    x0, y0, x1, y1 = win
    m = np.zeros(a.shape[:2], bool)
    m[y0:y1, x0:x1] = pred(a[y0:y1, x0:x1])
    lab, n = ndimage.label(m)
    if n == 0:
        return None, None
    sizes = ndimage.sum(m, lab, range(1, n + 1))
    k = int(np.argmax(sizes)) + 1
    c = lab == k
    if fill:
        c = ndimage.binary_fill_holes(c)
    ys, xs = np.nonzero(c)
    return [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1], c


def save_mask(c, name, grow=0, rect=False):
    m = c.copy()
    if rect:
        ys, xs = np.nonzero(m)
        m[:] = False
        m[max(ys.min() - grow, 0):ys.max() + 1 + grow, max(xs.min() - grow, 0):xs.max() + 1 + grow] = True
    elif grow:
        m = ndimage.binary_dilation(m, iterations=grow)
    img = Image.fromarray(np.where(m, 0, 255).astype(np.uint8))
    p = f"{ROOT}/masks/{name}.png"
    img.save(p)
    return p


def overlap(b1, b2):
    x0, y0 = max(b1[0], b2[0]), max(b1[1], b2[1])
    x1, y1 = min(b1[2], b2[2]), min(b1[3], b2[3])
    if x1 <= x0 or y1 <= y0:
        return {"px": 0, "box": None, "gap_x": max(b2[0] - b1[2], b1[0] - b2[2]), "gap_y": max(b2[1] - b1[3], b1[1] - b2[3])}
    return {"px": (x1 - x0) * (y1 - y0), "box": [x0, y0, x1, y1],
            "frac_of_second": round((x1 - x0) * (y1 - y0) / ((b2[2] - b2[0]) * (b2[3] - b2[1])), 3)}


def template_place(screen, sprite_path, size, win, step=4):
    """Place a keyed sprite (alpha) scaled to `size` inside `win` by least squared RGB error on opaque pixels."""
    sp = Image.open(sprite_path).convert("RGBA").resize(size, Image.LANCZOS)
    s = np.asarray(sp).astype(float)
    alpha = s[..., 3] > 200
    x0, y0, x1, y1 = win
    best = None
    sub = alpha[::3, ::3]
    srgb = s[::3, ::3, :3]
    for y in range(y0, y1 - size[1] + 1, step):
        for x in range(x0, x1 - size[0] + 1, step):
            patch = screen[y:y + size[1]:3, x:x + size[0]:3].astype(float)
            if patch.shape[:2] != sub.shape:
                continue
            e = ((patch - srgb) ** 2).sum(2)[sub].mean()
            if best is None or e < best[0]:
                best = (e, x, y)
    e, bx, by = best
    for y in range(by - step, by + step + 1):  # refine at 1 px
        for x in range(bx - step, bx + step + 1):
            patch = screen[y:y + size[1]:3, x:x + size[0]:3].astype(float)
            if patch.shape[:2] != sub.shape:
                continue
            e2 = ((patch - srgb) ** 2).sum(2)[sub].mean()
            if e2 < e:
                e, bx, by = e2, x, y
    m = np.zeros(screen.shape[:2], bool)
    h = min(size[1], screen.shape[0] - by)
    w = min(size[0], screen.shape[1] - bx)
    m[by:by + h, bx:bx + w] = alpha[:h, :w]
    return {"x": bx, "y": by, "size": list(size), "rmse_rgb": round(float(np.sqrt(e / 3)), 2)}, m


out = {"method": "colour predicate in a search window, largest connected component, holes filled; boxes [x0,y0,x1,y1) in canvas px of the 1920x1080 export", "screens": {}}


def run(key, path, items):
    a = rgb(path)
    res = {}
    for name, win, pred, mask_opts in items:
        box, c = comp(a, win, pred)
        res[name] = {"box": box, "window": list(win), "predicate": pred.__name__}
        if c is not None and mask_opts is not None:
            res[name]["mask"] = save_mask(c, f"{key}-{name}", **mask_opts)
            if mask_opts.get("rect"):
                res[name]["mask_note"] = f"bbox grown by {mask_opts.get('grow', 0)} px to include outline/halo/lip"
    out["screens"][key] = {"file": path, "items": res}
    return res


# ---- egg shop ----
for tag, f in [("egg01", "01-inspect-main-1920.png"), ("egg01v2", "01-inspect-main-1920-v2.png")]:
    run(tag, EGG + f, [
        ("buy_meadow", (760, 840, 1060, 1010), P_green, {"grow": 12, "rect": True}),
        ("chances_meadow", (760, 740, 1060, 850), P_white_btn, {"grow": 12, "rect": True}),
        ("buy_featured", (455, 840, 710, 1000), P_green, {"grow": 12, "rect": True}),
        ("chances_featured", (180, 840, 462, 1000), P_white_btn, {"grow": 12, "rect": True}),
        ("plus_coins", (525, 220, 645, 340), P_green, {"grow": 10, "rect": True}),
        ("close", (1690, 160, 1840, 310), P_red, {"grow": 10, "rect": True}),
    ])
run("egg02", EGG + "02-odds-open.png", [("buy", (200, 670, 580, 840), P_green, None)])
run("egg03", EGG + "03-review.png", [("buy", (200, 690, 580, 860), P_green, None),
                                      ("cancel", (200, 850, 580, 1000), P_white_btn, None)])
run("egg06", EGG + "06-confirmed.png", [("done", (555, 830, 960, 990), P_green, None),
                                         ("buy_again", (960, 830, 1360, 990), P_white_btn, None)])

# ---- anime summon ----
a01 = run("ani01", ANI + "01-main-1920.png", [
    ("summon_x1", (950, 870, 1410, 1060), P_cyan, {"grow": 0}),
    ("summon_x10", (1410, 870, 1870, 1060), P_cyan, {"grow": 0}),
    ("odds_units_stroke", (50, 890, 630, 1050), P_glass_stroke, None),
])
run("ani03", ANI + "03-review.png", [("confirm", (960, 750, 1400, 950), P_cyan, None)])
run("ani04", ANI + "04-commit.png", [("confirm", (960, 750, 1400, 950), P_cyan, None)])
run("ani05", ANI + "05-pending.png", [("summoning", (900, 700, 1460, 870), P_cyan, None),
                                       ("cancel_disabled", (460, 700, 880, 870), P_grey_btn, {"grow": 0})])
run("ani06", ANI + "06-reveal-1x.png", [("done", (1420, 860, 1870, 1060), P_cyan, None)])
run("ani07", ANI + "07-reveal-10x-summary.png", [("done", (1440, 900, 1890, 1080), P_cyan, None)])

# hero placement (template match of the keyed reference into the screen)
hero = {}
s01 = rgb(ANI + "01-main-1920.png")
info, m = template_place(s01, "content/ui/anime-summon/refs/keyed/kaida.png", (478, 700), (700, 100, 1420, 880))
info["mask"] = save_mask(m, "ani01-hero")
hero["ani01"] = info
s06 = rgb(ANI + "06-reveal-1x.png")
info, m = template_place(s06, "content/ui/anime-summon/refs/keyed/kaida.png", (640, 937), (60, 100, 1000, 1080))
info["mask"] = save_mask(m, "ani06-hero")
hero["ani06"] = info
out["hero_template_match"] = hero

# ---- overlaps (tap-through candidates: the commit button under the previous tap target) ----
S = out["screens"]
out["overlaps"] = {
    "egg02.buy -> egg03.buy (Chances popup Buy, then Review Buy)": overlap(S["egg02"]["items"]["buy"]["box"], S["egg03"]["items"]["buy"]["box"]),
    "egg01.buy_featured -> egg03.buy": overlap(S["egg01"]["items"]["buy_featured"]["box"], S["egg03"]["items"]["buy"]["box"]),
    "egg01.buy_meadow -> egg03.buy": overlap(S["egg01"]["items"]["buy_meadow"]["box"], S["egg03"]["items"]["buy"]["box"]),
    "ani01.summon_x1 -> ani03.confirm (if the x1 review uses this layout)": overlap(S["ani01"]["items"]["summon_x1"]["box"], S["ani03"]["items"]["confirm"]["box"]),
    "ani01.summon_x10 -> ani03.confirm": overlap(S["ani01"]["items"]["summon_x10"]["box"], S["ani03"]["items"]["confirm"]["box"]),
    "ani03.confirm -> ani05.summoning (pressed button moves/resizes)": {"before": S["ani03"]["items"]["confirm"]["box"], "after": S["ani05"]["items"]["summoning"]["box"]},
    "ani06.done -> ani01.summon_x10 (Done returns to main)": overlap(S["ani06"]["items"]["done"]["box"], S["ani01"]["items"]["summon_x10"]["box"]),
}
with open(f"{ROOT}/json/boxes.json", "w") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
