"""J009-T09 helper: masks of the visible card face (sky-blue coin card, purple featured card), holes NOT filled,
so buttons, egg art and text are excluded. Used as the 'surround' value for the buttons on that card."""
import numpy as np
from PIL import Image
from scipy import ndimage
R = "knowledge/jobs/J009-art-director/art/test-b/"
E = "content/ui/egg-shop/screens/"
def rgb(p): return np.asarray(Image.open(p).convert("RGB")).astype(int)
def P_sky(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (b > 200) & (b > r + 60) & (g > 140)
def P_purple(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (b > 190) & (r > 140) & (g < 160) & (b > g + 60)
for tag, f in [("egg01", "01-inspect-main-1920.png"), ("egg01v2", "01-inspect-main-1920-v2.png")]:
    a = rgb(E + f)
    for name, win, pred in [("card_meadow_face", (762, 380, 1062, 1020), P_sky), ("card_featured_face", (170, 380, 720, 1020), P_purple)]:
        x0, y0, x1, y1 = win
        m = np.zeros(a.shape[:2], bool)
        m[y0:y1, x0:x1] = pred(a[y0:y1, x0:x1])
        lab, n = ndimage.label(m)
        s = ndimage.sum(m, lab, range(1, n + 1))
        c = lab == (int(np.argmax(s)) + 1)
        Image.fromarray(np.where(c, 0, 255).astype(np.uint8)).save(R + f"masks/{tag}-{name}.png")
        print(tag, name, int(c.sum()))
