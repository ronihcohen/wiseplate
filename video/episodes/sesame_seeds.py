"""Sesame seeds explainer (English), based on https://wiseplate.blog/food/sesame-seeds/

Numbers are the article's, per 100 g: whole (unhulled) sesame seeds vs hulled
sesame seeds, plus raw tahini (~590 kcal / 100 g, ~90 kcal per tablespoon).
Keep them in sync with content/food/sesame-seeds.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Sesame Seeds: The Calcium Myth?"
SLUG = "sesame-seeds"
ARTICLE = "https://wiseplate.blog/food/sesame-seeds/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "SESAME", "top_size": 190, "bottom": "CALCIUM MYTH?", "bottom_size": 150,
         "badge": "7-15×", "badge_size": 110, "badge_label": "less calcium\nwhen hulled", "badge_color": "#DC2626",
         "scatter": "🥯", "hero": "🫙", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "ancient":  {"bpm": 96, "root": 65, "prog": ["vi", "IV", "I", "V"], "density": 0.55, "swing": 0.15},
    "calcium":  {"bpm": 104, "root": 67, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.1},
    "sesamin":  {"bpm": 116, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.8, "bright": 1.3},
    "heart":    {"bpm": 92, "root": 69, "prog": ["I", "iii", "IV", "V"], "density": 0.55},
    "minerals": {"bpm": 108, "root": 63, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF7ED", "ancient": "#FEF3C7", "calcium": "#F1F5F9", "sesamin": "#ECFDF5",
    "heart": "#FFE4E6", "minerals": "#E0F2FE", "catches": "#FEE2E2", "howto": "#ECFCCB",
    "outro": "#FFF7ED",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hey, it's me, Pip the pumpkin seed! And today... wait. Another seed? On my show?",
             {"mood": "surprised", "wave": True}),
            ("P", "Fine. I'll be a good sport. Today's guest: sesame!", {"mood": "smug", "jump": True}),
        ], "els": [
            E("🌱", 960, 200, 150, at=[1, "sesame"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Thank you, Pip. Sesame is tiny, but it's famous for one big number: calcium. "
                  "Today we'll check that number, look at the science, and cover the catches.", {}),
            ("P", "Tiny? Sesame makes me look huge. I love this episode already.", {"mood": "smug"}),
        ], "els": [
            E("🌱", 420, 330, 200, at=[0, "Sesame"], wobble=True),
            T("Sesame Seeds", 640, 300, 120, at=[0, "Sesame"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🦴", "title": "The calcium number", "at": [0, "calcium"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "📚", "title": "What science says", "at": [0, "science"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "⚠️", "title": "The catches", "at": [0, "catches"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "ancient", "title": "An Ancient Oil Seed", "emoji": "🏺", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Sesame, or Sesamum indicum, is one of the first plants ever grown for oil, more than three thousand years ago.",
             {"say": "Sesame, or Sesamum indicum, is one of the first plants ever grown for oil, more than three thousand years ago."}),
            ("H", "In Israeli cooking it's a true star, thanks to tahini.", {}),
            ("P", "Three thousand years? Okay, respect your elders. Even if they're tiny.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 760, "h": 150, "emoji": "🌱", "title": "Sesamum indicum",
             "body": "the plant's scientific name", "at": [0, "indicum"], "italic_title": True},
            {"type": "card", "x": 720, "y": 440, "w": 760, "h": 150, "emoji": "🏺", "title": "3,000+ years",
             "body": "one of the first oil crops", "at": [0, "three"]},
            {"type": "card", "x": 720, "y": 650, "w": 760, "h": 150, "emoji": "🫙", "title": "Tahini", "body": "a star of Israeli cooking", "at": [1, "tahini"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Here's the basic profile. One hundred grams of whole sesame seeds gives about five hundred seventy-three calories, "
                  "fifty grams of fat, seventeen point seven grams of protein, and eleven point eight grams of fiber.", {}),
            ("H", "Nutritious, for sure. But two of its numbers tend to be presented in a misleading way. Let's start with the famous one.", {}),
        ], "els": [
            T("Whole sesame, per 100 g", 720, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 270, "y": 400, "w": 330, "h": 280, "value": 573, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "seventy"]},
            {"type": "stat", "x": 620, "y": 400, "w": 330, "h": 280, "value": 50, "unit": " g", "label": "fat", "emoji": "🫒", "at": [0, "fat"]},
            {"type": "stat", "x": 970, "y": 400, "w": 330, "h": 280, "value": 17.7, "decimals": 1, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "protein"]},
            {"type": "stat", "x": 1320, "y": 400, "w": 330, "h": 280, "value": 11.8, "decimals": 1, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [0, "fiber"]},
            {"type": "banner", "x": 760, "y": 720, "text": "2 numbers get misread", "color": "#F97316", "at": [1, "misleading"]},
        ], "pip_hide": True},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "calcium", "title": "The Calcium Gap", "emoji": "🦴", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Sesame is marketed as a great plant source of calcium, with an impressive number: "
                  "nine hundred seventy-five milligrams per hundred grams. That's almost eight times more than milk.", {}),
            ("P", "Eight times milk?! I'm suddenly feeling very... un-calcified.", {"mood": "worried"}),
            ("H", "Don't worry, Pip. The number is correct, but it only applies to whole sesame, with the hull. And that creates two problems.", {}),
        ], "els": [
            T("The famous calcium number", 760, 150, 60, at=0, font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 470, "y": 440, "w": 560, "h": 340, "value": 975, "unit": " mg", "label": "calcium per 100 g", "emoji": "🦴", "at": [0, "nine"]},
            {"type": "banner", "x": 1080, "y": 330, "text": "≈ 8× milk", "color": "#0EA5E9", "at": [0, "eight"]},
            {"type": "pill", "x": 760, "y": 760, "text": "only for whole sesame, with the hull", "color": "orange", "at": [2, "hull"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Problem one: most of the sesame people eat is hulled. Regular raw tahini, and the white seeds you sprinkle on top, "
                  "are made from seeds with the hull removed.", {}),
            ("H", "The calcium sits almost entirely in the hull. Hulled seeds keep only about sixty to one hundred thirty milligrams per hundred grams.", {}),
            ("H", "That's a gap of seven to fifteen times.", {}),
        ], "els": [
            T("Calcium per 100 g", 760, 180, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "versus", "x": 120, "y": 400, "w": 1440, "row_h": 140, "names": ["Whole (with hull)", "Hulled"],
             "at": [1, "calcium"], "rows": [
                {"label": "Calcium", "a": 975, "b": 130, "unit": " mg", "b_text": "60 to 130 mg", "at": [1, "sixty"]},
            ]},
            {"type": "banner", "x": 760, "y": 650, "text": "7 to 15 times less", "color": "#DC2626", "at": [2, "seven"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Problem two: even in whole seeds, absorption is limited. The hull is rich in oxalates and phytic acid, "
                  "which bind calcium and block its absorption.", {}),
            ("H", "So the calcium you actually absorb is much lower than from milk, at about thirty-two percent, or kale, at about fifty.", {}),
            ("P", "So the big number is real... it just doesn't all show up. Like my gym membership.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 240, "w": 960, "h": 170, "emoji": "🔒", "title": "Oxalates + phytic acid",
             "body": "bind calcium, block absorption", "at": 0},
            {"type": "card", "x": 470, "y": 520, "w": 460, "h": 150, "emoji": "🥛", "title": "Milk ~32%", "body": "absorbed", "at": [1, "milk,"]},
            {"type": "card", "x": 980, "y": 520, "w": 460, "h": 150, "emoji": "🥬", "title": "Kale ~50%", "body": "absorbed", "at": [1, "kale,"]},
            {"type": "pill", "x": 720, "y": 720, "text": "sesame: much lower", "color": "orange", "at": [1, "lower"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The practical takeaway: whole sesame is a good calcium add-on, but not a replacement for main calcium sources.", {}),
            ("H", "For plant calcium your body can really use, look to tofu set with calcium sulfate, or kale. "
                  "And whole sesame tahini beats regular tahini for this, by a lot.", {}),
        ], "els": [
            {"type": "banner", "x": 720, "y": 190, "text": "A good add-on, not a main source", "color": "#475569", "at": 0},
            {"type": "card", "x": 430, "y": 430, "w": 560, "h": 160, "emoji": "🧊", "title": "Tofu", "body": "set with calcium sulfate", "at": [1, "tofu"]},
            {"type": "card", "x": 1030, "y": 430, "w": 460, "h": 160, "emoji": "🥬", "title": "Kale", "at": [1, "kale."]},
            {"type": "card", "x": 720, "y": 660, "w": 960, "h": 160, "emoji": "🫙", "title": "Whole tahini > regular",
             "body": "for calcium", "at": [1, "beats"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "sesamin", "title": "Sesamin: The Secret Weapon", "emoji": "🧪", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now for the most interesting thing in sesame: two lignans called sesamin and sesamolin. "
                  "They're almost unique to sesame.",
             {"say": "Now for the most interesting thing in sesame: two lignans called sesamin, and sesamolin. "
                     "They're almost unique to sesame."}),
            ("H", "They act as antioxidants, and studies link them to effects on blood fats and blood pressure.", {}),
            ("P", "Sesamin and sesamolin. Sounds like a magic act. Ta-da!", {"mood": "happy", "jump": True}),
        ], "els": [
            T("Sesamin", 460, 250, 100, at=0, font="fredoka", weight=700, color="#7C3AED"),
            T("+", 760, 250, 90, at=0, font="fredoka", weight=700, color="orange"),
            T("Sesamolin", 1080, 250, 100, at=0, font="fredoka", weight=700, color="#7C3AED"),
            {"type": "pill", "x": 760, "y": 390, "text": "almost unique to sesame", "color": "green", "at": [0, "unique"]},
            {"type": "card", "x": 460, "y": 600, "w": 560, "h": 150, "emoji": "🛡️", "title": "Antioxidants", "at": [1, "antioxidants"]},
            {"type": "card", "x": 1080, "y": 600, "w": 600, "h": 150, "emoji": "❤️", "title": "Blood fats, BP", "body": "linked in studies", "at": [1, "fats"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Sesamin also protects the vitamin E in the oil and slows down its oxidation. "
                  "That helps explain why sesame oil is relatively stable.", {}),
            ("H", "And sesame is rich in gamma-tocopherol, a form of vitamin E that's studied separately "
                  "from the alpha-tocopherol that's common in supplements.",
             {"say": "And sesame is rich in gamma toco-ferol, a form of vitamin E that's studied separately "
                     "from the alpha toco-ferol that's common in supplements."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 270, "w": 1000, "h": 180, "emoji": "🫗", "title": "Protects vitamin E in the oil",
             "body": "slows oxidation · a stable oil", "at": [0, "protects"]},
            {"type": "card", "x": 720, "y": 540, "w": 1000, "h": 180, "emoji": "🌻", "title": "Rich in gamma-tocopherol",
             "body": "a form of vitamin E, studied separately", "at": [1, "gamma"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "heart", "title": "Heart Numbers", "emoji": "❤️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "So what about the heart? Meta-analyses of controlled trials found that eating sesame or sesame oil "
                  "lowers total cholesterol, LDL, and triglycerides.",
             {"say": "So what about the heart? Meta-analyses of controlled trials found that eating sesame or sesame oil "
                     "lowers total cholesterol, L D L, and triglycerides."}),
            ("H", "The effect is modest, but consistent. And most of the fat in sesame is polyunsaturated and monounsaturated.", {}),
        ], "els": [
            T("Sesame and blood fats", 810, 100, 60, at=0, font="fredoka", weight=700, color="green"),
            {"type": "check", "x": 160, "y": 210, "w": 1300, "ok": True, "text": "Total cholesterol: lower", "at": [0, "total"]},
            {"type": "check", "x": 160, "y": 340, "w": 1300, "ok": True, "text": "LDL: lower", "at": [0, "L"]},
            {"type": "check", "x": 160, "y": 470, "w": 1300, "ok": True, "text": "Triglycerides: lower", "at": [0, "triglycerides"]},
            {"type": "banner", "x": 810, "y": 640, "text": "Modest, but consistent", "color": "#0EA5E9", "at": [1, "modest"]},
            {"type": "pill", "x": 810, "y": 780, "text": "mostly unsaturated fats", "color": "ok", "at": [1, "polyunsaturated"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Blood pressure is a weaker story. Several small trials showed lower blood pressure with sesame oil, "
                  "mostly in people with high blood pressure.", {}),
            ("H", "But those trials had few participants, so the evidence is limited.", {}),
            ("P", "Promising, but small. Like... a seed. I get it.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 280, "w": 960, "h": 180, "emoji": "🩺", "title": "Lower blood pressure",
             "body": "with sesame oil · mostly in hypertension", "at": 0},
            {"type": "pill", "x": 720, "y": 500, "text": "small trials · limited evidence", "color": "orange", "at": [1, "few"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "minerals", "title": "Minerals and Protein", "emoji": "💎", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Sesame is also loaded with minerals. One hundred grams gives more than one hundred percent of the daily value of copper.", {}),
            ("H", "Plus three hundred fifty-one milligrams of magnesium, and fourteen point six milligrams of iron. "
                  "It's also a source of zinc, manganese and phosphorus.", {}),
            ("H", "Just remember, this is non-heme iron, the plant kind. It's absorbed better with vitamin C.", {}),
        ], "els": [
            T("Per 100 g whole sesame", 760, 150, 52, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 330, "y": 390, "w": 420, "h": 290, "value": 100, "unit": "%+", "label": "copper, daily value", "emoji": "🟠", "at": [0, "hundred"]},
            {"type": "stat", "x": 790, "y": 390, "w": 420, "h": 290, "value": 351, "unit": " mg", "label": "magnesium", "emoji": "⚡", "at": [1, "magnesium"]},
            {"type": "stat", "x": 1250, "y": 390, "w": 420, "h": 290, "value": 14.6, "decimals": 1, "unit": " mg", "label": "iron", "emoji": "🩸", "at": [1, "iron."]},
            {"type": "pill", "x": 790, "y": 610, "text": "+ zinc, manganese, phosphorus", "color": "green", "at": [1, "zinc"]},
            {"type": "pill", "x": 790, "y": 710, "text": "plant iron: pair with vitamin C", "color": "orange", "at": [2, "vitamin"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Sesame's protein has one weak spot: its limiting amino acid is lysine. "
                  "Legumes like chickpeas are rich in lysine, but low in methionine.",
             {"say": "Sesame's protein has one weak spot: its limiting amino acid is lysine. "
                     "Legumes like chickpeas are rich in lysine, but low in meth-eye-oh-neen."}),
            ("H", "Put them together, and they complete each other. That's exactly the nutrition logic behind hummus with tahini.", {}),
            ("P", "Hummus and tahini, a love story. I'd sprinkle myself on that.", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "card", "x": 420, "y": 300, "w": 540, "h": 170, "emoji": "🌱", "title": "Sesame", "body": "low in lysine", "at": 0},
            {"type": "card", "x": 1040, "y": 300, "w": 540, "h": 170, "emoji": "🫘", "title": "Chickpeas", "body": "rich in lysine", "at": [0, "chickpeas"]},
            T("+", 730, 300, 90, at=[0, "chickpeas"], font="fredoka", weight=700, color="orange"),
            {"type": "banner", "x": 730, "y": 560, "text": "Hummus + tahini = a complete team", "color": "#16A34A", "at": [1, "hummus"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Here's how whole and hulled sesame compare, per hundred grams. Calories and protein are similar. "
                  "But fiber drops from eleven point eight grams to three point nine, iron from fourteen point six to seven point eight, "
                  "and copper from four point one to one point five milligrams.", {}),
        ], "els": [
            T("Per 100 g", 760, 140, 52, at=0, font="fredoka", weight=600, color="green"),
            {"type": "versus", "x": 120, "y": 300, "w": 1440, "row_h": 112, "names": ["Whole", "Hulled"], "at": 0, "rows": [
                {"label": "Calories", "a": 573, "b": 588, "at": [0, "Calories"]},
                {"label": "Protein", "a": 17.7, "b": 17, "unit": " g", "decimals": 1, "at": [0, "protein"]},
                {"label": "Fiber", "a": 11.8, "b": 3.9, "unit": " g", "decimals": 1, "at": [0, "fiber"]},
                {"label": "Iron", "a": 14.6, "b": 7.8, "unit": " mg", "decimals": 1, "at": [0, "iron"]},
                {"label": "Copper", "a": 4.1, "b": 1.5, "unit": " mg", "decimals": 1, "at": [0, "copper"]},
            ]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Now the catches. The biggest one is allergy. Sesame allergy keeps rising, and it's now officially a major allergen "
                  "that has to be labeled.", {}),
            ("H", "In the U.S. it was added to the major allergen list by the FASTER Act. In the European Union, it has been labeled for years. "
                  "Reactions can be severe, even anaphylactic.",
             {"say": "In the U S, it was added to the major allergen list by the Faster Act. In the European Union, it has been labeled for years. "
                     "Reactions can be severe, even ana-fil-actic."}),
            ("H", "And in Israel, where people eat a lot of tahini from a young age, it's a relatively common allergy.", {}),
        ], "els": [
            T("#1 Allergy", 760, 150, 80, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 420, "y": 360, "w": 600, "h": 160, "emoji": "🇺🇸", "title": "US: FASTER Act", "body": "a major allergen", "at": [1, "FASTER"]},
            {"type": "card", "x": 1080, "y": 360, "w": 620, "h": 160, "emoji": "🇪🇺", "title": "EU: labeled", "body": "for years", "at": [1, "European"]},
            {"type": "banner", "x": 760, "y": 570, "text": "Can be severe", "color": "#DC2626", "at": [1, "severe"]},
            {"type": "pill", "x": 760, "y": 720, "text": "relatively common in Israel", "color": "orange", "at": [2, "Israel"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Number two: calories. Whole sesame has five hundred seventy-three calories per hundred grams, and raw tahini about five hundred ninety.", {}),
            ("H", "It's very easy to overdo. One tablespoon of tahini is about ninety calories, "
                  "and a plate of hummus with tahini can reach four hundred calories or more.", {}),
            ("P", "Ninety calories a spoon? Tahini, you sneaky little dip.", {"mood": "surprised"}),
        ], "els": [
            T("#2 Calories", 760, 150, 76, at=0, font="fredoka", weight=700, color="red"),
            {"type": "stat", "x": 330, "y": 430, "w": 420, "h": 300, "value": 590, "unit": "", "label": "tahini, per 100 g", "emoji": "🫙", "at": [0, "ninety."]},
            {"type": "stat", "x": 790, "y": 430, "w": 420, "h": 300, "value": 90, "unit": "", "label": "per tablespoon", "emoji": "🥄", "at": [1, "tablespoon"]},
            {"type": "stat", "x": 1250, "y": 430, "w": 420, "h": 300, "value": 400, "unit": "+", "label": "hummus plate", "emoji": "🍽️", "at": [1, "plate"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Number three: oxalates. The hull has a lot of them. That matters if you're prone to calcium oxalate kidney stones, "
                  "especially with lots of whole tahini.", {}),
            ("H", "Number four: phytic acid, which lowers mineral absorption. Light toasting and soaking reduce it, partly.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "🪨", "title": "#3 Oxalates",
             "body": "matters if you're prone to kidney stones", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🔒", "title": "#4 Phytic acid",
             "body": "less absorption · toasting and soaking help a bit", "at": 1},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Number five: oxidation. With so much fat, ground sesame and tahini can go rancid, even with sesamin's partial protection. "
                  "Keep tahini in the fridge after opening.", {}),
            ("H", "And number six: salmonella. There have been outbreaks traced to industrial tahini, from seeds contaminated before processing. "
                  "Buying a known brand with quality control lowers the risk.", {}),
            ("P", "Fridge, known brand. Noted. Respect the seed, people.", {"mood": "smug", "jump": True}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "❄️", "title": "#5 Oxidation",
             "body": "fridge after opening", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🦠", "title": "#6 Salmonella",
             "body": "past outbreaks · pick a known brand", "at": 1},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "How to Eat It", "emoji": "🥙", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So how do you get the most out of sesame? If calcium and fiber matter to you, choose whole sesame tahini. It wins by a huge margin.", {}),
            ("H", "It's darker, more bitter and coarser, and many people prefer the milder hulled kind. "
                  "But this one choice matters more than anything else.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 180, "emoji": "🫙", "title": "Choose whole tahini",
             "body": "for calcium and fiber", "at": 0, "fill": "#DCFCE7"},
            {"type": "pill", "x": 720, "y": 490, "text": "darker · more bitter · coarser", "color": "orange", "at": [1, "darker"]},
            {"type": "banner", "x": 720, "y": 650, "text": "The choice that matters most", "color": "#16A34A", "at": [1, "choice"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Light toasting improves the flavor a lot, and cuts a little phytic acid. Two to three minutes in a dry pan, on medium heat, is enough. "
                  "Toasting too hard damages the fat and the flavor.", {}),
            ("H", "Tahini also beats whole seeds. A whole sesame seed can pass through your gut without being fully broken down, "
                  "a bit like flax seeds, though less so. Ground seeds are absorbed better.", {}),
            ("P", "Some seeds just refuse to be digested. I respect that.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 250, "w": 1000, "h": 180, "emoji": "🍳", "title": "Toast: 2 to 3 min, dry pan",
             "body": "medium heat · not too hard", "at": 0},
            {"type": "card", "x": 720, "y": 510, "w": 1000, "h": 180, "emoji": "🫙", "title": "Tahini beats whole seeds",
             "body": "whole seeds can pass through undigested", "at": [1, "Tahini"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Add lemon to your tahini. It's not just about flavor: the vitamin C helps you absorb the iron.", {}),
            ("H", "And storage: raw tahini goes in the fridge after opening. Seeds go in an airtight jar in a cool place, "
                  "ideally refrigerated for the long term.", {}),
        ], "els": [
            E("🍋", 360, 330, 170, at=[0, "lemon"]),
            T("+", 540, 330, 100, at=[0, "lemon"], font="fredoka", weight=700, color="orange"),
            E("🫙", 720, 330, 170, at=[0, "tahini."]),
            T("vitamin C helps absorb iron", 540, 480, 46, at=[0, "vitamin"], font="fredoka", weight=600, color="green"),
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 170, "emoji": "❄️", "title": "Tahini: fridge after opening",
             "body": "seeds: airtight, cool, ideally fridge", "at": [1, "storage"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: sesame gives unsaturated fats, protein, fiber, and an unusual range of minerals.", {}),
            ("H", "Two: its lignans, like sesamin, have a measurable effect on blood fats.", {}),
            ("H", "Three: the calcium claim is only true for whole sesame. Hulled seeds, used for most tahini, keep just a fraction.", {}),
            ("H", "Four: the two main downsides are a growing allergy, and lots of calories.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Good fats, protein, fiber, minerals", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Sesamin: a measurable effect on blood fats", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Calcium: only whole sesame", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Watch for allergy and calories", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "Okay, sesame. You're tiny, you're ancient, and you're pretty great. Truce?", {"mood": "happy"}),
            ("H", "I think that's a yes. Seed friends forever.", {}),
            ("P", "Seed friends forever!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Go get the whole tahini!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article + sources: wiseplate.blog/food/sesame-seeds", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
