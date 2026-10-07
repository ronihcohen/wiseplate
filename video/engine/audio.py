"""Audio: Kokoro-82M narration (cached), a tiny procedural music synth, and SFX."""
import hashlib
import os

import numpy as np
import soundfile as sf

from gfx import CACHE

SR = 48000
TTS_SR = 24000
_kokoro = None


def kokoro():
    global _kokoro
    if _kokoro is None:
        from kokoro_onnx import Kokoro
        _kokoro = Kokoro(os.path.join(CACHE, "models", "kokoro-v1.0.onnx"),
                         os.path.join(CACHE, "models", "voices-v1.0.bin"))
    return _kokoro


def tts(text, voice, speed=1.0):
    """Synthesize one line with Kokoro-82M; returns mono float32 at 48 kHz."""
    key = hashlib.sha1(f"{voice}|{speed}|{text}".encode()).hexdigest()[:16]
    path = os.path.join(CACHE, "tts", key + ".wav")
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        samples, sr = kokoro().create(text, voice=voice, speed=speed, lang="en-us")
        samples = np.asarray(samples, dtype=np.float32)
        # trim leading/trailing silence
        nz = np.where(np.abs(samples) > 0.01)[0]
        if len(nz):
            samples = samples[max(0, nz[0] - int(0.03 * sr)): nz[-1] + int(0.08 * sr)]
        sf.write(path, samples, sr)
    x, sr = sf.read(path, dtype="float32")
    # 24k -> 48k
    t_new = np.arange(int(len(x) * SR / sr)) * sr / SR
    return np.interp(t_new, np.arange(len(x)), x).astype(np.float32)


def envelope(x, fps):
    """Per-video-frame loudness 0..1, used to drive Pip's mouth."""
    hop = SR // fps
    n = int(np.ceil(len(x) / hop))
    pad = np.pad(x, (0, n * hop - len(x)))
    rms = np.sqrt((pad.reshape(n, hop) ** 2).mean(axis=1))
    rms = rms / (np.percentile(rms, 95) + 1e-6)
    return np.clip(rms, 0, 1.2)


# ---------------------------------------------------------------- synth
def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def _t(dur):
    return np.arange(int(dur * SR)) / SR


def mallet(freq, dur=0.6, bright=1.0):
    t = _t(dur)
    out = np.zeros_like(t)
    for k, (h, a, d) in enumerate([(1, 1.0, 3.5), (2, 0.35 * bright, 7), (3, 0.12 * bright, 11), (4.2, 0.08 * bright, 18)]):
        out += a * np.sin(2 * np.pi * freq * h * t) * np.exp(-d * t)
    atk = np.minimum(1, t / 0.004)
    return out * atk * 0.35


def musicbox(freq, dur=1.2):
    t = _t(dur)
    out = np.sin(2 * np.pi * freq * t) * np.exp(-2.2 * t) + 0.25 * np.sin(2 * np.pi * freq * 3.01 * t) * np.exp(-6 * t)
    return out * np.minimum(1, t / 0.003) * 0.3


def bass(freq, dur=0.5):
    t = _t(dur)
    out = np.sin(2 * np.pi * freq * t) + 0.25 * np.sin(4 * np.pi * freq * t)
    return out * np.exp(-3.0 * t) * np.minimum(1, t / 0.01) * 0.45


def pad(freqs, dur):
    t = _t(dur)
    out = np.zeros_like(t)
    for f in freqs:
        for det in (-0.12, 0.12):
            out += np.sin(2 * np.pi * f * (1 + det / 100) * t)
    env = np.minimum(1, t / 0.8) * np.minimum(1, (dur - t) / 0.8)
    return out * env * 0.035


def kick():
    t = _t(0.25)
    f = 50 + 70 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14) * 0.55


def shaker(rng):
    t = _t(0.06)
    n = rng.standard_normal(len(t))
    n = np.diff(n, prepend=0)
    return n * np.exp(-t * 70) * 0.05


def snap(rng):
    t = _t(0.12)
    n = rng.standard_normal(len(t))
    return (n * 0.6 + np.sin(2 * np.pi * 190 * t)) * np.exp(-t * 35) * 0.16


def _add(buf, sig, at):
    i = int(at * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i]


CHORDS = {  # semitone offsets from key root
    "I": [0, 4, 7], "ii": [2, 5, 9], "iii": [4, 7, 11], "IV": [5, 9, 12],
    "V": [7, 11, 14], "vi": [9, 12, 16], "bVII": [10, 14, 17],
}


def music(duration, style, seed=0):
    """Loop-based background track. style keys: bpm, root (midi), prog, inst,
    drums (bool), density (0..1). Returns stereo (n, 2) float32."""
    rng = np.random.default_rng(seed)
    n = int(duration * SR) + SR
    L = np.zeros(n, np.float32)
    R = np.zeros(n, np.float32)
    beat = 60.0 / style["bpm"]
    root = style["root"]
    prog = style["prog"]
    inst = style.get("inst", "mallet")
    density = style.get("density", 0.7)
    drums = style.get("drums", True)
    swing = style.get("swing", 0.0)
    # fixed motif per track so it feels like a tune, not random noodling
    motif = [rng.choice([0, 1, 2, 3, -1], p=[0.3, 0.2, 0.25, 0.15, 0.1]) for _ in range(8)]
    motif2 = [rng.choice([0, 1, 2, 3, -1], p=[0.25, 0.25, 0.2, 0.2, 0.1]) for _ in range(8)]
    bar = 0
    t = 0.0
    while t < duration + 1:
        ch = CHORDS[prog[bar % len(prog)]]
        # pad + bass
        p = pad([mtof(root + c - 12) for c in ch], beat * 4 + 0.6)
        _add(L, p, t)
        _add(R, p, t)
        for b in range(4):
            if b in (0, 2) or (b == 3 and density > 0.6):
                note = root - 24 + ch[0] + (7 if b == 2 and density > 0.5 else 0)
                s = bass(mtof(note), beat * 0.9)
                _add(L, s, t + b * beat)
                _add(R, s, t + b * beat)
        # melody (8th notes)
        mot = motif if (bar // 2) % 2 == 0 else motif2
        for k in range(8):
            deg = mot[k]
            if deg < 0 or rng.random() > density + 0.25:
                continue
            octave = 12 if deg == 3 else 0
            m = root + ch[deg % 3] + octave + 12
            dt = k * beat / 2 + (swing * beat / 2 if k % 2 else 0)
            s = musicbox(mtof(m)) if inst == "musicbox" else mallet(mtof(m), 0.7, style.get("bright", 1.0))
            pan = 0.5 + 0.3 * np.sin(k)
            _add(L, s * (1 - pan) * 1.4, t + dt)
            _add(R, s * pan * 1.4, t + dt)
        if drums:
            for b in range(4):
                if b in (0, 2):
                    _add(L, kick(), t + b * beat)
                    _add(R, kick(), t + b * beat)
                if b in (1, 3):
                    s = snap(rng)
                    _add(L, s, t + b * beat)
                    _add(R, s, t + b * beat)
                for h in range(2):
                    s = shaker(rng)
                    _add(L, s * 0.9, t + b * beat + h * beat / 2)
                    _add(R, s * 1.1, t + b * beat + h * beat / 2)
        t += beat * 4
        bar += 1
    out = np.stack([L, R], 1)[: int(duration * SR)]
    fade = int(min(1.0, duration / 4) * SR)
    ramp = np.linspace(0, 1, fade)[:, None]
    out[:fade] *= ramp
    out[-fade:] *= ramp[::-1]
    peak = np.abs(out).max() + 1e-6
    return (out / peak * 0.5).astype(np.float32)


# ---------------------------------------------------------------- sfx
def sfx(kind):
    rng = np.random.default_rng(len(kind))
    if kind == "pop":
        t = _t(0.12)
        f = 900 * np.exp(-t * 18) + 300
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30) * 0.30
    if kind == "whoosh":
        t = _t(0.7)
        n = rng.standard_normal(len(t))
        # crude band-pass sweep: moving-average lowpass minus heavier lowpass
        env = np.sin(np.pi * t / 0.7) ** 2
        k1 = np.convolve(n, np.ones(6) / 6, "same")
        k2 = np.convolve(n, np.ones(40) / 40, "same")
        return (k1 - k2) * env * 0.35
    if kind == "ding":
        t = _t(0.9)
        return (np.sin(2 * np.pi * 1318 * t) + 0.5 * np.sin(2 * np.pi * 1975 * t)) * np.exp(-t * 6) * 0.16
    if kind == "buzz":
        t = _t(0.3)
        return np.sign(np.sin(2 * np.pi * 140 * t)) * np.exp(-t * 9) * 0.06
    if kind == "boing":
        t = _t(0.45)
        f = 260 + 140 * np.sin(t * 40) * np.exp(-t * 6)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7) * 0.22
    if kind == "tick":
        t = _t(0.03)
        return np.sin(2 * np.pi * 2200 * t) * np.exp(-t * 200) * 0.12
    raise ValueError(kind)
