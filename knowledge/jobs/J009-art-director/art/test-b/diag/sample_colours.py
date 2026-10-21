"""J009-T09 helper: rendered colour modes inside text boxes (quantised to 8 levels/channel, then the exact
mean of each bucket). The two biggest buckets are normally background and text fill; the script prints the
top 5 so the pair can be checked. Output: json/colour-samples.json. Pairs then go to look_check contrast."""
import json

import numpy as np
from PIL import Image

E = "content/ui/egg-shop/screens/"
A = "content/ui/anime-summon/screens/"
BOXES = {
    "E1 review muted labels (Cost/You have/After)": (E + "03-review.png", (235, 540, 400, 670)),
    "E2 odds column head 'Pet'": (E + "02-odds-open.png", (715, 340, 780, 378)),
    "E3 odds footnote": (E + "02-odds-open.png", (620, 908, 1580, 947)),
    "E4 confirmed 'Added to your pets.'": (E + "06-confirmed.png", (790, 788, 1132, 826)),
    "E5 failed body muted": (E + "07-failed.png", (560, 620, 1362, 712)),
    "E6 card name 'Meadow Egg'": (E + "01-inspect-main-1920.png", (800, 400, 1025, 447)),
    "E7 Buy label on green face": (E + "01-inspect-main-1920.png", (865, 895, 960, 952)),
    "E8 sunburst ray on panel": (E + "06-confirmed.png", (1100, 465, 1230, 505)),
    "E9 'Need more' label on grey": (E + "01-inspect-main-1920.png", (1480, 895, 1720, 952)),
    "E10 focus ring on white panel": (E + "03-review.png", (240, 690, 540, 712)),
    "E11 need-coins muted labels": (E + "08-not-enough-coins.png", (718, 622, 880, 712)),
    "A1 'Ends in 6d 12h'": (A + "01-main-1920.png", (95, 318, 382, 360)),
    "A2 'Sure Mythic in 53 summons'": (A + "01-main-1920.png", (95, 785, 648, 830)),
    "A3a MYTHIC word": (A + "01-main-1920.png", (230, 443, 390, 485)),
    "A3b LEGENDARY word": (A + "01-main-1920.png", (230, 498, 482, 540)),
    "A3c EPIC word": (A + "01-main-1920.png", (230, 555, 326, 596)),
    "A3d RARE word": (A + "01-main-1920.png", (230, 610, 345, 652)),
    "A4 pity count '37 / 90'": (A + "01-main-1920.png", (525, 688, 666, 730)),
    "A5 review pity line (yellow)": (A + "03-review.png", (460, 598, 1342, 642)),
    "A6 review chance line (muted)": (A + "03-review.png", (460, 485, 1445, 575)),
    "A7 reveal fact line (muted)": (A + "06-reveal-1x.png", (1000, 475, 1715, 566)),
    "A8 SUMMON label on crystal": (A + "01-main-1920.png", (1025, 905, 1335, 957)),
    "A9 10x pity line (yellow)": (A + "07-reveal-10x-summary.png", (60, 968, 850, 1012)),
    "A10 disabled CANCEL label on grey": (A + "05-pending.png", (565, 758, 775, 812)),
    "A11 card EPIC word on ink strip": (A + "07-reveal-10x-summary.png", (815, 410, 912, 450)),
    "A12 '-50' debit": (A + "06-reveal-1x.png", (1105, 72, 1187, 116)),
    "A13 odds intro (muted)": (A + "02-odds-open.png", (200, 168, 1625, 258)),
    "A14 '0.5 % per summon' on banner": (A + "01-main-1920.png", (1360, 598, 1792, 642)),
    "A15 focus ring on popup panel": (A + "03-review.png", (970, 758, 1392, 772)),
}


def modes(img, box, k=5):
    x0, y0, x1, y1 = box
    p = img[y0:y1, x0:x1].reshape(-1, 3)
    q = p // 32
    keys, inv, counts = np.unique(q, axis=0, return_inverse=True, return_counts=True)
    order = np.argsort(-counts)[:k]
    res = []
    for o in order:
        mean = p[inv.ravel() == o].mean(0).round().astype(int)
        res.append({"hex": "%02x%02x%02x" % tuple(mean), "share": round(float(counts[o] / len(p)), 3)})
    return res


out = {}
cache = {}
for name, (path, box) in BOXES.items():
    if path not in cache:
        cache[path] = np.asarray(Image.open(path).convert("RGB")).astype(int)
    out[name] = {"file": path, "box": list(box), "modes": modes(cache[path], box)}
json.dump(out, open("knowledge/jobs/J009-art-director/art/test-b/json/colour-samples.json", "w"), indent=1)
for n, v in out.items():
    print(n, " | ".join(f"{m['hex']} {m['share']}" for m in v["modes"]))
