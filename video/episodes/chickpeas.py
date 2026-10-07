"""Chickpeas explainer (English), based on https://wiseplate.blog/food/chickpeas/

Numbers are the article's: cooked chickpeas without salt per 100 g (USDA FDC
173757) with % daily value, its protein-by-form table, and hummus spread values
(per 100 g and a ~200 g restaurant plate). Keep them in sync with
content/food/chickpeas.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Chickpeas: Carb or Protein?"
SLUG = "chickpeas"
ARTICLE = "https://wiseplate.blog/food/chickpeas/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "CHICKPEAS", "top_size": 170, "bottom": "CARB OR PROTEIN?", "bottom_size": 120,
         "badge": "27 / 9", "badge_size": 100, "badge_label": "g carbs / protein\nper 100 g", "badge_color": "#0EA5E9",
         "scatter": "🫘", "hero": "🧆", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "carb":     {"bpm": 104, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.65, "swing": 0.15},
    "protein":  {"bpm": 116, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.8, "bright": 1.3},
    "inside":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "benefits": {"bpm": 100, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.6, "swing": 0.1},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "gas":      {"bpm": 120, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.8, "swing": 0.2},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF7ED", "carb": "#FEF3C7", "protein": "#E0F2FE", "inside": "#ECFDF5",
    "benefits": "#ECFCCB", "catches": "#FEE2E2", "gas": "#F5F3FF", "outro": "#FFF7ED",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hey everyone, Pip the pumpkin seed here! Today's guest is round, beige, and famous worldwide.", {"mood": "happy", "wave": True}),
            ("P", "Give it up for the chickpea!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🫘", 960, 200, 160, at=[1, "chickpea"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today it's chickpeas. We'll answer the question everyone searches for, is it a carb or a protein? "
                  "Then what's inside, the benefits, and how to stop the gas.", {}),
            ("P", "The gas. Of course there's a gas chapter.", {"mood": "worried"}),
            ("H", "There is. Let's dig in.", {}),
        ], "els": [
            E("🫘", 420, 330, 200, at=[0, "chickpeas"], wobble=True),
            T("Chickpeas", 640, 300, 120, at=[0, "chickpeas"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "❓", "title": "Carb or protein?", "at": [0, "carb"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "⭐", "title": "The benefits", "at": [0, "benefits"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "💨", "title": "Stopping the gas", "at": [0, "gas"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "carb", "title": "Carb or Protein?", "emoji": "❓", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "The short answer: both. Chickpeas are a legume with carbs and protein.", {}),
            ("H", "One hundred grams of cooked chickpeas, without salt, has about twenty-seven point four grams of carbs, "
                  "and eight point nine grams of protein. So by weight, there are more carbs than protein.", {}),
            ("H", "Of those carbs, seven point six grams are fiber. The fiber is already counted inside the carbs, not added on top. "
                  "Take it out, and you're left with about nineteen point eight grams.", {}),
        ], "els": [
            {"type": "banner", "x": 760, "y": 160, "text": "Both!", "color": "#16A34A", "at": [0, "both"]},
            T("Cooked, no salt, per 100 g (USDA)", 760, 260, 44, at=[1, "cooked"], color="muted"),
            {"type": "bars", "x": 200, "y": 380, "w": 1200, "row_h": 110, "max": 28, "unit": " g", "rows": [
                {"label": "Carbs", "value": 27.4, "decimals": 1, "color": "#F59E0B", "at": [1, "carbs,"]},
                {"label": "Protein", "value": 8.9, "decimals": 1, "color": "#0EA5E9", "at": [1, "protein."]},
                {"label": "Fat", "value": 2.6, "decimals": 1, "color": "#94A3B8", "at": [1, "weight"]},
                {"label": "Fiber", "value": 7.6, "decimals": 1, "color": "#16A34A", "at": [2, "fiber"]},
            ]},
            {"type": "pill", "x": 760, "y": 850, "text": "fiber is part of the carbs · the rest ≈ 19.8 g", "color": "orange", "at": [2, "nineteen"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "A quick word on names. The plant is Cicer arietinum. In English, they're chickpeas, or garbanzo beans.",
             {"say": "A quick word on names. The plant is Sisser airy-et-eye-num. In English, they're chickpeas, or garbanzo beans."}),
            ("H", "Hummus is the spread made from them, with tahini, and sometimes olive oil, lemon and garlic. "
                  "Its numbers depend on the recipe, so it's important to keep the beans and the spread apart.", {}),
            ("P", "Beans and dip are different foods? My mind is blown.", {"mood": "surprised", "jump": True}),
        ], "els": [
            {"type": "card", "x": 440, "y": 270, "w": 580, "h": 190, "emoji": "🫘", "title": "Chickpeas",
             "body": "Cicer arietinum · garbanzo beans", "at": [0, "chickpeas,"]},
            {"type": "card", "x": 1060, "y": 270, "w": 580, "h": 190, "emoji": "🥣", "title": "Hummus",
             "body": "the spread", "at": [1, "Hummus"]},
            T("+ tahini, olive oil, lemon, garlic", 1060, 440, 38, at=[1, "tahini"], color="muted"),
            {"type": "banner", "x": 750, "y": 640, "text": "Beans and spread are different foods", "color": "#F97316", "at": [1, "apart"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "protein", "title": "Protein in Every Form", "emoji": "💪", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "How much protein you get depends on the form. Per hundred grams: dry chickpeas, before cooking, have nineteen to twenty grams. "
                  "They soak up water and double in weight, so cooked chickpeas have eight point nine.", {}),
            ("H", "Canned and drained: seven to eight grams, with more sodium. Hummus spread: seven point nine. "
                  "Chickpea flour, the base for pancakes and falafel: twenty-two. And aquafaba, the liquid in the can: only about one gram.",
             {"say": "Canned and drained: seven to eight grams, with more sodium. Hummus spread: seven point nine. "
                     "Chickpea flour, the base for pancakes and falafel: twenty-two. And aqua-fabba, the liquid in the can: only about one gram."}),
        ], "els": [
            T("Protein per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 260, "w": 1200, "row_h": 100, "max": 22, "unit": " g", "rows": [
                {"label": "Dry", "value": 20, "text": "19 to 20 g", "color": "#B45309", "at": [0, "dry"]},
                {"label": "Cooked", "value": 8.9, "decimals": 1, "color": "#16A34A", "at": [0, "cooked"], "star": True},
                {"label": "Canned", "value": 8, "text": "7 to 8 g", "color": "#0EA5E9", "at": [1, "Canned"]},
                {"label": "Hummus", "value": 7.9, "decimals": 1, "color": "#F59E0B", "at": [1, "Hummus"]},
                {"label": "Flour", "value": 22, "color": "#8B5CF6", "at": [1, "flour"]},
                {"label": "Aquafaba", "value": 1, "text": "~1 g", "color": "#94A3B8", "at": [1, "aquafaba"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Now the restaurant plate. About two hundred grams of hummus gives around sixteen grams of protein. "
                  "But also about four hundred sixty calories and twenty-eight grams of fat, mostly from the tahini and olive oil.", {}),
            ("H", "It's good-quality fat. But that plate is not a light meal.", {}),
            ("P", "Four hundred sixty calories? I need to sit down. With pita.", {"mood": "surprised"}),
        ], "els": [
            E("🍽️", 720, 230, 160, at=0),
            T("Hummus plate, ~200 g", 720, 360, 56, at=0, font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 300, "y": 600, "w": 380, "h": 280, "value": 16, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "sixteen"], "color": "ok"},
            {"type": "stat", "x": 720, "y": 600, "w": 380, "h": 280, "value": 460, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "sixty"], "color": "orange"},
            {"type": "stat", "x": 1140, "y": 600, "w": 380, "h": 280, "value": 28, "unit": " g", "label": "fat", "emoji": "🫒", "at": [0, "fat,"], "color": "orange"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "What about protein quality? Chickpea protein is relatively low in the amino acid methionine, and rich in lysine. "
                  "Grains are the exact opposite.",
             {"say": "What about protein quality? Chickpea protein is relatively low in the amino acid meth-eye-oh-neen, and rich in lysine. "
                     "Grains are the exact opposite."}),
            ("H", "So hummus with pita or bread isn't just tradition. Together, they make a complete amino acid profile. "
                  "And they don't even have to be in the same meal. Over the day is enough.", {}),
        ], "els": [
            {"type": "card", "x": 440, "y": 270, "w": 580, "h": 190, "emoji": "🫘", "title": "Chickpeas",
             "body": "low methionine · high lysine", "at": [0, "methionine"]},
            {"type": "card", "x": 1060, "y": 270, "w": 580, "h": 190, "emoji": "🫓", "title": "Grains",
             "body": "the exact opposite", "at": [0, "Grains"]},
            {"type": "banner", "x": 750, "y": 530, "text": "Together: complete protein", "color": "#16A34A", "at": [1, "complete"]},
            {"type": "pill", "x": 750, "y": 700, "text": "across the day is enough", "color": "ok", "at": [1, "day"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "inside", "title": "What Else Is Inside?", "emoji": "🔬", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "One hundred grams of cooked chickpeas has one hundred sixty-four calories. Here's the percent of the daily value.", {}),
            ("H", "Folate and manganese, forty-three percent each. Copper, thirty-nine. Fiber, twenty-seven. Protein, eighteen. "
                  "Iron, sixteen. Zinc, fourteen. And magnesium, eleven.", {}),
            ("P", "Folate and manganese tied for first? Awkward podium.", {"mood": "smug"}),
        ], "els": [
            T("% Daily Value · 100 g cooked · 164 kcal", 760, 150, 50, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 240, "w": 1200, "row_h": 82, "max": 45, "rows": [
                {"label": "Folate", "value": 43, "color": "#16A34A", "at": [1, "Folate"], "star": True},
                {"label": "Manganese", "value": 43, "color": "#8B5CF6", "at": [1, "manganese"]},
                {"label": "Copper", "value": 39, "color": "#B45309", "at": [1, "Copper"]},
                {"label": "Fiber", "value": 27, "color": "#84CC16", "at": [1, "Fiber"]},
                {"label": "Protein", "value": 18, "color": "#0EA5E9", "at": [1, "Protein"]},
                {"label": "Iron", "value": 16, "color": "#EF4444", "at": [1, "Iron"]},
                {"label": "Zinc", "value": 14, "color": "#F59E0B", "at": [1, "Zinc"]},
                {"label": "Magnesium", "value": 11, "color": "#14B8A6", "at": [1, "magnesium"]},
            ]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "benefits", "title": "The Benefits", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Benefit one: fullness. The protein and fiber combo makes chickpeas one of the most filling foods for their calories.", {}),
            ("H", "Studies on legumes even found people ate fewer calories at the next meal. It's called the second meal effect.", {}),
            ("P", "A food that works on your next meal too? That's overtime.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 270, "w": 1000, "h": 180, "emoji": "😌", "title": "Very filling",
             "body": "protein + fiber, per calorie", "at": [0, "fullness"]},
            {"type": "card", "x": 720, "y": 530, "w": 1000, "h": 180, "emoji": "🍽️", "title": "The second meal effect",
             "body": "fewer calories at the next meal", "at": [1, "second"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Benefit two: blood sugar. The glycemic index of chickpeas is about twenty-eight, one of the lowest for a carb-rich food. "
                  "That's why they're recommended for diabetes and prediabetes.", {}),
            ("H", "Benefit three: folate. Forty-three percent of the daily value in one serving, which matters especially in pregnancy, and when planning one.", {}),
        ], "els": [
            {"type": "stat", "x": 440, "y": 360, "w": 520, "h": 330, "value": 28, "unit": "", "label": "glycemic index", "emoji": "📉", "at": [0, "twenty"], "color": "ok"},
            T("one of the lowest for carb-rich foods", 440, 600, 36, at=[0, "lowest"], color="muted"),
            {"type": "stat", "x": 1060, "y": 360, "w": 520, "h": 330, "value": 43, "unit": "%", "label": "folate, daily value", "emoji": "🤰", "at": [1, "folate"]},
            T("key in pregnancy", 1060, 600, 36, at=[1, "pregnancy"], color="muted"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Benefit four: resistant starch. Some of the starch in chickpeas isn't digested in the small intestine. "
                  "It reaches the colon, where it feeds bacteria that make butyrate.",
             {"say": "Benefit four: resistant starch. Some of the starch in chickpeas isn't digested in the small intestine. "
                     "It reaches the colon, where it feeds bacteria that make byoo-tuh-rate."}),
            ("H", "Butyrate is a short-chain fatty acid that feeds the cells lining your gut, and it has anti-inflammatory activity.",
             {"say": "Byoo-tuh-rate is a short chain fatty acid that feeds the cells lining your gut, and it has anti-inflammatory activity."}),
            ("H", "And benefit five: cholesterol. Systematic reviews of legume studies found a small but consistent drop in L D L with regular eating, "
                  "credited to the soluble fiber.",
             {"say": "And benefit five: cholesterol. Systematic reviews of legume studies found a small but consistent drop in L D L with regular eating, "
                     "credited to the soluble fiber."}),
        ], "els": [
            {"type": "card", "x": 340, "y": 270, "w": 420, "h": 160, "emoji": "🫘", "title": "Resistant starch", "at": [0, "resistant"]},
            {"type": "arrow", "x1": 560, "y1": 270, "x2": 680, "y2": 270, "at": [0, "colon"]},
            {"type": "card", "x": 900, "y": 270, "w": 400, "h": 160, "emoji": "🦠", "title": "Gut bacteria", "at": [0, "bacteria"]},
            {"type": "arrow", "x1": 1110, "y1": 270, "x2": 1180, "y2": 270, "at": [0, "butyrate."]},
            {"type": "card", "x": 900, "y": 470, "w": 560, "h": 160, "emoji": "✨", "title": "Butyrate", "body": "feeds gut lining · calms inflammation", "at": [1, "Butyrate"]},
            {"type": "check", "x": 160, "y": 720, "w": 1300, "ok": True, "text": "LDL: small but consistent drop", "at": [2, "L"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch one, the most common: gas and bloating. Chickpeas contain oligosaccharides, raffinose and stachyose, "
                  "that your small intestine can't break down.",
             {"say": "Catch one, the most common: gas and bloating. Chickpeas contain oligo-saccharides, raffinose and stack-ee-ose, "
                     "that your small intestine can't break down."}),
            ("H", "They reach the colon, bacteria ferment them, and the result is gas. The good news: the fixes work, and we'll get to them.", {}),
            ("P", "Fermenting in the colon. That's a sentence I didn't need today.", {"mood": "worried"}),
        ], "els": [
            T("#1 Gas", 760, 160, 80, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 760, "y": 360, "w": 1100, "h": 180, "emoji": "🧬", "title": "Oligosaccharides",
             "body": "raffinose, stachyose · not digested", "at": [0, "oligosaccharides"]},
            {"type": "card", "x": 760, "y": 600, "w": 1100, "h": 180, "emoji": "💨", "title": "Fermented in the colon = gas",
             "at": [1, "ferment"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch two: phytic acid, which binds iron, zinc and calcium and reduces their absorption. "
                  "Soaking and cooking cut it a lot, and a vitamin C source like lemon offsets the effect on iron.", {}),
            ("H", "Catch three: FODMAPs. Chickpeas are a problem food for irritable bowel syndrome. "
                  "About forty grams of well-drained canned chickpeas is usually tolerated.",
             {"say": "Catch three: fod-maps. Chickpeas are a problem food for irritable bowel syndrome. "
                     "About forty grams of well drained canned chickpeas is usually tolerated."}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "🔒", "title": "#2 Phytic acid",
             "body": "soak, cook, and add lemon", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🎈", "title": "#3 FODMAPs: IBS ~40 g canned",
             "body": "drained well", "at": 1},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch four: sodium. Canned chickpeas often have two hundred fifty to four hundred milligrams per hundred grams. "
                  "Draining and rinsing removes about forty percent. Store-bought hummus often has cheap oils and preservatives too.", {}),
            ("H", "Catch five: spread calories. Chickpeas are one hundred sixty-four calories per hundred grams, hummus spread is two hundred thirty. "
                  "Nearly all the difference is olive oil and tahini.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 240, "w": 1100, "h": 180, "emoji": "🧂", "title": "#4 Canned: 250 to 400 mg sodium",
             "body": "rinse: about 40% less", "at": 0},
            T("#5 Calories per 100 g", 760, 500, 56, at=1, font="fredoka", weight=700, color="red"),
            {"type": "bars", "x": 200, "y": 610, "w": 1200, "row_h": 110, "max": 240, "unit": "", "rows": [
                {"label": "Chickpeas", "value": 164, "color": "#16A34A", "at": [1, "sixty"]},
                {"label": "Hummus", "value": 230, "color": "#F97316", "at": [1, "thirty"]},
            ]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch six: lectins. Dry chickpeas that aren't fully cooked contain lectins that can upset digestion. "
                  "Full cooking neutralizes them. Never eat soaked chickpeas without cooking them.", {}),
            ("H", "And an important clarification about favism. People with G six P D deficiency need to avoid fava beans, not chickpeas. "
                  "But a few isolated cases of sensitivity to chickpeas have been reported, so caution and advice are usually recommended.",
             {"say": "And an important clarification about favism. People with G 6 P D deficiency need to avoid fava beans, not chickpeas. "
                     "But a few isolated cases of sensitivity to chickpeas have been reported, so caution and advice are usually recommended."}),
            ("P", "Cook them fully, and check with a pro if you have G six P D. Got it.", {"mood": "happy",
             "say": "Cook them fully, and check with a pro if you have G 6 P D. Got it."}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "🍲", "title": "#6 Lectins: cook fully",
             "body": "never eat soaked, uncooked chickpeas", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🩺", "title": "G6PD: avoid fava, not chickpeas",
             "body": "rare reports, so ask a professional", "at": [1, "fava"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "gas", "title": "Beat the Gas", "emoji": "💨", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Here's how to beat the gas. These steps work, and they add up.", {}),
            ("H", "One: soak for eight to twelve hours at room temperature, and change the water at least once. "
                  "A lot of the gassy sugars dissolve into the water.", {}),
            ("H", "Two: pour out the soaking water and cook in fresh water. This is the step most people skip.", {}),
            ("H", "Three: a teaspoon of baking soda in the soaking water softens the beans and shortens cooking. "
                  "Four: cook them long and fully, until completely soft. A bean that stays hard digests poorly.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 210, "w": 1300, "ok": True, "text": "1. Soak 8 to 12 hours, change the water", "at": [1, "soak"]},
            {"type": "check", "x": 160, "y": 340, "w": 1300, "ok": True, "text": "2. Pour it out, cook in fresh water", "at": [2, "pour"]},
            {"type": "check", "x": 160, "y": 470, "w": 1300, "ok": True, "text": "3. A teaspoon of baking soda", "at": [3, "baking"]},
            {"type": "check", "x": 160, "y": 600, "w": 1300, "ok": True, "text": "4. Cook until completely soft", "at": [3, "Four"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Five: peel off the skins after cooking. It's a chore, but it really improves both the hummus texture and how well you tolerate it.", {}),
            ("H", "Six: season with cumin. It's a traditional gas remedy, and the effect is probably real.", {}),
            ("H", "And seven: build up slowly. Eating legumes regularly changes your gut bacteria, and symptoms drop a lot within weeks. "
                  "People who rarely eat legumes suffer the most.", {}),
            ("P", "So the secret is practice. Your gut needs training, like a tiny gym.", {"mood": "smug", "jump": True}),
        ], "els": [
            {"type": "check", "x": 160, "y": 210, "w": 1300, "ok": True, "text": "5. Peel the skins", "at": [0, "peel"]},
            {"type": "check", "x": 160, "y": 340, "w": 1300, "ok": True, "text": "6. Season with cumin", "at": [1, "cumin"]},
            {"type": "check", "x": 160, "y": 470, "w": 1300, "ok": True, "text": "7. Build up slowly, eat them often", "at": [2, "slowly"]},
            {"type": "banner", "x": 810, "y": 650, "text": "Your gut adapts within weeks", "color": "#16A34A", "at": [2, "weeks"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Bonus: canned or dried? Dried is better for nutrition and your wallet, with less sodium and full control over cooking.", {}),
            ("H", "Canned is far more convenient, and the gap shrinks a lot if you drain and rinse them well.", {}),
        ], "els": [
            {"type": "card", "x": 440, "y": 330, "w": 580, "h": 200, "emoji": "🫘", "title": "Dried",
             "body": "less sodium · cheaper · full control", "at": [0, "Dried"], "fill": "#DCFCE7"},
            {"type": "card", "x": 1060, "y": 330, "w": 580, "h": 200, "emoji": "🥫", "title": "Canned",
             "body": "convenient · rinse well", "at": [1, "Canned"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: chickpeas are carbs and protein. Per hundred grams cooked, about twenty-seven point four grams of carbs, "
                  "including seven point six of fiber, and eight point nine grams of protein.", {}),
            ("H", "Two: they also bring folate, manganese, iron and zinc.", {}),
            ("H", "Three: the beans and the spread aren't the same food. Hummus spread has about forty percent more calories, from tahini and olive oil.", {}),
            ("H", "Four: gas, the main downside, is mostly fixed by a long soak, changing the water, and full cooking.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Carbs and protein: 27.4 g and 8.9 g", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Folate, manganese, iron, zinc", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Spread: about 40% more calories", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Gas: soak, change water, cook fully", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So chickpeas: half carb, half protein, all delicious. And a little bit noisy.", {"mood": "smug"}),
            ("H", "Not if you soak them, Pip.", {}),
            ("P", "Silent chickpeas! The dream!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Change the soaking water!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article + sources: wiseplate.blog/food/chickpeas", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
