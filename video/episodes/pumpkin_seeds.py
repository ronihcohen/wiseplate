"""Pumpkin seeds explainer (English), based on https://wiseplate.blog/food/pumpkin-seeds/

Numbers are the article's: shelled, roasted, unsalted seeds, USDA FDC 170557,
per 28 g serving. Keep them in sync with content/food/pumpkin-seeds.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Pumpkin Seeds: Tiny Seed, Big Deal?"
SLUG = "pumpkin-seeds"
ARTICLE = "https://wiseplate.blog/food/pumpkin-seeds/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

MUSIC = {
    "intro":   {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "names":   {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "inside":  {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "mag":     {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "zinc":    {"bpm": 96, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.6, "swing": 0.1},
    "prostate": {"bpm": 90, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.5, "drums": True},
    "sleep":   {"bpm": 72, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.45, "inst": "musicbox", "drums": False},
    "catches": {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":   {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":   {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF7ED", "names": "#FEF3C7", "inside": "#ECFDF5", "mag": "#E0F2FE",
    "zinc": "#FFEDD5", "prostate": "#F1F5F9", "sleep": "#1E1B4B", "catches": "#FEE2E2",
    "howto": "#ECFCCB", "outro": "#FFF7ED",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Psst. Hey. Down here. Yes, you! The tiny green thing is talking.",
             {"mood": "happy", "wave": True}),
            ("P", "Hi! I'm Pip, and I'm a pumpkin seed.", {"mood": "happy", "jump": True}),
        ], "els": []},
        {"pip": PIP_R, "lines": [
            ("H", "Pip is right. Today we're talking about pumpkin seeds: what's actually inside them, "
                  "what the science really says, and the catches nobody prints on the bag.", {}),
            ("P", "Spoiler alert: I'm kind of a big deal.", {"mood": "smug"}),
            ("H", "We'll see about that. Let's crack this open.", {}),
        ], "els": [
            E("🎃", 420, 330, 200, at=[0, "pumpkin"], wobble=True),
            T("Pumpkin Seeds", 760, 300, 120, at=[0, "pumpkin"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 560, "h": 110, "emoji": "🔬", "title": "What's inside", "at": [0, "inside"]},
            {"type": "card", "x": 760, "y": 650, "w": 560, "h": 110, "emoji": "📚", "title": "What science says", "at": [0, "science"]},
            {"type": "card", "x": 760, "y": 780, "w": 560, "h": 110, "emoji": "⚠️", "title": "The catches", "at": [0, "catches"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "names", "title": "Two Names, Two Seeds", "emoji": "🏷️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "First, a quick name check. In English, they're pumpkin seeds. The green, shelled ones also go by pepitas, "
                  "from the Spanish pepita de calabaza, which simply means little pumpkin seed.",
             {"say": "First, a quick name check. In English, they're pumpkin seeds. The green, shelled ones also go by pepitas, "
                     "from the Spanish, pepita de calabaza, which simply means, little pumpkin seed."}),
            ("H", "And the plant itself has a very fancy science name: Cucurbita pepo.",
             {"say": "And the plant itself has a very fancy science name: Cucurbita pepo."}),
            ("P", "Cucurbita pepo! Try saying that three times fast. I'll wait.", {"mood": "smug"}),
        ], "els": [
            T("Pumpkin seeds", 700, 250, 96, at=[0, "pumpkin"], font="fredoka", weight=700, color="green"),
            T("= pepitas", 700, 380, 84, at=[0, "pepitas"], font="fredoka", weight=600, color="orange"),
            T("from Spanish: pepita de calabaza", 700, 480, 46, at=[0, "Spanish"], color="muted", weight=500),
            T("“little pumpkin seed”", 700, 545, 46, at=[0, "simply"], color="ink", weight=600),
            {"type": "card", "x": 700, "y": 720, "w": 720, "h": 130, "emoji": "🌱", "title": "Cucurbita pepo",
             "body": "the plant's scientific name", "at": [1, "Cucurbita"], "italic_title": True},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Now, here's the distinction that actually matters. The white seeds in the shell, the ones you crack open as a snack, "
                  "are not the same product as the green, shelled ones.", {}),
            ("H", "The green ones pack more nutrition per gram. The white ones add insoluble fiber from the shell, "
                  "but only if you actually eat the shell.", {}),
            ("P", "Which, let's be honest, most people spit out.", {"mood": "worried"}),
        ], "els": [
            {"type": "seed", "kind": "shell", "x": 420, "y": 400, "size": 260, "rot": -0.25, "at": [0, "white"], "spin": True},
            T("In the shell", 420, 610, 56, at=[0, "white"], font="fredoka", weight=600, color="ink"),
            T("crunchy snack", 420, 670, 40, at=[0, "snack"], color="muted"),
            {"type": "seed", "kind": "green", "x": 1060, "y": 400, "size": 240, "rot": 0.25, "at": [0, "green,"], "spin": True},
            T("Shelled (pepitas)", 1060, 610, 56, at=[0, "green,"], font="fredoka", weight=600, color="ink"),
            T("vs", 740, 400, 110, at=[0, "not"], font="fredoka", weight=700, color="orange"),
            {"type": "pill", "x": 1060, "y": 760, "text": "more nutrition per gram", "color": "ok", "at": [1, "nutrition"]},
            {"type": "pill", "x": 420, "y": 760, "text": "+ fiber (if you eat the shell)", "color": "orange", "at": [1, "fiber"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Pumpkin seeds also have a long history. They were a staple food in Mesoamerica centuries before they ever reached Europe.", {}),
            ("H", "People there also used them as a folk remedy, mostly for prostate health. Hold that thought, we'll come back to it.", {}),
            ("P", "Ooh, a cliffhanger.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 340, "y": 380, "w": 500, "h": 190, "emoji": "🌽", "title": "Mesoamerica",
             "body": "a staple food", "at": [0, "Mesoamerica"]},
            {"type": "arrow", "x1": 625, "y1": 380, "x2": 840, "y2": 380, "at": [0, "centuries"]},
            T("centuries later", 732, 315, 34, at=[0, "centuries"], color="muted"),
            {"type": "card", "x": 1060, "y": 380, "w": 380, "h": 190, "emoji": "🏰", "title": "Europe",
             "body": "", "at": [0, "Europe."]},
            {"type": "card", "x": 720, "y": 680, "w": 760, "h": 160, "emoji": "🌿", "title": "Folk remedy",
             "body": "mostly for prostate health", "at": [1, "remedy"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "inside", "title": "What's in a Handful?", "emoji": "🔬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So what's actually inside? All the numbers in this video are for shelled, roasted, unsalted seeds, "
                  "from the U.S. Department of Agriculture's FoodData Central database.",
             {"say": "So what's actually inside? All the numbers in this video are for shelled, roasted, unsalted seeds, "
                     "from the U S Department of Agriculture's Food Data Central database."}),
            ("H", "Our example serving is one ounce, which is twenty-eight grams. That's roughly a small handful.", {}),
            ("P", "Twenty-eight grams of me? That's a whole crowd of Pips!", {"mood": "surprised", "jump": True}),
        ], "els": [
            {"type": "pill", "x": 700, "y": 200, "text": "shelled · roasted · unsalted", "color": "green", "at": [0, "shelled"]},
            T("Source: USDA FoodData Central #170557", 700, 280, 34, at=[0, "FoodData"], color="muted"),
            {"type": "seedpile", "x": 700, "y": 560, "n": 60, "at": [1, "ounce"]},
            T("1 serving = 28 g", 700, 790, 80, at=[1, "twenty"], font="fredoka", weight=700, color="green"),
            T("(about a small handful)", 700, 870, 40, at=[1, "handful"], color="muted"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "That handful gives you about one hundred sixty-one calories, eight point four grams of protein, "
                  "and thirteen point seven grams of fat, mostly the unsaturated kind.", {}),
        ], "els": [
            {"type": "stat", "x": 290, "y": 470, "w": 400, "h": 300, "value": 161, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "sixty"]},
            {"type": "stat", "x": 740, "y": 470, "w": 400, "h": 300, "value": 8.4, "decimals": 1, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "protein"]},
            {"type": "stat", "x": 1190, "y": 470, "w": 400, "h": 300, "value": 13.7, "decimals": 1, "unit": " g", "label": "fat, mostly good fats", "emoji": "🫒", "at": [0, "fat"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "But the real story is minerals. These bars show the percent of the daily value in that one handful.", {}),
            ("H", "Manganese, fifty-five percent. Copper, forty. Magnesium, thirty-seven. Phosphorus, twenty-six. Zinc, nineteen. And iron, thirteen.", {}),
            ("P", "Not bad for something the size of a fingernail, right?", {"mood": "smug"}),
            ("H", "One note: daily values are U.S. food label references, not a personal target. They're just a handy yardstick.",
             {"say": "One note: daily values are U S food label references, not a personal target. They're just a handy yardstick."}),
        ], "els": [
            T("% Daily Value per 28 g", 760, 175, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 260, "y": 270, "w": 1000, "row_h": 92, "max": 60, "rows": [
                {"label": "Manganese", "value": 55, "color": "#8B5CF6", "at": [1, "Manganese"]},
                {"label": "Copper", "value": 40, "color": "#F97316", "at": [1, "Copper"]},
                {"label": "Magnesium", "value": 37, "color": "#0EA5E9", "at": [1, "Magnesium"], "star": True},
                {"label": "Phosphorus", "value": 26, "color": "#14B8A6", "at": [1, "Phosphorus"]},
                {"label": "Zinc", "value": 19, "color": "#F59E0B", "at": [1, "Zinc"]},
                {"label": "Iron", "value": 13, "color": "#EF4444", "at": [1, "iron"]},
            ]},
            T("US label reference values, not personal advice", 760, 860, 34, at=[3, "label"], color="muted"),
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "mag", "title": "The Magnesium Superstar", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "If pumpkin seeds have one superpower, it's magnesium. One handful covers about thirty-seven percent of the daily value.", {}),
            ("P", "Thirty-seven percent! I'm basically a tiny magnesium supplement with a face.", {"mood": "happy", "jump": True}),
            ("H", "And that matters, because magnesium is a mineral many people really do fall short on. "
                  "In Western diets, roughly half of people don't reach the recommended intake.", {}),
        ], "els": [
            {"type": "ring", "x": 520, "y": 400, "r": 190, "value": 37, "color": "#0EA5E9", "label": "magnesium", "at": [0, "thirty"]},
            T("Mg", 1020, 330, 130, at=[0, "magnesium."], font="fredoka", weight=700, color="#0369A1"),
            T("in one handful", 1020, 450, 44, at=[0, "handful"], color="muted"),
            {"type": "people", "x": 760, "y": 780, "n": 10, "k": 5, "size": 90, "at": [2, "Western"], "at_k": [2, "half"]},
            T("~1 in 2 fall short", 760, 900, 44, at=[2, "half"], font="fredoka", weight=600, color="#0369A1"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Your body uses magnesium in more than three hundred enzyme reactions.", {}),
            ("H", "It helps make A T P, your cells' energy currency. It helps regulate blood sugar. "
                  "It helps muscles contract and relax. And it plays a part in blood pressure.",
             {"say": "It helps make A T P, your cells' energy currency. It helps regulate blood sugar. "
                     "It helps muscles contract and relax. And it plays a part in blood pressure."}),
        ], "els": [
            T("300+ enzyme reactions", 720, 200, 80, at=[0, "three"], font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 390, "y": 420, "w": 600, "h": 160, "emoji": "⚡", "title": "Energy (ATP)", "body": "your cells' fuel", "at": [1, "A"]},
            {"type": "card", "x": 1050, "y": 420, "w": 600, "h": 160, "emoji": "🩸", "title": "Blood sugar", "body": "helps regulate it", "at": [1, "sugar"]},
            {"type": "card", "x": 390, "y": 640, "w": 600, "h": 160, "emoji": "💪", "title": "Muscles", "body": "contract & relax", "at": [1, "muscles"]},
            {"type": "card", "x": 1050, "y": 640, "w": 600, "h": 160, "emoji": "❤️", "title": "Blood pressure", "body": "plays a part", "at": [1, "pressure"]},
        ], "pip_hide": True},
        {"pip": PIP_C, "lines": [
            ("H", "Out of everything on the label, this is the benefit with the strongest backing, by a wide margin.", {}),
            ("P", "Write that down. Magnesium. That's my headline.", {"mood": "smug", "wave": True}),
        ], "els": [
            {"type": "banner", "x": 960, "y": 180, "text": "#1 benefit: MAGNESIUM", "color": "#0EA5E9", "at": [0, "strongest"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "zinc", "title": "Zinc and the Phytate Plot Twist", "emoji": "🛡️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Next up: zinc. A handful gives you about nineteen percent of the daily value, "
                  "which makes pumpkin seeds one of the best plant sources around.", {}),
            ("H", "Zinc supports your immune system, wound healing, your sense of taste and smell, and testosterone production.", {}),
            ("H", "That's especially useful on a plant-based diet, where zinc is one of the trickier minerals to get enough of.", {}),
        ], "els": [
            {"type": "ring", "x": 330, "y": 330, "r": 140, "value": 19, "color": "#F59E0B", "label": "zinc", "at": [0, "nineteen"]},
            {"type": "card", "x": 720, "y": 250, "w": 440, "h": 130, "emoji": "🛡️", "title": "Immune system", "at": [1, "immune"]},
            {"type": "card", "x": 1190, "y": 250, "w": 440, "h": 130, "emoji": "🩹", "title": "Wound healing", "at": [1, "wound"]},
            {"type": "card", "x": 720, "y": 410, "w": 440, "h": 130, "emoji": "👅", "title": "Taste & smell", "at": [1, "taste"]},
            {"type": "card", "x": 1190, "y": 410, "w": 440, "h": 130, "emoji": "🧬", "title": "Testosterone", "at": [1, "testosterone"]},
            {"type": "card", "x": 760, "y": 680, "w": 1000, "h": 150, "emoji": "🥦", "title": "Extra useful for plant-based eaters",
             "at": [2, "plant"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("P", "But... there's a plot twist, isn't there?", {"mood": "worried"}),
            ("H", "There is. Plant foods, seeds included, contain compounds called phytates. "
                  "Phytates can bind minerals like zinc and reduce how much your body absorbs.",
             {"say": "There is. Plant foods, seeds included, contain compounds called fy-tates. "
                     "Fy-tates can bind minerals like zinc and reduce how much your body absorbs."}),
            ("H", "So the number on the table is what's in the seed, not necessarily what ends up in you.", {}),
            ("P", "Hey! I'm still sharing. Mostly.", {"mood": "worried"}),
            ("H", "Fair. And to be clear, this does not mean pumpkin seeds cause a deficiency. It just means the label isn't the whole story.", {}),
        ], "els": [
            {"type": "phytate", "x": 720, "y": 450, "at": [1, "phytates."], "grab": [1, "bind"]},
            T("Phytates", 300, 150, 84, at=[1, "phytates."], font="fredoka", weight=700, color="#7C3AED"),
            {"type": "pill", "x": 720, "y": 780, "text": "in the seed ≠ absorbed", "color": "orange", "at": [2, "number"]},
            {"type": "pill", "x": 720, "y": 865, "text": "but no, they don't cause a deficiency", "color": "ok", "at": [4, "deficiency"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "prostate", "title": "The Prostate Question", "emoji": "🔎", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now, the most famous claim about pumpkin seeds: prostate health. Let's be precise, because this one gets exaggerated a lot.", {}),
            ("H", "Controlled studies found improvements in the symptoms of B P H. That's benign prostatic hyperplasia, "
                  "a non-cancerous enlargement of the prostate. Things like how often you need to pee, and the quality of the flow.",
             {"say": "Controlled studies found improvements in the symptoms of B P H. That's benign prostatic hyperplasia, "
                     "a non cancerous enlargement of the prostate. Things like how often you need to pee, and the quality of the flow."}),
            ("P", "Ahem. Very glamorous science.", {"mood": "smug"}),
        ], "els": [
            T("BPH", 560, 260, 150, at=[1, "B"], font="fredoka", weight=700, color="green"),
            T("Benign Prostatic Hyperplasia", 560, 390, 46, at=[1, "benign"], color="ink", weight=600),
            T("a non-cancerous enlargement", 560, 450, 40, at=[1, "non"], color="muted"),
            {"type": "card", "x": 560, "y": 640, "w": 760, "h": 140, "emoji": "🚻", "title": "Symptoms improved",
             "body": "how often you go · how well it flows", "at": [1, "often"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "But here's the catch. Those results came mostly from concentrated pumpkin seed oil, not necessarily from eating the seeds. "
                  "The suspected reasons are plant sterols and zinc.", {}),
            ("H", "What has not been shown: that pumpkin seeds prevent prostate cancer, or that they shrink the gland itself.", {}),
            ("H", "So think of it as support for symptoms, not a treatment for disease.", {}),
        ], "els": [
            {"type": "check", "x": 240, "y": 230, "w": 1260, "ok": True, "text": "Helped BPH symptoms (mostly with the oil)", "at": [0, "oil"]},
            {"type": "check", "x": 240, "y": 360, "w": 1260, "ok": True, "text": "Likely why: plant sterols + zinc", "at": [0, "sterols"]},
            {"type": "check", "x": 240, "y": 490, "w": 1260, "ok": False, "text": "Prevents prostate cancer: not shown", "at": [1, "cancer"]},
            {"type": "check", "x": 240, "y": 620, "w": 1260, "ok": False, "text": "Shrinks the gland: not shown", "at": [1, "shrink"]},
            {"type": "banner", "x": 870, "y": 790, "text": "Symptom support, not a treatment", "color": "#475569", "at": [2, "support"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "sleep", "title": "Sleepy Seeds?", "emoji": "🌙", "dark": True, "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Pumpkin seeds are also one of the richest sources of tryptophan. "
                  "That's an amino acid your body uses to make serotonin and melatonin.", {}),
            ("P", "So I'm a bedtime snack! Goodnight, everybody.", {"mood": "sleepy"}),
            ("H", "Not so fast, Pip. The idea makes sense on paper, but the direct studies are small.", {}),
        ], "els": [
            {"type": "card", "x": 360, "y": 230, "w": 440, "h": 150, "emoji": "🎃", "title": "Tryptophan", "at": [0, "tryptophan"], "fill": "#312E81", "title_color": "white"},
            {"type": "arrow", "x1": 500, "y1": 315, "x2": 610, "y2": 375, "at": [0, "serotonin"], "color": "#A5B4FC"},
            {"type": "card", "x": 790, "y": 400, "w": 420, "h": 150, "emoji": "😊", "title": "Serotonin", "at": [0, "serotonin"], "fill": "#312E81", "title_color": "white"},
            {"type": "arrow", "x1": 930, "y1": 485, "x2": 1040, "y2": 545, "at": [0, "melatonin"], "color": "#A5B4FC"},
            {"type": "card", "x": 1220, "y": 570, "w": 420, "h": 150, "emoji": "😴", "title": "Melatonin", "at": [0, "melatonin"], "fill": "#312E81", "title_color": "white"},
            {"type": "zzz", "x": 1700, "y": 430, "at": 1, "out": 2},
            {"type": "pill", "x": 520, "y": 740, "text": "makes sense on paper", "color": "ok", "at": [2, "paper"]},
            {"type": "pill", "x": 520, "y": 830, "text": "direct studies are small", "color": "orange", "at": [2, "small"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "There's also a neat trick. For tryptophan to reach the brain, it helps to have a little carbohydrate alongside it. "
                  "So a handful of seeds with a date, or a slice of bread, makes more sense than seeds on their own.", {}),
            ("P", "A date? How romantic.", {"mood": "happy"}),
        ], "els": [
            E("🎃", 330, 420, 170, at=[0, "tryptophan"]),
            T("+", 560, 420, 140, at=[0, "carbohydrate"], font="fredoka", weight=700, color="white"),
            E("🌴", 790, 400, 150, at=[0, "date"]),
            T("a date", 790, 530, 48, at=[0, "date"], color="white", font="fredoka", weight=600),
            T("or", 1000, 420, 56, at=[0, "slice"], color="#A5B4FC"),
            E("🍞", 1200, 400, 150, at=[0, "bread"]),
            T("bread", 1200, 530, 48, at=[0, "bread"], color="white", font="fredoka", weight=600),
            T("Tryptophan + a little carb", 760, 720, 64, at=[0, "makes"], color="#FDE68A", font="fredoka", weight=700),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Two bonus facts. Pumpkin seeds bring plant sterols, about two hundred sixty-five milligrams per hundred grams, "
                  "which compete with cholesterol for absorption in the gut. Plus unsaturated fats and vitamin E.", {}),
        ], "els": [
            {"type": "card", "x": 560, "y": 330, "w": 880, "h": 190, "emoji": "🌿", "title": "Plant sterols ~265 mg / 100 g",
             "body": "compete with cholesterol in the gut", "at": [0, "sterols"], "fill": "#312E81", "title_color": "white"},
            {"type": "card", "x": 560, "y": 590, "w": 880, "h": 160, "emoji": "🫒", "title": "Unsaturated fats + vitamin E",
             "at": [0, "unsaturated"], "fill": "#312E81", "title_color": "white"},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_C, "lines": [
            ("H", "Alright. Every food has its downsides, and Pip has a few.", {}),
            ("P", "I prefer the word... quirks.", {"mood": "smug"}),
        ], "els": [
            T("Downsides", 960, 140, 100, at=0, font="fredoka", weight=700, color="red", strike=[1, "quirks"]),
            T("Quirks", 960, 255, 84, at=[1, "quirks"], font="fredoka", weight=700, color="green", rot=-0.06),
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Quirk number one: calories. One hundred grams of these seeds is about five hundred seventy-four calories. "
                  "Snack straight from the bag, and you can get there faster than you think.", {}),
            ("H", "So measure a portion into a small bowl. In practice, the difference between a measured bowl and the open bag can be three times or more.", {}),
        ], "els": [
            T("#1 Calories", 760, 160, 76, at=0, font="fredoka", weight=700, color="red"),
            {"type": "stat", "x": 470, "y": 460, "w": 460, "h": 330, "value": 574, "unit": "", "label": "calories per 100 g", "emoji": "🔥", "at": [0, "five"]},
            {"type": "stat", "x": 1060, "y": 460, "w": 460, "h": 330, "value": 161, "unit": "", "label": "per 28 g bowl", "emoji": "🥣", "at": [1, "bowl."], "color": "ok"},
            {"type": "banner", "x": 760, "y": 780, "text": "Bag snacking = 3× or more", "color": "#DC2626", "at": [1, "three"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Quirk number two: salt. In salted products, the sodium varies a lot from brand to brand. "
                  "Compare labels, and pick unsalted if you're cutting back on sodium.", {}),
            ("H", "Quirk number three: bloating. A big pile of seeds and fiber, especially with the shells, "
                  "or if you're not used to fiber, can upset your stomach. Start smaller, and try shelled seeds.", {}),
            ("P", "Translation: don't eat a whole bucket of me. Respect the seed.", {"mood": "smug", "jump": True}),
        ], "els": [
            {"type": "card", "x": 760, "y": 300, "w": 1100, "h": 190, "emoji": "🧂", "title": "#2 Salt",
             "body": "sodium varies by brand · compare labels · go unsalted", "at": 0},
            {"type": "card", "x": 760, "y": 560, "w": 1100, "h": 190, "emoji": "🎈", "title": "#3 Bloating",
             "body": "big portions + shells · start small · try shelled", "at": 1},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And quirk number four: kidney stones. If you've been told to limit oxalates or sodium because of kidney stones, "
                  "the right amount depends on your stone type and your overall diet.", {}),
            ("H", "So check with your healthcare professional, instead of following a blanket rule.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 330, "w": 1000, "h": 200, "emoji": "🪨", "title": "#4 Kidney stones",
             "body": "depends on stone type and your whole diet", "at": 0},
            {"type": "card", "x": 720, "y": 600, "w": 1000, "h": 160, "emoji": "🩺", "title": "Ask your healthcare professional",
             "at": [1, "healthcare"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "howto", "title": "How to Eat Them", "emoji": "🥗", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So, how do you actually use them? Sprinkle a measured handful on a salad, on Greek yogurt, or in granola. "
                  "You get crunch, protein and magnesium.", {}),
            ("H", "Pair them with something rich in vitamin C, like bell peppers or citrus. "
                  "That helps your body absorb the plant kind of iron, called non-heme iron.", {}),
        ], "els": [
            E("🥗", 330, 330, 170, at=[0, "salad"]),
            T("salad", 330, 460, 44, at=[0, "salad"], font="fredoka", weight=600),
            E("🥛", 720, 330, 170, at=[0, "yogurt"]),
            T("Greek yogurt", 720, 460, 44, at=[0, "yogurt"], font="fredoka", weight=600),
            E("🥣", 1110, 330, 170, at=[0, "granola"]),
            T("granola", 1110, 460, 44, at=[0, "granola"], font="fredoka", weight=600),
            {"type": "card", "x": 720, "y": 700, "w": 1060, "h": 170, "emoji": "🍊", "title": "+ vitamin C (peppers, citrus)",
             "body": "helps absorb plant (non-heme) iron", "at": [1, "vitamin"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Pumpkin seed oil is dark green, with a strong, nutty flavor. Use it in dressings only. It's not for cooking with heat. "
                  "And fun fact: that's the form used in those prostate studies.", {}),
            ("H", "Roasting at home? Go gentle. Up to about one hundred fifty degrees Celsius, around three hundred Fahrenheit, "
                  "for about fifteen minutes, keeps most of the good stuff and improves the flavor.", {}),
            ("P", "And if I taste bitter, that's not my personality. It means my fats have oxidized. Toss me.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 370, "y": 300, "w": 560, "h": 200, "emoji": "🫙", "title": "Seed oil",
             "body": "dressings only · no heat", "at": [0, "oil"]},
            {"type": "card", "x": 1000, "y": 300, "w": 640, "h": 200, "emoji": "🔥", "title": "Up to 150°C / 300°F",
             "body": "about 15 minutes", "at": [1, "Celsius"]},
            {"type": "card", "x": 720, "y": 590, "w": 1000, "h": 170, "emoji": "😖", "title": "Bitter = oxidized fats",
             "body": "throw them out", "at": [2, "bitter"], "fill": "#FEE2E2"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And soaking? You can do it if a recipe calls for it. But there's no solid evidence that soaking "
                  "improves mineral absorption in pumpkin seeds.", {}),
        ], "els": [
            E("💧", 720, 340, 200, at=0, wobble=True),
            {"type": "pill", "x": 720, "y": 560, "text": "fine for recipes", "color": "ok", "at": [0, "recipe"]},
            {"type": "pill", "x": 720, "y": 650, "text": "no proof it boosts mineral absorption", "color": "orange", "at": [0, "evidence"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 9
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: magnesium is the real star. A handful gives about thirty-seven percent of the daily value, and it's a mineral many people miss.", {}),
            ("H", "Two: zinc and protein are solid bonuses. About nineteen percent of the daily value, and eight point four grams of protein.", {}),
            ("H", "Three: the prostate benefit is real but limited. Mostly for B P H symptoms, and mostly with the oil.",
             {"say": "Three: the prostate benefit is real but limited. Mostly for B P H symptoms, and mostly with the oil."}),
            ("H", "Four: the catches that matter most are portion size and salt. Measure, and check the label.", {}),
        ], "els": [
            {"type": "check", "x": 200, "y": 200, "w": 1300, "ok": True, "text": "Magnesium is the star: 37% DV per handful", "at": 1},
            {"type": "check", "x": 200, "y": 340, "w": 1300, "ok": True, "text": "Bonus: zinc 19% DV + 8.4 g protein", "at": 2},
            {"type": "check", "x": 200, "y": 480, "w": 1300, "ok": True, "text": "Prostate: BPH symptoms, mostly the oil", "at": 3},
            {"type": "check", "x": 200, "y": 620, "w": 1300, "ok": True, "text": "Watch portion size and salt", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So... am I a big deal or not?", {"mood": "surprised"}),
            ("H", "Honestly, Pip? Pretty big, for a tiny seed.", {}),
            ("P", "I knew it!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate dot blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Go eat a measured handful!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article + sources: wiseplate.blog/food/pumpkin-seeds", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
