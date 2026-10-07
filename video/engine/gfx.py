"""Drawing helpers: cached text/emoji surfaces, easing, shapes and the Pip mascot.

Everything is drawn with pycairo onto a 1920x1080 ARGB surface. Text and emoji
go through Pillow (it handles variable fonts and colour emoji) and are cached
as cairo surfaces, so per-frame cost is just compositing.
"""
import math
import os
from functools import lru_cache

import cairo
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(os.path.dirname(HERE), ".cache")

FONT_FILES = {
    "fredoka": os.path.join(CACHE, "fonts", "Fredoka.ttf"),
    "rubik": os.path.join(CACHE, "fonts", "Rubik.ttf"),
}
EMOJI_FONT = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

# Wise Plate palette (site + branding/youtube)
C = {
    "green": "#064E3B",
    "green2": "#065F46",
    "mint": "#A7F3D0",
    "mint2": "#D1FAE5",
    "orange": "#F97316",
    "orange2": "#FDBA74",
    "cream": "#FFF7ED",
    "white": "#FFFFFF",
    "ink": "#1F2937",
    "muted": "#6B7280",
    "red": "#DC2626",
    "ok": "#16A34A",
    "purple": "#7C3AED",
    "sky": "#0EA5E9",
    "pip": "#7FA33A",
    "pip_dark": "#4D6B1F",
    "pip_light": "#B5CF6B",
}


def rgb(c, a=1.0):
    if isinstance(c, str):
        c = C.get(c, c)
        c = c.lstrip("#")
        return (int(c[0:2], 16) / 255, int(c[2:4], 16) / 255, int(c[4:6], 16) / 255, a)
    return (*c[:3], a)


# ---------------------------------------------------------------- easing
def clamp(x, a=0.0, b=1.0):
    return a if x < a else b if x > b else x


def ease_out_cubic(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3


def ease_in_out(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def ease_out_back(x, s=1.70158):
    x = clamp(x)
    x -= 1
    return x * x * ((s + 1) * x + s) + 1


def lerp(a, b, t):
    return a + (b - a) * t


# ---------------------------------------------------------------- pillow -> cairo
def pil_to_surface(img):
    img = img.convert("RGBA")
    arr = np.asarray(img).astype(np.uint16)
    a = arr[..., 3:4]
    rgbp = (arr[..., :3] * a + 127) // 255
    bgra = np.concatenate([rgbp[..., ::-1], a], axis=2).astype(np.uint8)
    h, w = bgra.shape[:2]
    stride = cairo.ImageSurface.format_stride_for_width(cairo.FORMAT_ARGB32, w)
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    surf.flush()
    dst = np.ndarray((h, stride), dtype=np.uint8, buffer=surf.get_data())
    dst[:, : w * 4] = bgra.reshape(h, w * 4)
    surf.mark_dirty()
    return surf


@lru_cache(maxsize=None)
def _font(name, size, weight):
    f = ImageFont.truetype(FONT_FILES[name], size)
    try:
        axes = f.get_variation_axes()
        vals = []
        for ax in axes:
            nm = ax.get("name", b"")
            nm = nm.decode() if isinstance(nm, bytes) else nm
            if nm.lower().startswith("weight"):
                vals.append(weight)
            else:
                vals.append(ax["default"])
        f.set_variation_by_axes(vals)
    except Exception:
        pass
    return f


def wrap(text, font, max_w):
    out = []
    for para in text.split("\n"):
        words = para.split(" ")
        line = ""
        for w in words:
            cand = (line + " " + w).strip()
            if font.getlength(cand) <= max_w or not line:
                line = cand
            else:
                out.append(line)
                line = w
        out.append(line)
    return out


@lru_cache(maxsize=4096)
def text_surface(text, size=60, font="rubik", weight=500, color="ink", max_w=None,
                 align="center", line_h=1.18, stroke=0, stroke_color="white"):
    if font == "fredoka" and any(c in text for c in "≠≤≥≈"):
        font = "rubik"  # Fredoka has no math glyphs
        weight = min(700, weight + 100)
    f = _font(font, size, weight)
    lines = wrap(text, f, max_w) if max_w else text.split("\n")
    asc, desc = f.getmetrics()
    lh = int(size * line_h)
    widths = [f.getlength(l) for l in lines]
    w = int(max(widths) + 2 * stroke + 8)
    h = int(lh * (len(lines) - 1) + asc + desc + 2 * stroke + 8)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    col = tuple(int(v * 255) for v in rgb(color))
    scol = tuple(int(v * 255) for v in rgb(stroke_color))
    for i, (l, lw) in enumerate(zip(lines, widths)):
        if align == "center":
            x = (w - lw) / 2
        elif align == "right":
            x = w - lw - stroke - 4
        else:
            x = stroke + 4
        d.text((x, stroke + 4 + i * lh), l, font=f, fill=col,
               stroke_width=stroke, stroke_fill=scol)
    return pil_to_surface(img)


@lru_cache(maxsize=512)
def emoji_surface(ch, size=120):
    f = ImageFont.truetype(EMOJI_FONT, 109)
    img = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
    ImageDraw.Draw(img).text((80, 80), ch, font=f, embedded_color=True, anchor="mm")
    bbox = img.getbbox() or (0, 0, 160, 160)
    img = img.crop(bbox)
    s = size / max(img.size)
    img = img.resize((max(1, int(img.width * s)), max(1, int(img.height * s))), Image.LANCZOS)
    return pil_to_surface(img)


@lru_cache(maxsize=64)
def png_surface(path, size):
    img = Image.open(path).convert("RGBA")
    img = img.resize((size, int(img.height * size / img.width)), Image.LANCZOS)
    return pil_to_surface(img)


def blit(ctx, surf, x, y, scale=1.0, alpha=1.0, rot=0.0, anchor="c"):
    if alpha <= 0.001 or scale <= 0.001:
        return
    w, h = surf.get_width(), surf.get_height()
    ox = {"c": -w / 2, "l": 0, "r": -w}[anchor[0]] if anchor else -w / 2
    ctx.save()
    ctx.translate(x, y)
    if rot:
        ctx.rotate(rot)
    ctx.scale(scale, scale)
    ctx.set_source_surface(surf, ox, -h / 2)
    ctx.get_source().set_filter(cairo.FILTER_GOOD)
    ctx.paint_with_alpha(alpha)
    ctx.restore()


def text(ctx, s, x, y, size=60, font="rubik", weight=500, color="ink", max_w=None,
         align="center", scale=1.0, alpha=1.0, anchor="c", stroke=0, stroke_color="white", rot=0.0):
    surf = text_surface(s, size, font, weight, color, max_w, align, 1.18, stroke, stroke_color)
    blit(ctx, surf, x, y, scale, alpha, rot, anchor)
    return surf.get_width(), surf.get_height()


def emoji(ctx, ch, x, y, size=120, scale=1.0, alpha=1.0, rot=0.0):
    blit(ctx, emoji_surface(ch, size), x, y, scale, alpha, rot)


# ---------------------------------------------------------------- shapes
def rrect(ctx, x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    ctx.arc(x + r, y + r, r, math.pi, 1.5 * math.pi)
    ctx.close_path()


def shadow_rrect(ctx, x, y, w, h, r, alpha=0.12, off=10):
    for i, k in enumerate((1.0, 0.6, 0.3)):
        ctx.set_source_rgba(0, 0, 0, alpha * k / 2)
        rrect(ctx, x - i * 3, y + off - i * 2, w + i * 6, h + i * 6, r + i * 3)
        ctx.fill()


def card(ctx, x, y, w, h, fill="white", r=28, alpha=1.0, border=None, shadow=True):
    if shadow:
        shadow_rrect(ctx, x, y, w, h, r, 0.14 * alpha)
    ctx.set_source_rgba(*rgb(fill, alpha))
    rrect(ctx, x, y, w, h, r)
    ctx.fill_preserve()
    if border:
        ctx.set_source_rgba(*rgb(border, alpha))
        ctx.set_line_width(5)
        ctx.stroke()
    else:
        ctx.new_path()


def seed_path(ctx, w, h):
    """Pumpkin-seed silhouette centred on origin, pointy end up."""
    ctx.new_path()
    ctx.move_to(0, -h / 2)
    ctx.curve_to(w * 0.42, -h * 0.40, w * 0.55, h * 0.05, w * 0.42, h * 0.30)
    ctx.curve_to(w * 0.30, h * 0.50, -w * 0.30, h * 0.50, -w * 0.42, h * 0.30)
    ctx.curve_to(-w * 0.55, h * 0.05, -w * 0.42, -h * 0.40, 0, -h / 2)
    ctx.close_path()


def seed(ctx, x, y, size, kind="green", rot=0.0, alpha=1.0):
    """A plain seed (no face). kind: green (pepita) or shell (white hulled)."""
    if size <= 0.5 or alpha <= 0:
        return
    if kind == "shell":
        body, rim, hi = "#F5EBD3", "#D8C49A", "#FFFDF6"
    else:
        body, rim, hi = C["pip"], C["pip_dark"], C["pip_light"]
    w, h = size * 0.64, size
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(rot)
    seed_path(ctx, w, h)
    ctx.set_source_rgba(*rgb(body, alpha))
    ctx.fill_preserve()
    ctx.set_source_rgba(*rgb(rim, alpha))
    ctx.set_line_width(max(2, size * 0.05))
    ctx.stroke()
    if kind == "shell":  # the raised rim of a hulled seed
        ctx.scale(0.78, 0.84)
        seed_path(ctx, w, h)
        ctx.set_source_rgba(*rgb(rim, alpha * 0.55))
        ctx.set_line_width(max(1.5, size * 0.03))
        ctx.stroke()
        ctx.scale(1 / 0.78, 1 / 0.84)
    ctx.set_source_rgba(*rgb(hi, alpha * 0.7))
    ctx.save()
    ctx.translate(-w * 0.14, -h * 0.12)
    ctx.rotate(0.35)
    ctx.scale(w * 0.10, h * 0.22)
    ctx.arc(0, 0, 1, 0, 2 * math.pi)
    ctx.restore()
    ctx.fill()
    ctx.restore()


def check_badge(ctx, x, y, r, ok=True, alpha=1.0, scale=1.0):
    if scale <= 0.001 or alpha <= 0:
        return
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(scale, scale)
    ctx.set_source_rgba(*rgb("ok" if ok else "red", alpha))
    ctx.arc(0, 0, r, 0, 2 * math.pi)
    ctx.fill()
    ctx.set_source_rgba(1, 1, 1, alpha)
    ctx.set_line_width(r * 0.24)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    if ok:
        ctx.move_to(-r * 0.45, 0.02 * r)
        ctx.line_to(-r * 0.1, r * 0.36)
        ctx.line_to(r * 0.5, -r * 0.34)
    else:
        ctx.move_to(-r * 0.36, -r * 0.36)
        ctx.line_to(r * 0.36, r * 0.36)
        ctx.move_to(r * 0.36, -r * 0.36)
        ctx.line_to(-r * 0.36, r * 0.36)
    ctx.stroke()
    ctx.restore()


def arrow(ctx, x1, y1, x2, y2, p=1.0, color="green", width=10, alpha=1.0):
    if p <= 0:
        return
    xe, ye = lerp(x1, x2, p), lerp(y1, y2, p)
    ctx.set_source_rgba(*rgb(color, alpha))
    ctx.set_line_width(width)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.move_to(x1, y1)
    ctx.line_to(xe, ye)
    ctx.stroke()
    ang = math.atan2(y2 - y1, x2 - x1)
    hl = width * 2.6
    ctx.move_to(xe, ye)
    ctx.line_to(xe - hl * math.cos(ang - 0.5), ye - hl * math.sin(ang - 0.5))
    ctx.line_to(xe - hl * math.cos(ang + 0.5), ye - hl * math.sin(ang + 0.5))
    ctx.close_path()
    ctx.fill()


def person(ctx, x, y, s, color, alpha=1.0):
    ctx.set_source_rgba(*rgb(color, alpha))
    ctx.arc(x, y - s * 0.55, s * 0.22, 0, 2 * math.pi)
    ctx.fill()
    rrect(ctx, x - s * 0.3, y - s * 0.28, s * 0.6, s * 0.78, s * 0.26)
    ctx.fill()


# ---------------------------------------------------------------- Pip
def pip(ctx, x, y, size, t, mouth=0.0, mood="happy", look=(0.0, 0.0), talking=False,
        alpha=1.0, rot=0.0, squash=0.0, wave=0.0):
    """Pip the pumpkin seed. size = body height in px. mouth in 0..1."""
    if alpha <= 0.01 or size <= 1:
        return
    w, h = size * 0.68, size
    ctx.save()
    ctx.translate(x, y)
    # soft floor shadow
    ctx.save()
    ctx.translate(0, h * 0.52)
    ctx.scale(w * 0.55, h * 0.06)
    ctx.arc(0, 0, 1, 0, 2 * math.pi)
    ctx.restore()
    ctx.set_source_rgba(0, 0, 0, 0.12 * alpha)
    ctx.fill()

    bob = math.sin(t * (5.0 if talking else 2.2)) * h * (0.025 if talking else 0.018)
    ctx.translate(0, bob)
    ctx.rotate(rot + math.sin(t * 1.3) * 0.03)
    ctx.scale(1 + squash * 0.12, 1 - squash * 0.12)

    # arms (behind body)
    for side in (-1, 1):
        sway = math.sin(t * 6 + side) * 0.25 if talking else math.sin(t * 1.5 + side) * 0.08
        lift = wave if side == 1 else 0.0
        a0 = side * (0.95 + sway) - side * lift * 1.6
        sx, sy = side * w * 0.40, h * 0.12
        ex = sx + side * math.sin(abs(a0)) * h * 0.30
        ey = sy + math.cos(a0) * h * 0.30 * (1 if lift < 0.5 else -0.4)
        if lift > 0:
            ex = sx + side * h * 0.22
            ey = sy - h * (0.10 + 0.18 * lift) + math.sin(t * 14) * h * 0.05 * lift
        ctx.set_source_rgba(*rgb("pip_dark", alpha))
        ctx.set_line_width(size * 0.045)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.move_to(sx, sy)
        ctx.curve_to(sx + side * h * 0.08, sy + h * 0.02, ex - side * h * 0.04, ey, ex, ey)
        ctx.stroke()
        ctx.arc(ex, ey, size * 0.045, 0, 2 * math.pi)
        ctx.fill()

    # body
    seed_path(ctx, w, h)
    g = cairo.LinearGradient(-w / 2, -h / 2, w / 2, h / 2)
    g.add_color_stop_rgba(0, *rgb("#9DBF4F", alpha)[:3], alpha)
    g.add_color_stop_rgba(1, *rgb("#5F8A28", alpha)[:3], alpha)
    ctx.set_source(g)
    ctx.fill_preserve()
    ctx.set_source_rgba(*rgb("pip_dark", alpha))
    ctx.set_line_width(size * 0.035)
    ctx.stroke()
    # highlight
    ctx.save()
    ctx.translate(-w * 0.18, -h * 0.20)
    ctx.rotate(0.35)
    ctx.scale(w * 0.08, h * 0.17)
    ctx.arc(0, 0, 1, 0, 2 * math.pi)
    ctx.restore()
    ctx.set_source_rgba(1, 1, 1, 0.35 * alpha)
    ctx.fill()

    # face
    ey = h * 0.02
    ex = w * 0.17
    er = size * 0.075
    blink = 1.0
    ph = (t * 0.31) % 1.0
    if ph < 0.03:
        blink = abs(ph / 0.015 - 1)
    lx, ly = look
    for side in (-1, 1):
        cx = side * ex
        if mood == "sleepy":
            ctx.set_source_rgba(*rgb("ink", alpha))
            ctx.set_line_width(size * 0.022)
            ctx.arc(cx, ey, er * 0.8, 0.15 * math.pi, 0.85 * math.pi)
            ctx.stroke()
            continue
        sy = blink * (1.25 if mood == "surprised" else 1.0)
        ctx.save()
        ctx.translate(cx, ey)
        ctx.scale(1, max(0.08, sy))
        ctx.arc(0, 0, er, 0, 2 * math.pi)
        ctx.set_source_rgba(1, 1, 1, alpha)
        ctx.fill_preserve()
        ctx.set_source_rgba(*rgb("pip_dark", alpha))
        ctx.set_line_width(size * 0.012)
        ctx.stroke()
        if blink > 0.3:
            pr = er * (0.48 if mood != "surprised" else 0.40)
            ctx.arc(lx * er * 0.4, ly * er * 0.4, pr, 0, 2 * math.pi)
            ctx.set_source_rgba(*rgb("#1F2937", alpha))
            ctx.fill()
            ctx.arc(lx * er * 0.4 - pr * 0.35, ly * er * 0.4 - pr * 0.4, pr * 0.32, 0, 2 * math.pi)
            ctx.set_source_rgba(1, 1, 1, alpha)
            ctx.fill()
        ctx.restore()
        # brows
        ctx.set_source_rgba(*rgb("pip_dark", alpha))
        ctx.set_line_width(size * 0.02)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        by = ey - er * (1.75 if mood == "surprised" else 1.45)
        tilt = {"smug": 0.18, "worried": -0.22}.get(mood, 0.0) * side
        ctx.move_to(cx - er * 0.7, by + tilt * er * (1 if side < 0 else -1))
        ctx.line_to(cx + er * 0.7, by - tilt * er * (1 if side < 0 else -1))
        ctx.stroke()

    # cheeks
    for side in (-1, 1):
        ctx.save()
        ctx.translate(side * w * 0.29, h * 0.13)
        ctx.scale(size * 0.05, size * 0.03)
        ctx.arc(0, 0, 1, 0, 2 * math.pi)
        ctx.restore()
        ctx.set_source_rgba(*rgb("#F59E8B", 0.55 * alpha))
        ctx.fill()

    # mouth
    my = h * 0.17
    mw = size * 0.10
    open_ = clamp(mouth) if talking else 0.0
    if mood == "surprised" and not talking:
        open_ = 0.55
    if open_ > 0.06:
        mh = size * (0.02 + 0.10 * open_)
        ctx.save()
        ctx.translate(0, my)
        ctx.new_path()
        ctx.move_to(-mw, 0)
        ctx.curve_to(-mw, mh * 1.4, mw, mh * 1.4, mw, 0)
        ctx.curve_to(mw * 0.6, -mh * 0.25, -mw * 0.6, -mh * 0.25, -mw, 0)
        ctx.close_path()
        ctx.set_source_rgba(*rgb("#5B1A1A", alpha))
        ctx.fill_preserve()
        ctx.save()
        ctx.clip()
        ctx.arc(0, mh * 1.05, mw * 0.55, 0, 2 * math.pi)
        ctx.set_source_rgba(*rgb("#F87171", alpha))
        ctx.fill()
        ctx.restore()
        ctx.restore()
    else:
        ctx.set_source_rgba(*rgb("#3F2A1A", alpha))
        ctx.set_line_width(size * 0.022)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        if mood == "smug":
            ctx.move_to(-mw * 0.8, my + size * 0.01)
            ctx.curve_to(-mw * 0.2, my + size * 0.04, mw * 0.5, my + size * 0.03, mw, my - size * 0.02)
        elif mood == "worried":
            ctx.move_to(-mw * 0.7, my + size * 0.03)
            ctx.curve_to(-mw * 0.2, my - size * 0.01, mw * 0.2, my - size * 0.01, mw * 0.7, my + size * 0.03)
        else:
            ctx.move_to(-mw, my)
            ctx.curve_to(-mw * 0.5, my + size * 0.06, mw * 0.5, my + size * 0.06, mw, my)
        ctx.stroke()
    ctx.restore()
