"""Mango explainer (English), based on https://wiseplate.blog/food/mango/

Numbers are the article's: fresh mango per 100 g (about half a medium mango)
with % daily value, a whole medium mango (about 200 g of flesh), and its
glycemic index / load figures. Keep them in sync with content/food/mango.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Mango: Too Much Sugar?"
SLUG = "mango"
ARTICLE = "https://wiseplate.blog/food/mango/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "MANGO", "top_size": 210, "bottom": "TOO SWEET?", "bottom_size": 190,
         "badge": "27 g", "badge_label": "sugar per\nmedium mango", "badge_color": "#F97316",
         "scatter": "🥭", "hero": "🥭", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "fruit":    {"bpm": 104, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.65, "swing": 0.15},
    "inside":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "vitc":     {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "mangiferin": {"bpm": 96, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.6, "swing": 0.1},
    "sugar":    {"bpm": 92, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.55},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF7ED", "fruit": "#FEF3C7", "inside": "#ECFDF5", "vitc": "#FFEDD5",
    "mangiferin": "#F5F3FF", "sugar": "#FCE7F3", "catches": "#FEE2E2", "howto": "#ECFCCB",
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
            ("P", "Hello, hello! Pip the pumpkin seed here, reporting live from the fruit bowl.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest is big, orange, and very juicy. It's the mango!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🥭", 960, 200, 160, at=[1, "mango"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Mango is loved everywhere, but people keep asking one thing: is it healthy, or is it just too much sugar? "
                  "Today we'll look at both sides, and at a couple of downsides almost nobody talks about.", {}),
            ("P", "Ooh, secret downsides. Spill the juice.", {"mood": "surprised"}),
        ], "els": [
            E("🥭", 420, 330, 200, at=[0, "Mango"], wobble=True),
            T("Mango", 640, 300, 140, at=[0, "Mango"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🍊", "title": "The good stuff", "at": [0, "healthy"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🍬", "title": "The sugar question", "at": [0, "sugar"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "🤫", "title": "Hidden downsides", "at": [0, "downsides"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "fruit", "title": "The World's Favorite Fruit", "emoji": "🌏", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "The mango, Mangifera indica, is the most consumed fruit in the world by volume. "
                  "More than apples, bananas or grapes.",
             {"say": "The mango, Mangifera indica, is the most consumed fruit in the world by volume. "
                     "More than apples, bananas, or grapes."}),
            ("H", "It comes from South Asia, where it has been grown for more than four thousand years. In India, it's the national fruit.", {}),
            ("P", "Four thousand years of fame. I can't even get a sticker.", {"mood": "worried"}),
        ], "els": [
            T("#1 fruit in the world", 720, 180, 80, at=[0, "most"], font="fredoka", weight=700, color="orange"),
            T("by volume", 720, 260, 44, at=[0, "volume"], color="muted"),
            E("🍎", 420, 400, 110, at=[0, "apples"]),
            E("🍌", 720, 400, 110, at=[0, "bananas"]),
            E("🍇", 1020, 400, 110, at=[0, "grapes"]),
            {"type": "card", "x": 450, "y": 650, "w": 560, "h": 160, "emoji": "🏺", "title": "4,000+ years", "body": "from South Asia", "at": [1, "four"]},
            {"type": "card", "x": 1050, "y": 650, "w": 560, "h": 160, "emoji": "🇮🇳", "title": "India", "body": "the national fruit", "at": [1, "India"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Mango belongs to the same plant family as cashews and pistachios. Remember that, it explains some of the downsides later.", {}),
            ("H", "Nutritionally, mango is in an interesting spot. It's unusually rich in vitamin C and carotenoids. "
                  "And it also has more sugar than most common fruits.", {}),
            ("H", "Both are true at the same time. So, is mango healthy? The answer isn't a simple yes or no.", {}),
        ], "els": [
            T("One family:", 720, 160, 56, at=[0, "family"], font="fredoka", weight=700, color="green"),
            {"type": "pill", "x": 400, "y": 250, "text": "mango", "color": "orange", "at": [0, "family"]},
            {"type": "pill", "x": 720, "y": 250, "text": "cashew", "color": "#B45309", "at": [0, "cashews"]},
            {"type": "pill", "x": 1040, "y": 250, "text": "pistachio", "color": "green", "at": [0, "pistachios"]},
            {"type": "card", "x": 450, "y": 520, "w": 560, "h": 170, "emoji": "🍊", "title": "Vitamin C", "body": "+ carotenoids", "at": [1, "vitamin"], "fill": "#DCFCE7"},
            {"type": "card", "x": 1050, "y": 520, "w": 560, "h": 170, "emoji": "🍬", "title": "More sugar", "body": "than most fruits", "at": [1, "sugar"], "fill": "#FEE2E2"},
            {"type": "banner", "x": 750, "y": 760, "text": "Not a simple yes or no", "color": "#475569", "at": [2, "simple"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "inside", "title": "What's in Half a Mango?", "emoji": "🔬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Our serving is one hundred grams of fresh mango, roughly half a medium mango.", {}),
            ("H", "That's sixty calories and fifteen grams of carbs, of which thirteen point seven grams are sugars. "
                  "Plus one point six grams of fiber, and almost no protein or fat.", {}),
        ], "els": [
            T("100 g fresh ≈ half a mango", 720, 170, 66, at=0, font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 340, "y": 450, "w": 380, "h": 290, "value": 60, "unit": "", "label": "calories", "emoji": "🔥", "at": [1, "sixty"]},
            {"type": "stat", "x": 750, "y": 450, "w": 380, "h": 290, "value": 13.7, "decimals": 1, "unit": " g", "label": "sugars (of 15 g carbs)", "emoji": "🍬", "at": [1, "thirteen"]},
            {"type": "stat", "x": 1160, "y": 450, "w": 380, "h": 290, "value": 1.6, "decimals": 1, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [1, "fiber"]},
            T("protein 0.8 g · fat 0.4 g", 750, 690, 44, at=[1, "protein"], color="muted"),
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Here's the percent of the daily value in those hundred grams. Vitamin C is the clear winner, at forty percent.", {}),
            ("H", "Then copper, twelve. Folate, eleven. Vitamin A, from beta-carotene, six. Vitamin E, six. And potassium, four.", {}),
            ("P", "Vitamin C, forty percent. The rest... participation trophies.", {"mood": "smug"}),
        ], "els": [
            T("% Daily Value per 100 g", 760, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 280, "w": 1200, "row_h": 98, "max": 45, "rows": [
                {"label": "Vitamin C", "value": 40, "color": "#F97316", "at": [0, "forty"], "star": True},
                {"label": "Copper", "value": 12, "color": "#B45309", "at": [1, "copper"]},
                {"label": "Folate", "value": 11, "color": "#16A34A", "at": [1, "Folate"]},
                {"label": "Vitamin A", "value": 6, "color": "#F59E0B", "at": [1, "A,"]},
                {"label": "Vitamin E", "value": 6, "color": "#84CC16", "at": [1, "E,"]},
                {"label": "Potassium", "value": 4, "color": "#0EA5E9", "at": [1, "potassium"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "A whole medium mango, about two hundred grams of flesh, comes to around one hundred twenty calories, "
                  "and about twenty-seven grams of sugar.", {}),
            ("P", "Twenty-seven grams. That's a lot of sweet.", {"mood": "surprised"}),
        ], "els": [
            E("🥭", 720, 280, 200, at=0, wobble=True),
            {"type": "stat", "x": 470, "y": 590, "w": 440, "h": 290, "value": 120, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "twenty"]},
            {"type": "stat", "x": 970, "y": 590, "w": 440, "h": 290, "value": 27, "unit": " g", "label": "sugar", "emoji": "🍬", "at": [0, "seven"], "color": "orange"},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "vitc", "title": "Vitamin C and Carotenoids", "emoji": "🍊", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Benefit one: vitamin C. Half a mango gives about forty percent of the daily value. That's more than an orange of the same weight.", {}),
            ("H", "Vitamin C is needed to make collagen, and for your immune system. "
                  "And eaten in the same meal, it significantly boosts how much plant iron you absorb.", {}),
            ("P", "Mango beats orange? Somebody call the orange's lawyer.", {"mood": "surprised", "jump": True}),
        ], "els": [
            {"type": "ring", "x": 420, "y": 350, "r": 170, "value": 40, "color": "#F97316", "label": "vitamin C", "at": [0, "forty"]},
            T("> an orange, same weight", 1050, 300, 50, at=[0, "orange"], font="fredoka", weight=700, color="orange"),
            {"type": "card", "x": 450, "y": 690, "w": 520, "h": 150, "emoji": "🧴", "title": "Collagen", "at": [1, "collagen"]},
            {"type": "card", "x": 1000, "y": 520, "w": 520, "h": 150, "emoji": "🛡️", "title": "Immunity", "at": [1, "immune"]},
            {"type": "card", "x": 1000, "y": 690, "w": 520, "h": 150, "emoji": "🩸", "title": "Plant iron", "body": "absorbed better", "at": [1, "iron"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Benefit two: carotenoids. That orange color comes from beta-carotene and related compounds, "
                  "which your body turns into vitamin A.", {}),
            ("H", "Mango also has lutein and zeaxanthin, two carotenoids that build up in the retina of the eye, "
                  "and are linked with protection against macular degeneration.",
             {"say": "Mango also has lutein and zee-uh-zanthin, two carotenoids that build up in the retina of the eye, "
                     "and are linked with protection against macular degeneration."}),
        ], "els": [
            {"type": "card", "x": 360, "y": 300, "w": 520, "h": 170, "emoji": "🧡", "title": "Beta-carotene", "at": [0, "beta"]},
            {"type": "arrow", "x1": 640, "y1": 300, "x2": 790, "y2": 300, "at": [0, "turns"]},
            {"type": "card", "x": 1050, "y": 300, "w": 480, "h": 170, "emoji": "👀", "title": "Vitamin A", "at": [0, "vitamin"]},
            {"type": "card", "x": 720, "y": 600, "w": 1000, "h": 190, "emoji": "👁️", "title": "Lutein + zeaxanthin",
             "body": "in the retina · linked with eye protection", "at": [1, "lutein"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "mangiferin", "title": "Mangiferin and Friends", "emoji": "🧪", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Benefit three: mangiferin. Mango is one of the main food sources of this polyphenol.",
             {"say": "Benefit three: man-JIF-er-in. Mango is one of the main food sources of this polyphenol."}),
            ("H", "It's been studied a lot for antioxidant and anti-inflammatory activity, and a possible effect on how the body handles sugar and fat.", {}),
            ("H", "But most of that research is still in the lab, and in animals.", {}),
            ("P", "So mangiferin is a lab superstar. Not famous with humans yet.", {"mood": "smug"}),
        ], "els": [
            T("Mangiferin", 720, 200, 110, at=[0, "mangiferin"], font="fredoka", weight=700, color="#7C3AED"),
            {"type": "pill", "x": 340, "y": 400, "text": "antioxidant", "color": "green", "at": [1, "antioxidant"]},
            {"type": "pill", "x": 720, "y": 400, "text": "anti-inflammatory", "color": "#0EA5E9", "at": [1, "anti"]},
            {"type": "pill", "x": 1100, "y": 400, "text": "sugar and fat?", "color": "#F59E0B", "at": [1, "sugar"]},
            {"type": "card", "x": 720, "y": 620, "w": 1000, "h": 170, "emoji": "🐭", "title": "Mostly lab and animal studies",
             "at": [2, "lab"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Mango also contains amylases, enzymes that break starch into simple sugars. "
                  "They get more active as the fruit ripens, which is why a ripe mango tastes so much sweeter.", {}),
            ("H", "There's early evidence that mango, together with its fiber, helps with chronic constipation.", {}),
            ("H", "And its soluble fiber, pectin, helps you feel full, slows sugar absorption, and feeds your gut bacteria.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 170, "emoji": "✂️", "title": "Amylases",
             "body": "break starch into sugar · riper = sweeter", "at": [0, "amylases"]},
            {"type": "card", "x": 720, "y": 440, "w": 1000, "h": 170, "emoji": "🚽", "title": "Constipation",
             "body": "early evidence it helps", "at": [1, "constipation"]},
            {"type": "card", "x": 720, "y": 650, "w": 1000, "h": 170, "emoji": "🌾", "title": "Pectin",
             "body": "fullness · slower sugar · feeds gut bacteria", "at": [2, "pectin"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "sugar", "title": "The Sugar Question", "emoji": "🍬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the main downside: sugar. Twenty-seven grams in a medium mango is a real amount, "
                  "especially if you're managing diabetes, prediabetes, or a low-carb diet.", {}),
            ("H", "But keep it in proportion. This is natural sugar that comes with fiber, water and vitamins. "
                  "A mango is not a sugary drink. Still, the amount isn't trivial.", {}),
        ], "els": [
            {"type": "stat", "x": 450, "y": 330, "w": 460, "h": 300, "value": 27, "unit": " g", "label": "sugar, medium mango", "emoji": "🍬", "at": [0, "Twenty"], "color": "orange"},
            {"type": "card", "x": 1080, "y": 330, "w": 560, "h": 220, "emoji": "🩺", "title": "Matters for",
             "body": "diabetes · prediabetes · low-carb", "at": [0, "diabetes"]},
            {"type": "pill", "x": 760, "y": 640, "text": "comes with fiber, water, vitamins", "color": "ok", "at": [1, "fiber"]},
            {"type": "pill", "x": 760, "y": 740, "text": "not a sugary drink, but not trivial", "color": "orange", "at": [1, "trivial"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "What about the glycemic index? Fresh mango scores about fifty-one, which counts as low, since low is under fifty-five.", {}),
            ("H", "But the glycemic index alone is misleading, because it ignores how much you eat. The more useful number is glycemic load.", {}),
            ("H", "For one hundred grams of mango, the load is about eight, which is low. For a whole mango, about sixteen, which is medium.", {}),
        ], "els": [
            {"type": "stat", "x": 400, "y": 330, "w": 460, "h": 300, "value": 51, "unit": "", "label": "glycemic index (low)", "emoji": "📈", "at": [0, "fifty"], "color": "ok"},
            T("index ignores the amount", 1080, 300, 46, at=[1, "ignores"], font="fredoka", weight=600, color="orange"),
            T("Glycemic load", 760, 560, 56, at=[1, "load."], font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 200, "y": 670, "w": 1200, "row_h": 100, "max": 20, "unit": "", "rows": [
                {"label": "100 g", "value": 8, "color": "#16A34A", "at": [2, "eight"]},
                {"label": "Whole mango", "value": 16, "color": "#F59E0B", "at": [2, "sixteen"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "In practice: fresh mango in a sensible amount doesn't cause a sharp blood sugar spike in a healthy person, "
                  "thanks to the fiber and water. Dried mango or mango juice? A whole different story.", {}),
            ("P", "Fresh mango, fine. Mango juice, suspicious. Noted.", {"mood": "smug"}),
        ], "els": [
            {"type": "check", "x": 160, "y": 260, "w": 1280, "ok": True, "text": "Fresh, sensible amount: no sharp spike", "at": [0, "spike"]},
            {"type": "check", "x": 160, "y": 400, "w": 1280, "ok": False, "text": "Dried mango, mango juice", "at": [0, "Dried"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "More catches. First, FODMAPs. Mango has more fructose than glucose, so it counts as high FODMAP.",
             {"say": "More catches. First, fod-maps. Mango has more fructose than glucose, so it counts as high fod-map."}),
            ("H", "For people with irritable bowel syndrome or fructose malabsorption, a big portion can cause bloating, gas and diarrhea. "
                  "About forty grams is usually tolerated.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "🎈", "title": "High FODMAP",
             "body": "more fructose than glucose", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🥄", "title": "IBS: ~40 g is usually fine",
             "body": "big portions: bloating, gas, diarrhea", "at": [1, "forty"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Here's the downside almost nobody mentions. Mango peel and sap contain urushiol, "
                  "the same compound found in poison ivy.",
             {"say": "Here's the downside almost nobody mentions. Mango peel and sap contain yoo-roo-shee-ol, "
                     "the same compound found in poison ivy."}),
            ("H", "Sensitive people can get an itchy rash around the mouth and on the hands, after peeling it or biting into it with the skin. "
                  "The fix: peel with gloves, or wash well, and eat only the flesh.", {}),
            ("P", "Poison ivy? In a mango? This is the plot twist of the year.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("Urushiol", 720, 190, 110, at=[0, "urushiol"], font="fredoka", weight=700, color="red"),
            T("in the peel and sap, like poison ivy", 720, 300, 46, at=[0, "poison"], color="muted"),
            {"type": "card", "x": 450, "y": 520, "w": 560, "h": 170, "emoji": "😣", "title": "Itchy rash", "body": "mouth and hands", "at": [1, "rash"]},
            {"type": "card", "x": 1050, "y": 520, "w": 560, "h": 170, "emoji": "🧤", "title": "Gloves, wash", "body": "eat only the flesh", "at": [1, "gloves"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Next, oral allergy syndrome. People allergic to latex or pollen may get itching and mild swelling of the lips and throat after mango. "
                  "Cooking the fruit usually stops the reaction.", {}),
            ("H", "And the big one: dried mango and mango juice are not the same food. Dried mango concentrates the sugar many times over, "
                  "sometimes with added sugar. Juice loses almost all the fiber, so it's basically a sweetened drink.", {}),
            ("H", "The gap between the whole fruit and its products is the most important nutrition difference in mango.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 210, "w": 1100, "h": 160, "emoji": "👄", "title": "Oral allergy syndrome",
             "body": "with latex or pollen allergy · cooking helps", "at": 0},
            {"type": "card", "x": 470, "y": 470, "w": 520, "h": 160, "emoji": "🍬", "title": "Dried", "body": "sugar concentrated", "at": [1, "Dried"]},
            {"type": "card", "x": 1050, "y": 470, "w": 520, "h": 160, "emoji": "🧃", "title": "Juice", "body": "fiber removed", "at": [1, "Juice"]},
            {"type": "banner", "x": 760, "y": 720, "text": "Whole fruit is a different food", "color": "#DC2626", "at": [2, "gap"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Two last ones. Unripe mango is sour, hard to digest, and can upset your stomach. "
                  "And if you have kidney disease with a potassium limit, count mango's potassium too.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 300, "w": 1100, "h": 180, "emoji": "😖", "title": "Unripe: sour, tough on the stomach", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 180, "emoji": "🫘", "title": "Kidney disease: count the potassium", "at": [0, "kidney"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "How Much, and How", "emoji": "🍽️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "So how much mango a day? There's no official limit. For a healthy person, a practical guide is up to one medium mango a day, "
                  "about one hundred fifty to two hundred grams, as part of your two to three fruit servings.", {}),
            ("H", "With diabetes or prediabetes: about one hundred grams, half a mango, as part of a meal with protein or fat, "
                  "like yogurt, nuts or tahini. That softens the blood sugar response.", {}),
            ("H", "With irritable bowel syndrome: start at about forty grams and see how you feel. "
                  "And for weight loss, mango isn't more fattening than other fruits. Just have it instead of another snack, not on top.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 200, "w": 1100, "h": 140, "emoji": "🥭", "title": "Healthy: up to 1 medium mango", "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 760, "y": 370, "w": 1100, "h": 140, "emoji": "🩺", "title": "Diabetes: ~100 g, with a meal", "at": [1, "diabetes"]},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 140, "emoji": "🎈", "title": "IBS: start at ~40 g", "at": [2, "irritable"]},
            {"type": "card", "x": 760, "y": 710, "w": 1100, "h": 140, "emoji": "⚖️", "title": "Weight: instead of a snack", "at": [2, "weight"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Best way to eat it: the whole fruit, chilled. Cold makes the sweetness pop.", {}),
            ("H", "Frozen mango makes smoothies creamy without added sugar or ice cream. Blend it with Greek yogurt, "
                  "and the protein balances the sugar.", {}),
            ("H", "Or make a salsa: chopped mango, red onion, cilantro, lemon and chili. Great with fish and chicken.", {}),
            ("P", "Mango salsa with a pumpkin seed crunch? Just an idea. A brilliant idea.", {"mood": "smug"}),
        ], "els": [
            E("🧊", 300, 330, 150, at=[0, "chilled"]),
            T("chilled", 300, 450, 42, at=[0, "chilled"], font="fredoka", weight=600),
            E("🥤", 720, 330, 150, at=[1, "smoothies"]),
            T("smoothie + yogurt", 720, 450, 42, at=[1, "yogurt"], font="fredoka", weight=600),
            E("🌶️", 1140, 330, 150, at=[2, "salsa"]),
            T("salsa", 1140, 450, 42, at=[2, "salsa"], font="fredoka", weight=600),
            T("mango · red onion · cilantro · lemon · chili", 720, 600, 42, at=[2, "onion"], color="muted"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Green, unripe mango is eaten in Southeast Asia as a salty, spicy salad. It has much less sugar, and even more vitamin C.", {}),
            ("H", "What to avoid: mango canned in syrup, sweetened dried mango, and concentrated mango juices.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 180, "emoji": "🥗", "title": "Green mango salad",
             "body": "less sugar · more vitamin C", "at": 0, "fill": "#DCFCE7"},
            {"type": "check", "x": 220, "y": 520, "w": 1000, "ok": False, "text": "Canned in syrup", "at": [1, "syrup"]},
            {"type": "check", "x": 220, "y": 650, "w": 1000, "ok": False, "text": "Sweetened dried mango", "at": [1, "dried"]},
            {"type": "check", "x": 220, "y": 780, "w": 1000, "ok": False, "text": "Concentrated juice", "at": [1, "juices"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: mango is truly nutritious. Half a mango gives forty percent of your vitamin C, plus carotenoids, folate and mangiferin.",
             {"say": "One: mango is truly nutritious. Half a mango gives forty percent of your vitamin C, plus carotenoids, folate and man-JIF-er-in."}),
            ("H", "Two: the main downside is sugar, about twenty-seven grams in a medium mango.", {}),
            ("H", "Three: lesser-known catches are FODMAPs, and urushiol in the peel.",
             {"say": "Three: lesser known catches are fod-maps, and yoo-roo-shee-ol in the peel."}),
            ("H", "Four: one whole mango a day is a great choice. Juice and sweetened dried mango are a different food.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "40% vitamin C in half a mango", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Main catch: ~27 g sugar per mango", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Also: FODMAPs, urushiol in the peel", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Whole fruit, not juice or dried", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So mango: sweet, sunny, a little dramatic about its peel. I like it.", {"mood": "happy"}),
            ("H", "Same here, Pip. Just wear gloves.", {}),
            ("P", "Mango party! Gloves on!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Eat the fruit, skip the juice!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article + sources: wiseplate.blog/food/mango", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
