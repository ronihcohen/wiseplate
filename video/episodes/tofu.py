"""Tofu explainer (English), based on https://wiseplate.blog/en/food/tofu/

Numbers are the article's: tofu per 100 g (firm tofu about 144 calories and
15-17 g protein; silken 5-8 g), calcium by coagulant (calcium sulfate
200-350 mg, nigari under 50 mg), the types table (silken 5-8, soft 8-10,
firm 12-15, extra firm 15-17 g protein), PDCAAS about 0.9-1.0, the FDA claim
of 25 g soy protein a day, and a 4-hour gap for thyroxine. Keep them in sync
with content/food/tofu.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Tofu: Protein, Calcium and the Soy Hormone Myth"
SLUG = "tofu"
ARTICLE = "https://wiseplate.blog/en/food/tofu/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "TOFU", "top_size": 220, "bottom": "SOY MYTHS?", "bottom_size": 150,
         "badge": "15-17g", "badge_size": 92, "badge_label": "protein\nper 100 g", "badge_color": "#0EA5E9",
         "scatter": "🫘", "hero": "🥢", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "meet":     {"bpm": 104, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.65, "swing": 0.15},
    "calcium":  {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "protein":  {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "hormones": {"bpm": 92, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.55},
    "heart":    {"bpm": 100, "root": 69, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.1},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FEFCE8", "meet": "#FEF3C7", "calcium": "#E0F2FE", "protein": "#ECFCCB",
    "hormones": "#F1F5F9", "heart": "#FFE4E6", "catches": "#FEE2E2", "howto": "#FFEDD5",
    "outro": "#FEFCE8",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hi there! Pip the pumpkin seed here, plant-based since day one.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest is a fellow plant, pale, wobbly, and misunderstood. It's tofu!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🫘", 960, 200, 160, at=[1, "tofu"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today it's tofu. Its protein, a calcium twist almost nobody talks about, "
                  "the soy and hormones question, and how to make it actually taste good.", {}),
            ("P", "Hormones? Ooh, a myth to bust. My favorite.", {"mood": "smug"}),
        ], "els": [
            E("🫘", 420, 330, 200, at=[0, "tofu"], wobble=True),
            T("Tofu", 640, 300, 140, at=[0, "tofu"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "💪", "title": "The protein", "at": [0, "protein"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🦴", "title": "The calcium twist", "at": [0, "calcium"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "🔬", "title": "Soy and hormones", "at": [0, "hormones"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "meet", "title": "Meet Tofu", "emoji": "🫘", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Tofu is made from just three ingredients: soybeans, water, and a coagulant.", {}),
            ("H", "It's made a bit like cheese. The soybeans are soaked and ground into a drink, the drink is curdled with the coagulant, "
                  "and the curds are pressed into molds.", {}),
            ("H", "It started in China about two thousand years ago, and it's a major protein source in East Asian cooking.", {}),
            ("P", "Two thousand years old and still this smooth. What's the secret?", {"mood": "surprised"}),
        ], "els": [
            T("Just 3 ingredients", 720, 160, 72, at=0, font="fredoka", weight=700, color="green"),
            E("🫘", 400, 330, 130, at=[0, "soybeans"]),
            T("soybeans", 400, 440, 40, at=[0, "soybeans"], font="fredoka", weight=600),
            E("💧", 720, 330, 130, at=[0, "water"]),
            T("water", 720, 440, 40, at=[0, "water"], font="fredoka", weight=600),
            E("🧪", 1040, 330, 130, at=[0, "coagulant"]),
            T("coagulant", 1040, 440, 40, at=[0, "coagulant"], font="fredoka", weight=600),
            {"type": "pill", "x": 720, "y": 590, "text": "soak, grind, curdle, press", "color": "orange", "at": [1, "cheese"]},
            {"type": "pill", "x": 720, "y": 720, "text": "China, about 2,000 years ago", "color": "#0EA5E9", "at": [2, "China"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "A hundred grams of firm tofu has about one hundred forty-four calories, fifteen to seventeen grams of protein, "
                  "eight grams of fat, and two to three grams of carbs.", {}),
            ("H", "Silken tofu has more water, and less protein: about five to eight grams.", {}),
        ], "els": [
            T("Firm tofu, per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 330, "y": 390, "w": 400, "h": 280, "value": 144, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "calories"]},
            {"type": "stat", "x": 760, "y": 390, "w": 400, "h": 280, "value": 0, "text": "15–17 g", "vsize": 92, "label": "protein", "emoji": "💪", "at": [0, "fifteen"]},
            {"type": "stat", "x": 1190, "y": 390, "w": 400, "h": 280, "value": 8, "unit": " g", "label": "fat", "emoji": "🫒", "at": [0, "eight"]},
            {"type": "pill", "x": 760, "y": 620, "text": "carbs: 2–3 g", "color": "#B45309", "at": [0, "carbs"]},
            {"type": "pill", "x": 760, "y": 740, "text": "silken: 5–8 g protein, more water", "color": "#0EA5E9", "at": [1, "Silken"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "calcium", "title": "The Calcium Twist", "emoji": "🦴", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Here's the most practical point about tofu, and it's almost always missing from the conversation. "
                  "The coagulant decides how much calcium you get.", {}),
            ("H", "Calcium sulfate, also called gypsum, is used in most Western factory-made tofu. "
                  "It adds a lot of calcium: two hundred to three hundred fifty milligrams per hundred grams.", {}),
            ("H", "Nigari, which is magnesium chloride, is used in traditional Japanese tofu. "
                  "It gives a more delicate texture and taste, but adds almost no calcium, usually under fifty milligrams.",
             {"say": "Nee-gah-ree, which is magnesium chloride, is used in traditional Japanese tofu. "
                     "It gives a more delicate texture and taste, but adds almost no calcium, usually under fifty milligrams."}),
        ], "els": [
            T("Calcium per 100 g, by coagulant", 760, 160, 56, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 160, "y": 360, "w": 1300, "row_h": 150, "max": 350, "unit": " mg", "rows": [
                {"label": "Calcium sulfate", "value": 350, "text": "200–350 mg", "color": "#16A34A", "at": [1, "two"]},
                {"label": "Nigari", "value": 50, "text": "under 50 mg", "color": "#EF4444", "at": [2, "fifty"]},
            ]},
            {"type": "pill", "x": 760, "y": 680, "text": "a five- to sevenfold difference", "color": "orange", "at": 3},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "That's a five- to sevenfold difference. With calcium sulfate, tofu's calcium is comparable to cheese, "
                  "and even higher than milk by weight.", {}),
            ("H", "So tofu is not automatically a calcium source. If you rely on it for calcium on a vegan diet, "
                  "check the ingredient list for calcium sulfate.", {}),
            ("P", "Read the label, people. The tofu won't tell you itself.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 1000, "h": 180, "emoji": "🧀", "title": "Like cheese, beats milk",
             "body": "with calcium sulfate, by weight", "at": [0, "cheese"]},
            {"type": "card", "x": 720, "y": 470, "w": 1000, "h": 180, "emoji": "🏷️", "title": "Check the label",
             "body": "look for calcium sulfate", "at": [1, "ingredient"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Another plus: the calcium in tofu is well absorbed, about thirty percent, similar to milk. "
                  "That's because soy is low in oxalates, unlike spinach.", {}),
            ("P", "Sorry, spinach. Tofu wins this round.", {"mood": "happy"}),
        ], "els": [
            {"type": "ring", "x": 520, "y": 430, "r": 170, "value": 30, "color": "#16A34A", "label": "absorbed", "at": [0, "thirty"]},
            {"type": "card", "x": 1060, "y": 340, "w": 620, "h": 160, "emoji": "🥛", "title": "Similar to milk", "at": [0, "milk"]},
            {"type": "card", "x": 1060, "y": 560, "w": 620, "h": 160, "emoji": "🥬", "title": "Low oxalates", "at": [0, "oxalates"],
             "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "protein", "title": "Protein Power", "emoji": "💪", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Soy protein is one of the few plant proteins with all nine essential amino acids in sufficient amounts.", {}),
            ("H", "Its PDCAAS score, a measure of protein quality, is about zero point nine to one. "
                  "That's on par with egg and milk protein, and much higher than most plant proteins.",
             {"say": "Its P D C A A S score, a measure of protein quality, is about zero point nine to one. "
                     "That's on par with egg and milk protein, and much higher than most plant proteins."}),
            ("P", "A plant with a perfect score? Okay, I'm a little jealous.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 180, "emoji": "🧩", "title": "Complete protein",
             "body": "all 9 essential amino acids", "at": 0},
            {"type": "stat", "x": 520, "y": 540, "w": 560, "h": 300, "value": 0, "text": "0.9–1.0", "vsize": 96,
             "label": "PDCAAS score", "emoji": "🏅", "at": [1, "zero"]},
            E("🥚", 1010, 500, 120, at=[1, "egg"]),
            E("🥛", 1210, 500, 120, at=[1, "milk"]),
            T("on par", 1110, 620, 44, at=[1, "par"], font="fredoka", weight=600, color="green"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "For building muscle, trials comparing soy protein with whey found that both work. "
                  "Milk protein has a slight edge, because it has more leucine.",
             {"say": "For building muscle, trials comparing soy protein with whey found that both work. "
                     "Milk protein has a slight edge, because it has more loo-seen."}),
            ("H", "But the gap almost disappears when your total protein intake is high enough.", {}),
            ("H", "And with fifteen to seventeen grams of protein in one hundred forty-four calories, "
                  "it has a very good protein-to-calorie ratio, which suits weight management.", {}),
            ("P", "Muscles from beans. Pip approves.", {"mood": "happy", "jump": True}),
        ], "els": [
            T("Soy vs whey", 720, 170, 80, at=0, font="fredoka", weight=700, color="green"),
            {"type": "pill", "x": 460, "y": 310, "text": "both build muscle", "color": "green", "at": [0, "both"]},
            {"type": "pill", "x": 1000, "y": 310, "text": "whey: a bit more leucine", "color": "orange", "at": [0, "edge"]},
            {"type": "card", "x": 720, "y": 500, "w": 1000, "h": 170, "emoji": "📏", "title": "Gap almost closes",
             "body": "with enough total protein", "at": [1, "gap"]},
            {"type": "card", "x": 720, "y": 720, "w": 1000, "h": 170, "emoji": "⚖️", "title": "Great protein per calorie",
             "body": "15–17 g in 144 calories", "at": [2, "ratio"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "hormones", "title": "Soy and Hormones", "emoji": "🔬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the famous worry. Soy contains isoflavones, which are phytoestrogens, plant compounds that look a bit like estrogen.",
             {"say": "Now the famous worry. Soy contains eye-so-flay-vones, which are fyto-estrogens, plant compounds that look a bit like estrogen."}),
            ("H", "They bind mainly to the estrogen receptor called beta, and with a potency thousands of times lower than human estrogen.", {}),
            ("P", "Thousands of times weaker? That's like comparing me to a pumpkin.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 1000, "h": 180, "emoji": "🌱", "title": "Isoflavones",
             "body": "phytoestrogens from soy", "at": 0},
            {"type": "card", "x": 720, "y": 460, "w": 1000, "h": 180, "emoji": "🔑", "title": "Mainly receptor beta",
             "body": "thousands of times weaker", "at": [1, "beta"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And here's what the evidence says. Meta-analyses of controlled trials found no effect on testosterone or estrogen in men, "
                  "at dietary amounts. And no effect on sperm quality either.",
             {"say": "And here's what the evidence says. Meta analyses of controlled trials found no effect on testosterone or estrogen in men, "
                     "at dietary amounts. And no effect on sperm quality either."}),
            ("H", "On breast cancer, cohort studies lean toward a protective or neutral effect, "
                  "and leading organizations don't recommend avoiding soy.", {}),
            ("P", "Myth busted. Tofu, you're free to go.", {"mood": "happy", "jump": True}),
        ], "els": [
            T("Men, dietary amounts", 720, 170, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "check", "x": 220, "y": 300, "w": 1000, "ok": True, "text": "Testosterone: no effect", "at": [0, "testosterone"]},
            {"type": "check", "x": 220, "y": 420, "w": 1000, "ok": True, "text": "Estrogen: no effect", "at": [0, "estrogen"]},
            {"type": "check", "x": 220, "y": 540, "w": 1000, "ok": True, "text": "Sperm quality: no effect", "at": [0, "sperm"]},
            {"type": "pill", "x": 720, "y": 700, "text": "breast cancer: protective or neutral", "color": "#0EA5E9", "at": [1, "breast"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "heart", "title": "Heart and Minerals", "emoji": "❤️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Most of the fat in tofu is unsaturated, and it has no cholesterol.", {}),
            ("H", "The FDA approved a health claim: twenty-five grams of soy protein a day, in a diet low in saturated fat, "
                  "may reduce the risk of heart disease.",
             {"say": "The F D A approved a health claim: twenty-five grams of soy protein a day, in a diet low in saturated fat, "
                     "may reduce the risk of heart disease."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 170, "emoji": "🫒", "title": "Mostly unsaturated fat",
             "body": "and no cholesterol", "at": 0},
            {"type": "card", "x": 720, "y": 450, "w": 1000, "h": 190, "emoji": "❤️", "title": "FDA: 25 g soy protein",
             "body": "a day, low saturated fat diet", "at": [1, "twenty"], "fill": "#DCFCE7"},
            {"type": "pill", "x": 720, "y": 650, "text": "may reduce heart disease risk", "color": "green", "at": [1, "reduce"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Tofu is also a good source of iron. It's non-heme iron, which is absorbed less well, "
                  "but pairing it with vitamin C helps.",
             {"say": "Tofu is also a good source of iron. It's non heem iron, which is absorbed less well, "
                     "but pairing it with vitamin C helps."}),
            ("H", "Plus manganese, phosphorus and selenium. "
                  "And it's minimally processed: unlike factory-made meat substitutes, traditional tofu has just three ingredients.", {}),
            ("P", "Three ingredients. I respect a short label. Mine has one.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 180, "emoji": "🩸", "title": "Iron, non-heme",
             "body": "add vitamin C to absorb more", "at": 0},
            {"type": "pill", "x": 420, "y": 410, "text": "manganese", "color": "#8B5CF6", "at": [1, "manganese"]},
            {"type": "pill", "x": 760, "y": 410, "text": "phosphorus", "color": "#0EA5E9", "at": [1, "phosphorus"]},
            {"type": "pill", "x": 1090, "y": 410, "text": "selenium", "color": "#B45309", "at": [1, "selenium"]},
            {"type": "card", "x": 720, "y": 620, "w": 1000, "h": 180, "emoji": "✅", "title": "Minimally processed",
             "body": "soy, water, coagulant", "at": [1, "minimally"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Now the downsides. Soy allergy is one of the leading allergies in children, and it means avoiding soy completely.", {}),
            ("H", "Soy may interfere with absorbing thyroxine, the thyroid medication. Leave at least four hours between the pill and soy foods, "
                  "and coordinate with your doctor.",
             {"say": "Soy may interfere with absorbing thigh-rox-een, the thyroid medication. Leave at least four hours between the pill and soy foods, "
                     "and coordinate with your doctor."}),
            ("H", "If your thyroid works normally and you get enough iodine, there's no effect.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1300, "ok": False, "text": "Soy allergy: avoid completely", "at": [0, "allergy"]},
            {"type": "check", "x": 160, "y": 330, "w": 1300, "ok": False, "text": "Thyroxine: wait 4 hours", "at": [1, "four"]},
            {"type": "check", "x": 160, "y": 460, "w": 1300, "ok": True, "text": "Normal thyroid, enough iodine: fine", "at": [2, "iodine"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Phytate reduces the absorption of iron and zinc. Making tofu removes some of it, and vitamin C in the meal offsets it.",
             {"say": "Fy-tate reduces the absorption of iron and zinc. Making tofu removes some of it, and vitamin C in the meal offsets it."}),
            ("H", "Processed tofu products, like tofu sausages, schnitzels and flavored products, usually carry a lot of sodium, oils and additives. "
                  "They're entirely different from plain tofu.", {}),
            ("H", "And plain tofu is almost flavorless. That's a cooking advantage, since it soaks up flavors, "
                  "but people often see it as a flaw. Most tofu failures come from poor preparation, not the product.", {}),
            ("P", "Bland? Or a blank canvas? I say canvas.", {"mood": "smug"}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1300, "ok": False, "text": "Phytate: less iron and zinc", "at": [0, "Phytate"]},
            {"type": "check", "x": 160, "y": 330, "w": 1300, "ok": False, "text": "Processed tofu: sodium, oils", "at": [1, "sausages"]},
            {"type": "check", "x": 160, "y": 460, "w": 1300, "ok": False, "text": "Nearly flavorless on its own", "at": [2, "flavorless"]},
            {"type": "pill", "x": 760, "y": 620, "text": "vitamin C helps offset phytate", "color": "green", "at": [0, "offsets"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "Types and Tricks", "emoji": "🍳", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "There are four main types, and their protein per hundred grams goes up as they get firmer.", {}),
            ("H", "Silken: five to eight grams, for sauces, desserts, shakes and miso soup. Soft: eight to ten, for soups and delicate dishes.",
             {"say": "Silken: five to eight grams, for sauces, desserts, shakes and mee-so soup. Soft: eight to ten, for soups and delicate dishes."}),
            ("H", "Firm: twelve to fifteen, for stir-fries and baking. Extra firm: fifteen to seventeen, for roasting, frying and grilling.", {}),
        ], "els": [
            T("Protein per 100 g, by type", 760, 140, 56, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 160, "y": 290, "w": 1300, "row_h": 120, "max": 17, "unit": " g", "rows": [
                {"label": "Silken", "value": 8, "text": "5–8 g", "color": "#0EA5E9", "at": [1, "Silken"]},
                {"label": "Soft", "value": 10, "text": "8–10 g", "color": "#8B5CF6", "at": [1, "Soft"]},
                {"label": "Firm", "value": 15, "text": "12–15 g", "color": "#F97316", "at": [2, "Firm"]},
                {"label": "Extra firm", "value": 17, "text": "15–17 g", "color": "#16A34A", "at": [2, "Extra"]},
            ]},
            {"type": "pill", "x": 760, "y": 790, "text": "silken and firm don't swap", "color": "orange", "at": [2, "grilling"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Now the step that changes the result the most: pressing. Firm tofu holds a lot of water.", {}),
            ("H", "Press it between two plates with a weight on top for twenty to thirty minutes, or use a tofu press. "
                  "It concentrates the protein, improves the texture, and lets it soak up marinade much better.", {}),
            ("P", "Squeeze the tofu. Got it. Gently. It's been through enough.", {"mood": "worried"}),
        ], "els": [
            T("1. Press it", 720, 170, 80, at=0, font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 450, "y": 450, "w": 480, "h": 300, "value": 0, "text": "20–30", "vsize": 100,
             "label": "minutes", "emoji": "⏱️", "at": [1, "twenty"]},
            {"type": "card", "x": 1000, "y": 360, "w": 540, "h": 140, "emoji": "💪", "title": "More protein", "at": [1, "concentrates"]},
            {"type": "card", "x": 1000, "y": 540, "w": 540, "h": 140, "emoji": "🥢", "title": "Better texture", "at": [1, "texture"]},
            {"type": "card", "x": 1000, "y": 720, "w": 540, "h": 140, "emoji": "🧂", "title": "Soaks marinade", "at": [1, "marinade"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "A lesser-known trick: freeze it, then thaw it. Ice crystals tear the tofu's structure, "
                  "so after thawing it's spongy and much chewier. It soaks up marinade brilliantly, and the texture is almost meaty.", {}),
            ("H", "For crunch, coat pressed cubes in a spoonful of cornstarch before frying or baking.", {}),
            ("H", "And season boldly. Coconut aminos or soy sauce, garlic, ginger and sesame oil make a classic base. Give it at least thirty minutes.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 170, "emoji": "🧊", "title": "2. Freeze, then thaw",
             "body": "spongy, chewy, almost meaty", "at": 0},
            {"type": "card", "x": 720, "y": 410, "w": 1000, "h": 170, "emoji": "🌽", "title": "3. Cornstarch coat",
             "body": "for a crispy crust", "at": [1, "cornstarch"]},
            {"type": "card", "x": 720, "y": 620, "w": 1000, "h": 170, "emoji": "🧄", "title": "4. Marinate 30+ min",
             "body": "soy sauce, garlic, ginger, sesame", "at": [2, "season"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: tofu is one of the best plant proteins there is. Complete protein, comparable to egg and milk, with minimal processing.", {}),
            ("H", "Two: the worries about isoflavones aren't supported by the evidence.", {"say": "Two: the worries about eye-so-flay-vones aren't supported by the evidence."}),
            ("H", "Three: if calcium matters to you, check the coagulant on the label.", {}),
            ("H", "Four: press it or freeze it before cooking. That's the difference between great tofu and sad tofu.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Complete protein, minimal processing", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Isoflavone fears: not supported", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Calcium? Check the coagulant", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Press or freeze before cooking", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So tofu: quiet, wobbly, and secretly a protein champion. We plants have to stick together.", {"mood": "smug"}),
            ("H", "Team plant, Pip.", {}),
            ("P", "Team plant!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Remember: press your tofu!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/tofu", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
