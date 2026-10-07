"""Pecans explainer (English), based on https://wiseplate.blog/food/pecans/

Numbers are the article's, per 100 g of pecans (plus a 30 g handful, about 19
halves, about 200 kcal) and its per-100 g comparison with other nuts. Keep them
in sync with content/food/pecans.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Pecans: The Most Extreme Nut?"
SLUG = "pecans"
ARTICLE = "https://wiseplate.blog/food/pecans/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "PECANS", "top_size": 200, "bottom": "TOO EXTREME?", "bottom_size": 160,
         "badge": "4.3 g", "badge_size": 120, "badge_label": "net carbs\nper 100 g", "badge_color": "#16A34A",
         "scatter": "🌰", "hero": "🥧", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "extreme":  {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "showdown": {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "antiox":   {"bpm": 96, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.6, "swing": 0.1},
    "heart":    {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "versus":   {"bpm": 120, "root": 63, "prog": ["vi", "IV", "V", "I"], "density": 0.8, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF7ED", "extreme": "#FEF3C7", "showdown": "#ECFDF5", "antiox": "#F5F3FF",
    "heart": "#FFE4E6", "catches": "#FEE2E2", "howto": "#ECFCCB", "versus": "#E0F2FE",
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
            ("P", "Hi again! Pip here, pumpkin seed and part-time food critic.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest is big, brown, and a little bit fancy. Please welcome... the pecan!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🌰", 960, 200, 160, at=[1, "pecan"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The pecan is the most extreme nut on the shelf. Today: why it's extreme, "
                  "what it really does for you, and the one storage mistake almost everyone makes.", {}),
            ("P", "Extreme? I'm a tiny seed. I don't even do stairs.", {"mood": "worried"}),
            ("H", "Don't worry, Pip. Let's crack it open.", {}),
        ], "els": [
            E("🌰", 420, 330, 200, at=[0, "pecan"], wobble=True),
            T("Pecans", 640, 300, 130, at=[0, "pecan"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🔥", "title": "Why it's extreme", "at": [0, "extreme."]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "📚", "title": "What it does for you", "at": [0, "does"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "❄️", "title": "The storage mistake", "at": [0, "storage"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "extreme", "title": "The Extreme Nut", "emoji": "🌰", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "The pecan, Carya illinoinensis, is a tree nut from North America, and a relative of the walnut.",
             {"say": "The pecan, Carya illinoy-nensis, is a tree nut from North America, and a relative of the walnut."}),
            ("H", "It stands out among nuts for two extreme numbers: the highest fat of the common nuts, and at the same time, the lowest carbs.", {}),
            ("P", "Highest fat, lowest carbs. That's not a nut, that's a personality.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 760, "h": 150, "emoji": "🌳", "title": "Carya illinoinensis",
             "body": "from North America · a walnut relative", "at": [0, "Carya"], "italic_title": True},
            {"type": "banner", "x": 470, "y": 480, "text": "Most fat", "color": "#F97316", "at": [1, "highest"]},
            {"type": "banner", "x": 980, "y": 480, "text": "Fewest carbs", "color": "#16A34A", "at": [1, "lowest"]},
            T("among common nuts", 720, 600, 46, at=[1, "common"], color="muted"),
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Per one hundred grams, pecans give about six hundred ninety-one calories, seventy-two grams of fat, "
                  "nine point two grams of protein, and thirteen point nine grams of carbs.", {}),
            ("H", "But nine point six of those grams are fiber. So the net carbs are only about four point three grams.", {}),
            ("H", "That combo makes pecans the go-to nut for keto and low-carb diets.", {}),
        ], "els": [
            T("Per 100 g", 760, 140, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 300, "y": 360, "w": 360, "h": 270, "value": 691, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "ninety"]},
            {"type": "stat", "x": 680, "y": 360, "w": 360, "h": 270, "value": 72, "unit": " g", "label": "fat", "emoji": "🫒", "at": [0, "fat"]},
            {"type": "stat", "x": 1060, "y": 360, "w": 360, "h": 270, "value": 9.2, "decimals": 1, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "protein"]},
            {"type": "stat", "x": 300, "y": 680, "w": 360, "h": 270, "value": 13.9, "decimals": 1, "unit": " g", "label": "carbs", "emoji": "🍞", "at": [0, "carbs."]},
            {"type": "stat", "x": 680, "y": 680, "w": 360, "h": 270, "value": 9.6, "decimals": 1, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [1, "fiber"]},
            {"type": "stat", "x": 1060, "y": 680, "w": 360, "h": 270, "value": 4.3, "decimals": 1, "unit": " g", "label": "net carbs", "emoji": "✨", "at": [1, "net"], "color": "ok"},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "showdown", "title": "Nut Showdown", "emoji": "📊", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's line pecans up against other nuts, per hundred grams. Start with net carbs.", {}),
            ("H", "Pecans: four point three grams. Walnuts: seven. Almonds: nine point nine. Pistachios: seventeen. And cashews: twenty-seven.", {}),
            ("P", "Cashews, what happened? Did you eat a bagel?", {"mood": "surprised"}),
        ], "els": [
            T("Net carbs per 100 g", 760, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 290, "w": 1200, "row_h": 112, "max": 27, "unit": " g", "rows": [
                {"label": "Pecans", "value": 4.3, "decimals": 1, "color": "#16A34A", "at": [1, "Pecans"], "star": True},
                {"label": "Walnuts", "value": 7, "color": "#84CC16", "at": [1, "Walnuts"]},
                {"label": "Almonds", "value": 9.9, "decimals": 1, "color": "#F59E0B", "at": [1, "Almonds"]},
                {"label": "Pistachios", "value": 17, "color": "#F97316", "at": [1, "Pistachios"]},
                {"label": "Cashews", "value": 27, "color": "#EF4444", "at": [1, "cashews"]},
            ]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Now flip it around and look at calories. Pecans top this list too, at six hundred ninety-one. "
                  "Walnuts have six hundred fifty-four, almonds five hundred seventy-nine, pistachios five hundred sixty, and cashews five hundred fifty-three.", {}),
            ("H", "And for protein, pecans come last: nine point two grams, while almonds have twenty-one.", {}),
        ], "els": [
            T("Calories per 100 g", 760, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 290, "w": 1200, "row_h": 112, "max": 700, "unit": "", "rows": [
                {"label": "Pecans", "value": 691, "color": "#EF4444", "at": [0, "ninety"]},
                {"label": "Walnuts", "value": 654, "color": "#F97316", "at": [0, "Walnuts"]},
                {"label": "Almonds", "value": 579, "color": "#F59E0B", "at": [0, "almonds"]},
                {"label": "Pistachios", "value": 560, "color": "#84CC16", "at": [0, "pistachios"]},
                {"label": "Cashews", "value": 553, "color": "#16A34A", "at": [0, "cashews"]},
            ]},
            {"type": "pill", "x": 760, "y": 870, "text": "protein: pecans 9.2 g, almonds 21 g", "color": "orange", "at": [1, "protein"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "antiox", "title": "Antioxidants, Honestly", "emoji": "🛡️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Pecans are considered one of the richest nuts in antioxidants. The headliners are proanthocyanidins, "
                  "the same family of compounds found in grapes and wine, plus ellagic acid, and gamma-tocopherol.",
             {"say": "Pecans are considered one of the richest nuts in antioxidants. The headliners are pro-antho-cyanidins, "
                     "the same family of compounds found in grapes and wine, plus ellagic acid, and gamma toco-ferol."}),
            ("P", "Pro-antho-what? Can we call them the P team?", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 250, "w": 1000, "h": 160, "emoji": "🍇", "title": "Proanthocyanidins",
             "body": "same family as in grapes and wine", "at": [0, "proanthocyanidins"]},
            {"type": "card", "x": 470, "y": 470, "w": 500, "h": 140, "emoji": "🧪", "title": "Ellagic acid", "at": [0, "ellagic"]},
            {"type": "card", "x": 1000, "y": 470, "w": 520, "h": 140, "emoji": "🌻", "title": "Gamma-tocopherol", "at": [0, "gamma"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Gamma-tocopherol deserves its own moment. Most people know vitamin E as alpha-tocopherol, the form used in supplements.",
             {"say": "Gamma toco-ferol deserves its own moment. Most people know vitamin E as alpha toco-ferol, the form used in supplements."}),
            ("H", "Pecans are rich in the gamma form instead. It's studied separately, and works a bit differently, "
                  "mainly by neutralizing nitrogen-based free radicals. One hundred grams gives about twenty-four milligrams.", {}),
        ], "els": [
            T("Vitamin E comes in forms", 720, 170, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 420, "y": 400, "w": 560, "h": 170, "emoji": "💊", "title": "Alpha", "body": "common in supplements", "at": [0, "alpha"]},
            {"type": "card", "x": 1040, "y": 400, "w": 600, "h": 170, "emoji": "🌰", "title": "Gamma", "body": "rich in pecans", "at": [1, "gamma"], "fill": "#DCFCE7"},
            {"type": "stat", "x": 720, "y": 700, "w": 480, "h": 230, "value": 24, "unit": " mg", "label": "gamma-tocopherol / 100 g", "emoji": "", "at": [1, "twenty"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "One important caveat. Pecans used to be marketed on their high ORAC score, a test-tube antioxidant measure.",
             {"say": "One important caveat. Pecans used to be marketed on their high or-ack score, a test tube antioxidant measure."}),
            ("H", "But in twenty twelve, the U S Department of Agriculture removed its ORAC database, saying those test-tube values "
                  "have no proven biological meaning in the body.",
             {"say": "But in twenty twelve, the U S Department of Agriculture removed its or-ack database, saying those test tube values "
                     "have no proven biological meaning in the body."}),
            ("H", "Pecans really are rich in polyphenols. But arguments based on ORAC don't hold up.",
             {"say": "Pecans really are rich in polyphenols. But arguments based on or-ack don't hold up."}),
            ("P", "So no more bragging about test-tube scores. Got it.", {"mood": "smug"}),
        ], "els": [
            T("ORAC score", 720, 190, 96, at=[0, "ORAC"], font="fredoka", weight=700, color="red", strike=[1, "removed"]),
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 170, "emoji": "🏛️", "title": "USDA dropped it in 2012",
             "body": "no proven meaning in the body", "at": [1, "twenty"]},
            {"type": "check", "x": 220, "y": 620, "w": 1000, "ok": True, "text": "Rich in polyphenols", "at": [2, "polyphenols"]},
            {"type": "check", "x": 220, "y": 750, "w": 1000, "ok": False, "text": "ORAC-based claims", "at": [2, "hold"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "heart", "title": "The Good Stuff", "emoji": "❤️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the benefits. About sixty percent of the fat in pecans is monounsaturated, mostly oleic acid. "
                  "That's the same fatty acid that dominates olive oil.", {}),
            ("H", "In controlled trials where pecans replaced some of the fat in people's diets, "
                  "L D L and total cholesterol went down, without weight gain.",
             {"say": "In controlled trials where pecans replaced some of the fat in people's diets, "
                     "L D L and total cholesterol went down, without weight gain."}),
            ("P", "Same fat as olive oil? Fancy.", {"mood": "happy"}),
        ], "els": [
            {"type": "ring", "x": 420, "y": 360, "r": 170, "value": 60, "color": "#16A34A", "label": "monounsaturated", "at": [0, "sixty"]},
            {"type": "card", "x": 1060, "y": 300, "w": 600, "h": 160, "emoji": "🫒", "title": "Oleic acid", "body": "like olive oil", "at": [0, "oleic"]},
            {"type": "check", "x": 180, "y": 660, "w": 1260, "ok": True, "text": "LDL and total cholesterol down", "at": [1, "L"]},
            {"type": "check", "x": 180, "y": 790, "w": 1260, "ok": True, "text": "No weight gain in those trials", "at": [1, "without"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Pecans also give nine point six grams of fiber per hundred grams, which helps with fullness and gut health.", {}),
            ("H", "And the minerals are remarkable. One hundred grams gives more than two hundred percent of the daily value of manganese, "
                  "and about one hundred thirty percent of copper. Both help antioxidant enzymes do their job.", {}),
            ("H", "Plus a decent four point five milligrams of zinc, and one hundred twenty-one milligrams of magnesium.", {}),
        ], "els": [
            {"type": "stat", "x": 300, "y": 330, "w": 380, "h": 280, "value": 9.6, "decimals": 1, "unit": " g", "label": "fiber / 100 g", "emoji": "🌾", "at": [0, "nine"]},
            {"type": "stat", "x": 720, "y": 330, "w": 380, "h": 280, "value": 200, "unit": "%+", "label": "manganese DV", "emoji": "🟣", "at": [1, "manganese"]},
            {"type": "stat", "x": 1140, "y": 330, "w": 380, "h": 280, "value": 130, "unit": "%", "label": "copper DV", "emoji": "🟠", "at": [1, "copper"]},
            {"type": "pill", "x": 720, "y": 590, "text": "help antioxidant enzymes", "color": "green", "at": [1, "enzymes"]},
            {"type": "pill", "x": 480, "y": 720, "text": "zinc 4.5 mg", "color": "#F59E0B", "at": [2, "zinc"]},
            {"type": "pill", "x": 960, "y": 720, "text": "magnesium 121 mg", "color": "#0EA5E9", "at": [2, "magnesium"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "What about weight? Like other nuts, long-term studies don't find weight gain with controlled portions, "
                  "despite all those calories.", {}),
            ("H", "Part of the reason: some of the fat stays locked inside the cell walls and isn't fully absorbed. "
                  "And nuts have a real effect on fullness.", {}),
            ("P", "Locked fat. The nut keeps some secrets. I respect that.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 180, "emoji": "⚖️", "title": "No weight gain",
             "body": "in long-term studies, with controlled portions", "at": [0, "long"]},
            {"type": "card", "x": 470, "y": 530, "w": 520, "h": 170, "emoji": "🔒", "title": "Locked fat", "body": "not fully absorbed", "at": [1, "locked"]},
            {"type": "card", "x": 1030, "y": 530, "w": 520, "h": 170, "emoji": "😌", "title": "Fullness", "body": "a real effect", "at": [1, "fullness"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch number one: pecans are the most calorie-dense common nut. A thirty gram handful is already about two hundred calories.", {}),
            ("H", "The fat isn't the problem. The problem is how easy it is to eat a lot without noticing.", {}),
        ], "els": [
            T("#1 Calories", 760, 160, 76, at=0, font="fredoka", weight=700, color="red"),
            {"type": "stat", "x": 470, "y": 440, "w": 480, "h": 320, "value": 691, "unit": "", "label": "per 100 g", "emoji": "🔥", "at": [0, "dense"]},
            {"type": "stat", "x": 1050, "y": 440, "w": 480, "h": 320, "value": 200, "unit": "", "label": "per 30 g handful", "emoji": "✋", "at": [0, "handful"], "color": "ok"},
            {"type": "pill", "x": 760, "y": 720, "text": "easy to overeat without noticing", "color": "orange", "at": [1, "noticing"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch number two is the one that's special to pecans: they go rancid unusually fast. "
                  "Very high fat, plus a porous structure, means they spoil quickly. Rancid pecans taste bitter and sharp.", {}),
            ("H", "So they must be refrigerated or frozen. At room temperature they last about two months. "
                  "In the fridge, about nine months. And in the freezer, about two years.", {}),
            ("P", "Two months on the counter? I'd last way longer. Just saying.", {"mood": "smug"}),
        ], "els": [
            T("#2 They go rancid fast", 760, 160, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "bars", "x": 200, "y": 330, "w": 1200, "row_h": 120, "max": 24, "unit": " mo", "rows": [
                {"label": "Room temp", "value": 2, "color": "#EF4444", "at": [1, "room"]},
                {"label": "Fridge", "value": 9, "color": "#0EA5E9", "at": [1, "fridge"]},
                {"label": "Freezer", "value": 24, "color": "#16A34A", "at": [1, "freezer"]},
            ]},
            {"type": "pill", "x": 760, "y": 760, "text": "bitter or sharp taste = rancid", "color": "orange", "at": [0, "bitter"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch three: aflatoxins. Nuts stored in damp conditions can grow a mold that makes aflatoxin, "
                  "a known liver toxin and carcinogen. Skip any nuts that look or smell suspicious.",
             {"say": "Catch three: afla-toxins. Nuts stored in damp conditions can grow a mold that makes afla-toxin, "
                     "a known liver toxin and carcinogen. Skip any nuts that look or smell suspicious."}),
            ("H", "Catch four: tree nut allergy. Pecans are a known allergen, often with a cross-reaction to walnuts, "
                  "because they're related. This allergy usually doesn't go away with age.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "🍄", "title": "#3 Aflatoxins",
             "body": "from damp storage · skip suspicious nuts", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🚫", "title": "#4 Tree nut allergy",
             "body": "often cross-reacts with walnuts", "at": 1},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch five: candied pecans, caramel-coated pecans and pecan pie are a different food entirely. "
                  "They're loaded with sugar, sometimes with more sugar and syrup than nuts.", {}),
            ("H", "And catch six: phytic acid, which slightly reduces how much iron and zinc you absorb. Soaking reduces it, partly.", {}),
            ("P", "Pecan pie isn't a nut serving? My whole worldview is crumbling.", {"mood": "worried", "jump": True}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "🥧", "title": "#5 Candied pecans, pie",
             "body": "a sugar food, not a nut food", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🔒", "title": "#6 Phytic acid",
             "body": "a bit less iron and zinc · soaking helps a bit", "at": 1},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "howto", "title": "How to Eat Them", "emoji": "🥗", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "How much? A handful a day, about thirty grams. That's roughly nineteen pecan halves, and about two hundred calories. "
                  "It's the usual amount in nut studies.", {}),
            ("H", "Fun math: one pecan half weighs about one and a half grams, and has about ten calories.", {}),
        ], "els": [
            {"type": "stat", "x": 320, "y": 330, "w": 400, "h": 280, "value": 30, "unit": " g", "label": "a daily handful", "emoji": "✋", "at": [0, "thirty"]},
            {"type": "stat", "x": 740, "y": 330, "w": 400, "h": 280, "value": 19, "unit": "", "label": "halves", "emoji": "🌰", "at": [0, "nineteen"]},
            {"type": "stat", "x": 1160, "y": 330, "w": 400, "h": 280, "value": 200, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "hundred"]},
            {"type": "card", "x": 740, "y": 650, "w": 1000, "h": 160, "emoji": "🧮", "title": "1 half ≈ 1.5 g ≈ 10 calories",
             "at": [1, "half"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Storage is the most important part. Keep them in the fridge in an airtight container, or in the freezer for the long term. "
                  "If one tastes bitter or sharp, it's oxidized. Toss it.", {}),
            ("H", "Pecans in the shell keep better than halves or chopped pieces.", {}),
            ("H", "Toasting makes them taste much better, but speeds up oxidation. So toast a small batch, about three to four minutes in a dry pan, "
                  "and eat it soon.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 170, "emoji": "❄️", "title": "Fridge or freezer, airtight",
             "body": "bitter or sharp = toss it", "at": [0, "fridge"], "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 440, "w": 1000, "h": 150, "emoji": "🐚", "title": "In-shell keeps best", "at": [1, "shell"]},
            {"type": "card", "x": 720, "y": 650, "w": 1000, "h": 170, "emoji": "🍳", "title": "Toast a small batch",
             "body": "3 to 4 min, dry pan · eat it soon", "at": [2, "batch"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Ways to eat them: in salads, especially with goat cheese and fruit, in oatmeal, on yogurt, or just as a snack.", {}),
            ("H", "And because they're so low in carbs, pecans are a key ingredient in keto baking made with nut flour.", {}),
            ("P", "Pecans on yogurt? Hey, that's my spot!", {"mood": "worried", "jump": True}),
        ], "els": [
            E("🥗", 300, 330, 160, at=[0, "salads"]),
            T("salads", 300, 450, 42, at=[0, "salads"], font="fredoka", weight=600),
            E("🥣", 620, 330, 160, at=[0, "oatmeal"]),
            T("oatmeal", 620, 450, 42, at=[0, "oatmeal"], font="fredoka", weight=600),
            E("🥛", 940, 330, 160, at=[0, "yogurt"]),
            T("yogurt", 940, 450, 42, at=[0, "yogurt"], font="fredoka", weight=600),
            E("😋", 1260, 330, 160, at=[0, "snack"]),
            T("snack", 1260, 450, 42, at=[0, "snack"], font="fredoka", weight=600),
            {"type": "card", "x": 780, "y": 680, "w": 1000, "h": 160, "emoji": "🧁", "title": "Keto baking with nut flour",
             "at": [1, "keto"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "versus", "title": "Pecan vs Walnut", "emoji": "🥊", "scenes": [
        {"pip": PIP_C, "lines": [
            ("H", "Finally, the family rivalry. Pecan versus walnut.", {}),
            ("P", "Ooh, a family feud! I've got snacks. Well... I am a snack.", {"mood": "happy", "jump": True}),
        ], "els": [
            T("Pecan vs Walnut", 960, 170, 110, at=0, font="fredoka", weight=700, color="green"),
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "The pecan is sweeter and milder, lower in carbs, and richer in monounsaturated fat.", {}),
            ("H", "The walnut has much more plant omega-3, called A L A, and more protein. "
                  "And for heart health, walnuts have the stronger research behind them.",
             {"say": "The walnut has much more plant omega 3, called A L A, and more protein. "
                     "And for heart health, walnuts have the stronger research behind them."}),
            ("H", "Bottom line: both are excellent, and they complement each other.", {}),
        ], "els": [
            T("Pecan", 460, 170, 80, at=0, font="fredoka", weight=700, color="#B45309"),
            {"type": "card", "x": 460, "y": 340, "w": 600, "h": 130, "emoji": "🍯", "title": "Sweeter, milder", "at": [0, "sweeter"]},
            {"type": "card", "x": 460, "y": 500, "w": 600, "h": 130, "emoji": "📉", "title": "Fewer carbs", "at": [0, "carbs"]},
            {"type": "card", "x": 460, "y": 660, "w": 600, "h": 130, "emoji": "🫒", "title": "More mono fat", "at": [0, "monounsaturated"]},
            T("Walnut", 1100, 170, 80, at=[1, "walnut"], font="fredoka", weight=700, color="#475569"),
            {"type": "card", "x": 1100, "y": 340, "w": 600, "h": 130, "emoji": "🐟", "title": "More omega-3 (ALA)", "at": [1, "omega"]},
            {"type": "card", "x": 1100, "y": 500, "w": 600, "h": 130, "emoji": "💪", "title": "More protein", "at": [1, "protein"]},
            {"type": "card", "x": 1100, "y": 660, "w": 600, "h": 130, "emoji": "❤️", "title": "Stronger heart research", "at": [1, "heart"]},
            {"type": "banner", "x": 780, "y": 840, "text": "Both excellent", "color": "#16A34A", "at": [2, "both"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: the pecan is the most extreme nut. The most fat, the fewest carbs, and the most calories.", {}),
            ("H", "Two: it brings monounsaturated fat, polyphenols, gamma-tocopherol, and lots of manganese and copper.",
             {"say": "Two: it brings monounsaturated fat, polyphenols, gamma toco-ferol, and lots of manganese and copper."}),
            ("H", "Three: its standout strength is for low-carb eating.", {}),
            ("H", "And four: it's not a pantry nut. Keep it in the fridge or freezer.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Most fat, fewest carbs, most calories", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Good fats, polyphenols, manganese, copper", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Great for low-carb eating", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Store in the fridge or freezer", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So pecans are extreme, delicious, and they need a fridge. Like a celebrity with a rider.", {"mood": "smug"}),
            ("H", "Pretty much, Pip.", {}),
            ("P", "I still don't need a fridge. Just saying!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Go check your fridge!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article + sources: wiseplate.blog/food/pecans", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
