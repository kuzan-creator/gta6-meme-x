#!/usr/bin/env python3
"""Draw the Leonida Airlines boarding-pass meme at 1200x1200 with PIL.
Every word is real text rendered with system fonts, so nothing is garbled.
Run: python3 draw_meme.py  ->  meme.png (+ meme-480.png preview)"""
import math, random
from PIL import Image, ImageDraw, ImageFont

W = H = 1200
LIB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
DEJ = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
DEJ_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def text_w(draw, s, f):
    return draw.textlength(s, font=f)

def fit_font(draw, s, path, max_w, start):
    size = start
    while size > 10 and text_w(draw, s, font(path, size)) > max_w:
        size -= 2
    return font(path, size)

def star_points(cx, cy, r_out, r_in, points=5, rot=-90):
    pts = []
    for i in range(points * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / points)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts

def sparkle(draw, cx, cy, r, fill):
    draw.polygon(star_points(cx, cy, r, r * 0.28, 4), fill=fill)

# ---------- background: diagonal sunset gradient ----------
small = Image.new("RGB", (64, 64))
sp = small.load()
c_top = (255, 46, 136)     # hot pink
c_mid = (255, 122, 26)     # orange
c_bot = (16, 181, 166)     # teal
for y in range(64):
    for x in range(64):
        t = (x + y) / 126.0
        if t < 0.5:
            u = t / 0.5
            c = tuple(int(c_top[i] + (c_mid[i] - c_top[i]) * u) for i in range(3))
        else:
            u = (t - 0.5) / 0.5
            c = tuple(int(c_mid[i] + (c_bot[i] - c_mid[i]) * u) for i in range(3))
        sp[x, y] = c
img = small.resize((W, H), Image.BICUBIC)
draw = ImageDraw.Draw(img, "RGBA")

# sparkles on the background
random.seed(7)
for _ in range(14):
    x = random.randint(15, 1185); y = random.randint(15, 1185)
    r = random.randint(5, 13)
    sparkle(draw, x, y, r, (255, 255, 255, 200))
for _ in range(22):
    x = random.randint(10, 1190); y = random.randint(10, 1190)
    r = random.randint(3, 6)
    draw.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, 170))

# ---------- boarding-pass card ----------
CARD_L, CARD_R, CARD_T, CARD_B = 70, 1130, 40, 1160
draw.rounded_rectangle([CARD_L, CARD_T, CARD_R, CARD_B], radius=36, fill="white")
# black header (square bottom corners)
draw.rounded_rectangle([CARD_L, CARD_T, CARD_R, 262], radius=36, fill="black")
draw.rectangle([CARD_L, 200, CARD_R, 262], fill="black")
# magenta footer (square top corners)
draw.rounded_rectangle([CARD_L, 920, CARD_R, CARD_B], radius=36, fill="#E6007E")
draw.rectangle([CARD_L, 950, CARD_R, 1010], fill="#E6007E")

# ---------- header text ----------
f1 = fit_font(draw, "LEONIDA AIRLINES", LIB, 1000, 128)
draw.text((600, 62), "LEONIDA AIRLINES", font=f1, fill="white", anchor="ma")
f2 = fit_font(draw, "BOARDING PASS \u2014 FLIGHT GTA-VI", LIB, 1000, 72)
draw.text((600, 178), "BOARDING PASS \u2014 FLIGHT GTA-VI", font=f2, fill="white", anchor="ma")

# ---------- body ----------
f3 = fit_font(draw, "PASSENGER: EVERY FAN", LIB, 1000, 66)
draw.text((600, 288), "PASSENGER: EVERY FAN", font=f3, fill="black", anchor="ma")

f4 = fit_font(draw, "LOS SANTOS \u2192 VICE CITY", DEJ, 1000, 100)
draw.text((600, 360), "LOS SANTOS \u2192 VICE CITY", font=f4, fill="black", anchor="ma")

draw.line([110, 462, 1010, 462], fill="black", width=3)

# departed / arriving
draw.text((110, 480), "DEPARTED", font=font(LIB, 38), fill="black", anchor="la")
draw.text((1010, 480), "ARRIVING", font=font(LIB, 38), fill="black", anchor="ra")
f5 = fit_font(draw, "SEP 17, 2013", LIB, 430, 72)
draw.text((110, 522), "SEP 17, 2013", font=f5, fill="black", anchor="la")
f6 = fit_font(draw, "NOV 19, 2026", LIB, 430, 72)
draw.text((1010, 522), "NOV 19, 2026", font=f6, fill="black", anchor="ra")

draw.line([110, 618, 1010, 618], fill="black", width=3)

# gate / seat / status boxes + barcode
BOX_T, BOX_B = 638, 752
boxes = [(110, 340), (350, 580), (590, 820)]
labels = ["GATE", "SEAT", "STATUS:"]
for (x0, x1), lab in zip(boxes, labels):
    draw.rounded_rectangle([x0, BOX_T, x1, BOX_B], radius=10, outline="black", width=3)
    draw.text(((x0 + x1) / 2, BOX_T + 10), lab, font=font(LIB, 30), fill="black", anchor="ma")
draw.text((225, BOX_T + 48), "VI", font=font(LIB, 66), fill="black", anchor="ma")
draw.text((465, BOX_T + 48), "13A", font=font(LIB, 66), fill="black", anchor="ma")
draw.text((705, BOX_T + 38), "FINALLY", font=font(LIB, 33), fill="black", anchor="ma")
draw.text((705, BOX_T + 72), "BOARDING", font=font(LIB, 33), fill="black", anchor="ma")

# barcode (right column, aligned with the boxes)
random.seed(42)
bx, bw = 868, 1012
x = bx
while x < bw - 4:
    wdt = random.choice([3, 4, 5, 6, 8])
    if random.random() < 0.7:
        draw.rectangle([x, BOX_T + 4, x + wdt, BOX_B - 4], fill="black")
    x += wdt + random.choice([2, 3, 4])

# crew / baggage
draw.text((110, 766), "CREW: JASON & LUCIA", font=font(LIB, 34), fill="black", anchor="la")
f7 = fit_font(draw, "BAGGAGE: 13 YEARS OF PATIENCE \u2014 1 BAG, OVERWEIGHT", LIB, 1000, 34)
draw.text((110, 802), "BAGGAGE: 13 YEARS OF PATIENCE \u2014 1 BAG, OVERWEIGHT",
          font=f7, fill="black", anchor="la")

# ---------- red DELAYED stamp (own band, overlaps nothing) ----------
stamp = Image.new("RGBA", (640, 80), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rounded_rectangle([6, 6, 634, 74], radius=10, outline="#D50000", width=6)
sd.rounded_rectangle([14, 14, 626, 66], radius=7, outline="#D50000", width=2)
sf = fit_font(sd, "DELAYED 13 YEARS", LIB, 580, 50)
sd.text((320, 40), "DELAYED 13 YEARS", font=sf, fill="#D50000", anchor="mm")
stamp = stamp.rotate(-3, expand=True, resample=Image.BICUBIC)
sw, sh = stamp.size
img.paste(stamp, (600 - sw // 2, 888 - sh // 2), stamp)
draw = ImageDraw.Draw(img, "RGBA")

# ---------- footer: ghost + text ----------
# ghost body as one smooth polygon: dome top, straight sides, 3 scallops
gx, gy, gw, gh = 108, 972, 200, 178
pts = []
cx = gx + gw / 2
for a in range(180, -1, -6):  # dome, left -> right over the top
    r = math.radians(a)
    pts.append((cx + (gw / 2) * math.cos(r), gy + (gh * 0.52) + (gh * 0.52) * math.sin(r) * -1))
# NOTE: dome handled below by explicit arc points instead
pts = []
top_cy = gy + 88
for deg in range(180, 361, 6):
    r = math.radians(deg)
    pts.append((cx + 100 * math.cos(r), top_cy + 88 * math.sin(r)))
# right side down to hem
pts.append((gx + gw, gy + gh - 26))
# 3 scallops right -> left along the hem (semicircle bumps dipping down)
seg = gw / 3
for i in range(3):
    x1 = gx + gw - i * seg
    x0 = x1 - seg
    midx = (x0 + x1) / 2
    for deg in range(0, 181, 10):
        r = math.radians(deg)
        pts.append((midx + (seg / 2) * math.cos(r), gy + gh - 26 + 26 * math.sin(r)))
pts.append((gx, gy + gh - 26))
draw.polygon(pts, fill="white", outline="black", width=6)

# sparkle eyes
for ex in (cx - 42, cx + 42):
    sparkle(draw, ex, gy + 92, 26, "black")
    draw.ellipse([ex - 4, gy + 82, ex + 6, gy + 92], fill="white")
# open smile
draw.ellipse([cx - 15, gy + 128, cx + 15, gy + 156], fill="black")
draw.ellipse([cx - 8, gy + 142, cx + 8, gy + 154], fill="#FF8FBF")
# blush
draw.ellipse([cx - 72, gy + 118, cx - 52, gy + 130], fill="#FFB3C8")
draw.ellipse([cx + 52, gy + 118, cx + 72, gy + 130], fill="#FFB3C8")

# star coin (magenta star + yellow inner star) held at ghost's lower right
sx, sy = gx + gw - 22, gy + gh - 30
draw.polygon(star_points(sx, sy, 44, 19), fill="#E6007E", outline="black", width=5)
draw.polygon(star_points(sx, sy, 25, 11), fill="#FFC93C", outline="black", width=3)
sparkle(draw, sx + 52, sy - 48, 13, "white")
sparkle(draw, sx - 56, sy + 40, 9, "white")

# footer text
f8 = fit_font(draw, "PAID BY MY AI AGENT", LIB, 745, 86)
draw.text((352, 982), "PAID BY MY AI AGENT", font=f8, fill="white", anchor="la")
f9 = font(LIB, 34)
small = "with a bounty payout it earned on"
draw.text((352, 1092), small, font=f9, fill="white", anchor="la")
pill_x0 = 352 + int(text_w(draw, small, f9)) + 18
pill_x1 = 1108
draw.rounded_rectangle([pill_x0, 1084, pill_x1, 1136], radius=26, fill="white")
fp = fit_font(draw, "make.fun", LIB, pill_x1 - pill_x0 - 24, 42)
draw.text(((pill_x0 + pill_x1) / 2, 1110), "make.fun", font=fp, fill="black", anchor="mm")

img.save("/home/hatch/workspace/gta6-meme-x/meme.png")
img.resize((480, 480), Image.LANCZOS).save("/home/hatch/workspace/gta6-meme-x/meme-480.png")
img.convert("RGB").save("/home/hatch/workspace/gta6-meme-x/meme.jpg", quality=92)
print("saved meme.png 1200x1200, meme-480.png, meme.jpg")
