#!/usr/bin/env python3
"""Render a narrated explainer video from an episode script.

    python3 video/build.py pumpkin_seeds                 # full build -> video/out/<slug>/
    python3 video/build.py pumpkin_seeds --stills 5,42   # PNG frames at those seconds
    python3 video/build.py pumpkin_seeds --range 60,90   # render only a clip

See video/README.md for setup (Kokoro model files, fonts).
"""
import argparse
import bisect
import importlib
import math
import multiprocessing as mp
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "engine"))
sys.path.insert(0, os.path.join(ROOT, "episodes"))

import cairo  # noqa: E402
import numpy as np  # noqa: E402
import soundfile as sf  # noqa: E402

import audio  # noqa: E402
import elements  # noqa: E402
import gfx  # noqa: E402
from gfx import clamp, ease_in_out, ease_out_back, ease_out_cubic, lerp, rgb  # noqa: E402

W, H, FPS = 1920, 1080, 30
XF = 0.35        # crossfade between scenes
CARD_DUR = 2.7   # chapter title card length
LOGO = os.path.join(ROOT, "assets", "logo.png")

EP = None
TL = None


# ================================================================ timeline
def split_caption(text, max_len=64):
    """Split a line into caption chunks: sentences first, then at the comma
    (or space) nearest the middle, so chunks stay balanced."""
    def halve(p):
        if len(p) <= max_len:
            return [p]
        mid = len(p) // 2
        cands = [m.end() for m in re.finditer(r"[,;] ", p)]
        cands = [c for c in cands if 18 < c < len(p) - 18]
        if not cands:
            cands = [m.end() for m in re.finditer(r" ", p)]
        cut = min(cands, key=lambda c: abs(c - mid))
        return halve(p[:cut].strip()) + halve(p[cut:].strip())

    chunks = []
    for p in re.split(r"(?<=[.!?:])\s+", text.strip()):
        chunks += halve(p)
    merged = []
    for c in chunks:
        if merged and len(merged[-1]) + len(c) + 1 <= max_len and (len(c) < 24 or len(merged[-1]) < 24):
            merged[-1] += " " + c
        else:
            merged.append(c)
    return merged


def resolve(spec, lines):
    if spec is None:
        return None
    if isinstance(spec, (int, float)):
        i = int(spec)
        if i >= len(lines):
            return lines[-1]["end"]
        L = lines[i]
        return L["start"] + (spec - i) * L["dur"]
    i, word = spec
    L = lines[i]
    for txt in (L["say"], L["text"]):
        pos = txt.find(word)
        if pos < 0:
            pos = txt.lower().find(word.lower())
        if pos >= 0:
            return max(L["start"], L["start"] + L["dur"] * pos / len(txt) - 0.15)
    print(f"  ! word {word!r} not in line {i}: {L['text'][:50]}")
    return L["start"]


def build_timeline():
    ep = EP
    scenes, chapters = [], []
    cur = 0.0
    voice_meta = ep.VOICES
    for ci, ch in enumerate(ep.CHAPTERS):
        chapters.append({"title": ch["title"], "start": cur, "key": ch["key"]})
        if ch.get("card", True):
            scenes.append({"kind": "card", "chapter": ci, "start": cur, "dur": CARD_DUR, "ch": ch,
                           "num": ci, "lines": [], "els": []})
            cur += CARD_DUR
        for si, sc in enumerate(ch["scenes"]):
            s = dict(sc)
            s["kind"] = "scene"
            s["chapter"] = ci
            s["ch"] = ch
            s["start"] = cur
            t = cur + 0.5
            lines = []
            prev_spk = None
            for spk, text, opts in sc["lines"]:
                if prev_spk is not None:
                    t += 0.32 if spk == prev_spk else 0.5
                say = opts.get("say", text)
                v = voice_meta[spk]
                wav = audio.tts(say, v["voice"], v["speed"])
                dur = len(wav) / audio.SR
                lines.append({"spk": spk, "text": text, "say": say, "opts": opts, "start": t, "dur": dur,
                              "end": t + dur, "wav": wav, "env": audio.envelope(wav, FPS),
                              "chunks": split_caption(text)})
                t += dur
                prev_spk = spk
            t += 0.9
            s["dur"] = max(t - cur, sc.get("dur_min", 0))
            s["lines"] = lines
            els = []
            for el in sc.get("els", []):
                e = dict(el)
                e["_at"] = resolve(el.get("at", 0), lines)
                e["_out"] = resolve(el.get("out"), lines)
                if "strike" in el:
                    e["_strike"] = resolve(el["strike"], lines)
                if "at_k" in el:
                    e["_at_k"] = resolve(el["at_k"], lines)
                if "grab" in el:
                    e["_grab"] = resolve(el["grab"], lines)
                if e["type"] in ("bars", "versus"):
                    e["rows"] = [dict(r, _at=resolve(r["at"], lines)) for r in el["rows"]]
                els.append(e)
            s["els"] = els
            scenes.append(s)
            cur += s["dur"]
    total = cur
    # Pip positions: each scene glides from the previous scene's spot
    last = None
    for s in scenes:
        if s["kind"] == "card":
            continue
        tgt = s.get("pip_to") or s["pip"]
        s["pip_from"] = s["pip"] if s.get("pip_to") else (last or s["pip"])
        s["pip_target"] = tgt
        last = tgt
    # captions
    caps = []
    for s in scenes:
        for L in s["lines"]:
            n = sum(len(c) for c in L["chunks"])
            t = L["start"]
            for c in L["chunks"]:
                d = L["dur"] * len(c) / n
                caps.append({"start": t, "end": t + d, "text": c, "spk": L["spk"]})
                t += d
    return {"scenes": scenes, "chapters": chapters, "total": total, "captions": caps,
            "starts": [s["start"] for s in scenes], "cap_starts": [c["start"] for c in caps], "logo": LOGO}


# ================================================================ drawing
_bg_cache = {}


def background(ctx, ch, t):
    key = ch["key"]
    col = EP.BG.get(key, "#FFF7ED")
    dark = ch.get("dark", False)
    ctx.set_source_rgba(*rgb(col))
    ctx.paint()
    g = cairo.RadialGradient(960, 420, 100, 960, 540, 1200)
    g.add_color_stop_rgba(0, 1, 1, 1, 0.0 if dark else 0.55)
    g.add_color_stop_rgba(1, 0, 0, 0, 0.25 if dark else 0.05)
    ctx.set_source(g)
    ctx.paint()
    import random
    rnd = random.Random(hash(key) % 1000)
    if dark:
        for i in range(90):
            x, y = rnd.uniform(0, W), rnd.uniform(0, H)
            tw = 0.5 + 0.5 * math.sin(t * rnd.uniform(1, 3) + i)
            ctx.set_source_rgba(1, 1, 0.9, 0.25 + 0.5 * tw)
            ctx.arc(x, y, rnd.uniform(1.2, 3.2), 0, 2 * math.pi)
            ctx.fill()
        ctx.set_source_rgba(1, 0.96, 0.8, 0.9)
        ctx.arc(1700, 150, 70, 0, 2 * math.pi)
        ctx.fill()
        ctx.set_source_rgba(*rgb(col))
        ctx.arc(1735, 130, 62, 0, 2 * math.pi)
        ctx.fill()
        return
    # faint drifting seeds
    for i in range(16):
        x0, y0 = rnd.uniform(-100, W + 100), rnd.uniform(0, H)
        sp = rnd.uniform(8, 22)
        y = (y0 - t * sp) % (H + 200) - 100
        x = x0 + math.sin(t * 0.3 + i) * 30
        gfx.seed(ctx, x, y, rnd.uniform(40, 90), "green", t * rnd.uniform(-0.3, 0.3) + i, 0.07)


def draw_card(ctx, sc, t):
    lt = t - sc["start"]
    ch = sc["ch"]
    ctx.set_source_rgba(*rgb("green"))
    ctx.paint()
    import random
    rnd = random.Random(sc["num"])
    for i in range(22):
        x, y = rnd.uniform(0, W), rnd.uniform(0, H)
        gfx.seed(ctx, x + lt * 20 * (1 if i % 2 else -1), y, rnd.uniform(50, 120), "green", rnd.uniform(0, 6) + lt * 0.2, 0.12)
    p1 = clamp((lt - 0.15) / 0.5)
    p2 = clamp((lt - 0.35) / 0.5)
    p3 = clamp((lt - 0.55) / 0.5)
    gfx.text(ctx, f"PART {sc['num']}", 960, 300 + (1 - ease_out_cubic(p1)) * 30, 46, "fredoka", 600, "mint",
             alpha=p1)
    gfx.emoji(ctx, ch.get("emoji", "🎃"), 960, 470, 190, ease_out_back(p2, 2.4), clamp(p2 * 3),
              math.sin(lt * 3) * 0.06)
    gfx.text(ctx, ch["title"], 960, 680 + (1 - ease_out_cubic(p3)) * 40, 104, "fredoka", 700, "white",
             max_w=1600, alpha=p3)
    # orange underline
    w = 260 * ease_out_cubic(clamp((lt - 0.8) / 0.5))
    if w > 1:
        ctx.set_source_rgba(*rgb("orange"))
        gfx.rrect(ctx, 960 - w / 2, 770, w, 14, 7)
        ctx.fill()


def draw_layer(ctx, sc, t):
    if sc["kind"] == "card":
        draw_card(ctx, sc, t)
        return
    background(ctx, sc["ch"], t)
    lt = t - sc["start"]
    k = ease_in_out(lt / max(sc["dur"], 1))
    idx = TL["scenes"].index(sc)
    z = 1.0 + 0.045 * k
    pan = (1 if idx % 2 else -1) * 24 * k
    ctx.save()
    ctx.translate(W / 2 + pan, H / 2 - 8 * k)
    ctx.scale(z, z)
    ctx.translate(-W / 2, -H / 2)
    for el in sorted(sc["els"], key=lambda e: e["type"] == "arrow"):  # arrows on top
        if t < el["_at"] - 0.01 and el["type"] not in ("bars",):
            continue
        elements.RENDER[el["type"]](ctx, el, t, TL)
    ctx.restore()


def pip_state(t, i):
    scenes = TL["scenes"]
    sc = scenes[i]
    lt = t - sc["start"]
    if sc["kind"] == "card":
        prev = scenes[i - 1] if i > 0 else None
        if not prev or prev["kind"] == "card":
            return None
        st = pip_state(sc["start"] - 1e-3, i - 1)
        if st is None:
            return None
        st["alpha"] *= 1 - clamp(lt / 0.3)
        return st
    if sc.get("pip_hide"):
        return None
    after_card = i > 0 and scenes[i - 1]["kind"] == "card"
    a, b = sc["pip_from"], sc["pip_target"]
    if sc.get("pip_to"):
        p = ease_in_out(clamp((lt - 0.1) / 1.0))
    elif after_card:
        p = 1.0
    else:
        p = ease_in_out(clamp(lt / 0.8))
    x, y, size = (lerp(a[k], b[k], p) for k in ("x", "y", "size"))
    alpha = 1.0
    scale = 1.0
    if after_card:
        q = clamp((lt - 0.15) / 0.45)
        alpha = clamp(q * 3)
        scale = ease_out_back(q, 2.2)
    st = {"x": x, "y": y, "size": size * scale, "alpha": alpha, "mood": "happy", "mouth": 0.0, "talking": False,
          "look": (clamp((960 - x) / 700, -1, 1) * 0.5, 0.15), "squash": 0.0, "wave": 0.0}
    for L in sc["lines"]:
        if L["spk"] != "P":
            if L["start"] <= t < L["end"]:
                st["look"] = (clamp((800 - x) / 500, -1, 1) * 0.9, 0.1)
            continue
        if L["start"] <= t < L["end"] + 1.5:
            st["mood"] = L["opts"].get("mood", "happy")
        if L["start"] <= t < L["end"]:
            fi = int((t - L["start"]) * FPS)
            st["mouth"] = float(L["env"][min(fi, len(L["env"]) - 1)])
            st["talking"] = True
            st["look"] = (0.0, 0.15)
            if L["opts"].get("wave"):
                st["wave"] = clamp((t - L["start"]) / 0.3) * clamp((L["end"] - t) / 0.3)
        if L["opts"].get("jump"):
            jp = (t - L["start"]) / 0.55
            if 0 <= jp <= 1:
                st["y"] -= math.sin(math.pi * jp) * st["size"] * 0.32
                st["squash"] = -0.5 * math.sin(math.pi * jp)
            elif 1 < jp < 1.35:
                st["squash"] = 0.6 * math.sin(math.pi * (jp - 1) / 0.35)
    return st


def draw_caption(ctx, t):
    caps = TL["captions"]
    i = bisect.bisect_right(TL["cap_starts"], t) - 1
    if i < 0:
        return
    c = caps[i]
    if t >= c["end"] + 0.25:
        return
    a = clamp((t - c["start"]) / 0.12) * clamp((c["end"] + 0.25 - t) / 0.12)
    if a <= 0:
        return
    surf = gfx.text_surface(c["text"], 44, "rubik", 500, "white", 1460)
    w, h = surf.get_width() + 56, surf.get_height() + 24
    y = 1040 - h / 2
    fill = "#4D6B1F" if c["spk"] == "P" else "#064E3B"
    ctx.set_source_rgba(*rgb(fill, 0.9 * a))
    gfx.rrect(ctx, 960 - w / 2, y - h / 2, w, h, 22)
    ctx.fill()
    gfx.blit(ctx, surf, 960, y, 1, a)
    if c["spk"] == "P":
        ls = gfx.text_surface("PIP", 28, "fredoka", 700, "#4D6B1F")
        lw = ls.get_width() + 30
        ctx.set_source_rgba(*rgb("#D9F99D", a))
        gfx.rrect(ctx, 960 - w / 2 + 18, y - h / 2 - 22, lw, 40, 20)
        ctx.fill()
        gfx.blit(ctx, ls, 960 - w / 2 + 18 + lw / 2, y - h / 2 - 2, 1, a)


def render_frame(t):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(surf)
    scenes = TL["scenes"]
    i = max(0, bisect.bisect_right(TL["starts"], t) - 1)
    sc = scenes[i]
    lt = t - sc["start"]
    wipe = 0.5 if sc["kind"] == "card" else XF
    if i > 0 and lt < wipe:
        draw_layer(ctx, scenes[i - 1], t)
        p = ease_in_out(lt / wipe)
        if sc["kind"] == "card":
            ctx.save()
            ctx.arc(1660, 640, 2300 * p, 0, 2 * math.pi)
            ctx.clip()
            draw_layer(ctx, sc, t)
            ctx.restore()
        else:
            ctx.push_group()
            draw_layer(ctx, sc, t)
            ctx.pop_group_to_source()
            ctx.paint_with_alpha(p)
    else:
        draw_layer(ctx, sc, t)
    st = pip_state(t, i)
    if st and st["alpha"] > 0.01:
        gfx.pip(ctx, st["x"], st["y"], st["size"], t, st["mouth"], st["mood"], st["look"], st["talking"],
                st["alpha"], 0.0, st["squash"], st["wave"])
    draw_caption(ctx, t)
    # fade in/out of the whole video
    edge = min(t / 0.4, (TL["total"] - t) / 0.8)
    if edge < 1:
        ctx.set_source_rgba(0, 0, 0, 1 - clamp(edge))
        ctx.paint()
    surf.flush()
    return surf


# ================================================================ audio
def build_audio(path):
    total = TL["total"]
    n = int(total * audio.SR) + audio.SR
    voice = np.zeros(n, np.float32)
    fx = np.zeros(n, np.float32)
    music = np.zeros((n, 2), np.float32)

    def put(buf, sig, at):
        i = int(at * audio.SR)
        j = min(len(buf), i + len(sig))
        if i < j:
            buf[i:j] += sig[: j - i]

    for s in TL["scenes"]:
        if s["kind"] == "card":
            put(fx, audio.sfx("whoosh"), s["start"])
            continue
        for L in s["lines"]:
            put(voice, L["wav"], L["start"])
            if L["spk"] == "P" and L["opts"].get("jump"):
                put(fx, audio.sfx("boing"), L["start"])
        for el in s["els"]:
            kind = elements.SFX.get(el["type"])
            if el["type"] == "check" and not el["ok"]:
                kind = "buzz"
            if el["type"] in ("bars", "versus"):
                for r in el["rows"]:
                    put(fx, audio.sfx("tick"), r["_at"])
            if el["type"] == "people":
                for k in range(el["n"]):
                    put(fx, audio.sfx("tick") * 0.6, el["_at"] + k * 0.06)
            if kind:
                put(fx, audio.sfx(kind) * (0.7 if kind == "pop" else 1.0), el["_at"])
    chs = TL["chapters"]
    for ci, ch in enumerate(chs):
        st = ch["start"]
        en = chs[ci + 1]["start"] if ci + 1 < len(chs) else total
        style = EP.MUSIC[ch["key"]]
        m = audio.music(en - st + 1.0, style, seed=ci + 1)
        i = int(max(0, st - 0.5) * audio.SR)
        j = min(n, i + len(m))
        music[i:j] += m[: j - i]
    # duck music under the voice
    blk = audio.SR // 100
    nb = n // blk
    rms = np.sqrt((voice[: nb * blk].reshape(nb, blk) ** 2).mean(1))
    lvl = np.clip(rms * 12, 0, 1)
    sm = np.zeros(nb)
    v = 0.0
    for k in range(nb):
        target = lvl[k]
        v += (target - v) * (0.5 if target > v else 0.04)
        sm[k] = v
    gain = 1 - 0.55 * sm
    gain = np.interp(np.arange(n) / blk, np.arange(nb), gain).astype(np.float32)
    mix = np.zeros((n, 2), np.float32)
    mix += voice[:, None] * 0.9
    mix += music * (0.30 * gain)[:, None]
    mix += fx[:, None] * 0.7
    mix = mix[: int(total * audio.SR)]
    peak = np.abs(mix).max()
    if peak > 0.98:
        mix *= 0.98 / peak
    sf.write(path, mix, audio.SR)


# ================================================================ outputs
def fmt_ts(t, srt=False):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    if srt:
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"
    return f"{int(m)}:{int(s):02d}" if h < 1 else f"{int(h)}:{int(m):02d}:{int(s):02d}"


def write_srt(path):
    with open(path, "w") as f:
        for k, c in enumerate(TL["captions"], 1):
            f.write(f"{k}\n{fmt_ts(c['start'], True)} --> {fmt_ts(c['end'], True)}\n{c['text']}\n\n")


def chapter_list():
    return "\n".join(f"{fmt_ts(c['start'] if k else 0)} {c['title']}" for k, c in enumerate(TL["chapters"]))


def thumbnail(path):
    """1280x720 YouTube thumbnail: big Pip, big words, one hard number."""
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(surf)
    g = cairo.RadialGradient(1350, 560, 50, 1350, 560, 1300)
    g.add_color_stop_rgb(0, *rgb("#FFF3C4")[:3])
    g.add_color_stop_rgb(1, *rgb("#FDBA74")[:3])
    ctx.set_source(g)
    ctx.paint()
    for k in range(18):  # sunburst
        a0 = k * 2 * math.pi / 18
        ctx.move_to(1350, 560)
        ctx.arc(1350, 560, 1600, a0, a0 + math.pi / 18)
        ctx.close_path()
        ctx.set_source_rgba(1, 1, 1, 0.22)
        ctx.fill()
    th = getattr(EP, "THUMB", {})
    import random
    rnd = random.Random(5)
    for i in range(14):  # scattered food (pumpkin seeds by default)
        x, y, s, r = rnd.uniform(900, 1880), rnd.uniform(40, 1040), rnd.uniform(70, 130), rnd.uniform(-1.5, 1.5)
        if th.get("scatter"):
            gfx.emoji(ctx, th["scatter"], x, y, s * 0.9, 1.0, 0.9, r * 0.3)
        else:
            gfx.seed(ctx, x, y, s, "green", r, 0.9)
    gfx.pip(ctx, 1380, 600, 760, 0.6, 0.0, th.get("mood", "surprised"), (-0.4, 0.0), False, 1.0, -0.08)
    if th.get("hero"):  # the food itself, next to Pip
        gfx.emoji(ctx, th["hero"], 1000, 820, 300, 1.0, 1.0, -0.12)
    gfx.text(ctx, th.get("top", "TINY SEED"), 70, 300, th.get("top_size", 190), "fredoka", 700, "white",
             anchor="l", stroke=14, stroke_color="#064E3B")
    gfx.text(ctx, th.get("bottom", "BIG DEAL?"), 70, 520, th.get("bottom_size", 210), "fredoka", 700, "#F97316",
             anchor="l", stroke=14, stroke_color="#064E3B")
    # badge
    ctx.save()
    ctx.translate(330, 820)
    ctx.rotate(-0.06)
    gfx.card(ctx, -280, -105, 580, 210, th.get("badge_color", "#0EA5E9"), 40, 1.0)
    gfx.text(ctx, th.get("badge", "37%"), -130, -8, th.get("badge_size", 130), "fredoka", 700, "white")
    gfx.text(ctx, th.get("badge_label", "magnesium\nper handful"), 40, 0, 46, "fredoka", 600, "white",
             align="left", anchor="l")
    ctx.restore()
    gfx.blit(ctx, gfx.png_surface(LOGO, 120), 1820, 980)
    surf.flush()
    tmp = path + ".full.png"
    surf.write_to_png(tmp)
    from PIL import Image
    Image.open(tmp).convert("RGB").resize((1280, 720), Image.LANCZOS).save(path, quality=92)
    os.remove(tmp)


def render_range(args):
    f0, f1, path = args
    cmd = ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-tune", "animation",
           "-pix_fmt", "yuv420p", path]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(f0, f1):
        s = render_frame(f / FPS)
        p.stdin.write(bytes(s.get_data()))
        if (f - f0) % 900 == 0:
            print(f"  frames {f}/{f1}", flush=True)
    p.stdin.close()
    p.wait()
    return path


def main():
    global EP, TL
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--stills", default="")
    ap.add_argument("--range", default="")
    ap.add_argument("--thumb", action="store_true")
    ap.add_argument("--workers", type=int, default=max(1, os.cpu_count() or 1))
    a = ap.parse_args()
    EP = importlib.import_module(a.episode)
    out = os.path.join(ROOT, "out", EP.SLUG)
    os.makedirs(out, exist_ok=True)
    if a.thumb:
        thumbnail(os.path.join(out, "thumbnail.jpg"))
        return
    print("timeline + narration (Kokoro-82M)...", flush=True)
    TL = build_timeline()
    print(f"  duration {fmt_ts(TL['total'])} ({TL['total']:.1f}s), {len(TL['scenes'])} scenes", flush=True)
    thumbnail(os.path.join(out, "thumbnail.jpg"))
    if a.stills:
        for s in a.stills.split(","):
            t = float(s)
            render_frame(t).write_to_png(os.path.join(out, f"still_{t:07.2f}.png"))
        return
    wav = os.path.join(out, "mix.wav")
    print("audio mix...", flush=True)
    build_audio(wav)
    write_srt(os.path.join(out, "subtitles.en.srt"))
    with open(os.path.join(out, "chapters.txt"), "w") as f:
        f.write(chapter_list() + "\n")
    t0, t1 = 0.0, TL["total"]
    if a.range:
        t0, t1 = (float(x) for x in a.range.split(","))
    f0, f1 = int(t0 * FPS), int(t1 * FPS)
    nw = a.workers
    step = math.ceil((f1 - f0) / nw)
    jobs = [(f0 + k * step, min(f1, f0 + (k + 1) * step), os.path.join(out, f"part{k}.mp4")) for k in range(nw)]
    jobs = [j for j in jobs if j[0] < j[1]]
    print(f"rendering {f1 - f0} frames on {len(jobs)} workers...", flush=True)
    ctx = mp.get_context("fork")
    with ctx.Pool(len(jobs)) as pool:
        parts = pool.map(render_range, jobs)
    lst = os.path.join(out, "parts.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    final = os.path.join(out, f"{EP.SLUG}.mp4" if not a.range else f"clip_{int(t0)}_{int(t1)}.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-ss", str(t0), "-t", str(t1 - t0), "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", "-shortest", final], check=True)
    for p in parts:
        os.remove(p)
    os.remove(lst)
    print("done:", final)


if __name__ == "__main__":
    main()
