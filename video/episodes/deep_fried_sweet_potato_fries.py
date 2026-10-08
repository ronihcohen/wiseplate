"""Deep-fried sweet potato fries explainer (English), based on
https://wiseplate.blog/en/food/deep-fried-sweet-potato-fries/

Numbers are the article's: calories and fat per 100 g for five preparations
(ranges), beta-carotene per 100 g of orange sweet potato, a 150 to 200 g
restaurant serving, sodium per 100 g of commercial fries, temperatures in
degrees Celsius (Fahrenheit as in the English article). Keep them in sync with
content/food/deep-fried-sweet-potato-fries.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Sweet Potato Fries: Healthier Than Regular Fries?"
SLUG = "deep-fried-sweet-potato-fries"
ARTICLE = "https://wiseplate.blog/en/food/deep-fried-sweet-potato-fries/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "SWEET POTATO", "top_size": 130, "bottom": "FRIES: HEALTHY?", "bottom_size": 106,
         "badge": "x3", "badge_label": "calories\nwhen fried", "badge_color": "#DC2626",
         "scatter": "🍟", "hero": "🍠", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "halo":     {"bpm": 104, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.65, "swing": 0.15},
    "calories": {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "survives": {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "acryl":    {"bpm": 92, "root": 63, "prog": ["vi", "IV", "I", "V"], "density": 0.55},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFEDD5", "halo": "#FEF9C3", "calories": "#FEE2E2", "survives": "#ECFDF5",
    "acryl": "#F1F5F9", "catches": "#FEF3C7", "howto": "#ECFCCB", "outro": "#FFEDD5",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hey there! Pip the pumpkin seed here. Today's guest is orange, crispy, and very sure of itself.", {"mood": "happy", "wave": True}),
            ("P", "It claims to be the healthy kind of fries. Sweet potato fries! Let's check that halo.", {"mood": "smug", "jump": True}),
        ], "els": [
            E("🍠", 960, 200, 160, at=[1, "Sweet"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today it's deep-fried sweet potato fries. We'll compare the calories with regular fries, "
                  "see what actually survives the fryer, look at a compound called acrylamide, and make a better version at home.",
             {"say": "Today it's deep fried sweet potato fries. We'll compare the calories with regular fries, "
                     "see what actually survives the fryer, look at a compound called a-krill-a-mide, and make a better version at home."}),
            ("P", "A fry-off. I'm here for it.", {"mood": "happy"}),
        ], "els": [
            E("🍟", 420, 330, 200, at=[0, "sweet"], wobble=True),
            T("Sweet potato fries", 560, 300, 104, at=[0, "sweet"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🔥", "title": "The calories", "at": [0, "calories"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🔬", "title": "Acrylamide", "at": [0, "acrylamide"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "🏠", "title": "A better version", "at": [0, "better"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "halo", "title": "The Healthy Halo", "emoji": "😇", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Sweet potato fries are usually sold as the healthy alternative to regular fries. That's only partly true.", {}),
            ("H", "The sweet potato itself is indeed better than the potato. But deep frying flattens most of the difference.", {}),
            ("P", "Flattened. By oil. That's rough.", {"mood": "worried"}),
        ], "els": [
            T("The \"healthy\" fries?", 720, 170, 76, at=0, font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 720, "y": 400, "w": 1000, "h": 180, "emoji": "🍠", "title": "Sweet potato > potato",
             "body": "as a raw ingredient", "at": [1, "better"], "fill": "#DCFCE7"},
            {"type": "banner", "x": 720, "y": 640, "text": "Deep frying flattens the gap", "color": "#DC2626", "at": [1, "flattens"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "On calories, deep-fried sweet potato fries are very close to regular fries, and sometimes even higher.", {}),
            ("H", "That's because sweet potato soaks up more oil, thanks to its sugar content and softer texture.", {}),
            ("P", "So the sweet one is also the thirsty one. Noted.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 250, "w": 1000, "h": 180, "emoji": "⚖️", "title": "Calories: about the same",
             "body": "sometimes even higher", "at": 0},
            {"type": "card", "x": 720, "y": 500, "w": 1000, "h": 180, "emoji": "🛢️", "title": "Soaks up more oil",
             "body": "more sugar, softer texture", "at": [1, "oil"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "calories", "title": "The Calorie Showdown", "emoji": "🔥", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Here's the comparison that explains everything, in calories per hundred grams.", {}),
            ("H", "Sweet potato baked in its skin: ninety calories. Oven sweet potato fries with a teaspoon of oil: one hundred fifty to one hundred seventy.", {}),
            ("H", "Deep-fried sweet potato fries: two hundred eighty to three hundred thirty. Deep-fried potato fries: two hundred ninety to three hundred twenty.", {}),
            ("H", "And frozen commercial sweet potato fries, fried: three hundred ten to three hundred fifty.", {}),
        ], "els": [
            T("Calories per 100 g", 760, 150, 60, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 300, "y": 280, "w": 1100, "row_h": 110, "max": 350, "unit": "", "rows": [
                {"label": "Baked", "value": 90, "text": "90", "color": "#16A34A", "at": [1, "baked"]},
                {"label": "Oven fries", "value": 170, "text": "150-170", "color": "#65A30D", "at": [1, "Oven"]},
                {"label": "Deep-fried", "value": 330, "text": "280-330", "color": "#F97316", "at": [2, "Deep"], "star": False},
                {"label": "Potato fries", "value": 320, "text": "290-320", "color": "#F59E0B", "at": [2, "potato fries"]},
                {"label": "Frozen, fried", "value": 350, "text": "310-350", "color": "#DC2626", "at": [3, "frozen"]},
            ]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "And fat, per hundred grams: zero point two grams baked, five to six in the oven fries, "
                  "and fifteen to eighteen grams deep-fried. Potato fries: fifteen to seventeen. Frozen: seventeen to twenty.", {}),
        ], "els": [
            T("Fat per 100 g", 760, 150, 60, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 300, "y": 280, "w": 1100, "row_h": 110, "max": 20, "unit": " g", "rows": [
                {"label": "Baked", "value": 0.2, "text": "0.2 g", "color": "#16A34A", "at": [0, "zero"]},
                {"label": "Oven fries", "value": 6, "text": "5-6 g", "color": "#65A30D", "at": [0, "oven"]},
                {"label": "Deep-fried", "value": 18, "text": "15-18 g", "color": "#F97316", "at": [0, "deep"]},
                {"label": "Potato fries", "value": 17, "text": "15-17 g", "color": "#F59E0B", "at": [0, "Potato"]},
                {"label": "Frozen, fried", "value": 20, "text": "17-20 g", "color": "#DC2626", "at": [0, "Frozen"]},
            ]},
        ]},
        {"pip": PIP_C, "lines": [
            ("H", "The bottom line in one sentence: frying triples the calories of the sweet potato, and the gap with fried potato shrinks almost to zero.", {}),
            ("H", "If you pick sweet potato fries for health reasons, you mostly get a different taste.", {}),
            ("P", "Triple?! From ninety to three hundred? That's not a glow-up, that's a pool party in a fryer.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("x3 calories", 960, 170, 120, at=[0, "triples"], font="fredoka", weight=700, color="red"),
            T("gap with potato fries: almost zero", 960, 290, 50, at=[0, "gap"], font="fredoka", weight=600, color="muted"),
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "survives", "title": "What Survives the Fryer", "emoji": "🥕", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So what does remain of the sweet potato? First, beta-carotene. And this time, frying actually helps.", {}),
            ("H", "Orange sweet potato is very rich in it: about eight thousand five hundred micrograms per hundred grams. And beta-carotene is fat-soluble.", {}),
            ("H", "Fat significantly improves its absorption, as bioavailability studies have shown consistently. "
                  "Some carotenoids are destroyed by high heat, but more of what remains gets absorbed.",
             {"say": "Fat significantly improves its absorption, as bio-availability studies have shown consistently. "
                     "Some carotenoids are destroyed by high heat, but more of what remains gets absorbed."}),
            ("P", "A plot twist! The oil is finally useful for something.", {"mood": "surprised"}),
        ], "els": [
            {"type": "stat", "x": 470, "y": 330, "w": 560, "h": 320, "value": 8500, "unit": " mcg", "label": "beta-carotene per 100 g", "emoji": "🥕", "at": [1, "eight"], "color": "orange"},
            {"type": "card", "x": 1080, "y": 250, "w": 520, "h": 150, "emoji": "🫒", "title": "Fat-soluble", "at": [1, "soluble"], "fill": "#DCFCE7"},
            {"type": "card", "x": 1080, "y": 430, "w": 520, "h": 150, "emoji": "📈", "title": "Better absorbed", "at": [2, "absorption"], "fill": "#DCFCE7"},
            {"type": "pill", "x": 720, "y": 650, "text": "some is lost to high heat", "color": "orange", "at": [2, "destroyed"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "That's the only real advantage of the fried version.", {}),
            ("H", "Potassium and fiber are mostly kept. But vitamin C is almost completely destroyed at frying temperatures.", {}),
        ], "els": [
            T("After the fryer", 720, 170, 72, at=0, font="fredoka", weight=700, color="green"),
            {"type": "check", "x": 160, "y": 330, "w": 1160, "ok": True, "text": "Beta-carotene: better absorbed", "at": 0},
            {"type": "check", "x": 160, "y": 470, "w": 1160, "ok": True, "text": "Potassium and fiber: mostly kept", "at": [1, "Potassium"]},
            {"type": "check", "x": 160, "y": 610, "w": 1160, "ok": False, "text": "Vitamin C: almost all gone", "at": [1, "vitamin"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "acryl", "title": "Golden, Not Brown", "emoji": "🔬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the downsides. Let's start with acrylamide. It forms in starchy foods above one hundred twenty degrees Celsius, "
                  "or two hundred forty-eight Fahrenheit, from a reaction between asparagine and reducing sugars.",
             {"say": "Now the downsides. Let's start with a-krill-a-mide. It forms in starchy foods above one hundred twenty degrees Celsius, "
                     "or two hundred forty-eight Fahrenheit, from a reaction between a-spara-jean and reducing sugars."}),
            ("H", "And sweet potato has more sugar than potato. So it browns faster, and makes acrylamide faster at a given temperature.",
             {"say": "And sweet potato has more sugar than potato. So it browns faster, and makes a-krill-a-mide faster at a given temperature."}),
            ("P", "Wait. The sweetness that makes it tasty also makes it brown faster? Sneaky.", {"mood": "worried"}),
        ], "els": [
            T("Acrylamide", 720, 170, 80, at=0, font="fredoka", weight=700, color="red"),
            {"type": "pill", "x": 720, "y": 290, "text": "above 120°C (248°F)", "color": "orange", "at": [0, "twenty"]},
            {"type": "card", "x": 720, "y": 470, "w": 1000, "h": 180, "emoji": "⚗️", "title": "Asparagine + sugars",
             "body": "react in starchy foods", "at": [0, "asparagine"]},
            {"type": "card", "x": 720, "y": 690, "w": 1000, "h": 180, "emoji": "🍬", "title": "More sugar, faster",
             "body": "sweet potato browns sooner than potato", "at": [1, "sugar"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_C, "lines": [
            ("H", "Acrylamide is classified as probably carcinogenic to humans, group two A by the I A R C.",
             {"say": "A-krill-a-mide is classified as probably carcinogenic to humans, group two A, by the I A R C."}),
            ("H", "The practical rule: golden, not brown. Dark browning is exactly where the amount jumps.", {}),
            ("P", "Golden, not brown. I'm writing that on my shell.", {"mood": "happy", "jump": True}),
        ], "els": [
            T("IARC Group 2A: probably carcinogenic", 960, 160, 54, at=0, font="fredoka", weight=600, color="muted"),
            {"type": "check", "x": 140, "y": 330, "w": 520, "ok": True, "text": "Golden", "at": [1, "golden"]},
            {"type": "check", "x": 1260, "y": 330, "w": 520, "ok": False, "text": "Brown", "at": [1, "brown."]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "catches", "title": "More Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Next, calorie density. A restaurant serving weighs one hundred fifty to two hundred grams. "
                  "That's four hundred fifty to six hundred fifty calories, for the side dish alone.", {}),
            ("P", "For a side dish? That's a main character.", {"mood": "surprised"}),
        ], "els": [
            T("One restaurant serving", 760, 170, 66, at=0, font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 500, "y": 450, "w": 500, "h": 300, "value": 0, "text": "150-200 g", "vsize": 88, "label": "serving", "emoji": "🍟", "at": [0, "serving"]},
            {"type": "stat", "x": 1060, "y": 450, "w": 540, "h": 300, "value": 0, "text": "450-650", "vsize": 96, "label": "calories", "emoji": "🔥", "at": [0, "four"], "color": "red"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Then the oil. Oil used for frying again and again, as is common in restaurants and food stands, "
                  "builds up aldehydes and other oxidation products. That's the hardest downside to control outside the home.",
             {"say": "Then the oil. Oil used for frying again and again, as is common in restaurants and food stands, "
                     "builds up al-de-hides and other oxidation products. That's the hardest downside to control outside the home."}),
            ("H", "Trans fats are rare in commercial oils today, but small amounts still form during long frying at high heat.", {}),
            ("H", "And sodium: commercial fries are generously salted, sometimes four hundred to six hundred milligrams per hundred grams.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 220, "w": 1240, "ok": False, "text": "Reused oil: oxidation products", "at": [0, "again"]},
            {"type": "check", "x": 160, "y": 360, "w": 1240, "ok": False, "text": "Trans fats: small amounts", "at": [1, "Trans"]},
            {"type": "check", "x": 160, "y": 500, "w": 1240, "ok": False, "text": "Sodium: 400-600 mg per 100 g", "at": [2, "sodium"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Frozen ones have a hidden extra. Most frozen sweet potato fries are coated in starch or flour to make them crisp. "
                  "That's added processed carbohydrate that isn't in the product name.", {}),
            ("H", "And the glycemic index: fried sweet potato has a higher one than baked or boiled, because high heat changes the starch structure.", {}),
            ("P", "A secret coat? These fries are wearing a disguise.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1040, "h": 180, "emoji": "🧊", "title": "Frozen: starch coating",
             "body": "not in the product name", "at": [0, "coated"], "fill": "#FEF3C7"},
            {"type": "card", "x": 720, "y": 510, "w": 1040, "h": 180, "emoji": "📈", "title": "Higher glycemic index",
             "body": "than baked or boiled sweet potato", "at": [1, "glycemic"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "howto", "title": "Make Them Better", "emoji": "🍠", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So how do you make a much better version? Option one: the oven, at two hundred to two hundred twenty degrees Celsius, "
                  "that's three ninety to four thirty Fahrenheit, with a tablespoon of olive oil on a baking sheet.", {}),
            ("H", "That's one hundred fifty to one hundred seventy calories per hundred grams, instead of three hundred.", {}),
            ("H", "Option two: an air fryer. It gets similar crispness with one to two teaspoons of oil, "
                  "and studies have documented less acrylamide than with deep frying.",
             {"say": "Option two: an air fryer. It gets similar crispness with one to two teaspoons of oil, "
                     "and studies have documented less a-krill-a-mide than with deep frying."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1040, "h": 190, "emoji": "♨️", "title": "Oven, 200-220°C",
             "body": "390-430°F · 1 tablespoon olive oil", "at": [0, "oven"]},
            {"type": "pill", "x": 720, "y": 400, "text": "150-170 calories, not 300", "color": "green", "at": [1, "instead"]},
            {"type": "card", "x": 720, "y": 590, "w": 1040, "h": 190, "emoji": "🌀", "title": "Air fryer",
             "body": "1-2 teaspoons oil · less acrylamide", "at": [2, "air"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Three: soak them in water for thirty minutes first. That removes extra starch and sugars from the surface, "
                  "so less fast browning and less acrylamide.",
             {"say": "Three: soak them in water for thirty minutes first. That removes extra starch and sugars from the surface, "
                     "so less fast browning and less a-krill-a-mide."}),
            ("H", "Four: dry them well before adding oil. Water is the enemy of crispness.", {}),
            ("H", "Five: take them out when they're golden, not brown.", {}),
            ("H", "Six: leave the skin on. A good part of the fiber and polyphenols sits there.", {}),
            ("H", "And seven: season with smoked paprika, turmeric or cinnamon, instead of adding salt.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 170, "w": 1300, "ok": True, "text": "Soak 30 minutes in water", "at": [0, "soak"]},
            {"type": "check", "x": 160, "y": 290, "w": 1300, "ok": True, "text": "Dry them well", "at": [1, "dry"]},
            {"type": "check", "x": 160, "y": 410, "w": 1300, "ok": True, "text": "Out when golden", "at": [2, "golden"]},
            {"type": "check", "x": 160, "y": 530, "w": 1300, "ok": True, "text": "Keep the skin", "at": [3, "skin"]},
            {"type": "check", "x": 160, "y": 650, "w": 1300, "ok": True, "text": "Paprika, turmeric, cinnamon", "at": [4, "paprika"]},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "Soak, dry, bake, golden. Even I could do that, and I don't have hands.", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🍠", 560, 260, 150, at=0),
            {"type": "arrow", "x1": 680, "y1": 260, "x2": 1220, "y2": 260, "at": 0, "color": "orange"},
            E("🍟", 1360, 260, 150, at=0.4),
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: deep-fried sweet potato fries have two hundred eighty to three hundred thirty calories per hundred grams. "
                  "That's three times baked sweet potato, and practically the same as potato fries.", {}),
            ("H", "Two: the healthy image is mostly undeserved. Frying cancels most of the raw ingredient's advantage.", {}),
            ("H", "Three: what does remain is the beta-carotene, which is absorbed even better with fat.", {}),
            ("H", "Four: as an occasional side, it's no problem. For the real benefit, bake it with a tablespoon of oil. "
                  "Same taste, about half the calories.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": False, "text": "280-330 calories per 100 g", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": False, "text": "The healthy image: mostly undeserved", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Beta-carotene: still there", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Bake it: about half the calories", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So sweet potato fries: sweet, yes. A health food, not really. Bake them, and we can be friends.", {"mood": "smug"}),
            ("H", "Very generous of you, Pip.", {}),
            ("P", "Golden, not brown, forever!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Soak them first!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/deep-fried-sweet-potato-fries", 760, 350, 34, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
