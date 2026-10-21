# Contact sheet: images in a grid with a caption strip under each (captions are outside the images).
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# python contact_sheet.py <out.png> <cols> <thumb_w> "<title>" <img>|<caption> ...
import sys

from PIL import Image, ImageDraw, ImageFont

out, cols, tw, title = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
items = [a.split("|", 1) for a in sys.argv[5:]]
imgs = []
for path, cap in items:
    im = Image.open(path).convert("RGB")
    th = round(im.height * tw / im.width)
    imgs.append((im.resize((tw, th), Image.LANCZOS), cap))
th = max(i.height for i, _ in imgs)
cap_h, pad, head = 46, 10, 40
rows = (len(imgs) + cols - 1) // cols
W = cols * tw + (cols + 1) * pad
H = head + rows * (th + cap_h + pad) + pad
sheet = Image.new("RGB", (W, H), (24, 24, 28))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("arial.ttf", 15)
    tfont = ImageFont.truetype("arialbd.ttf", 18)
except OSError:
    font = tfont = ImageFont.load_default()
d.text((pad, 10), title, fill=(235, 235, 235), font=tfont)
for k, (im, cap) in enumerate(imgs):
    r, c = divmod(k, cols)
    x = pad + c * (tw + pad)
    y = head + r * (th + cap_h + pad)
    sheet.paste(im, (x, y))
    lines = cap.split("\\n")
    for li, line in enumerate(lines[:2]):
        d.text((x + 2, y + th + 4 + li * 19), line, fill=(220, 220, 220), font=font)
sheet.save(out)
print("wrote", out, sheet.size)
