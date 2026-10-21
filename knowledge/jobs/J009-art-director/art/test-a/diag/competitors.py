"""Share of non-egg pixels at or above the egg's median WCAG luminance, by image third (diagnostic).
  python competitors.py <image> <egg mask: dark = egg> <out json>"""
import json, sys
import numpy as np
from PIL import Image
rgb = np.asarray(Image.open(sys.argv[1]).convert("RGB")).astype(np.float64) / 255
lin = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
y = lin @ np.array([0.2126, 0.7152, 0.0722])
egg = np.asarray(Image.open(sys.argv[2]).convert("L")) < 128
med = float(np.median(y[egg]))
hot = (y >= med) & ~egg
h = y.shape[0]
thirds = {name: round(float(hot[a:b].sum() / hot.size), 5) for name, (a, b) in
          {"top": (0, h // 3), "middle": (h // 3, 2 * h // 3), "bottom": (2 * h // 3, h)}.items()}
rec = {"image": sys.argv[1], "mask": sys.argv[2], "egg_median_Y": round(med, 4), "egg_area_frac": round(float(egg.mean()), 4),
       "non_egg_px_at_or_above_egg_median_frac_of_frame": round(float(hot.mean()), 5),
       "ratio_to_egg_area": round(float(hot.sum() / egg.sum()), 3), "by_third_frac_of_frame": thirds,
       "verdict": "measured (diagnostic)"}
over = (np.asarray(Image.open(sys.argv[1]).convert("RGB")) * 0.35).astype(np.uint8)
over[hot] = (0, 255, 255); over[egg] = (255, 0, 255)
Image.fromarray(over).save(sys.argv[3].replace(".json", "-overlay.png"))
open(sys.argv[3], "w").write(json.dumps(rec, indent=2)); print(json.dumps(rec))
