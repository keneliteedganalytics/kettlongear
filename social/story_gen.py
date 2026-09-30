#!/usr/bin/env python3
"""Kettlon Instagram story generator.

Draws 1080x1920 story cards in the Kettlon visual grammar (ink background, brand
orange, Clash Display type, code-drawn kettlebell mark). Content comes from
calendar.json; pick a day with --day N or --date YYYY-MM-DD, or --all.

Usage:
  python3 story_gen.py --date 2026-10-01 --out out/
  python3 story_gen.py --all --out out/
Requires: Pillow. Fonts are downloaded from Fontshare on first run.
"""
import argparse, json, os, sys, io, zipfile, urllib.request, datetime as dt
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, ".fonts")
INK, ORANGE, CREAM, MUTED, LINE = "#1B1F24", "#E4572E", "#F3EFE8", "#9AA1A9", "#2C323A"
W, H = 1080, 1920
SAFE_TOP, SAFE_BOTTOM = 260, 300  # Instagram overlays profile/reply UI here


def fonts():
    os.makedirs(FONT_DIR, exist_ok=True)
    need = ["ClashDisplay-Semibold.otf", "ClashDisplay-Medium.otf", "ClashDisplay-Regular.otf"]
    if not all(os.path.exists(os.path.join(FONT_DIR, n)) for n in need):
        data = urllib.request.urlopen("https://api.fontshare.com/v2/fonts/download/clash-display", timeout=60).read()
        z = zipfile.ZipFile(io.BytesIO(data))
        for m in z.namelist():
            base = os.path.basename(m)
            if base in need:
                open(os.path.join(FONT_DIR, base), "wb").write(z.read(m))
    f = lambda name, size: ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    return f


_MARK = None
def draw_mark(d, cx, cy, s, color=ORANGE):
    """Paste the canonical Kettlon mark (from the profile image) centred at cx, cy with height s*1.6."""
    global _MARK
    if _MARK is None:
        src = Image.open(os.path.join(HERE, "mark_src.png")).convert("RGB")
        import numpy as np
        a = np.array(src); m = ((a[:, :, 0] > 150) & (a[:, :, 1] < 140)).astype("uint8") * 255
        _MARK = Image.fromarray(m, "L")
    h = int(s * 1.6); w = int(_MARK.width * h / _MARK.height)
    m = _MARK.resize((w, h), Image.LANCZOS)
    col = Image.new("RGB", (w, h), color)
    d._image.paste(col, (int(cx - w / 2), int(cy - h / 2)), m)


def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines


def text_block(d, x, y, text, font, fill, maxw, spacing=1.12, align="left"):
    lines = wrap(d, text, font, maxw)
    lh = font.size * spacing
    for i, ln in enumerate(lines):
        lx = x if align == "left" else x + (maxw - d.textlength(ln, font=font)) / 2
        d.text((lx, y + i * lh), ln, font=font, fill=fill)
    return y + len(lines) * lh


def tracked(d, x, y, text, font, fill, tracking=6):
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking
    return x


def header(d, f, kicker):
    tracked(d, 80, SAFE_TOP, kicker.upper(), f("ClashDisplay-Medium.otf", 30), ORANGE, 7)
    d.line([80, SAFE_TOP + 56, W - 80, SAFE_TOP + 56], fill=LINE, width=2)


def footer(d, f, cta):
    y = H - SAFE_BOTTOM - 140
    d.line([80, y, W - 80, y], fill=LINE, width=2)
    draw_mark(d, 112, y + 76, 40)
    d.text((160, y + 46), "KETTLON", font=f("ClashDisplay-Semibold.otf", 36), fill=CREAM)
    d.text((160, y + 92), cta, font=f("ClashDisplay-Regular.otf", 30), fill=MUTED)


def t_statement(item, f):
    im = Image.new("RGB", (W, H), INK); d = ImageDraw.Draw(im)
    header(d, f, item["kicker"])
    y = text_block(d, 80, 560, item["headline"], f("ClashDisplay-Semibold.otf", 104), CREAM, W - 160, 1.02)
    d.rectangle([80, y + 40, 200, y + 48], fill=ORANGE)
    text_block(d, 80, y + 90, item["body"], f("ClashDisplay-Regular.otf", 42), MUTED, W - 160, 1.3)
    footer(d, f, item.get("cta", "kettlongear.com"))
    return im


def t_spec(item, f):
    im = Image.new("RGB", (W, H), INK); d = ImageDraw.Draw(im)
    header(d, f, item["kicker"])
    text_block(d, 80, 400, item["headline"], f("ClashDisplay-Semibold.otf", 88), CREAM, W - 160, 1.02)
    rows = item["rows"]
    y0 = 760; rh = 200
    for i, (k, v) in enumerate(rows):
        y = y0 + i * rh
        d.rounded_rectangle([80, y, W - 80, y + rh - 24], radius=18, fill="#22272E", outline=LINE, width=2)
        d.text((120, y + 40), k, font=f("ClashDisplay-Semibold.otf", 72), fill=ORANGE)
        text_block(d, 330, y + 44, v, f("ClashDisplay-Regular.otf", 40), CREAM, W - 450, 1.25)
    text_block(d, 80, y0 + len(rows) * rh + 20, item["body"], f("ClashDisplay-Regular.otf", 36), MUTED, W - 160, 1.3)
    footer(d, f, item.get("cta", "kettlongear.com"))
    return im


def t_mark(item, f):
    im = Image.new("RGB", (W, H), INK); d = ImageDraw.Draw(im)
    draw_mark(d, W // 2, 700, 280)
    fnt = f("ClashDisplay-Semibold.otf", 150)
    x = (W - sum(d.textlength(c, font=fnt) + 18 for c in "KETTLON") + 18) / 2
    tracked(d, x, 940, "KETTLON", fnt, CREAM, 18)
    text_block(d, 80, 1090, item["headline"], f("ClashDisplay-Medium.otf", 54), ORANGE, W - 160, 1.15, align="center")
    text_block(d, 120, 1240, item["body"], f("ClashDisplay-Regular.otf", 40), MUTED, W - 240, 1.3, align="center")
    footer(d, f, item.get("cta", "kettlongear.com"))
    return im


def t_question(item, f):
    im = Image.new("RGB", (W, H), ORANGE); d = ImageDraw.Draw(im)
    tracked(d, 80, SAFE_TOP, item["kicker"].upper(), f("ClashDisplay-Medium.otf", 30), INK, 7)
    d.line([80, SAFE_TOP + 56, W - 80, SAFE_TOP + 56], fill=INK, width=2)
    y = text_block(d, 80, 560, item["headline"], f("ClashDisplay-Semibold.otf", 104), INK, W - 160, 1.02)
    text_block(d, 80, y + 70, item["body"], f("ClashDisplay-Regular.otf", 44), INK, W - 160, 1.3)
    # reply prompt box
    by = H - SAFE_BOTTOM - 330
    d.rounded_rectangle([80, by, W - 80, by + 150], radius=24, fill=INK)
    d.text((120, by + 52), item.get("prompt", "Reply to this story"), font=f("ClashDisplay-Medium.otf", 40), fill=CREAM)
    d.text((80, H - SAFE_BOTTOM - 120), "KETTLON  ·  kettlongear.com", font=f("ClashDisplay-Semibold.otf", 32), fill=INK)
    return im


TEMPLATES = {"statement": t_statement, "spec": t_spec, "mark": t_mark, "question": t_question}


def render(item, f):
    return TEMPLATES[item["template"]](item, f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date"); ap.add_argument("--day", type=int); ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", default=os.path.join(HERE, "out"))
    a = ap.parse_args()
    cal = json.load(open(os.path.join(HERE, "calendar.json")))
    start = dt.date.fromisoformat(cal["start"])
    items = cal["days"]
    f = fonts(); os.makedirs(a.out, exist_ok=True)
    if a.all:
        idx = range(len(items))
    else:
        if a.date:
            n = (dt.date.fromisoformat(a.date) - start).days
        else:
            n = (a.day or 1) - 1
        idx = [n % len(items)]  # calendar loops after day 30
    for n in idx:
        item = items[n]
        im = render(item, f)
        p = os.path.join(a.out, f"story_{n+1:02d}.jpg")
        im.save(p, quality=92)
        print(p, "|", item["headline"])
        open(os.path.join(a.out, f"story_{n+1:02d}.txt"), "w").write(item.get("caption", ""))


if __name__ == "__main__":
    main()
