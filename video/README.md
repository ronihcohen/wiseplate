# Video generator

Turns an episode script into a narrated, animated YouTube explainer
(1920x1080, 30 fps): Kokoro-82M narration with two voices (a host and Pip the
pumpkin-seed mascot), animated cards and charts, a gentle camera push per
scene, procedural music per chapter that ducks under the voice, sound
effects, burned-in captions, an `.srt` file, a chapter list and a thumbnail.

This folder lives outside `static/`, so Hugo does not publish it.

## Setup (once)

```bash
python3 -m pip install kokoro-onnx soundfile pycairo pillow numpy
mkdir -p video/.cache/models video/.cache/fonts
# Kokoro-82M (Apache-2.0) ONNX weights + voices
curl -L -o video/.cache/models/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -L -o video/.cache/models/voices-v1.0.bin  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
# Fonts (OFL)
curl -L -o video/.cache/fonts/Fredoka.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/fredoka/Fredoka%5Bwdth,wght%5D.ttf"
curl -L -o video/.cache/fonts/Rubik.ttf   "https://raw.githubusercontent.com/google/fonts/main/ofl/rubik/Rubik%5Bwght%5D.ttf"
```

Also needs `ffmpeg` and the Noto Color Emoji font
(`/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf`, package `fonts-noto-color-emoji`).

## Build

```bash
python3 video/build.py pumpkin_seeds                # full video -> video/out/pumpkin-seeds/
python3 video/build.py pumpkin_seeds --stills 30,95 # PNG frames, for checking layout
python3 video/build.py pumpkin_seeds --range 60,90  # render a short clip
python3 video/build.py pumpkin_seeds --thumb        # thumbnail only
```

Outputs: `<slug>.mp4`, `thumbnail.jpg`, `subtitles.en.srt`, `chapters.txt`.
Narration is cached per line in `.cache/tts/`, so re-renders after visual
tweaks are fast. A full render takes roughly 15-25 minutes on 4 cores.

## Writing a new episode

Copy `episodes/pumpkin_seeds.py`. An episode is a list of chapters; each
chapter gets a title card (except the first) and its own music style; each
chapter holds scenes; each scene has spoken `lines` and visual `els`.

- Line: `("H" | "P", caption text, {"say": tts text, "mood": ..., "jump": True, "wave": True})`.
  Pip moods: `happy`, `smug`, `surprised`, `worried`, `sleepy`.
- Element `at`: a line index, or `[line_index, "word"]` to appear roughly when
  that word is spoken.
- Element types are in `engine/elements.py` (`text`, `emoji`, `card`, `pill`,
  `banner`, `stat`, `bars`, `ring`, `people`, `check`, `arrow`, `seed`, ...).
- Keep visuals above y=900; captions sit at the bottom.

## Files

- `build.py`: timeline, frame compositing, audio mix, parallel render, thumbnail.
- `engine/gfx.py`: text/emoji caching, shapes, and the Pip mascot.
- `engine/elements.py`: animated scene elements.
- `engine/audio.py`: Kokoro TTS, music synth, sound effects.
- `assets/logo.png`: channel watermark from `branding/youtube/`.
