"""Cinnamon explainer (English), based on https://wiseplate.blog/en/food/cinnamon/

Numbers are the article's: ground cinnamon per teaspoon (2.6 g) with % daily
value, coumarin in mg per gram of Ceylon vs cassia and per teaspoon of cassia,
the EFSA tolerable daily intake (0.1 mg coumarin per kg body weight, 6 mg for
a 60 kg person), and the fasting-glucose drop in mg/dL from meta-analyses.
Keep them in sync with content/food/cinnamon.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Cinnamon: Is Your Everyday Cinnamon the Wrong Kind?"
SLUG = "cinnamon"
ARTICLE = "https://wiseplate.blog/en/food/cinnamon/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "CINNAMON", "top_size": 180, "bottom": "WRONG KIND?", "bottom_size": 140,
         "badge": "1 tsp", "badge_size": 110, "badge_label": "cassia may\nhit the limit", "badge_color": "#B45309",
         "scatter": "🪵", "hero": "🥄", "mood": "worried"}

MUSIC = {
    "intro":    {"bpm": 110, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "meet":     {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "inside":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "versus":   {"bpm": 116, "root": 62, "prog": ["I", "bVII", "IV", "I"], "density": 0.8, "swing": 0.1},
    "coumarin": {"bpm": 86, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "sugar":    {"bpm": 94, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.55},
    "benefits": {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "kitchen":  {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF7ED", "meet": "#FEF3C7", "inside": "#FFEDD5", "versus": "#FDF2F8",
    "coumarin": "#1E1B4B", "sugar": "#E0F2FE", "benefits": "#ECFCCB", "catches": "#FEE2E2",
    "kitchen": "#FFEDD5", "outro": "#FFF7ED",
}

DARK = {"fill": "#312E81", "title_color": "white"}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hi! Pip the pumpkin seed here. Today's guest isn't a seed, it's a bark. And it smells amazing.",
             {"mood": "happy", "wave": True}),
            ("P", "It's in almost every kitchen. It's cinnamon!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🪵", 960, 200, 160, at=[1, "cinnamon"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today: cinnamon. What's in a teaspoon, the two very different kinds sold under one name, "
                  "what it really does for blood sugar, and how much is too much.", {}),
            ("P", "Two kinds under one name? This is a spy story now.", {"mood": "surprised"}),
        ], "els": [
            E("🪵", 400, 330, 200, at=[0, "cinnamon"], wobble=True),
            T("Cinnamon", 600, 300, 140, at=[0, "cinnamon"], font="fredoka", weight=700, color="#B45309", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 680, "h": 110, "emoji": "⚖️", "title": "Ceylon vs cassia", "at": [0, "kinds"]},
            {"type": "card", "x": 760, "y": 650, "w": 680, "h": 110, "emoji": "🩸", "title": "Blood sugar", "at": [0, "blood"]},
            {"type": "card", "x": 760, "y": 780, "w": 680, "h": 110, "emoji": "🥄", "title": "How much is too much", "at": [0, "much"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "meet", "title": "Meet Cinnamon", "emoji": "🌳", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Cinnamon is made from the inner bark of trees in the Cinnamomum genus. "
                  "It's one of the oldest spices in the world.",
             {"say": "Cinnamon is made from the inner bark of trees in the Sin-uh-moe-mum genus. "
                     "It's one of the oldest spices in the world."}),
            ("H", "It's mentioned in the Hebrew Bible, it was traded in ancient Egypt, "
                  "and it was among the most valuable goods of the ancient world.", {}),
            ("H", "Today it's in almost every kitchen, and in recent years researchers have studied it mainly for blood sugar control.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 160, "emoji": "🌳", "title": "Inner bark of Cinnamomum",
             "body": "one of the oldest spices", "at": 0},
            {"type": "pill", "x": 380, "y": 400, "text": "Hebrew Bible", "color": "#B45309", "at": [1, "Bible"]},
            {"type": "pill", "x": 760, "y": 400, "text": "ancient Egypt", "color": "#F59E0B", "at": [1, "Egypt"]},
            {"type": "pill", "x": 1130, "y": 400, "text": "precious", "color": "#8B5CF6", "at": [1, "valuable"]},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 160, "emoji": "🔬", "title": "Research focus: blood sugar",
             "at": [2, "blood"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "But the most important point in this video isn't a benefit. It's a distinction.", {}),
            ("H", "Two quite different products are sold as cinnamon: Ceylon, and cassia. "
                  "They differ in a substance that can harm the liver. And most of the cinnamon sold around the world is cassia.",
             {"say": "Two quite different products are sold as cinnamon: Ceylon, and cassia. "
                     "They differ in a substance that can harm the liver. And most of the cinnamon sold around the world is cassia."}),
            ("P", "Plot twist! The cinnamon in your cupboard might be a cassia in disguise.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("Two cinnamons", 720, 170, 80, at=0, font="fredoka", weight=700, color="#B45309"),
            {"type": "card", "x": 420, "y": 420, "w": 560, "h": 200, "emoji": "🇱🇰", "title": "Ceylon", "body": "the rare one",
             "at": [1, "Ceylon"]},
            {"type": "card", "x": 1040, "y": 420, "w": 560, "h": 200, "emoji": "🛒", "title": "Cassia", "body": "most of what's sold",
             "at": [1, "cassia"]},
            {"type": "banner", "x": 720, "y": 690, "text": "They differ in a liver-harming substance", "color": "#DC2626", "at": [1, "liver"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "inside", "title": "What's in a Teaspoon?", "emoji": "🥄", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "We eat cinnamon in tiny amounts, so its direct nutrition is limited. Here's one teaspoon of ground cinnamon, two point six grams.", {}),
            ("H", "Six calories. Two point one grams of carbs, of which one point four is fiber. "
                  "And sugar? Zero point zero six grams.", {}),
            ("P", "Zero point zero six? It's basically sugar-free and still tastes like dessert. Magic.", {"mood": "surprised"}),
        ], "els": [
            T("Per teaspoon (2.6 g)", 720, 150, 56, at=0, font="fredoka", weight=600, color="#B45309"),
            {"type": "stat", "x": 300, "y": 430, "w": 380, "h": 300, "value": 6, "unit": "", "label": "calories", "emoji": "🔥", "at": [1, "Six"]},
            {"type": "stat", "x": 720, "y": 430, "w": 380, "h": 300, "value": 1.4, "decimals": 1, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [1, "fiber"]},
            {"type": "stat", "x": 1140, "y": 430, "w": 380, "h": 300, "value": 0.06, "decimals": 2, "unit": " g", "label": "sugar", "emoji": "🍬",
             "color": "#DC2626", "at": [1, "sugar"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "As a percent of the daily value, the standout is manganese: seventeen percent. Fiber, five. Calcium, two. Iron and vitamin K, one each.", {}),
            ("H", "Cinnamon feels sweet because our brains link its smell with sweet pastries. But the spice itself is almost sugar-free. "
                  "That's what makes it a great way to add a sense of sweetness to porridge or yogurt, without sugar.", {}),
            ("H", "More than two thirds of its carbs are fiber, and it's one of the densest foods in polyphenols for its weight. "
                  "But remember: we're talking about just a few grams.", {}),
        ], "els": [
            T("% Daily Value per teaspoon", 760, 150, 56, at=0, font="fredoka", weight=600, color="#B45309"),
            {"type": "bars", "x": 200, "y": 270, "w": 1200, "row_h": 95, "max": 20, "rows": [
                {"label": "Manganese", "value": 17, "color": "#B45309", "at": [0, "manganese"], "star": True},
                {"label": "Fiber", "value": 5, "color": "#84CC16", "at": [0, "Fiber"]},
                {"label": "Calcium", "value": 2, "color": "#0EA5E9", "at": [0, "Calcium"]},
                {"label": "Iron", "value": 1, "color": "#EF4444", "at": [0, "Iron"]},
                {"label": "Vitamin K", "value": 1, "color": "#16A34A", "at": [0, "vitamin"]},
            ]},
            {"type": "banner", "x": 760, "y": 800, "text": "Sweet smell, almost no sugar", "color": "#B45309", "at": [1, "sugar-free"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "versus", "title": "Ceylon vs Cassia", "emoji": "⚖️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Ceylon, Cinnamomum verum, comes from Sri Lanka. It's called true cinnamon. "
                  "It's a papery, brittle roll of many thin layers, light tan-brown, with a delicate, sweet, floral flavor.",
             {"say": "Ceylon, Sin-uh-moe-mum vair-um, comes from Sri Lanka. It's called true cinnamon. "
                     "It's a papery, brittle roll of many thin layers, light tan brown, with a delicate, sweet, floral flavor."}),
            ("H", "Cassia, Cinnamomum cassia, comes from China, Indonesia and Vietnam. It's the regular cinnamon. "
                  "One thick bark, rolled into a hard stick, dark reddish-brown, with a sharp, spicy, intense flavor.",
             {"say": "Cassia, Sin-uh-moe-mum cassia, comes from China, Indonesia and Vietnam. It's the regular cinnamon. "
                     "One thick bark, rolled into a hard stick, dark reddish brown, with a sharp, spicy, intense flavor."}),
        ], "els": [
            T("Ceylon", 420, 160, 72, at=0, font="fredoka", weight=700, color="#D97706"),
            T("Cassia", 1080, 160, 72, at=1, font="fredoka", weight=700, color="#7C2D12"),
            {"type": "card", "x": 420, "y": 330, "w": 600, "h": 150, "emoji": "🇱🇰", "title": "Sri Lanka", "body": "\"true cinnamon\"",
             "at": [0, "Sri"]},
            {"type": "card", "x": 420, "y": 510, "w": 600, "h": 150, "emoji": "📜", "title": "Thin, brittle", "body": "many layers",
             "at": [0, "papery"]},
            {"type": "card", "x": 420, "y": 690, "w": 600, "h": 150, "emoji": "🌸", "title": "Sweet, floral", "body": "light tan-brown",
             "at": [0, "floral"]},
            {"type": "card", "x": 1080, "y": 330, "w": 600, "h": 150, "emoji": "🌏", "title": "China, Asia", "body": "\"regular cinnamon\"",
             "at": [1, "China"]},
            {"type": "card", "x": 1080, "y": 510, "w": 600, "h": 150, "emoji": "🪵", "title": "Thick, hard", "body": "one layer",
             "at": [1, "thick"]},
            {"type": "card", "x": 1080, "y": 690, "w": 600, "h": 150, "emoji": "🌶️", "title": "Sharp, spicy", "body": "dark reddish-brown",
             "at": [1, "spicy"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Ceylon costs three to five times more, and you'll find it in health food stores and specialty spice shops. "
                  "Cassia is cheap, and it's in most supermarkets.", {}),
            ("H", "And the big one: coumarin. Ceylon has a negligible amount, about zero point zero one seven milligrams per gram. "
                  "Cassia has about two to four milligrams per gram.",
             {"say": "And the big one: coo-ma-rin. Ceylon has a negligible amount, about zero point zero one seven milligrams per gram. "
                     "Cassia has about two to four milligrams per gram."}),
            ("P", "Hundreds of times more? Cassia, explain yourself.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 420, "y": 230, "w": 600, "h": 160, "emoji": "💰", "title": "3-5× pricier", "body": "specialty shops",
             "at": [0, "three"]},
            {"type": "card", "x": 1080, "y": 230, "w": 600, "h": 160, "emoji": "🛒", "title": "Cheap", "body": "most supermarkets",
             "at": [0, "cheap"]},
            T("Coumarin, mg per gram", 750, 450, 52, at=[1, "big"], font="fredoka", weight=600, color="#B45309"),
            {"type": "bars", "x": 180, "y": 570, "w": 1260, "row_h": 130, "max": 4, "unit": " mg", "rows": [
                {"label": "Ceylon", "value": 0.017, "text": "~0.017 mg", "color": "#16A34A", "at": [1, "negligible"]},
                {"label": "Cassia", "value": 4, "text": "~2-4 mg", "color": "#DC2626", "at": [1, "Cassia has"]},
            ]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "coumarin", "title": "The Coumarin Math", "emoji": "🧮", "dark": True, "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Coumarin is a natural aromatic compound. At high doses it damages the liver, and it was also found to cause cancer in animals.",
             {"say": "Coo-ma-rin is a natural aromatic compound. At high doses it damages the liver, and it was also found to cause cancer in animals."}),
            ("H", "The European Food Safety Authority set a tolerable daily intake: zero point one milligrams of coumarin per kilo of body weight.",
             {"say": "The European Food Safety Authority set a tolerable daily intake: zero point one milligrams of coo-ma-rin per kilo of body weight."}),
            ("H", "Now the math. For a sixty kilo person, the daily limit is six milligrams. "
                  "One teaspoon of cassia has about five to ten milligrams of coumarin.",
             {"say": "Now the math. For a sixty kilo person, the daily limit is six milligrams. "
                     "One teaspoon of cassia has about five to ten milligrams of coo-ma-rin."}),
            ("H", "So one teaspoon of cassia a day may reach, or go over, the daily limit.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 190, "w": 1000, "h": 150, "emoji": "⚠️", "title": "Coumarin",
             "body": "liver damage at high doses", "at": 0, **DARK},
            {"type": "card", "x": 720, "y": 370, "w": 1000, "h": 150, "emoji": "🇪🇺", "title": "Limit: 0.1 mg per kg a day",
             "at": [1, "tolerable"], **DARK},
            {"type": "card", "x": 420, "y": 580, "w": 560, "h": 180, "emoji": "🧍", "title": "60 kg: 6 mg",
             "body": "daily limit", "at": [2, "sixty"], **DARK},
            {"type": "card", "x": 1040, "y": 580, "w": 560, "h": 180, "emoji": "🥄", "title": "1 tsp: 5-10 mg",
             "body": "cassia", "at": [2, "teaspoon"], **DARK},
            {"type": "banner", "x": 720, "y": 790, "text": "1 teaspoon can hit the limit", "color": "#DC2626", "at": [3, "reach"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "To keep it in proportion: this is a conservative limit, set with a safety margin. Going over it once in a while is not dangerous.", {}),
            ("H", "But people who take cinnamon regularly, in therapeutic amounts, like many trying to manage blood sugar, may go over it for a long time. "
                  "A few cases in the literature describe reversible liver damage after cassia supplements.", {}),
            ("H", "So: a pinch to half a teaspoon of cassia is perfectly fine. A teaspoon or more every day, or a supplement? Switch to Ceylon. "
                  "And if the package doesn't say Ceylon, it's almost always cassia.", {}),
            ("P", "Read the label. Even seeds know that.", {"mood": "smug"}),
        ], "els": [
            {"type": "check", "x": 140, "y": 210, "w": 1300, "ok": True, "text": "Over the limit once in a while: OK", "at": [0, "once"]},
            {"type": "check", "x": 140, "y": 330, "w": 1300, "ok": False, "text": "Daily therapeutic doses of cassia", "at": [1, "therapeutic"]},
            {"type": "card", "x": 420, "y": 580, "w": 560, "h": 180, "emoji": "🤏", "title": "Pinch to ½ tsp",
             "body": "cassia is fine", "at": [2, "pinch"], **DARK},
            {"type": "card", "x": 1040, "y": 580, "w": 560, "h": 180, "emoji": "🇱🇰", "title": "1 tsp+ daily",
             "body": "switch to Ceylon", "at": [2, "Switch"], **DARK},
            T("No \"Ceylon\" on the label = cassia", 720, 790, 50, at=[2, "package"], font="fredoka", weight=700, color="#FDE68A"),
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "sugar", "title": "Blood Sugar: Fact Check", "emoji": "🩸", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now, the most researched benefit: blood sugar. Meta-analyses found a drop in fasting glucose after eating cinnamon, "
                  "about ten to twenty-five milligrams per deciliter, in people with type two diabetes.", {}),
            ("H", "The proposed mechanisms: slower stomach emptying, blocking gut enzymes that break down carbs, "
                  "and better sensitivity of the insulin receptor.", {}),
        ], "els": [
            {"type": "stat", "x": 450, "y": 380, "w": 560, "h": 320, "value": 0, "text": "10-25", "vsize": 110,
             "label": "mg/dL lower fasting glucose", "emoji": "🩸", "at": [0, "ten"]},
            {"type": "pill", "x": 1100, "y": 260, "text": "slower stomach", "color": "#0EA5E9", "at": [1, "stomach"]},
            {"type": "pill", "x": 1100, "y": 380, "text": "carb enzymes", "color": "#F59E0B", "at": [1, "enzymes"]},
            {"type": "pill", "x": 1100, "y": 500, "text": "insulin receptor", "color": "#16A34A", "at": [1, "insulin"]},
            T("type 2 diabetes · meta-analyses", 720, 700, 46, at=[0, "type"], color="muted"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "But here's the balance. The effect on HbA1c, the measure of long-term control, was inconsistent across studies. "
                  "Some found no improvement at all.",
             {"say": "But here's the balance. The effect on H B A 1 C, the measure of long term control, was inconsistent across studies. "
                     "Some found no improvement at all."}),
            ("H", "Cinnamon is not a substitute for medication, and it's not enough on its own to control diabetes.", {}),
            ("P", "So: a helpful sidekick, not the superhero. I respect a good sidekick.", {"mood": "happy"}),
        ], "els": [
            {"type": "check", "x": 140, "y": 220, "w": 1300, "ok": True, "text": "Fasting glucose: lower", "at": 0},
            {"type": "check", "x": 140, "y": 340, "w": 1300, "ok": False, "text": "HbA1c: inconsistent", "at": [0, "inconsistent"]},
            {"type": "check", "x": 140, "y": 460, "w": 1300, "ok": False, "text": "Replaces medication", "at": [1, "substitute"]},
            {"type": "banner", "x": 720, "y": 680, "text": "An addition, not a treatment", "color": "#0EA5E9", "at": [1, "enough"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "benefits", "title": "Other Benefits", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Cinnamaldehyde is the main compound. It gives the aroma and most of the biological activity, "
                  "including anti-inflammatory and antimicrobial effects shown in the lab.",
             {"say": "Sin-uh-mal-de-hyde is the main compound. It gives the aroma and most of the biological activity, "
                     "including anti inflammatory and antimicrobial effects shown in the lab."}),
            ("H", "It has high antioxidant activity, with one of the highest polyphenol levels in food for its weight.", {}),
            ("H", "Cinnamon oil stops bacteria and fungi in the lab, and was once used as a preservative. But its use inside the human body is limited.", {}),
            ("H", "And some studies showed a slight drop in LDL and triglycerides. But the findings aren't consistent.",
             {"say": "And some studies showed a slight drop in L D L and triglycerides. But the findings aren't consistent."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 190, "w": 1000, "h": 150, "emoji": "👃", "title": "Cinnamaldehyde",
             "body": "aroma + most of the activity", "at": 0},
            {"type": "card", "x": 720, "y": 370, "w": 1000, "h": 150, "emoji": "🛡️", "title": "Very high in polyphenols", "at": [1, "antioxidant"]},
            {"type": "card", "x": 720, "y": 550, "w": 1000, "h": 150, "emoji": "🦠", "title": "Antimicrobial in the lab",
             "body": "limited use in the body", "at": [2, "bacteria"], "fill": "#FEF3C7"},
            {"type": "card", "x": 720, "y": 730, "w": 1000, "h": 150, "emoji": "📉", "title": "LDL: slight, inconsistent", "at": [3, "LDL"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And maybe the biggest practical benefit of all: cinnamon adds a sense of sweetness to coffee, oatmeal or yogurt, "
                  "without a single gram of sugar.", {}),
            ("P", "Sweetness with zero sugar. Cinnamon, you clever bark.", {"mood": "happy", "jump": True}),
        ], "els": [
            E("☕", 320, 330, 180, at=[0, "coffee"]),
            E("🥣", 720, 330, 180, at=[0, "oatmeal"]),
            E("🍦", 1120, 330, 180, at=[0, "yogurt"]),
            {"type": "banner", "x": 720, "y": 620, "text": "Sweet taste, 0 g sugar", "color": "#B45309", "at": [0, "single"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch one: coumarin and the liver, with regular, high amounts of cassia.",
             {"say": "Catch one: coo-ma-rin and the liver, with regular, high amounts of cassia."}),
            ("H", "Catch two: blood thinners. Coumarin is related in structure to warfarin. "
                  "If you take anticoagulants, avoid large amounts of cassia, and talk to your doctor.",
             {"say": "Catch two: blood thinners. Coo-ma-rin is related in structure to warfarin. "
                     "If you take anticoagulants, avoid large amounts of cassia, and talk to your doctor."}),
            ("H", "Catch three: low blood sugar. With metformin or insulin, cinnamon may push blood sugar too low. Monitoring is needed.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 230, "w": 1100, "h": 180, "emoji": "🫀", "title": "#1 Coumarin and the liver",
             "body": "regular, high cassia intake", "at": 0},
            {"type": "card", "x": 760, "y": 460, "w": 1100, "h": 180, "emoji": "💊", "title": "#2 Anticoagulants",
             "body": "related to warfarin · ask a doctor", "at": 1},
            {"type": "card", "x": 760, "y": 690, "w": 1100, "h": 180, "emoji": "📉", "title": "#3 Low blood sugar",
             "body": "with metformin or insulin", "at": 2},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch four: irritation. Lots of ground cinnamon irritates the mouth and throat. "
                  "The cinnamon challenge, swallowing a spoonful of dry cinnamon, has caused choking and lung injury. It's dangerous.", {}),
            ("P", "Do not do the challenge. Pip says no.", {"mood": "worried"}),
            ("H", "Catch five: allergy. Cinnamon is a known mouth allergen. It can cause mouth ulcers and inflamed lips, "
                  "especially from cinnamon gum and toothpaste.", {}),
            ("H", "In pregnancy, cinnamon as seasoning is safe, but concentrated supplements and cinnamon oil aren't recommended. "
                  "And stop cinnamon supplements about two weeks before surgery, because of the effect on blood sugar and clotting.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 200, "w": 1100, "h": 160, "emoji": "🚫", "title": "#4 No cinnamon challenge",
             "body": "choking, lung injury", "at": [0, "challenge"], "fill": "#FEE2E2"},
            {"type": "card", "x": 760, "y": 390, "w": 1100, "h": 160, "emoji": "👄", "title": "#5 Mouth allergy",
             "body": "cinnamon gum, toothpaste", "at": [2, "allergy"]},
            {"type": "card", "x": 760, "y": 580, "w": 1100, "h": 160, "emoji": "🤰", "title": "Pregnancy: seasoning only",
             "body": "no supplements or oil", "at": [3, "pregnancy"]},
            {"type": "card", "x": 760, "y": 770, "w": 1100, "h": 150, "emoji": "🏥", "title": "Surgery: stop 2 weeks before", "at": [3, "surgery"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "kitchen", "title": "In the Kitchen", "emoji": "🍳", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "In coffee and hot chocolate, a pinch of cinnamon cuts the need for sugar.", {}),
            ("H", "In oatmeal and yogurt, it's the classic combo, and especially helpful for the blood sugar response.", {}),
            ("H", "And in savory dishes: in Moroccan, Persian and Middle Eastern cooking, cinnamon seasons meat, rice and tagine. "
                  "There, the spicier cassia is actually the better fit.",
             {"say": "And in savory dishes: in Moroccan, Persian and Middle Eastern cooking, cinnamon seasons meat, rice and ta-zheen. "
                     "There, the spicier cassia is actually the better fit."}),
            ("P", "Cassia gets a redemption arc. Love that for it.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 160, "emoji": "☕", "title": "Coffee, hot chocolate",
             "body": "a pinch, less sugar", "at": 0},
            {"type": "card", "x": 720, "y": 410, "w": 1000, "h": 160, "emoji": "🥣", "title": "Oatmeal, yogurt",
             "body": "the classic combo", "at": 1},
            {"type": "card", "x": 720, "y": 610, "w": 1000, "h": 160, "emoji": "🍲", "title": "Meat, rice, tagine",
             "body": "here cassia fits best", "at": [2, "savory"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Sticks keep their aroma much longer. Ground cinnamon loses its volatile oils within months.", {}),
            ("H", "And store it in an airtight container, away from light and heat.", {}),
        ], "els": [
            {"type": "card", "x": 420, "y": 330, "w": 560, "h": 200, "emoji": "🪵", "title": "Sticks", "body": "aroma lasts",
             "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 1040, "y": 330, "w": 560, "h": 200, "emoji": "🥄", "title": "Ground", "body": "fades in months",
             "at": [0, "Ground"], "fill": "#FEF3C7"},
            {"type": "card", "x": 720, "y": 630, "w": 1000, "h": 170, "emoji": "🫙", "title": "Airtight, dark, cool", "at": [1, "airtight"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 9
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: cinnamon is dense in polyphenols and almost completely sugar-free.", {}),
            ("H", "Two: it can lower fasting glucose, but its effect on long-term control is inconsistent, and it's no substitute for treatment.", {}),
            ("H", "Three: most cinnamon on the market is cassia. A teaspoon or more a day can go over the safe coumarin limit.",
             {"say": "Three: most cinnamon on the market is cassia. A teaspoon or more a day can go over the safe coo-ma-rin limit."}),
            ("H", "Four: for occasional seasoning, no problem. If you eat a lot every day, switch to Ceylon.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Polyphenols, almost no sugar", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Glucose help, not a treatment", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Most cinnamon is cassia", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Lots every day? Go Ceylon", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So cinnamon: sweet smell, no sugar, and a secret twin you should know about.", {"mood": "smug"}),
            ("H", "Well put, Pip.", {}),
            ("P", "Check your label, spice fans!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Look for the word Ceylon!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/cinnamon", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
