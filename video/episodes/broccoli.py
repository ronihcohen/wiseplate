"""Broccoli explainer (English), based on https://wiseplate.blog/en/food/broccoli/

Numbers are the article's: fresh broccoli per 100 g with % of daily intake,
orange vitamin C per 100 g for comparison, and temperatures in degrees
Celsius (roasting also given in Fahrenheit, as in the English article).
Keep them in sync with content/food/broccoli.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Broccoli: Are You Cooking It Wrong?"
SLUG = "broccoli"
ARTICLE = "https://wiseplate.blog/en/food/broccoli/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "BROCCOLI", "top_size": 180, "bottom": "COOKED WRONG?", "bottom_size": 120,
         "badge": "40", "badge_label": "minutes to\nwait first", "badge_color": "#16A34A",
         "scatter": "🥦", "hero": "🥦", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "inside":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "orange":   {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "secret":   {"bpm": 88, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "fixes":    {"bpm": 114, "root": 64, "prog": ["I", "vi", "IV", "V"], "density": 0.75, "swing": 0.1},
    "matters":  {"bpm": 96, "root": 65, "prog": ["I", "iii", "IV", "V"], "density": 0.55},
    "quirks":   {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#F0FDF4", "inside": "#ECFDF5", "orange": "#FFEDD5", "secret": "#1E1B4B",
    "fixes": "#ECFCCB", "matters": "#F1F5F9", "quirks": "#FEF3C7", "howto": "#FFEDD5",
    "outro": "#F0FDF4",
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
            ("P", "Hi there! Pip the pumpkin seed here, back to review another green thing.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest looks like a tiny tree, and it's not a seed. It's broccoli!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🥦", 960, 200, 160, at=[1, "broccoli"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Broccoli is one of the most nutrient-dense vegetables there is. "
                  "We'll look at what's inside, a hidden compound called sulforaphane, "
                  "the cooking mistake almost everyone makes, and the quirks worth knowing.",
             {"say": "Broccoli is one of the most nutrient-dense vegetables there is. "
                     "We'll look at what's inside, a hidden compound called sul-for-a-fane, "
                     "the cooking mistake almost everyone makes, and the quirks worth knowing."}),
            ("P", "A cooking mistake? Please tell me it's not boiling. My grandma boils everything.", {"mood": "worried"}),
        ], "els": [
            E("🥦", 420, 330, 200, at=[0, "Broccoli"], wobble=True),
            T("Broccoli", 640, 300, 140, at=[0, "Broccoli"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 480, "w": 640, "h": 96, "emoji": "📊", "title": "What's inside", "at": [0, "inside"]},
            {"type": "card", "x": 760, "y": 588, "w": 640, "h": 96, "emoji": "🔬", "title": "Sulforaphane", "at": [0, "compound"]},
            {"type": "card", "x": 760, "y": 696, "w": 640, "h": 96, "emoji": "🍳", "title": "The cooking mistake", "at": [0, "mistake"]},
            {"type": "card", "x": 760, "y": 804, "w": 640, "h": 96, "emoji": "💨", "title": "The quirks", "at": [0, "quirks"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "inside", "title": "What's Inside", "emoji": "📊", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Per hundred grams of fresh broccoli: just thirty-four calories, two point eight grams of protein, "
                  "six point six grams of carbs, two point six grams of fiber, and zero point four grams of fat.", {}),
            ("P", "Thirty-four calories. That's barely a snack. I'm worth way more than that.", {"mood": "smug"}),
        ], "els": [
            T("Fresh broccoli, per 100 g", 720, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 330, "y": 370, "w": 400, "h": 260, "value": 34, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "thirty"]},
            {"type": "stat", "x": 760, "y": 370, "w": 400, "h": 260, "value": 2.8, "decimals": 1, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "protein"]},
            {"type": "stat", "x": 1190, "y": 370, "w": 400, "h": 260, "value": 6.6, "decimals": 1, "unit": " g", "label": "carbs", "emoji": "🍞", "at": [0, "carbs"]},
            {"type": "stat", "x": 540, "y": 680, "w": 400, "h": 260, "value": 2.6, "decimals": 1, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [0, "fiber"]},
            {"type": "stat", "x": 980, "y": 680, "w": 400, "h": 260, "value": 0.4, "decimals": 1, "unit": " g", "label": "fat", "emoji": "🫒", "at": [0, "fat"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Now the daily values. Vitamin C: eighty-nine milligrams, ninety-nine percent of your daily intake. "
                  "Vitamin K: one hundred two micrograms, eighty-five percent.", {}),
            ("H", "Folate: sixteen percent. Fiber: nine. Potassium: seven. Protein: six. Calcium: five. And vitamin A: three percent.", {}),
            ("P", "Ninety-nine percent of vitamin C. In a vegetable. That looks like a tree.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("% of daily intake, per 100 g", 760, 150, 52, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 240, "w": 1200, "row_h": 82, "max": 100, "rows": [
                {"label": "Vitamin C", "value": 99, "color": "#F97316", "at": [0, "Vitamin C"], "star": True},
                {"label": "Vitamin K", "value": 85, "color": "#16A34A", "at": [0, "Vitamin K"]},
                {"label": "Folate", "value": 16, "color": "#0EA5E9", "at": [1, "Folate"]},
                {"label": "Fiber", "value": 9, "color": "#A16207", "at": [1, "Fiber"]},
                {"label": "Potassium", "value": 7, "color": "#7C3AED", "at": [1, "Potassium"]},
                {"label": "Protein", "value": 6, "color": "#DB2777", "at": [1, "Protein"]},
                {"label": "Calcium", "value": 5, "color": "#64748B", "at": [1, "Calcium"]},
                {"label": "Vitamin A", "value": 3, "color": "#EAB308", "at": [1, "vitamin A"]},
            ]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "orange", "title": "Move Over, Orange", "emoji": "🍊", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "That vitamin C is the first surprise. Broccoli has eighty-nine milligrams per hundred grams. "
                  "An orange has fifty-three.", {}),
            ("H", "If you think of vitamin C as a citrus thing, you're missing the better source.", {}),
            ("P", "Oranges everywhere, clutching their vitamin C. Sorry, team citrus.", {"mood": "smug"}),
        ], "els": [
            T("Vitamin C per 100 g", 760, 170, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 200, "y": 360, "w": 1200, "row_h": 140, "max": 100, "unit": " mg", "rows": [
                {"label": "Broccoli", "value": 89, "color": "#16A34A", "at": [0, "eighty"]},
                {"label": "Orange", "value": 53, "color": "#F97316", "at": [0, "orange"]},
            ]},
            {"type": "pill", "x": 760, "y": 700, "text": "the better source", "color": "green", "at": [1, "better"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Vitamin K, at eighty-five percent of your daily intake, matters for blood clotting, and for directing calcium to your bones.", {}),
            ("H", "The fiber, two point six grams per hundred grams, plus plenty of water, helps you feel full and keeps your bowels regular.", {}),
            ("H", "Folate, at sixteen percent, is important in pregnancy. "
                  "And lutein and zeaxanthin support eye health.",
             {"say": "Folate, at sixteen percent, is important in pregnancy. "
                     "And loo-teen and zee-a-zanthin support eye health."}),
            ("H", "Put it together, and broccoli has one of the highest nutrient-to-calorie ratios of any vegetable.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1260, "ok": True, "text": "Vitamin K: clotting, calcium to bone", "at": [0, "clotting"]},
            {"type": "check", "x": 160, "y": 330, "w": 1260, "ok": True, "text": "Fiber: fullness, regularity", "at": [1, "fiber"]},
            {"type": "check", "x": 160, "y": 460, "w": 1260, "ok": True, "text": "Folate: important in pregnancy", "at": [2, "Folate"]},
            {"type": "check", "x": 160, "y": 590, "w": 1260, "ok": True, "text": "Lutein, zeaxanthin: eyes", "at": [2, "eye"]},
            {"type": "pill", "x": 760, "y": 740, "text": "top nutrients per calorie", "color": "green", "at": [3, "ratios"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "secret", "title": "The Sulforaphane Secret", "emoji": "🔬", "dark": True, "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the part that makes broccoli more researched than any other vegetable. It's not a vitamin. It's sulforaphane.",
             {"say": "Now the part that makes broccoli more researched than any other vegetable. It's not a vitamin. It's sul-for-a-fane."}),
            ("H", "Here's the twist: broccoli doesn't actually contain sulforaphane. "
                  "It contains two separate things, kept in different cells.",
             {"say": "Here's the twist: broccoli doesn't actually contain sul-for-a-fane. "
                     "It contains two separate things, kept in different cells."}),
            ("H", "One: glucoraphanin, a stable, inactive sulfur compound. "
                  "Two: myrosinase, an enzyme that turns glucoraphanin into sulforaphane.",
             {"say": "One: gloo-co-raf-a-nin, a stable, inactive sulfur compound. "
                     "Two: my-ro-sin-ase, an enzyme that turns gloo-co-raf-a-nin into sul-for-a-fane."}),
            ("P", "Two ingredients in separate rooms. Like a buddy cop movie.", {"mood": "happy"}),
        ], "els": [
            T("Sulforaphane", 720, 160, 90, at=0, font="fredoka", weight=700, color="white"),
            {"type": "card", "x": 420, "y": 420, "w": 560, "h": 200, "emoji": "🧪", "title": "Glucoraphanin",
             "body": "stable, inactive", "at": [2, "One"], **DARK},
            {"type": "card", "x": 1020, "y": 420, "w": 560, "h": 200, "emoji": "✂️", "title": "Myrosinase",
             "body": "the enzyme", "at": [2, "Two"], **DARK},
            T("separate cells", 720, 600, 50, at=[1, "separate"], font="fredoka", weight=600, color="#C7D2FE"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "They only meet when the cells break: when you cut, chew or crush the broccoli.", {}),
            ("H", "And myrosinase is very sensitive to heat. It's already switched off at around sixty to seventy degrees Celsius.",
             {"say": "And my-ro-sin-ase is very sensitive to heat. It's already switched off at around sixty to seventy degrees Celsius."}),
            ("H", "So broccoli thrown into a boiling pot, or stir-fried on high heat, loses the enzyme before the reaction can happen. "
                  "The glucoraphanin stays, and almost no sulforaphane forms.",
             {"say": "So broccoli thrown into a boiling pot, or stir fried on high heat, loses the enzyme before the reaction can happen. "
                     "The gloo-co-raf-a-nin stays, and almost no sul-for-a-fane forms."}),
            ("P", "So the enzyme just clocks out? Rude.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 160, "emoji": "🔪", "title": "Cut, chew or crush",
             "body": "the two finally meet", "at": [0, "cut"], **DARK},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 160, "emoji": "🌡️", "title": "Enzyme off at 60-70°C",
             "at": [1, "sixty"], **DARK},
            {"type": "banner", "x": 720, "y": 650, "text": "Boiling: almost no sulforaphane", "color": "#DC2626", "at": [2, "boiling"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "fixes", "title": "Four Easy Fixes", "emoji": "🛠️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "The good news: there are four practical fixes.", {}),
            ("H", "Fix one: cut it, and wait forty minutes before cooking. Cutting starts the reaction while it's still cold. "
                  "By the time the heat arrives, the sulforaphane has formed, and it's heat-stable itself.",
             {"say": "Fix one: cut it, and wait forty minutes before cooking. Cutting starts the reaction while it's still cold. "
                     "By the time the heat arrives, the sul-for-a-fane has formed, and it's heat stable itself."}),
            ("H", "It's the most effective step, and it costs nothing.", {}),
            ("P", "Forty minutes of doing nothing? Finally, a health tip I'm good at.", {"mood": "sleepy"}),
        ], "els": [
            T("Fix #1", 720, 170, 80, at=[1, "one"], font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 720, "y": 420, "w": 620, "h": 280, "value": 40, "unit": " min", "label": "cut, then wait",
             "emoji": "⏱️", "at": [1, "forty"]},
            {"type": "pill", "x": 720, "y": 680, "text": "most effective, and free", "color": "green", "at": [2, "effective"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Fix two: steam it for just three to four minutes. Don't boil. "
                  "Brief steaming keeps the inside cool enough to save some of the enzyme, and stops vitamin C leaching into the water.", {}),
            ("H", "Fix three: add an outside source of myrosinase to the cooked broccoli. "
                  "A pinch of mustard powder, sesame, radish or arugula. They carry the active enzyme and bring the reaction back.",
             {"say": "Fix three: add an outside source of my-ro-sin-ase to the cooked broccoli. "
                     "A pinch of mustard powder, sesame, radish or arugula. They carry the active enzyme and bring the reaction back."}),
            ("H", "And fix four: eat some of it raw, in a salad or as a dip.", {}),
            ("P", "Sesame to the rescue! A fellow seed. I'm so proud.", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 170, "emoji": "♨️", "title": "#2 Steam 3-4 minutes",
             "body": "don't boil", "at": [0, "steam"]},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 170, "emoji": "🌭", "title": "#3 Add the enzyme back",
             "body": "mustard powder, sesame, radish, arugula", "at": [1, "mustard"]},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 170, "emoji": "🥗", "title": "#4 Eat some raw",
             "body": "in a salad or as a dip", "at": [2, "raw"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "One important note about frozen broccoli. It's blanched before freezing, and that switches off the myrosinase almost completely.",
             {"say": "One important note about frozen broccoli. It's blanched before freezing, and that switches off the my-ro-sin-ase almost completely."}),
            ("H", "Frozen broccoli keeps its vitamins well, sometimes even better, since it's frozen soon after harvest. "
                  "But it makes almost no sulforaphane, unless you add an enzyme source like mustard powder.",
             {"say": "Frozen broccoli keeps its vitamins well, sometimes even better, since it's frozen soon after harvest. "
                     "But it makes almost no sul-for-a-fane, unless you add an enzyme source like mustard powder."}),
        ], "els": [
            T("Frozen broccoli", 720, 170, 80, at=0, font="fredoka", weight=700, color="#0EA5E9"),
            {"type": "check", "x": 170, "y": 340, "w": 1100, "ok": True, "text": "Vitamins: kept well", "at": [1, "vitamins"]},
            {"type": "check", "x": 170, "y": 470, "w": 1100, "ok": False, "text": "Sulforaphane: almost none", "at": [1, "almost"]},
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 160, "emoji": "🌭", "title": "Fix: a pinch of mustard powder",
             "at": [1, "mustard"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "matters", "title": "Why It Matters", "emoji": "🧬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So why bother? Sulforaphane switches on the Nrf2 pathway, "
                  "which turns on phase two detox enzymes and antioxidant enzymes.",
             {"say": "So why bother? Sul-for-a-fane switches on the N R F 2 pathway, "
                     "which turns on phase two detox enzymes and antioxidant enzymes."}),
            ("H", "It's been studied for protection against cancer, for inflammation, and for cardiometabolic function.", {}),
            ("H", "But keep it in proportion. The evidence in the lab and in animals is strong. "
                  "In human studies, it's promising, but still early.", {}),
            ("P", "Promising but early. Like me before my morning stretch.", {"mood": "sleepy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 170, "emoji": "🔑", "title": "Switches on Nrf2",
             "body": "detox and antioxidant enzymes", "at": [0, "Nrf2"]},
            {"type": "pill", "x": 330, "y": 360, "text": "cancer", "color": "#7C3AED", "at": [1, "cancer"]},
            {"type": "pill", "x": 680, "y": 360, "text": "inflammation", "color": "#7C3AED", "at": [1, "inflammation"]},
            {"type": "pill", "x": 1110, "y": 360, "text": "cardiometabolic", "color": "#7C3AED", "at": [1, "cardiometabolic"]},
            {"type": "check", "x": 170, "y": 520, "w": 1100, "ok": True, "text": "Lab and animals: strong", "at": [2, "lab"]},
            {"type": "check", "x": 170, "y": 650, "w": 1100, "ok": False, "text": "Humans: promising, still early", "at": [2, "human"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "quirks", "title": "The Quirks", "emoji": "💨", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the downsides. Quirk one: gas and bloating. Broccoli has raffinose and fructans, "
                  "carbs that aren't digested in the small intestine, and get fermented in the colon.",
             {"say": "Now the downsides. Quirk one: gas and bloating. Broccoli has raff-in-ose and fructans, "
                     "carbs that aren't digested in the small intestine, and get fermented in the colon."}),
            ("H", "That's the reason for the gas, and it's not a sign of a problem. "
                  "The stalks have more fructans than the florets, so sensitive people can stick to the florets. "
                  "Longer cooking also helps.", {}),
            ("P", "I'm not going to make the obvious joke. I'm a professional.", {"mood": "smug"}),
            ("H", "Same reason it's limited on a low-FODMAP diet. But florets, up to seventy-five grams, count as low-FODMAP. "
                  "The stalk is the problem part.",
             {"say": "Same reason it's limited on a low fod-map diet. But florets, up to seventy-five grams, count as low fod-map. "
                     "The stalk is the problem part."}),
        ], "els": [
            T("#1 Gas and bloating", 720, 160, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 720, "y": 330, "w": 1000, "h": 160, "emoji": "💨", "title": "Raffinose and fructans",
             "body": "fermented in the colon", "at": [0, "raffinose"]},
            {"type": "pill", "x": 720, "y": 480, "text": "stalks have more than florets", "color": "orange", "at": [1, "stalks"]},
            {"type": "card", "x": 720, "y": 690, "w": 1000, "h": 170, "emoji": "🥦", "title": "Low-FODMAP: florets",
             "body": "up to 75 g", "at": [3, "FODMAP"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Quirk two: goitrogens and the thyroid. The glucosinolates in broccoli may interfere with iodine uptake by the thyroid.",
             {"say": "Quirk two: goy-tro-jens and the thyroid. The gloo-co-sin-o-lates in broccoli may interfere with iodine uptake by the thyroid."}),
            ("H", "But keep it in proportion. It only matters with existing iodine deficiency, plus very large amounts of raw cruciferous vegetables. "
                  "Cooking reduces it a lot, and with enough iodine, it's not a practical concern.", {}),
            ("H", "Quirk three: vitamin K and blood thinners. People taking Coumadin don't need to avoid broccoli. "
                  "They need to keep their intake steady, so the drug dose can be set around it. Sharp swings are the problem, not the vegetable.",
             {"say": "Quirk three: vitamin K and blood thinners. People taking Coo-ma-din don't need to avoid broccoli. "
                     "They need to keep their intake steady, so the drug dose can be set around it. Sharp swings are the problem, not the vegetable."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 170, "emoji": "🦋", "title": "#2 Thyroid",
             "body": "glucosinolates and iodine uptake", "at": 0},
            {"type": "pill", "x": 720, "y": 360, "text": "only with low iodine + lots of raw", "color": "orange", "at": [1, "deficiency"]},
            {"type": "pill", "x": 720, "y": 460, "text": "cooking reduces it", "color": "green", "at": [1, "Cooking"]},
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 180, "emoji": "💊", "title": "#3 On Coumadin?",
             "body": "keep your intake steady", "at": [2, "Coumadin"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Quirk four: boiling. Long boiling can remove over fifty percent of the vitamin C, which ends up in the water. "
                  "Steaming keeps most of it.", {}),
            ("H", "Quirk five: pesticide residues. The dense florets are hard to wash. "
                  "A short soak in water with a little baking soda, then a rinse, works better than rinsing alone.", {}),
            ("H", "Quirk six: some people find it bitter. That's a genetic sensitivity to sulfur compounds, linked to the TAS2R38 gene. "
                  "Roasting with olive oil caramelizes them, and cuts the bitterness a lot.",
             {"say": "Quirk six: some people find it bitter. That's a genetic sensitivity to sulfur compounds, linked to the T A S 2 R 38 gene. "
                     "Roasting with olive oil caramelizes them, and cuts the bitterness a lot."}),
            ("P", "Bitter broccoli? It's in your genes. Not my fault, not yours.", {"mood": "happy"}),
        ], "els": [
            {"type": "check", "x": 160, "y": 210, "w": 1340, "ok": False, "text": "#4 Long boiling: over 50% of vitamin C lost", "at": [0, "fifty"]},
            {"type": "check", "x": 160, "y": 350, "w": 1340, "ok": True, "text": "Steaming keeps most of it", "at": [0, "Steaming"]},
            {"type": "check", "x": 160, "y": 490, "w": 1340, "ok": True, "text": "#5 Soak in baking soda, then rinse", "at": [1, "soak"]},
            {"type": "check", "x": 160, "y": 630, "w": 1340, "ok": True, "text": "#6 Bitter? Roast with olive oil", "at": [2, "Roasting"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "How to Eat It", "emoji": "🍳", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Let's put it into practice. Step one: cut it, and wait forty minutes. That's the step with the biggest impact.", {}),
            ("H", "Step two: steam for three to four minutes, until it's bright green. If it turned olive green, it's overcooked.", {}),
            ("P", "Bright green is good. I'm bright green. Just saying.", {"mood": "smug"}),
            ("H", "Not a fan of the taste? Roast it in the oven at two hundred twenty degrees Celsius, that's four hundred twenty-eight Fahrenheit, "
                  "with olive oil and garlic.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 190, "w": 1000, "h": 150, "emoji": "⏱️", "title": "Cut, wait 40 minutes", "at": [0, "cut"]},
            T("bright green", 450, 380, 60, at=[1, "bright"], font="fredoka", weight=700, color="#16A34A"),
            T("olive green", 1000, 380, 60, at=[1, "olive"], font="fredoka", weight=700, color="#6B7A2A"),
            T("perfect", 450, 450, 40, at=[1, "bright"], color="muted"),
            T("overcooked", 1000, 450, 40, at=[1, "olive"], color="muted"),
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 180, "emoji": "🔥", "title": "Roast at 220°C (428°F)",
             "body": "with olive oil and garlic", "at": [3, "Roast"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Don't throw away the stalk. It's edible, sweeter than the florets, and great peeled and sliced, or grated into a salad.", {}),
            ("H", "Add a pinch of mustard powder to the finished broccoli, especially if it's frozen.", {}),
            ("H", "And pair it with olive oil. It helps you absorb the carotenoids, and it softens the taste.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 170, "emoji": "🥕", "title": "Keep the stalk",
             "body": "sweeter: peel, slice or grate", "at": [0, "stalk"]},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 170, "emoji": "🌭", "title": "Pinch of mustard powder",
             "body": "especially for frozen", "at": [1, "mustard"]},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 170, "emoji": "🫒", "title": "Add olive oil",
             "body": "better carotenoid absorption", "at": [2, "olive"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: a hundred grams of broccoli gives almost all your vitamin C and eighty-five percent of your vitamin K, in thirty-four calories.", {}),
            ("H", "Two: the one thing to remember is how to cook it. Cut it, wait forty minutes, and steam for just three to four minutes.", {}),
            ("H", "Three: broccoli boiled until soft is still a good vegetable. But it has lost most of what makes it special.", {}),
            ("H", "Four: if you buy frozen, a pinch of mustard powder at the end brings back what blanching took away.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Vitamin C and K in 34 calories", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Cut, wait 40 min, steam 3-4 min", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Boiled is still good, just less", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Frozen? Add mustard powder", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So broccoli: a tiny tree with a secret, and it needs a forty-minute nap before dinner.", {"mood": "happy"}),
            ("H", "Pretty much, Pip.", {}),
            ("P", "Respect the tree. And the seed!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Cut it, and wait!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/broccoli", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
