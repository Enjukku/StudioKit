# Overlay the blocking map: cameras with horizontal view cones, positions per beat, action axis, labels.
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# python draw_map.py <map_f175.png> <events.json> <out.png>
import json
import math
import sys

from PIL import Image, ImageDraw, ImageFont

base, events, out = sys.argv[1], sys.argv[2], sys.argv[3]
ev = json.load(open(events, encoding="utf-8"))
im = Image.open(base).convert("RGB")
W = im.width
S = W / 66.0  # px per stud (ortho_scale 66 across the image)


def P(x, y):
    return (W / 2 + x * S, W / 2 - y * S)


d = ImageDraw.Draw(im, "RGBA")
try:
    f = ImageFont.truetype("arial.ttf", 20)
    fb = ImageFont.truetype("arialbd.ttf", 22)
except OSError:
    f = fb = ImageFont.load_default()

# action axis (explorer -> guardian), the cameras of B, C, D stay on its south side
d.line([P(-14, 0), P(14, 0)], fill=(255, 210, 80, 200), width=2)
d.text(P(13.0, 0.8), "action axis", fill=(255, 210, 80), font=f)
# moon shaft footprint
x0, y0 = P(7.5 - 2.6, 2.6)
x1, y1 = P(7.5 + 2.6, -2.6)
d.ellipse([x0, y0, x1, y1], outline=(150, 180, 255, 255), width=2)
d.text(P(10.4, -2.2), "moon shaft", fill=(150, 180, 255), font=f)


def dot(x, y, r, col, label=None, dx=0.8, dy=0.8):
    cx, cy = P(x, y)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    if label:
        d.text(P(x + dx, y + dy), label, fill=col[:3], font=f)


def arrow(a, b, col):
    (ax, ay), (bx, by) = P(*a), P(*b)
    d.line([(ax, ay), (bx, by)], fill=col, width=4)
    ang = math.atan2(by - ay, bx - ax)
    for s in (-1, 1):
        d.line([(bx, by), (bx - 16 * math.cos(ang + s * 0.5), by - 16 * math.sin(ang + s * 0.5))], fill=col, width=4)


dot(0, 0, 9, (255, 170, 60, 255), "beacon", -1.0, 4.4)
arrow((-2.5, 0), (-4.9, 0), (240, 235, 220, 255))
dot(-2.5, 0, 7, (240, 235, 220, 255))
dot(-4.9, 0, 7, (240, 235, 220, 255), "explorer (step back in C)", -11.0, 3.2)
arrow((8.0, 0), (5.0, 0), (200, 200, 210, 255))
dot(8.0, 0, 9, (200, 200, 210, 255), "guardian: kneels B-D, lunges in E", 1.0, 4.0)
dot(-1.6, -1.1, 6, (120, 220, 255, 255), "strike", -3.6, -0.6)
dot(-5.2, 29.5, 10, (40, 90, 200, 255), "EXIT (lit arch)", 1.0, -2.2)
dot(-29.7, 0, 10, (160, 160, 160, 255), "entry (play)", 1.0, 1.0)

cams = dict(ev["cameras"])
cams["PLAY"] = {"name": "PLAYCAM_beat1", "focal_mm": 14.46, "location": [-26.0, -3.5, 9.0], "look_at": [2.0, 2.5, 4.5]}
colors = {"B": (255, 120, 120), "C": (120, 255, 140), "D": (255, 120, 255), "E": (120, 200, 255), "PLAY": (180, 180, 180)}
for sid, c in cams.items():
    lx, ly = c["location"][0], c["location"][1]
    tx, ty = c["look_at"][0], c["look_at"][1]
    yaw = math.atan2(ty - ly, tx - lx)
    half = math.atan(18.0 / c["focal_mm"])  # horizontal half-angle, 36 mm sensor, HORIZONTAL fit
    L = 9.0
    col = colors[sid] + (90,)
    pts = [P(lx, ly), P(lx + L * math.cos(yaw + half), ly + L * math.sin(yaw + half)),
           P(lx + L * math.cos(yaw - half), ly + L * math.sin(yaw - half))]
    d.polygon(pts, fill=col, outline=colors[sid] + (255,))
    dot(lx, ly, 7, colors[sid] + (255,))
    d.text(P(lx - 1.0, ly - 1.4), ("CAM_" + sid) if sid != "PLAY" else "play camera (beat 1)", fill=colors[sid],
           font=fb)
d.rectangle([0, 0, W, 64], fill=(0, 0, 0, 170))
d.text((14, 8), "boss-reveal rev 5 - blocking map (top view, north up, the room is 60 studs across; previs r5 frame 175)",
       fill=(240, 240, 240), font=fb)
d.text((14, 36), "Cameras B, C, D on the south side of the axis; E over the explorer's right shoulder; cones = horizontal view at 16:9",
       fill=(220, 220, 220), font=f)
im.save(out)
print("wrote", out)
