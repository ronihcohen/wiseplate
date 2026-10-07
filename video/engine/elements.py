"""Scene elements. Each renderer gets (ctx, el, t, tl) where el["_at"] is the
absolute appear time (resolved by the timeline) and t is the absolute time."""
import math

import cairo

import gfx
from gfx import C, rgb, clamp, ease_out_back, ease_out_cubic, lerp

APPEAR = 0.45


def progress(el, t, dur=APPEAR):
    return clamp((t - el["_at"]) / dur)


def out_alpha(el, t):
    if el.get("_out") is None:
        return 1.0
    return 1.0 - clamp((t - el["_out"]) / 0.3)


def pop(el, t):
    """(scale, alpha, dy) for the element's entrance."""
    p = progress(el, t)
    a = out_alpha(el, t)
    anim = el.get("anim", "pop")
    if anim == "fade":
        return 1.0, ease_out_cubic(p) * a, 0
    if anim == "up":
        return 1.0, ease_out_cubic(p) * a, (1 - ease_out_cubic(p)) * 40
    return max(0.0, ease_out_back(p, 2.2)), clamp(p * 3) * a, 0


# ---------------------------------------------------------------- renderers
def r_text(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    if a <= 0:
        return
    rot = el.get("rot", 0.0)
    w, h = gfx.text(ctx, el["text"], el["x"], el["y"] + dy, el.get("size", 64), el.get("font", "rubik"),
                    el.get("weight", 500), el.get("color", "ink"), el.get("max_w"), el.get("align", "center"),
                    scale=s, alpha=a, anchor=el.get("anchor", "c"), rot=rot,
                    stroke=el.get("stroke", 0), stroke_color=el.get("stroke_color", "white"))
    if el.get("_strike") is not None:
        p = clamp((t - el["_strike"]) / 0.35)
        if p > 0:
            x0 = el["x"] - w / 2 if el.get("anchor", "c") == "c" else el["x"]
            ctx.set_source_rgba(*rgb("ink", 0.85 * a))
            ctx.set_line_width(12)
            ctx.set_line_cap(cairo.LINE_CAP_ROUND)
            ctx.move_to(x0 + 10, el["y"] + 8)
            ctx.line_to(x0 + 10 + (w - 20) * ease_out_cubic(p), el["y"] - 4 + 8)
            ctx.stroke()


def r_emoji(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    rot = math.sin(t * 2.5) * 0.08 if el.get("wobble") else 0.0
    bob = math.sin(t * 2 + el["x"] * 0.01) * 6
    gfx.emoji(ctx, el["ch"], el["x"], el["y"] + dy + bob, el.get("size", 140), s, a, rot)


def r_card(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    if a <= 0:
        return
    w, h = el["w"], el["h"]
    ctx.save()
    ctx.translate(el["x"], el["y"] + dy)
    ctx.scale(s, s)
    gfx.card(ctx, -w / 2, -h / 2, w, h, el.get("fill", "white"), 30, a)
    ex = -w / 2 + 30
    has_e = bool(el.get("emoji"))
    es = min(h * 0.55, 96)
    if has_e:
        gfx.emoji(ctx, el["emoji"], ex + es / 2 + 6, 0, es, 1.0, a)
    tx = ex + (es + 34 if has_e else 10)
    maxw = w - (tx + w / 2) - 24
    tc = el.get("title_color", "green")
    body = el.get("body")
    tsize = 52 if h >= 150 else 46
    if body:
        gfx.text(ctx, el["title"], tx, -h * 0.16, tsize, "fredoka", 600, tc, maxw, "left", alpha=a, anchor="l")
        bc = "#C7D2FE" if tc == "white" else "muted"
        gfx.text(ctx, body, tx, h * 0.22, 36, "rubik", 400, bc, maxw, "left", alpha=a, anchor="l")
    else:
        gfx.text(ctx, el["title"], tx, 0, tsize, "fredoka", 600, tc, maxw, "left", alpha=a, anchor="l")
    ctx.restore()


def r_pill(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    if a <= 0:
        return
    surf = gfx.text_surface(el["text"], 42, "rubik", 600, "white")
    w, h = surf.get_width() + 60, 76
    ctx.save()
    ctx.translate(el["x"], el["y"] + dy)
    ctx.scale(s, s)
    gfx.card(ctx, -w / 2, -h / 2, w, h, el.get("color", "green"), h / 2, a)
    gfx.blit(ctx, surf, 0, 0, 1, a)
    ctx.restore()


def r_banner(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    if a <= 0:
        return
    surf = gfx.text_surface(el["text"], 60, "fredoka", 700, "white")
    w, h = surf.get_width() + 90, 110
    ctx.save()
    ctx.translate(el["x"], el["y"] + dy)
    ctx.rotate(-0.025)
    ctx.scale(s, s)
    gfx.card(ctx, -w / 2, -h / 2, w, h, el.get("color", "orange"), 24, a)
    gfx.blit(ctx, surf, 0, 0, 1, a)
    ctx.restore()


def r_stat(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    if a <= 0:
        return
    w, h = el["w"], el["h"]
    p = ease_out_cubic(clamp((t - el["_at"]) / 1.1))
    v = el["value"] * p
    dec = el.get("decimals", 0)
    txt = f"{v:,.{dec}f}{el.get('unit', '')}"
    ctx.save()
    ctx.translate(el["x"], el["y"] + dy)
    ctx.scale(s, s)
    gfx.card(ctx, -w / 2, -h / 2, w, h, "white", 34, a)
    if el.get("emoji"):
        gfx.emoji(ctx, el["emoji"], 0, -h / 2 + 62, 74, 1, a)
    gfx.text(ctx, txt, 0, 10, 104, "fredoka", 700, el.get("color", "green"), alpha=a)
    gfx.text(ctx, el["label"], 0, h / 2 - 52, 36, "rubik", 500, "muted", w - 40, alpha=a)
    ctx.restore()


def r_bars(ctx, el, t, tl):
    x0, y0, W, rh = el["x"], el["y"], el["w"], el.get("row_h", 90)
    label_w = 300
    for i, row in enumerate(el["rows"]):
        at = row["_at"]
        p = clamp((t - at) / 0.9)
        a = clamp((t - at) / 0.25)
        if a <= 0:
            continue
        y = y0 + i * rh
        gfx.text(ctx, row["label"], x0 + label_w - 20, y, 46, "fredoka", 600, "ink", alpha=a, anchor="r")
        bw = (W - label_w - 120) * row["value"] / el["max"] * ease_out_cubic(p)
        ctx.set_source_rgba(*rgb("#E5E7EB", a))
        gfx.rrect(ctx, x0 + label_w, y - 28, W - label_w - 120, 56, 28)
        ctx.fill()
        if bw > 4:
            ctx.set_source_rgba(*rgb(row["color"], a))
            gfx.rrect(ctx, x0 + label_w, y - 28, max(56, bw), 56, 28)
            ctx.fill()
        dec = row.get("decimals", el.get("decimals", 0))
        val = f'{row["value"] * ease_out_cubic(p):.{dec}f}{row.get("unit", el.get("unit", "%"))}'
        if row.get("text") and p >= 1:
            val = row["text"]
        gfx.text(ctx, val, x0 + label_w + max(56, bw) + 20, y, 46, "fredoka", 700, row["color"], alpha=a, anchor="l")
        if row.get("star") and p >= 1:
            pulse = 1 + 0.08 * math.sin(t * 6)
            gfx.emoji(ctx, "⭐", x0 + label_w + bw + 150, y, 54, pulse, a)


def r_versus(ctx, el, t, tl):
    """Side-by-side comparison: per row, two bars (A on top, B below), each
    scaled to that row's larger value. Rows: label, a, b, unit, decimals, at."""
    x0, y0, W, rh = el["x"], el["y"], el["w"], el.get("row_h", 120)
    label_w = el.get("label_w", 300)
    ca, cb = el.get("color_a", "green"), el.get("color_b", "#94A3B8")
    a0 = clamp((t - el["_at"]) / 0.3)
    if a0 > 0 and el.get("names"):  # legend
        na, nb = el["names"]
        lx = x0 + label_w
        ctx.set_source_rgba(*rgb(ca, a0))
        gfx.rrect(ctx, lx, y0 - 92, 40, 40, 12)
        ctx.fill()
        wa, _ = gfx.text(ctx, na, lx + 56, y0 - 72, 40, "fredoka", 600, ca, alpha=a0, anchor="l")
        ctx.set_source_rgba(*rgb(cb, a0))
        gfx.rrect(ctx, lx + 56 + wa + 50, y0 - 92, 40, 40, 12)
        ctx.fill()
        gfx.text(ctx, nb, lx + 56 + wa + 106, y0 - 72, 40, "fredoka", 600, "#64748B", alpha=a0, anchor="l")
    full = W - label_w - 200
    for i, row in enumerate(el["rows"]):
        at = row["_at"]
        p = ease_out_cubic(clamp((t - at) / 0.9))
        a = clamp((t - at) / 0.25)
        if a <= 0:
            continue
        y = y0 + i * rh
        gfx.text(ctx, row["label"], x0 + label_w - 24, y, 44, "fredoka", 600, "ink", alpha=a, anchor="r")
        m = max(row["a"], row["b"]) or 1
        dec = row.get("decimals", 0)
        unit = row.get("unit", "")
        for j, (v, c) in enumerate(((row["a"], ca), (row["b"], cb))):
            yy = y - 24 + j * 48
            bw = max(40, full * v / m * p)
            ctx.set_source_rgba(*rgb(c, a))
            gfx.rrect(ctx, x0 + label_w, yy - 19, bw, 38, 19)
            ctx.fill()
            txt = row.get(("a_text", "b_text")[j]) if p >= 1 else None
            gfx.text(ctx, txt or f"{v * p:.{dec}f}{unit}", x0 + label_w + bw + 16, yy, 36, "fredoka", 700,
                     c if j == 0 else "#64748B", alpha=a, anchor="l")


def r_ring(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    if a <= 0:
        return
    p = ease_out_cubic(clamp((t - el["_at"]) / 1.3))
    x, y, r = el["x"], el["y"] + dy, el["r"]
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(s, s)
    ctx.set_source_rgba(1, 1, 1, a)
    ctx.arc(0, 0, r + 26, 0, 2 * math.pi)
    ctx.fill()
    ctx.set_line_width(r * 0.24)
    ctx.set_source_rgba(*rgb("#E5E7EB", a))
    ctx.arc(0, 0, r, 0, 2 * math.pi)
    ctx.stroke()
    ctx.set_source_rgba(*rgb(el["color"], a))
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.arc(0, 0, r, -math.pi / 2, -math.pi / 2 + 2 * math.pi * el["value"] / 100 * p + 1e-3)
    ctx.stroke()
    gfx.text(ctx, f"{int(round(el['value'] * p))}%", 0, -r * 0.08, int(r * 0.62), "fredoka", 700, el["color"], alpha=a)
    gfx.text(ctx, el["label"], 0, r * 0.38, int(r * 0.2), "rubik", 600, "muted", alpha=a)
    ctx.restore()


def r_people(ctx, el, t, tl):
    a = clamp((t - el["_at"]) / 0.3)
    if a <= 0:
        return
    n, k, sz = el["n"], el["k"], el.get("size", 90)
    gap = sz * 1.05
    x0 = el["x"] - gap * (n - 1) / 2
    for i in range(n):
        pi = clamp((t - el["_at"] - i * 0.06) / 0.35)
        if pi <= 0:
            continue
        hl = i < k and t >= el["_at_k"] + i * 0.08
        col = "#0EA5E9" if hl else "#CBD5E1"
        sc = ease_out_back(pi, 2.0)
        ctx.save()
        ctx.translate(x0 + i * gap, el["y"])
        ctx.scale(sc, sc)
        gfx.person(ctx, 0, 0, sz, col, a)
        ctx.restore()


def r_seed(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    rot = el.get("rot", 0) + (math.sin(t * 1.4) * 0.12 if el.get("spin") else 0)
    gfx.seed(ctx, el["x"], el["y"] + dy, el["size"] * s, el.get("kind", "green"), rot, a)


def r_seedpile(ctx, el, t, tl):
    import random
    rnd = random.Random(7)
    n = el.get("n", 50)
    for i in range(n):
        ang = rnd.random() * 2 * math.pi
        rad = (rnd.random() ** 0.6) * 230
        x = el["x"] + math.cos(ang) * rad * 1.3
        y = el["y"] + math.sin(ang) * rad * 0.42
        at = el["_at"] + i * 0.022
        p = clamp((t - at) / 0.4)
        if p <= 0:
            continue
        drop = (1 - ease_out_cubic(p)) * -260
        gfx.seed(ctx, x, y + drop, 64, "green", rnd.uniform(-1.4, 1.4), clamp(p * 3))


def r_arrow(ctx, el, t, tl):
    p = ease_out_cubic(clamp((t - el["_at"]) / 0.5))
    gfx.arrow(ctx, el["x1"], el["y1"], el["x2"], el["y2"], p, el.get("color", "orange"), el.get("width", 12))


def r_check(ctx, el, t, tl):
    p = clamp((t - el["_at"]) / 0.4)
    if p <= 0:
        return
    a = clamp(p * 3)
    dx = (1 - ease_out_cubic(p)) * -60
    x, y, w = el["x"] + dx, el["y"], el["w"]
    gfx.card(ctx, x, y - 52, w, 104, "white", 26, a)
    gfx.check_badge(ctx, x + 62, y, 34, el["ok"], a, ease_out_back(clamp((t - el["_at"] - 0.15) / 0.4), 2.5))
    gfx.text(ctx, el["text"], x + 120, y, 50, "fredoka", 600, "ink", alpha=a, anchor="l")


def r_phytate(ctx, el, t, tl):
    """Zinc 'Zn' balls drift; a purple phytate grabs some of them."""
    a = clamp((t - el["_at"]) / 0.4)
    if a <= 0:
        return
    cx, cy = el["x"], el["y"]
    g = ease_out_cubic(clamp((t - el["_grab"]) / 1.2))
    # phytate blob
    ctx.save()
    ctx.translate(cx, cy)
    sc = ease_out_back(clamp((t - el["_at"]) / 0.5), 2)
    ctx.scale(sc, sc)
    ctx.set_source_rgba(*rgb("#7C3AED", 0.92 * a))
    for k in range(6):
        ang = k * math.pi / 3 + t * 0.4
        ctx.arc(math.cos(ang) * 70, math.sin(ang) * 70, 52, 0, 2 * math.pi)
        ctx.fill()
    ctx.arc(0, 0, 90, 0, 2 * math.pi)
    ctx.fill()
    gfx.text(ctx, "phytate", 0, 0, 40, "fredoka", 700, "white", alpha=a)
    ctx.restore()
    # zinc balls
    import random
    rnd = random.Random(3)
    for i in range(8):
        ang0 = rnd.random() * 2 * math.pi
        rad0 = 300 + rnd.random() * 120
        caught = i % 2 == 0
        ang = ang0 + t * (0.25 + 0.1 * rnd.random())
        rad = rad0
        if caught:
            target = 170
            rad = lerp(rad0, target, g)
            ang = lerp(ang, i * math.pi / 4 + t * 0.4, g)
        x = cx + math.cos(ang) * rad * 1.35
        y = cy + math.sin(ang) * rad * 0.62
        ctx.set_source_rgba(*rgb("#F59E0B", a))
        ctx.arc(x, y, 42, 0, 2 * math.pi)
        ctx.fill()
        ctx.set_source_rgba(*rgb("#B45309", a))
        ctx.set_line_width(4)
        ctx.arc(x, y, 42, 0, 2 * math.pi)
        ctx.stroke()
        gfx.text(ctx, "Zn", x, y, 34, "fredoka", 700, "white", alpha=a)


def r_zzz(ctx, el, t, tl):
    a = out_alpha(el, t) * clamp((t - el["_at"]) / 0.3)
    if a <= 0:
        return
    for i in range(3):
        ph = ((t - el["_at"]) * 0.6 + i / 3) % 1.0
        gfx.text(ctx, "Z", el["x"] + ph * 90 + i * 10, el["y"] - ph * 200, 50 + i * 16, "fredoka", 700, "#C7D2FE",
                 alpha=a * math.sin(ph * math.pi))


def r_confetti(ctx, el, t, tl):
    import random
    dt = t - el["_at"]
    if dt <= 0 or dt > 5:
        return
    rnd = random.Random(11)
    cols = ["#F97316", "#0EA5E9", "#16A34A", "#F59E0B", "#8B5CF6", "#EF4444"]
    for i in range(120):
        x0 = rnd.uniform(100, 1820)
        vy = rnd.uniform(250, 520)
        vx = rnd.uniform(-80, 80)
        x = x0 + vx * dt + math.sin(dt * 3 + i) * 20
        y = -40 - rnd.uniform(0, 500) + vy * dt
        if y < -30 or y > 1100:
            continue
        ctx.save()
        ctx.translate(x, y)
        ctx.rotate(dt * rnd.uniform(-6, 6))
        ctx.set_source_rgba(*rgb(rnd.choice(cols), clamp(5 - dt)))
        ctx.rectangle(-9, -5, 18, 10)
        ctx.fill()
        ctx.restore()


def r_logo(ctx, el, t, tl):
    s, a, dy = pop(el, t)
    surf = gfx.png_surface(tl["logo"], el["size"])
    gfx.blit(ctx, surf, el["x"], el["y"] + dy, s, a)


def r_endslot(ctx, el, t, tl):
    a = clamp((t - el["_at"]) / 0.5)
    if a <= 0:
        return
    if el.get("subscribe"):
        return
    x, y, w, h = el["x"], el["y"], el["w"], el["h"]
    ctx.set_source_rgba(*rgb("green", 0.10 * a))
    gfx.rrect(ctx, x - w / 2, y - h / 2, w, h, 26)
    ctx.fill()
    ctx.set_source_rgba(*rgb("green", 0.35 * a))
    ctx.set_line_width(4)
    ctx.set_dash([18, 12])
    gfx.rrect(ctx, x - w / 2, y - h / 2, w, h, 26)
    ctx.stroke()
    ctx.set_dash([])
    gfx.text(ctx, "Watch next", x, y, 54, "fredoka", 600, "green", alpha=a * 0.8)


RENDER = {
    "text": r_text, "emoji": r_emoji, "card": r_card, "pill": r_pill, "banner": r_banner,
    "stat": r_stat, "bars": r_bars, "versus": r_versus, "ring": r_ring, "people": r_people, "seed": r_seed,
    "seedpile": r_seedpile, "arrow": r_arrow, "check": r_check, "phytate": r_phytate,
    "zzz": r_zzz, "confetti": r_confetti, "logo": r_logo, "endslot": r_endslot,
}

# which sound an element makes when it appears
SFX = {"card": "pop", "pill": "pop", "banner": "ding", "stat": "pop", "emoji": "pop", "seed": "pop",
       "ring": "ding", "check": "ding", "logo": "pop", "confetti": "pop", "phytate": "boing"}
