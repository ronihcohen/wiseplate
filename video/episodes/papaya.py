"""Papaya explainer (English), based on https://wiseplate.blog/food/papaya/

Numbers are the article's: fresh papaya per 100 g with % daily value, and a
whole medium papaya (about 300 g of flesh). Keep them in sync with
content/food/papaya.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Papaya: More Vitamin C Than an Orange?"
SLUG = "papaya"
ARTICLE = "https://wiseplate.blog/food/papaya/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "PAPAYA", "top_size": 200, "bottom": "BEATS ORANGE?", "bottom_size": 150,
         "badge": "68%", "badge_label": "vitamin C\nper 100 g", "badge_color": "#F97316",
         "scatter": "🍈", "hero": "🍊", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "meet":     {"bpm": 104, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.65, "swing": 0.15},
    "inside":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "papain":   {"bpm": 116, "root": 62, "prog": ["I", "bVII", "IV", "I"], "density": 0.8, "swing": 0.1},
    "seeds":    {"bpm": 84, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "benefits": {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF7ED", "meet": "#FEF3C7", "inside": "#ECFDF5", "papain": "#FFE4E6",
    "seeds": "#1E1B4B", "benefits": "#ECFCCB", "catches": "#FEE2E2", "howto": "#FFEDD5",
    "outro": "#FFF7ED",
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
            ("P", "Aloha! Pip the pumpkin seed here, in my tropical shirt. Metaphorically.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest is orange, juicy, and full of little black seeds. My people! It's the papaya!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🌴", 960, 200, 160, at=[1, "papaya"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today: papaya. Its vitamin C, the famous enzyme papain, whether you should eat the seeds, "
                  "and the catches worth knowing.", {}),
            ("P", "The seeds part. I'm emotionally invested.", {"mood": "smug"}),
        ], "els": [
            E("🌴", 420, 330, 200, at=[0, "papaya"], wobble=True),
            T("Papaya", 640, 300, 140, at=[0, "papaya"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🍊", "title": "Vitamin C", "at": [0, "vitamin"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🥩", "title": "The papain enzyme", "at": [0, "papain"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "🖤", "title": "The seeds", "at": [0, "seeds"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "meet", "title": "Meet the Papaya", "emoji": "🌴", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Papaya, Carica papaya, is a tropical fruit from Central America, and today it's grown all over the world.",
             {"say": "Papaya, Carica papaya, is a tropical fruit from Central America, and today it's grown all over the world."}),
            ("H", "It stands out for three things. An unusual amount of vitamin C, about sixty-one milligrams per hundred grams, "
                  "almost double an orange. A high concentration of carotenoids. And a unique enzyme called papain, that breaks down protein.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 860, "h": 140, "emoji": "🌎", "title": "Carica papaya",
             "body": "from Central America", "at": 0, "italic_title": True},
            {"type": "card", "x": 720, "y": 400, "w": 860, "h": 140, "emoji": "🍊", "title": "~61 mg vitamin C",
             "body": "almost double an orange", "at": [1, "sixty"]},
            {"type": "card", "x": 720, "y": 570, "w": 860, "h": 140, "emoji": "🧡", "title": "Carotenoids", "at": [1, "carotenoids"]},
            {"type": "card", "x": 720, "y": 740, "w": 860, "h": 140, "emoji": "✂️", "title": "Papain", "body": "breaks down protein", "at": [1, "papain"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "And unlike other sweet tropical fruits, papaya is fairly low in sugar. "
                  "Seven point eight grams per hundred grams, less than mango, at thirteen point seven, or banana, at twelve point two.", {}),
            ("P", "A tropical fruit that's chill about sugar? Respect.", {"mood": "happy"}),
        ], "els": [
            T("Sugar per 100 g", 760, 180, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 330, "w": 1200, "row_h": 120, "max": 14, "unit": " g", "rows": [
                {"label": "Papaya", "value": 7.8, "decimals": 1, "color": "#16A34A", "at": [0, "seven"], "star": True},
                {"label": "Banana", "value": 12.2, "decimals": 1, "color": "#F59E0B", "at": [0, "banana"]},
                {"label": "Mango", "value": 13.7, "decimals": 1, "color": "#F97316", "at": [0, "mango"]},
            ]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "inside", "title": "What's Inside?", "emoji": "🔬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "One hundred grams of fresh papaya has just forty-three calories, ten point eight grams of carbs, "
                  "of which seven point eight are sugars, and one point seven grams of fiber.", {}),
            ("H", "It also has about one thousand eight hundred thirty micrograms of lycopene, and two hundred seventy-four of beta-carotene.", {}),
        ], "els": [
            T("Per 100 g fresh", 720, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 300, "y": 380, "w": 380, "h": 280, "value": 43, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "forty"]},
            {"type": "stat", "x": 720, "y": 380, "w": 380, "h": 280, "value": 7.8, "decimals": 1, "unit": " g", "label": "sugars", "emoji": "🍬", "at": [0, "seven"]},
            {"type": "stat", "x": 1140, "y": 380, "w": 380, "h": 280, "value": 1.7, "decimals": 1, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [0, "fiber"]},
            {"type": "pill", "x": 470, "y": 680, "text": "lycopene 1,830 mcg", "color": "#EF4444", "at": [1, "lycopene"]},
            {"type": "pill", "x": 1000, "y": 680, "text": "beta-carotene 274 mcg", "color": "orange", "at": [1, "beta"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "And here's the percent of the daily value. Vitamin C wins big: sixty-eight percent.", {}),
            ("H", "Then folate, nine. Fiber, six. Vitamin A and magnesium, five each. And potassium, four.", {}),
            ("H", "A whole medium papaya, about three hundred grams of flesh, gives around one hundred thirty calories, "
                  "and more than one hundred eighty milligrams of vitamin C. That's twice the recommended daily intake.", {}),
            ("P", "Twice? Papaya, you overachiever.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("% Daily Value per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 260, "w": 1200, "row_h": 86, "max": 70, "rows": [
                {"label": "Vitamin C", "value": 68, "color": "#F97316", "at": [0, "sixty"], "star": True},
                {"label": "Folate", "value": 9, "color": "#16A34A", "at": [1, "folate"]},
                {"label": "Fiber", "value": 6, "color": "#84CC16", "at": [1, "Fiber"]},
                {"label": "Vitamin A", "value": 5, "color": "#F59E0B", "at": [1, "Vitamin"]},
                {"label": "Magnesium", "value": 5, "color": "#14B8A6", "at": [1, "magnesium"]},
                {"label": "Potassium", "value": 4, "color": "#0EA5E9", "at": [1, "potassium"]},
            ]},
            {"type": "banner", "x": 760, "y": 820, "text": "Whole papaya: 2× your daily vitamin C", "color": "#F97316", "at": [2, "twice"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "papain", "title": "Papain: The Famous Enzyme", "emoji": "🥩", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Papain is a protein-splitting enzyme, from a group called cysteine proteases.",
             {"say": "Papain is a protein splitting enzyme, from a group called cysteine pro-tee-ases."}),
            ("H", "It's concentrated mostly in the milky sap, or latex, of the unripe green fruit. And as the fruit ripens, the amount drops a lot.", {}),
        ], "els": [
            T("Papain", 720, 190, 120, at=0, font="fredoka", weight=700, color="#DC2626"),
            T("a protein-splitting enzyme", 720, 300, 48, at=0, color="muted"),
            {"type": "card", "x": 450, "y": 540, "w": 560, "h": 190, "emoji": "🟢", "title": "Green fruit",
             "body": "lots, in the milky sap", "at": [1, "unripe"]},
            {"type": "arrow", "x1": 740, "y1": 540, "x2": 850, "y2": 540, "at": [1, "ripens"]},
            {"type": "card", "x": 1080, "y": 540, "w": 440, "h": 190, "emoji": "🟠", "title": "Ripe fruit",
             "body": "much less", "at": [1, "drops"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "What does it really do? One: it tenderizes meat. That's its most proven and common use. "
                  "Papain breaks down collagen fibers and softens tough cuts. Commercial meat tenderizer powders are based on it.", {}),
            ("H", "Two: help digesting protein. Papain supplements were studied for bloating and discomfort after meals, with mixed results.", {}),
            ("H", "And remember, the ripe papaya you eat has much less papain than a supplement, and stomach acid breaks some of it down.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 220, "w": 1300, "ok": True, "text": "Tenderizes meat: proven", "at": [0, "tenderizes"]},
            {"type": "check", "x": 160, "y": 350, "w": 1300, "ok": True, "text": "Digestion supplements: mixed results", "at": [1, "mixed"]},
            {"type": "card", "x": 720, "y": 600, "w": 1000, "h": 180, "emoji": "🍈", "title": "Ripe fruit ≠ supplement",
             "body": "less papain · stomach acid breaks it", "at": [2, "ripe"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "What it doesn't do: papaya doesn't burn fat, doesn't cleanse your liver, and doesn't replace pancreatic enzymes "
                  "when the pancreas isn't working. Those claims are marketing, with no backing.", {}),
            ("H", "A kitchen tip that really works: tenderize meat with grated green papaya or its juice. But only fifteen to thirty minutes. "
                  "Longer, and the meat turns mushy.", {}),
            ("P", "Fifteen minutes, tender steak. Thirty-one minutes, steak soup. Got it.", {"mood": "smug"}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1300, "ok": False, "text": "Burns fat", "at": [0, "burn"]},
            {"type": "check", "x": 160, "y": 320, "w": 1300, "ok": False, "text": "Cleanses the liver", "at": [0, "cleanse"]},
            {"type": "check", "x": 160, "y": 440, "w": 1300, "ok": False, "text": "Replaces pancreatic enzymes", "at": [0, "pancreatic"]},
            {"type": "card", "x": 810, "y": 690, "w": 1300, "h": 180, "emoji": "🥩", "title": "Tenderize: 15 to 30 minutes",
             "body": "green papaya or its juice · longer = mushy", "at": [1, "tip"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "seeds", "title": "The Seeds", "emoji": "🖤", "dark": True, "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now, the seeds. Papaya's black seeds are edible, with a sharp flavor that's a bit like black pepper.", {}),
            ("H", "They contain compounds called benzyl isothiocyanate and carpaine.",
             {"say": "They contain compounds called benzil eye-so-thigh-oh-sigh-a-nate, and car-pa-een."}),
            ("P", "Seeds with a peppery attitude. I knew I'd like them.", {"mood": "happy"}),
        ], "els": [
            E("🌶️", 720, 260, 160, at=[0, "pepper"]),
            T("edible · peppery", 720, 400, 60, at=[0, "edible"], font="fredoka", weight=700, color="#FDE68A"),
            {"type": "card", "x": 450, "y": 620, "w": 560, "h": 150, "title": "Benzyl isothiocyanate", "at": [1, "benzyl"], **DARK},
            {"type": "card", "x": 1060, "y": 620, "w": 440, "h": 150, "title": "Carpaine", "at": [1, "carpaine"], **DARK},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "What we have: lab studies, and very small human studies, looked at activity against parasites, mainly intestinal worms. "
                  "Plus antibacterial activity, and kidney protection in animal models.", {}),
            ("H", "What's missing: no good-quality clinical research in people that backs these uses. And no established dose.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "🧫", "title": "What we have",
             "body": "lab, animal and tiny human studies", "at": [0, "have"], **DARK},
            {"type": "card", "x": 720, "y": 520, "w": 1000, "h": 190, "emoji": "❓", "title": "What's missing",
             "body": "good clinical trials · a dose", "at": [1, "missing"], **DARK},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "And the important caveats. Studies in rats and monkeys found a reversible drop in sperm motility, after high doses of papaya seed extract.", {}),
            ("H", "Whether that applies to people eating normal food amounts isn't proven. "
                  "But men trying to have children shouldn't eat large amounts.", {}),
            ("H", "Pregnant women should avoid papaya seeds and unripe green papaya. The latex has compounds linked to uterine contractions. "
                  "Ripe papaya is considered safe.", {}),
            ("H", "A reasonable amount to try: one teaspoon a day, about five to seven ground seeds. No more.", {}),
            ("P", "One teaspoon. Even I agree, and I'm pro-seed.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 760, "y": 200, "w": 1100, "h": 150, "emoji": "🐀", "title": "High-dose extract: sperm motility down",
             "at": 0, **DARK},
            {"type": "card", "x": 760, "y": 380, "w": 1100, "h": 150, "emoji": "👨", "title": "Trying for kids? Not large amounts",
             "at": [1, "children"], **DARK},
            {"type": "card", "x": 760, "y": 560, "w": 1100, "h": 150, "emoji": "🤰", "title": "Pregnancy: no seeds, no green papaya",
             "at": [2, "Pregnant"], **DARK},
            {"type": "banner", "x": 760, "y": 750, "text": "Max: 1 teaspoon a day", "color": "#F59E0B", "at": [3, "teaspoon"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "benefits", "title": "The Benefits", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Benefit one: vitamin C, sixty-eight percent of the daily value in a hundred grams. "
                  "It supports your immune system, collagen production, and it significantly boosts plant iron absorption in the same meal.", {}),
            ("H", "Benefit two: carotenoids that your body absorbs unusually well. Bioavailability studies showed papaya's lycopene "
                  "and beta-cryptoxanthin are absorbed better than from tomato or carrot.",
             {"say": "Benefit two: carotenoids that your body absorbs unusually well. Bioavailability studies showed papaya's lycopene "
                     "and beta crypto-zanthin are absorbed better than from tomato or carrot."}),
            ("H", "That's probably due to the structure of the chromoplasts, the color-holding parts of the fruit's cells.",
             {"say": "That's probably due to the structure of the chromo-plasts, the color holding parts of the fruit's cells."}),
        ], "els": [
            {"type": "ring", "x": 420, "y": 330, "r": 160, "value": 68, "color": "#F97316", "label": "vitamin C", "at": [0, "sixty"]},
            {"type": "pill", "x": 1060, "y": 230, "text": "immunity", "color": "green", "at": [0, "immune"]},
            {"type": "pill", "x": 1060, "y": 320, "text": "collagen", "color": "#0EA5E9", "at": [0, "collagen"]},
            {"type": "pill", "x": 1060, "y": 410, "text": "plant iron", "color": "#EF4444", "at": [0, "iron"]},
            {"type": "card", "x": 720, "y": 680, "w": 1100, "h": 190, "emoji": "🧡", "title": "Absorbed better than tomato, carrot",
             "body": "lycopene + beta-cryptoxanthin", "at": [1, "better"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Benefit three: low sugar for a tropical fruit, less than mango, pineapple or banana. "
                  "So it's a relatively good fit if you're watching your sugar.", {}),
            ("H", "Benefit four: fiber and a lot of water, which help keep things moving. "
                  "A small study found less constipation and bloating with a papaya-based preparation.", {}),
            ("H", "Plus folate, nine percent of the daily value, and a skin-friendly mix of vitamin C, vitamin A and beta-carotene.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 150, "emoji": "🍬", "title": "Less sugar than most tropical fruit", "at": 0},
            {"type": "card", "x": 720, "y": 400, "w": 1000, "h": 150, "emoji": "💧", "title": "Fiber + water",
             "body": "small study: less constipation, bloating", "at": [1, "fiber"]},
            {"type": "card", "x": 720, "y": 590, "w": 1000, "h": 150, "emoji": "🌿", "title": "Folate 9%", "at": [2, "folate"]},
            {"type": "card", "x": 720, "y": 760, "w": 1000, "h": 130, "emoji": "✨", "title": "Skin: C, A, beta-carotene", "at": [2, "skin"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch one: allergy. Papain is a known allergen. People with a latex allergy have a higher risk of cross-reacting to papaya, "
                  "avocado, banana and kiwi. It's called latex-fruit syndrome.", {}),
            ("H", "Catch two: pregnancy. Avoid green papaya and the seeds. Ripe fruit is considered safe.", {}),
            ("H", "Catch three: blood thinners. Papain may boost the effect of warfarin. "
                  "If you take blood thinners, ask before using papain supplements.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 230, "w": 1100, "h": 180, "emoji": "🧤", "title": "#1 Latex-fruit syndrome",
             "body": "papaya · avocado · banana · kiwi", "at": 0},
            {"type": "card", "x": 760, "y": 460, "w": 1100, "h": 180, "emoji": "🤰", "title": "#2 Pregnancy",
             "body": "no green papaya, no seeds", "at": 1},
            {"type": "card", "x": 760, "y": 690, "w": 1100, "h": 180, "emoji": "💊", "title": "#3 Warfarin",
             "body": "ask before papain supplements", "at": 2},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch four: the soap taste. Some people find ripe papaya smells or tastes unpleasant, like soap. "
                  "That comes from isothiocyanates, and the sensitivity is genetic. It's not a sign the fruit is spoiled. "
                  "A squeeze of lemon neutralizes most of it.",
             {"say": "Catch four: the soap taste. Some people find ripe papaya smells or tastes unpleasant, like soap. "
                     "That comes from eye-so-thigh-oh-sigh-a-nates, and the sensitivity is genetic. It's not a sign the fruit is spoiled. "
                     "A squeeze of lemon neutralizes most of it."}),
            ("H", "Catch five: way too much beta-carotene over time can cause carotenodermia, an orange tint to the skin. "
                  "It's harmless, and fully reversible.",
             {"say": "Catch five: way too much beta carotene over time can cause carot-en-o-dermia, an orange tint to the skin. "
                     "It's harmless, and fully reversible."}),
            ("H", "And six: it's still sugar. A big portion adds up, so people with diabetes should count it in their daily total.", {}),
            ("P", "Orange skin from fruit? I'm green and I'm fine with it.", {"mood": "smug", "jump": True}),
        ], "els": [
            {"type": "card", "x": 760, "y": 230, "w": 1100, "h": 180, "emoji": "🧼", "title": "#4 Soap taste: genetic",
             "body": "not spoiled · lemon helps", "at": 0},
            {"type": "card", "x": 760, "y": 460, "w": 1100, "h": 180, "emoji": "🟠", "title": "#5 Orange skin, if overdone",
             "body": "harmless and reversible", "at": 1},
            {"type": "card", "x": 760, "y": 690, "w": 1100, "h": 180, "emoji": "🍬", "title": "#6 Still sugar",
             "body": "diabetes: count it", "at": 2},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "How to Use It", "emoji": "🍋", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Picking a ripe one: the skin should be mostly yellow-orange, and give slightly to a gentle press. "
                  "A completely green fruit won't ripen well after picking.", {}),
            ("H", "Squeeze lemon over it. It neutralizes that typical smell, and adds even more vitamin C.", {}),
        ], "els": [
            T("Picking a ripe one", 750, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "card", "x": 450, "y": 330, "w": 560, "h": 200, "emoji": "🟡", "title": "Ripe", "body": "yellow-orange, soft", "at": [0, "yellow"], "fill": "#DCFCE7"},
            {"type": "card", "x": 1060, "y": 330, "w": 560, "h": 200, "emoji": "🟢", "title": "All green", "body": "won't ripen well", "at": [0, "green"], "fill": "#FEE2E2"},
            {"type": "card", "x": 750, "y": 640, "w": 1000, "h": 170, "emoji": "🍋", "title": "Add lemon", "body": "less smell, more vitamin C", "at": [1, "lemon"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Green papaya is used as a vegetable. It's grated into Thai salad, som tam, or cooked. That version is very low in sugar.",
             {"say": "Green papaya is used as a vegetable. It's grated into Thai salad, som tum, or cooked. That version is very low in sugar."}),
            ("H", "A smart pairing: eat papaya with plant iron sources, like lentils or tahini, so the vitamin C helps you absorb the iron.", {}),
            ("H", "And don't add it to gelatin. Papain breaks down gelatin's proteins, so it won't set. Same rule for pineapple.", {}),
            ("P", "Papaya jello is a soup. Noted.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 1000, "h": 160, "emoji": "🥗", "title": "Green papaya salad", "body": "som tam · very low sugar", "at": 0},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 160, "emoji": "🫘", "title": "Pair with plant iron", "body": "lentils, tahini", "at": [1, "lentils"]},
            {"type": "card", "x": 720, "y": 620, "w": 1000, "h": 160, "emoji": "🍮", "title": "Not in gelatin", "body": "it won't set · pineapple too", "at": [2, "gelatin"], "fill": "#FEE2E2"},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: papaya has more vitamin C than an orange, and carotenoids that are absorbed especially well.", {}),
            ("H", "Two: less sugar than most tropical fruits, at just forty-three calories per hundred grams.", {}),
            ("H", "Three: papain really works for tenderizing meat, but most health claims about it are exaggerated.", {}),
            ("H", "Four: try the seeds in moderation. And in pregnancy, skip the green fruit and the seeds.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "More vitamin C than an orange", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Low sugar: 43 calories per 100 g", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Papain: great on meat, overhyped otherwise", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Seeds in moderation · not in pregnancy", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So papaya: vitamin C champion, meat whisperer, and home to some very spicy seeds.", {"mood": "happy"}),
            ("H", "That's a fair summary, Pip.", {}),
            ("P", "Seed solidarity forever!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Squeeze some lemon on it!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article + sources: wiseplate.blog/food/papaya", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
