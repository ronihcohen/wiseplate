"""Pistachios explainer (English), based on https://wiseplate.blog/food/pistachios/

Numbers are the article's: raw (unroasted) pistachios per 100 g with % daily
value, a 30 g serving (about 49 kernels), and its raw vs dry-roasted vs
oil-roasted-and-salted comparison. Keep them in sync with
content/food/pistachios.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Pistachios: The Snack That Isn't a Nut?"
SLUG = "pistachios"
ARTICLE = "https://wiseplate.blog/food/pistachios/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "PISTACHIOS", "top_size": 160, "bottom": "NOT A NUT?", "bottom_size": 190,
         "badge": "49", "badge_label": "kernels in\none serving", "badge_color": "#16A34A",
         "scatter": "🥜", "hero": "🌰", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "nut":      {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "inside":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "powers":   {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "heart":    {"bpm": 96, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.6, "swing": 0.1},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "roast":    {"bpm": 112, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.7},
    "howmany":  {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#F7FEE7", "nut": "#FEF3C7", "inside": "#ECFDF5", "powers": "#E0F2FE",
    "heart": "#FFE4E6", "catches": "#FEE2E2", "roast": "#FFEDD5", "howmany": "#ECFCCB",
    "outro": "#F7FEE7",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hey! Pip here. Today's guest is small, green, and comes in a shell.", {"mood": "happy", "wave": True}),
            ("P", "Wait. Small and green? That's my whole brand! Pistachio, we need to talk.", {"mood": "surprised", "jump": True}),
        ], "els": [
            E("🥜", 960, 200, 150, at=[1, "Pistachio"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today it's pistachios: whether they're even a nut, what makes them special, "
                  "roasted versus raw, and how many to eat in a day.", {}),
            ("P", "Fine. But I'm still the original small green snack.", {"mood": "smug"}),
        ], "els": [
            E("🥜", 420, 330, 200, at=[0, "pistachios"], wobble=True),
            T("Pistachios", 640, 300, 120, at=[0, "pistachios"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🤔", "title": "Is it even a nut?", "at": [0, "nut"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🔥", "title": "Roasted or raw", "at": [0, "roasted"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "✋", "title": "How many a day", "at": [0, "many"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "nut", "title": "Is It Even a Nut?", "emoji": "🤔", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "The pistachio, Pistacia vera, has been grown in the Middle East and Central Asia for more than three thousand years.",
             {"say": "The pistachio, Pistacia vera, has been grown in the Middle East and Central Asia for more than three thousand years."}),
            ("H", "So, is it a nut? Botanically, no. It's the seed of a drupe, a stone fruit, in the same category as almonds, peaches and cherries. "
                  "What we eat is the kernel inside the pit.", {}),
            ("P", "A seed! I knew it. Welcome to the club, buddy.", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 820, "h": 150, "emoji": "🌳", "title": "Pistacia vera",
             "body": "grown for 3,000+ years", "at": [0, "Pistacia"], "italic_title": True},
            T("Botanically: a seed of a drupe", 720, 420, 56, at=[1, "drupe"], font="fredoka", weight=700, color="green"),
            E("🌰", 330, 600, 130, at=[1, "almonds"]),
            T("almond", 330, 700, 40, at=[1, "almonds"], font="fredoka", weight=600),
            E("🍑", 720, 600, 130, at=[1, "peaches"]),
            T("peach", 720, 700, 40, at=[1, "peaches"], font="fredoka", weight=600),
            E("🍒", 1110, 600, 130, at=[1, "cherries"]),
            T("cherry", 1110, 700, 40, at=[1, "cherries"], font="fredoka", weight=600),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "But nutritionally and in the kitchen, it's a nut in every way. And most importantly, for allergies it counts as a tree nut.", {}),
            ("H", "Pistachios belong to the same plant family as cashews and mango. That's why pistachio and cashew allergies often show up together.", {}),
        ], "els": [
            {"type": "check", "x": 180, "y": 200, "w": 1260, "ok": True, "text": "In the kitchen: a nut", "at": [0, "kitchen"]},
            {"type": "check", "x": 180, "y": 330, "w": 1260, "ok": True, "text": "For allergies: a tree nut", "at": [0, "allergies"]},
            T("One family:", 720, 500, 56, at=[1, "family"], font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 330, "y": 650, "w": 400, "h": 140, "emoji": "🥜", "title": "Pistachio", "at": [1, "family"]},
            {"type": "card", "x": 760, "y": 650, "w": 400, "h": 140, "emoji": "🌰", "title": "Cashew", "at": [1, "cashews"]},
            {"type": "card", "x": 1190, "y": 650, "w": 400, "h": 140, "emoji": "🥭", "title": "Mango", "at": [1, "mango."]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "inside", "title": "What's in a Handful?", "emoji": "🔬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "A practical serving is thirty grams. That's about forty-nine kernels.", {}),
            ("H", "It gives you one hundred fifty-nine calories, six grams of protein, thirteen grams of fat, and three grams of fiber.", {}),
            ("P", "Forty-nine kernels? I'd need a calculator. Or a very big hand.", {"mood": "surprised"}),
        ], "els": [
            T("1 serving = 30 g ≈ 49 kernels", 720, 170, 64, at=[0, "thirty"], font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 260, "y": 470, "w": 320, "h": 280, "value": 159, "unit": "", "label": "calories", "emoji": "🔥", "at": [1, "fifty"]},
            {"type": "stat", "x": 600, "y": 470, "w": 320, "h": 280, "value": 6, "unit": " g", "label": "protein", "emoji": "💪", "at": [1, "protein"]},
            {"type": "stat", "x": 940, "y": 470, "w": 320, "h": 280, "value": 13, "unit": " g", "label": "fat", "emoji": "🫒", "at": [1, "fat"]},
            {"type": "stat", "x": 1280, "y": 470, "w": 320, "h": 280, "value": 3, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [1, "fiber"]},
        ], "pip_hide": True},
        {"pip": PIP_S, "lines": [
            ("H", "Now zoom out to one hundred grams of raw pistachios, and look at the percent of the daily value.", {}),
            ("H", "Vitamin B6: one hundred thirty-one percent. Protein: forty. Phosphorus: thirty-nine. Fiber: thirty-eight. "
                  "Magnesium: twenty-nine. And potassium and iron, twenty-two each.", {}),
            ("P", "One hundred thirty-one percent of B6? Show-off.", {"mood": "smug"}),
        ], "els": [
            T("% Daily Value per 100 g (raw)", 760, 150, 54, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 250, "w": 1200, "row_h": 88, "max": 135, "rows": [
                {"label": "Vitamin B6", "value": 131, "color": "#8B5CF6", "at": [1, "B6"], "star": True},
                {"label": "Protein", "value": 40, "color": "#0EA5E9", "at": [1, "Protein"]},
                {"label": "Phosphorus", "value": 39, "color": "#14B8A6", "at": [1, "Phosphorus"]},
                {"label": "Fiber", "value": 38, "color": "#84CC16", "at": [1, "Fiber"]},
                {"label": "Magnesium", "value": 29, "color": "#F59E0B", "at": [1, "Magnesium"]},
                {"label": "Potassium", "value": 22, "color": "#F97316", "at": [1, "potassium"]},
                {"label": "Iron", "value": 22, "color": "#EF4444", "at": [1, "iron"]},
            ]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "powers", "title": "Pistachio Superpowers", "emoji": "⭐", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Superpower one: you get the most pieces per serving. Thirty grams is about forty-nine pistachios, "
                  "compared with about twenty-three almonds, or fourteen walnut halves.", {}),
            ("H", "Eating forty-nine things feels very different from eating fourteen. That really helps when you're managing snacks.", {}),
        ], "els": [
            T("Pieces in a 30 g serving", 760, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 300, "w": 1200, "row_h": 120, "max": 49, "unit": "", "rows": [
                {"label": "Pistachios", "value": 49, "color": "#16A34A", "at": [0, "forty"], "star": True},
                {"label": "Almonds", "value": 23, "color": "#F59E0B", "at": [0, "almonds"]},
                {"label": "Walnut halves", "value": 14, "color": "#94A3B8", "at": [0, "walnut"]},
            ]},
            {"type": "pill", "x": 760, "y": 720, "text": "more pieces, more satisfying", "color": "ok", "at": [1, "feels"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Superpower two: complete protein. Pistachios are one of the few plant sources with all nine essential amino acids, "
                  "in amounts that are enough for adults. And with twenty grams of protein per hundred grams, they're one of the most protein-rich nuts.", {}),
            ("H", "Superpower three: vitamin B6, the highest of all nuts. B6 is needed to process amino acids, make neurotransmitters, "
                  "and keep the immune system working.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "🧬", "title": "Complete protein",
             "body": "all 9 essential amino acids · 20 g per 100 g", "at": [0, "complete"]},
            {"type": "card", "x": 720, "y": 520, "w": 1000, "h": 190, "emoji": "⚡", "title": "Most vitamin B6 of any nut",
             "body": "amino acids · brain messengers · immunity", "at": [1, "B6"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Superpower four: lutein and zeaxanthin. Pistachios are the richest nut in these two carotenoids, "
                  "and they're what gives pistachios their greenish color.",
             {"say": "Superpower four: lutein and zee-uh-zanthin. Pistachios are the richest nut in these two carotenoids, "
                     "and they're what gives pistachios their greenish color."}),
            ("H", "Both build up in the retina of the eye, and they're linked with protection against age-related macular degeneration.", {}),
            ("P", "Wait. The green comes from eye vitamins? So I'm green for... style reasons only?", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "💚", "title": "Lutein + zeaxanthin",
             "body": "richest nut · the source of the green color", "at": [0, "lutein"]},
            {"type": "card", "x": 720, "y": 520, "w": 1000, "h": 190, "emoji": "👁️", "title": "Build up in the retina",
             "body": "linked to macular protection", "at": [1, "retina"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "heart", "title": "Heart and Blood Sugar", "emoji": "❤️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Heart health: controlled studies found that swapping other snacks for pistachios was linked to lower L D L, "
                  "and better function of the blood vessel lining, called the endothelium.",
             {"say": "Heart health: controlled studies found that swapping other snacks for pistachios was linked to lower L D L, "
                     "and better function of the blood vessel lining, called the endo-theelium."}),
            ("H", "Pistachios also have phytosterols, which compete with cholesterol for absorption in the gut.", {}),
        ], "els": [
            T("Heart health", 720, 120, 60, at=0, font="fredoka", weight=600, color="green"),
            {"type": "check", "x": 180, "y": 220, "w": 1260, "ok": True, "text": "Lower LDL", "at": [0, "L"]},
            {"type": "check", "x": 180, "y": 350, "w": 1260, "ok": True, "text": "Better blood vessel lining", "at": [0, "lining"]},
            {"type": "card", "x": 720, "y": 600, "w": 1000, "h": 180, "emoji": "🌿", "title": "Phytosterols",
             "body": "compete with cholesterol in the gut", "at": [1, "phytosterols"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Blood sugar: pistachios barely raise it. And studies found that adding them to a carb-heavy meal "
                  "lowers the blood sugar response to the whole meal.", {}),
            ("H", "They also have ten point six grams of fiber per hundred grams, and some of it feeds helpful gut bacteria.", {}),
            ("P", "Pistachios, calming down your bread. Respect.", {"mood": "happy"}),
        ], "els": [
            T("Blood sugar", 720, 160, 60, at=0, font="fredoka", weight=600, color="green"),
            E("🍞", 400, 330, 160, at=[0, "carb"]),
            T("+", 600, 330, 110, at=[0, "adding"], font="fredoka", weight=700, color="orange"),
            E("🥜", 800, 330, 160, at=[0, "adding"]),
            {"type": "banner", "x": 1150, "y": 330, "text": "Gentler spike", "color": "#16A34A", "at": [0, "lowers"]},
            {"type": "card", "x": 720, "y": 620, "w": 1000, "h": 180, "emoji": "🦠", "title": "10.6 g fiber per 100 g",
             "body": "some of it feeds good gut bacteria", "at": [1, "fiber"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch one: calories. Five hundred sixty per hundred grams. Handful after handful in front of the TV, "
                  "and you're at four hundred calories without noticing. The fix is simple: measure a portion, don't eat from the bag.", {}),
            ("H", "Catch two: salt. Salted pistachios often have four to five hundred milligrams of sodium per hundred grams, sometimes much more. "
                  "If you're managing blood pressure, choose unsalted.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "📺", "title": "#1 Calories: 560 per 100 g",
             "body": "measure a portion, skip the bag", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🧂", "title": "#2 Salt: 400 to 500+ mg",
             "body": "per 100 g salted · choose unsalted", "at": 1},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch three: aflatoxins. Pistachios are among the foods most prone to an Aspergillus mold that makes aflatoxins, "
                  "toxins classified as known human carcinogens, which also harm the liver.",
             {"say": "Catch three: afla-toxins. Pistachios are among the foods most prone to an Aspergillus mold that makes afla-toxins, "
                     "toxins classified as known human carcinogens, which also harm the liver."}),
            ("H", "The risk is well managed in regulated imports. Still, skip pistachios that taste musty or bitter, or show visible mold. "
                  "Store them somewhere cool and dry, ideally in the fridge.", {}),
        ], "els": [
            T("#3 Aflatoxins", 760, 160, 76, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 760, "y": 360, "w": 1100, "h": 170, "emoji": "🍄", "title": "Aspergillus mold",
             "body": "known carcinogen · harms the liver", "at": [0, "Aspergillus"]},
            {"type": "pill", "x": 760, "y": 600, "text": "well managed in regulated imports", "color": "ok", "at": [1, "managed"]},
            {"type": "pill", "x": 760, "y": 700, "text": "musty, bitter, moldy? toss it", "color": "orange", "at": [1, "musty"]},
            {"type": "pill", "x": 760, "y": 800, "text": "store cool, dry, ideally fridge", "color": "green", "at": [1, "cool"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch four: FODMAPs. Pistachios are high in fructans, which can be a problem with irritable bowel syndrome. "
                  "The tolerated portion is small, only about fifteen grams.",
             {"say": "Catch four: fod-maps. Pistachios are high in fructans, which can be a problem with irritable bowel syndrome. "
                     "The tolerated portion is small, only about fifteen grams."}),
            ("H", "Catch five: allergy, often together with cashew, and reactions can be severe. "
                  "Catch six: potassium, one thousand twenty-five milligrams per hundred grams. With kidney disease and a potassium limit, ask about the amount.", {}),
            ("H", "And seven: pistachios used to be dyed red to hide flaws. That's rare today, but heavily brined pistachios are still common.", {}),
            ("P", "Dyed red? To hide flaws? Pip has no flaws. Pip has character.", {"mood": "smug", "jump": True}),
        ], "els": [
            {"type": "card", "x": 760, "y": 200, "w": 1100, "h": 150, "emoji": "🎈", "title": "#4 FODMAPs: IBS limit ~15 g", "at": 0},
            {"type": "card", "x": 760, "y": 380, "w": 1100, "h": 150, "emoji": "🚫", "title": "#5 Allergy, often with cashew", "at": [1, "allergy"]},
            {"type": "card", "x": 760, "y": 560, "w": 1100, "h": 150, "emoji": "🍌", "title": "#6 Potassium: kidney limits", "at": [1, "potassium"]},
            {"type": "card", "x": 760, "y": 740, "w": 1100, "h": 150, "emoji": "🔴", "title": "#7 Red dye, heavy brine", "at": [2, "dyed"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "roast", "title": "Roasted or Raw?", "emoji": "🔥", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Roasted or raw? The nutrition difference is much smaller than people think.", {}),
            ("H", "Calories: about five hundred sixty raw, about five hundred seventy dry roasted, and five hundred ninety or more when roasted in oil and salted.", {}),
            ("H", "Sodium: about one milligram raw, about one milligram dry roasted without salt, and four to five hundred or more in the oil-roasted, salted kind.", {}),
        ], "els": [
            T("Per 100 g", 760, 140, 52, at=0, font="fredoka", weight=600, color="green"),
            T("Calories", 760, 230, 50, at=[1, "Calories"], font="fredoka", weight=700, color="ink"),
            {"type": "stat", "x": 340, "y": 400, "w": 400, "h": 250, "value": 560, "unit": "", "label": "raw", "emoji": "", "at": [1, "raw,"]},
            {"type": "stat", "x": 760, "y": 400, "w": 400, "h": 250, "value": 570, "unit": "", "label": "dry roasted", "emoji": "", "at": [1, "dry"]},
            {"type": "stat", "x": 1180, "y": 400, "w": 400, "h": 250, "value": 590, "unit": "+", "label": "oil + salt", "emoji": "", "at": [1, "oil"]},
            T("Sodium", 760, 600, 50, at=[2, "Sodium"], font="fredoka", weight=700, color="ink"),
            {"type": "pill", "x": 340, "y": 700, "text": "~1 mg", "color": "ok", "at": [2, "raw,"]},
            {"type": "pill", "x": 760, "y": 700, "text": "~1 mg", "color": "ok", "at": [2, "dry"]},
            {"type": "pill", "x": 1180, "y": 700, "text": "400 to 500+ mg", "color": "red", "at": [2, "oil"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Dry roasting without salt barely touches the nutrition. It slightly lowers the heat-sensitive antioxidants, "
                  "and improves the flavor and digestibility.", {}),
            ("H", "So the problem isn't roasting. It's the salt and oil that come with it. "
                  "Plus, roasting has a small upside: the heat neutralizes some mold, and extends shelf life.", {}),
            ("P", "So roasting is fine. Salt is the villain. Plot twist!", {"mood": "surprised", "jump": True}),
        ], "els": [
            {"type": "card", "x": 720, "y": 250, "w": 1000, "h": 180, "emoji": "🔥", "title": "Dry roasted, no salt: great",
             "body": "slightly fewer antioxidants · better flavor", "at": [0, "barely"], "fill": "#DCFCE7"},
            {"type": "banner", "x": 720, "y": 510, "text": "The problem: salt + oil", "color": "#DC2626", "at": [1, "salt"]},
            {"type": "pill", "x": 720, "y": 680, "text": "bonus: less mold, longer shelf life", "color": "ok", "at": [1, "mold"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howmany", "title": "How Many a Day?", "emoji": "✋", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "So how many? The usual serving is thirty grams a day, about forty-nine shelled kernels, around one hundred sixty calories. "
                  "That's the amount used in most of the clinical studies.", {}),
            ("H", "Watching your weight? Up to thirty grams, instead of another snack, not on top of it. "
                  "Athletes, or people on higher-calorie diets: forty-five to sixty grams is perfectly reasonable.", {}),
            ("H", "With irritable bowel syndrome, keep it to about fifteen grams. And with high blood pressure, no special limit, but unsalted only.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 200, "w": 1100, "h": 140, "emoji": "✋", "title": "Usual: 30 g ≈ 49 kernels", "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 760, "y": 370, "w": 1100, "h": 140, "emoji": "⚖️", "title": "Weight: up to 30 g, as a swap", "at": [1, "weight"]},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 140, "emoji": "🏃", "title": "Athletes: 45 to 60 g", "at": [1, "Athletes"]},
            {"type": "card", "x": 760, "y": 710, "w": 1100, "h": 140, "emoji": "🎈", "title": "IBS ~15 g · high BP: unsalted", "at": [2, "irritable"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And here's a trick that works, the pistachio principle. In one study, people who ate pistachios in the shell "
                  "ate about forty-one percent fewer calories than people eating shelled kernels.", {}),
            ("H", "The pile of empty shells on your plate shows how much you've eaten, and cracking them slows you down.", {}),
            ("P", "Shells as a scoreboard. Genius.", {"mood": "happy", "jump": True}),
        ], "els": [
            T("The pistachio principle", 720, 180, 80, at=0, font="fredoka", weight=700, color="green"),
            {"type": "ring", "x": 420, "y": 500, "r": 170, "value": 41, "color": "#16A34A", "label": "fewer calories", "at": [0, "forty"]},
            {"type": "card", "x": 1030, "y": 420, "w": 580, "h": 150, "emoji": "🐚", "title": "Shell pile", "body": "shows what you ate", "at": [1, "pile"]},
            {"type": "card", "x": 1030, "y": 620, "w": 580, "h": 150, "emoji": "🐢", "title": "Cracking", "body": "slows you down", "at": [1, "cracking"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "In the kitchen: snack on them in the shell. Grind them as a crust for fish or chicken, instead of breadcrumbs. "
                  "Add them to salads and granola.", {}),
            ("H", "They're also in Middle Eastern desserts like baklava, knafeh and malabi, though there they come with lots of sugar. "
                  "And for pistachio butter, check for added sugar and palm oil.",
             {"say": "They're also in Middle Eastern desserts like baklava, ka-nafeh and malabi, though there they come with lots of sugar. "
                     "And for pistachio butter, check for added sugar and palm oil."}),
        ], "els": [
            T("In the kitchen", 720, 150, 60, at=0, font="fredoka", weight=600, color="green"),
            E("🐟", 300, 300, 140, at=[0, "crust"]),
            T("crust", 300, 410, 42, at=[0, "crust"], font="fredoka", weight=600),
            E("🥗", 620, 300, 140, at=[0, "salads"]),
            T("salads", 620, 410, 42, at=[0, "salads"], font="fredoka", weight=600),
            E("🥣", 940, 300, 140, at=[0, "granola"]),
            T("granola", 940, 410, 42, at=[0, "granola"], font="fredoka", weight=600),
            E("🍰", 1260, 300, 140, at=[1, "baklava"]),
            T("desserts", 1260, 410, 42, at=[1, "baklava"], font="fredoka", weight=600),
            {"type": "card", "x": 780, "y": 660, "w": 1100, "h": 170, "emoji": "🫙", "title": "Pistachio butter",
             "body": "check for added sugar and palm oil", "at": [1, "butter"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: pistachios bring complete protein, tons of vitamin B6, eye-friendly lutein, and a low glycemic load.", {}),
            ("H", "Two: botanically a seed, but for allergies, a tree nut.", {}),
            ("H", "Three: buy unsalted. Salt, not roasting, is what makes them a problem snack.", {}),
            ("H", "Four: eat them in the shell. Thirty grams a day is the sweet spot.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Complete protein, B6, lutein", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "A seed, but a tree nut for allergies", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Unsalted: salt is the problem", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "In the shell, about 30 g a day", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "Okay, pistachio. You're green, you're a seed, you're great. You can stay.", {"mood": "happy"}),
            ("H", "Very generous, Pip.", {}),
            ("P", "Small green snacks, unite!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Keep your shells!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article + sources: wiseplate.blog/food/pistachios", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
