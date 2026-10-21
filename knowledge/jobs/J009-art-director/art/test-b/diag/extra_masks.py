"""J009-T09 helper: rectangle masks for anime glass buttons (found by their light outer stroke)."""
import json

import numpy as np
from PIL import Image
from scipy import ndimage

R = "knowledge/jobs/J009-art-director/art/test-b/"
A = "content/ui/anime-summon/screens/"


def rgb(p):
    return np.asarray(Image.open(p).convert("RGB")).astype(int)


def P_glass_stroke(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (b > 200) & (r > 90) & (r < 200) & (g > 80) & (g < 190) & (b > r + 40)


def comp(a, win, pred):
    x0, y0, x1, y1 = win
    m = np.zeros(a.shape[:2], bool)
    m[y0:y1, x0:x1] = pred(a[y0:y1, x0:x1])
    lab, n = ndimage.label(m)
    s = ndimage.sum(m, lab, range(1, n + 1))
    c = lab == (int(np.argmax(s)) + 1)
    ys, xs = np.nonzero(c)
    return [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]


extra = {}
for key, f, win in [("ani01-odds_units", "01-main-1920.png", (50, 890, 630, 1050)),
                    ("ani03-cancel", "03-review.png", (530, 765, 950, 930)),
                    ("ani01-plus", "01-main-1920.png", (1575, 30, 1710, 160))]:
    a = rgb(A + f)
    b = comp(a, win, P_glass_stroke)
    m = np.full(a.shape[:2], 255, np.uint8)
    m[b[1]:b[3], b[0]:b[2]] = 0
    Image.fromarray(m).save(R + "masks/" + key + ".png")
    extra[key] = {"file": A + f, "box": b, "window": list(win), "predicate": "P_glass_stroke (outer light stroke), bbox filled"}
json.dump(extra, open(R + "json/boxes-extra.json", "w"), indent=1)
print(json.dumps(extra))
