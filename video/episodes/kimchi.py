"""Kimchi explainer (English), based on https://wiseplate.blog/en/food/kimchi/

Numbers are the article's: kimchi per 100 g with % daily value, sodium as a
range (500-1,100 mg, 20-48% DV), against a 2,300 mg daily limit, and a
realistic side portion of 30-50 g (150-550 mg sodium). Temperatures are
degrees Celsius. Keep them in sync with content/food/kimchi.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Kimchi: Healthy Probiotic or Too Much Salt?"
SLUG = "kimchi"
ARTICLE = "https://wiseplate.blog/en/food/kimchi/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "KIMCHI", "top_size": 200, "bottom": "TOO SALTY?", "bottom_size": 150,
         "badge": "15", "badge_label": "calories\nper 100 g", "badge_color": "#DC2626",
         "scatter": "🌶️", "hero": "🥬", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "meet":     {"bpm": 104, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.65, "swing": 0.15},
    "made":     {"bpm": 96, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.6},
    "inside":   {"bpm": 108, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.75},
    "benefits": {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "salt":     {"bpm": 88, "root": 63, "prog": ["vi", "IV", "I", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF1F2", "meet": "#FEF3C7", "made": "#ECFDF5", "inside": "#E0F2FE",
    "benefits": "#ECFCCB", "salt": "#F1F5F9", "catches": "#FEE2E2", "howto": "#FFEDD5",
    "outro": "#FFF1F2",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hello hello! Pip the pumpkin seed here, guest reviewer and professional snack.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest is spicy, sour, and a little bit fizzy. It's kimchi!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🌶️", 960, 200, 160, at=[1, "kimchi"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today it's kimchi. How it's made, what's in it, its probiotic perks, "
                  "and the one big downside: salt.", {}),
            ("P", "Salt drama. I know a thing or two about salted seeds.", {"mood": "smug"}),
        ], "els": [
            E("🥬", 420, 330, 200, at=[0, "kimchi"], wobble=True),
            T("Kimchi", 640, 300, 140, at=[0, "kimchi"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🏺", "title": "How it's made", "at": [0, "made"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🦠", "title": "The probiotics", "at": [0, "probiotic"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "🧂", "title": "The salt", "at": [0, "salt"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "meet", "title": "Meet Kimchi", "emoji": "🇰🇷", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Kimchi is a traditional Korean dish of vegetables, pickled in salt and fermented in a spicy seasoning mix.", {}),
            ("H", "In Korea it's eaten at almost every meal, breakfast included, and it's considered the national dish.", {}),
            ("P", "Kimchi for breakfast? Bold. I respect it.", {"mood": "surprised"}),
        ], "els": [
            T("A Korean classic", 720, 170, 72, at=0, font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 720, "y": 390, "w": 1000, "h": 180, "emoji": "🥬", "title": "Salted, then fermented",
             "body": "vegetables in a spicy seasoning mix", "at": [0, "pickled"]},
            {"type": "card", "x": 720, "y": 620, "w": 1000, "h": 180, "emoji": "🍚", "title": "At almost every meal",
             "body": "Korea's national dish", "at": [1, "every"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The best-known version, baechu kimchi, is made with napa cabbage. "
                  "But there are more than one hundred eighty documented variations.",
             {"say": "The best known version, beh-choo kimchi, is made with napa cabbage. "
                     "But there are more than one hundred eighty documented variations."}),
            ("H", "Some use white radish, called kkakdugi. Some use cucumber, called oi sobagi. Others use green onion, and more.",
             {"say": "Some use white radish, called kak-doo-ghee. Some use cucumber, called oh-ee so-bah-ghee. Others use green onion, and more."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 170, "emoji": "🥬", "title": "Baechu kimchi",
             "body": "napa cabbage, the classic", "at": [0, "napa"]},
            {"type": "banner", "x": 720, "y": 400, "text": "180+ variations", "color": "orange", "at": [0, "eighty"]},
            E("⚪", 360, 580, 120, at=[1, "radish"]),
            T("radish", 360, 690, 40, at=[1, "radish"], font="fredoka", weight=600),
            E("🥒", 720, 580, 120, at=[1, "cucumber"]),
            T("cucumber", 720, 690, 40, at=[1, "cucumber"], font="fredoka", weight=600),
            E("🧅", 1080, 580, 120, at=[1, "onion"]),
            T("green onion", 1080, 690, 40, at=[1, "onion"], font="fredoka", weight=600),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "There's even a whole tradition around it. Kimjang is the communal kimchi making before winter. "
                  "In twenty thirteen, UNESCO declared it an intangible cultural heritage.",
             {"say": "There's even a whole tradition around it. Kim-jahng is the communal kimchi making before winter. "
                     "In twenty thirteen, you-ness-co declared it an intangible cultural heritage."}),
            ("H", "Whole families make hundreds of heads of cabbage together in late autumn. "
                  "It's a leftover from a time when this was the only way to have vegetables through the Korean winter.", {}),
            ("P", "Hundreds of cabbages? That's a lot of chopping. I'll supervise.", {"mood": "smug"}),
        ], "els": [
            T("Kimjang", 720, 190, 100, at=0, font="fredoka", weight=700, color="green"),
            {"type": "pill", "x": 720, "y": 330, "text": "UNESCO heritage since 2013", "color": "#0EA5E9", "at": [0, "thirteen"]},
            {"type": "card", "x": 720, "y": 540, "w": 1000, "h": 180, "emoji": "🥬", "title": "Families, together",
             "body": "hundreds of cabbages in late autumn", "at": [1, "families"]},
            {"type": "pill", "x": 720, "y": 730, "text": "vegetables for the whole winter", "color": "orange", "at": [1, "winter"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "made", "title": "How It's Made", "emoji": "🏺", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "How kimchi is made explains both its benefits and its downsides. There are three steps.", {}),
            ("H", "Step one, salting. The cabbage leaves sit in salt for several hours. "
                  "The salt draws water out, softens the leaves, and stops unwanted bacteria from growing.", {}),
            ("H", "And this is where kimchi's high sodium comes from.", {}),
            ("P", "Wait. So the salt is built right in? Oh no.", {"mood": "worried"}),
        ], "els": [
            T("1. Salting", 720, 170, 80, at=[1, "salting"], font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 720, "y": 400, "w": 1000, "h": 180, "emoji": "🧂", "title": "Several hours in salt",
             "body": "draws out water, softens, protects", "at": [1, "hours"]},
            {"type": "banner", "x": 720, "y": 640, "text": "Source of the sodium", "color": "#DC2626", "at": [2, "sodium"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Step two, seasoning. In goes a paste of gochugaru, which is Korean red pepper flakes, "
                  "plus garlic, ginger and green onion.",
             {"say": "Step two, seasoning. In goes a paste of go-choo-gah-roo, which is Korean red pepper flakes, "
                     "plus garlic, ginger and green onion."}),
            ("H", "And often something from the sea, too: fish sauce, salted shrimp called jeotgal, or seaweed.",
             {"say": "And often something from the sea, too: fish sauce, salted shrimp called jut-gahl, or seaweed."}),
            ("P", "Shrimp in my cabbage? I did not see that coming.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("2. Seasoning", 720, 170, 80, at=0, font="fredoka", weight=700, color="green"),
            E("🌶️", 300, 350, 120, at=[0, "gochugaru"]),
            T("gochugaru", 300, 450, 38, at=[0, "gochugaru"], font="fredoka", weight=600),
            E("🧄", 580, 350, 120, at=[0, "garlic"]),
            T("garlic", 580, 450, 38, at=[0, "garlic"], font="fredoka", weight=600),
            E("🫚", 860, 350, 120, at=[0, "ginger"]),
            T("ginger", 860, 450, 38, at=[0, "ginger"], font="fredoka", weight=600),
            E("🧅", 1140, 350, 120, at=[0, "onion"]),
            T("green onion", 1140, 450, 38, at=[0, "onion"], font="fredoka", weight=600),
            {"type": "pill", "x": 400, "y": 640, "text": "fish sauce", "color": "#0EA5E9", "at": [1, "fish"]},
            {"type": "pill", "x": 760, "y": 640, "text": "salted shrimp", "color": "#0EA5E9", "at": [1, "salted"]},
            {"type": "pill", "x": 1100, "y": 640, "text": "seaweed", "color": "#0EA5E9", "at": [1, "seaweed"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Step three, fermentation. The mix is packed into a sealed container, "
                  "left at room temperature for a day to a few days, then moved to the fridge.", {}),
            ("H", "Lactic acid bacteria that live naturally on the vegetables do the work. "
                  "First mostly Leuconostoc mesenteroides, and later Lactiplantibacillus plantarum.",
             {"say": "Lactic acid bacteria that live naturally on the vegetables do the work. "
                     "First mostly Loo-ko-noss-tock mez-en-ter-oy-deez, and later Lacti-planti-ba-sill-us plan-tar-um."}),
            ("H", "They eat the sugars and make lactic acid. The acidity preserves the food, and gives it that typical sour taste.", {}),
        ], "els": [
            T("3. Fermentation", 760, 160, 80, at=0, font="fredoka", weight=700, color="green"),
            {"type": "pill", "x": 500, "y": 300, "text": "1 to a few days, room temp", "color": "orange", "at": [0, "room"]},
            {"type": "pill", "x": 1150, "y": 300, "text": "then the fridge", "color": "#0EA5E9", "at": [0, "fridge"]},
            {"type": "card", "x": 760, "y": 490, "w": 1200, "h": 180, "emoji": "🦠", "title": "Lactic acid bacteria",
             "body": "Leuconostoc first, then Lactiplantibacillus", "at": [1, "Lactic"]},
            {"type": "card", "x": 760, "y": 720, "w": 1200, "h": 160, "emoji": "🍋", "title": "Sugar becomes lactic acid", "at": [2, "sugars"],
             "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Kimchi keeps fermenting in the fridge, so it gets more sour over time. "
                  "Aged, sour kimchi is considered especially good for cooking, in soups and stews.", {}),
            ("P", "It gets better with age. Like me. Well, like me until I go stale.", {"mood": "smug"}),
        ], "els": [
            E("🧊", 400, 330, 160, at=[0, "fridge"]),
            {"type": "arrow", "x1": 520, "y1": 330, "x2": 860, "y2": 330, "at": [0, "sour"], "color": "orange"},
            E("🍲", 1000, 330, 160, at=[0, "Aged"]),
            T("more sour over time", 720, 500, 56, at=[0, "sour"], font="fredoka", weight=600, color="green"),
            T("aged kimchi: great for soups and stews", 720, 600, 44, at=[0, "soups"], color="muted"),
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "inside", "title": "What's in 100 Grams?", "emoji": "🔬", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Per hundred grams, kimchi has just fifteen calories. "
                  "Plus one point one grams of protein, two point four grams of carbs, one point six grams of fiber, "
                  "and half a gram of fat.", {}),
            ("P", "Fifteen calories? That's barely a nibble. Not jealous. Okay, a little.", {"mood": "surprised"}),
        ], "els": [
            T("Per 100 g", 760, 150, 60, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 330, "y": 380, "w": 400, "h": 290, "value": 15, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "fifteen"]},
            {"type": "stat", "x": 760, "y": 380, "w": 400, "h": 290, "value": 1.1, "decimals": 1, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "protein"]},
            {"type": "stat", "x": 1190, "y": 380, "w": 400, "h": 290, "value": 2.4, "decimals": 1, "unit": " g", "label": "carbs", "emoji": "🍞", "at": [0, "carbs"]},
            {"type": "stat", "x": 540, "y": 700, "w": 400, "h": 290, "value": 1.6, "decimals": 1, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [0, "fiber"]},
            {"type": "stat", "x": 980, "y": 700, "w": 400, "h": 290, "value": 0.5, "decimals": 1, "unit": " g", "label": "fat", "emoji": "🫒", "at": [0, "fat"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Now the vitamins, as a share of the daily value. Vitamin K: thirty-seven percent. Vitamin C: seventeen percent.", {}),
            ("H", "Vitamin B6: twelve percent. Folate: eleven percent. And iron, three percent.",
             {"say": "Vitamin B 6: twelve percent. Folate: eleven percent. And iron, three percent."}),
            ("H", "Fiber adds six percent. All of that, for fifteen calories.", {}),
        ], "els": [
            T("% daily value, per 100 g", 760, 140, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 160, "y": 260, "w": 1300, "row_h": 105, "max": 40, "rows": [
                {"label": "Vitamin K", "value": 37, "color": "#16A34A", "at": [0, "thirty"]},
                {"label": "Vitamin C", "value": 17, "color": "#F97316", "at": [0, "seventeen"]},
                {"label": "B6", "value": 12, "color": "#0EA5E9", "at": [1, "twelve"]},
                {"label": "Folate", "value": 11, "color": "#8B5CF6", "at": [1, "eleven"]},
                {"label": "Iron", "value": 3, "color": "#B45309", "at": [1, "three"]},
                {"label": "Fiber", "value": 6, "color": "#65A30D", "at": [2, "six"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "But one number in the table stands out. Sodium: five hundred to eleven hundred milligrams per hundred grams.", {}),
            ("H", "That's twenty to forty-eight percent of the daily value. It's kimchi's main downside, and we'll come back to it.", {}),
            ("P", "Forty-eight percent? From a side dish? Somebody pass the water.", {"mood": "worried", "jump": True}),
        ], "els": [
            T("The odd one out", 720, 170, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "stat", "x": 720, "y": 440, "w": 760, "h": 320, "value": 0, "text": "500–1,100 mg", "vsize": 96,
             "label": "sodium per 100 g", "emoji": "🧂", "at": [0, "Sodium"], "color": "#DC2626"},
            {"type": "pill", "x": 720, "y": 700, "text": "20–48% of the daily value", "color": "#DC2626", "at": [1, "twenty"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "benefits", "title": "The Good Stuff", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "First, kimchi gives you live lactic acid bacteria, mainly Lactiplantibacillus and Leuconostoc strains.",
             {"say": "First, kimchi gives you live lactic acid bacteria, mainly Lacti-planti-ba-sill-us and Loo-ko-noss-tock strains."}),
            ("H", "And unlike yogurt and kefir, it's completely dairy-free. "
                  "That's a plus for people with lactose intolerance or a milk protein allergy.", {}),
            ("H", "The vegetables also bring fiber that feeds your gut bacteria. So you get probiotics and prebiotics in the same food.", {}),
            ("P", "Bacteria and their lunch, in one jar. Efficient.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 180, "emoji": "🦠", "title": "Live probiotics",
             "body": "lactic acid bacteria", "at": 0},
            {"type": "card", "x": 720, "y": 440, "w": 1000, "h": 180, "emoji": "🥛", "title": "Completely dairy-free",
             "body": "good for lactose intolerance", "at": [1, "dairy"], "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 670, "w": 1000, "h": 180, "emoji": "🌾", "title": "Plus prebiotic fiber",
             "body": "food for your gut bacteria", "at": [2, "fiber"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Next, nutrient density: thirty-seven percent of your vitamin K, and seventeen percent of your vitamin C, in just fifteen calories.", {}),
            ("H", "Napa cabbage contains glucosinolates, which are being studied for anti-inflammatory effects and cell protection.",
             {"say": "Napa cabbage contains glue-co-sin-oh-lates, which are being studied for anti inflammatory effects and cell protection."}),
            ("H", "And capsaicin, the compound that makes the pepper hot, has been studied for a mild effect on metabolism and fullness.",
             {"say": "And cap-say-sin, the compound that makes the pepper hot, has been studied for a mild effect on metabolism and fullness."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 180, "emoji": "🥇", "title": "37% K, 17% C",
             "body": "in only 15 calories", "at": 0},
            {"type": "card", "x": 720, "y": 440, "w": 1000, "h": 180, "emoji": "🥬", "title": "Glucosinolates",
             "body": "studied, from the cabbage", "at": [1, "glucosinolates"]},
            {"type": "card", "x": 720, "y": 670, "w": 1000, "h": 180, "emoji": "🌶️", "title": "Capsaicin",
             "body": "studied: metabolism, fullness", "at": [2, "capsaicin"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "A practical perk that's easy to miss: a spoonful of kimchi turns a plain bowl of rice, or a simple egg, "
                  "into a dish with bold flavor. That's an easy way to eat more vegetables.", {}),
            ("H", "And some small Korean studies found mild improvements in blood fats and insulin sensitivity with regular eating.", {}),
            ("H", "But these studies were small, mostly in Korean populations, so no strong conclusions.", {}),
            ("P", "Promising, but not proven. Got it. I'm a seed of science.", {"mood": "smug"}),
        ], "els": [
            E("🍚", 420, 260, 150, at=[0, "rice"]),
            E("🥚", 700, 260, 150, at=[0, "egg"]),
            T("+ kimchi = more veggies", 1050, 260, 52, at=[0, "vegetables"], font="fredoka", weight=600, color="green"),
            {"type": "card", "x": 720, "y": 520, "w": 1000, "h": 180, "emoji": "📊", "title": "Small Korean studies",
             "body": "blood fats, insulin sensitivity", "at": [1, "studies"]},
            {"type": "pill", "x": 720, "y": 720, "text": "early findings, no strong conclusions", "color": "orange", "at": [2, "small"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "salt", "title": "The Salt Problem", "emoji": "🧂", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Now the main downside. A hundred gram serving can carry five hundred to eleven hundred milligrams of sodium.", {}),
            ("H", "That's up to about half of the recommended daily limit of two thousand three hundred milligrams.", {}),
            ("H", "If you're managing high blood pressure, heart failure or kidney disease, you need to factor that in.", {}),
        ], "els": [
            T("Sodium vs the daily limit", 760, 160, 64, at=0, font="fredoka", weight=700, color="red"),
            {"type": "bars", "x": 160, "y": 350, "w": 1300, "row_h": 140, "max": 2300, "unit": " mg", "rows": [
                {"label": "100 g kimchi", "value": 1100, "text": "500–1,100 mg", "color": "#EF4444", "at": [0, "five"]},
                {"label": "Daily limit", "value": 2300, "text": "2,300 mg", "color": "#64748B", "at": [1, "limit"]},
            ]},
            {"type": "pill", "x": 760, "y": 680, "text": "blood pressure · heart failure · kidneys", "color": "#DC2626", "at": [2, "blood"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The fix is the portion. A realistic side is about thirty to fifty grams. "
                  "At that amount, the sodium comes to about one hundred fifty to five hundred fifty milligrams, which is reasonable.", {}),
            ("P", "So it's a side, not a main. Kimchi, know your role.", {"mood": "smug"}),
        ], "els": [
            T("Eat it as a side", 720, 180, 80, at=0, font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 450, "y": 450, "w": 500, "h": 300, "value": 0, "text": "30–50 g", "vsize": 96,
             "label": "a realistic side", "emoji": "🥄", "at": [0, "thirty"]},
            {"type": "stat", "x": 1000, "y": 450, "w": 500, "h": 300, "value": 0, "text": "150–550 mg", "vsize": 84,
             "label": "sodium", "emoji": "🧂", "at": [0, "hundred"], "color": "#16A34A"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "There's also a link with stomach cancer that's worth understanding properly.", {}),
            ("H", "Epidemiological studies in Korea found that eating a lot of salt-pickled vegetables is linked to a higher risk of stomach cancer. "
                  "And international research bodies class salt-preserved food as a possible risk factor.",
             {"say": "Epidemiological studies in Korea found that eating a lot of salt pickled vegetables is linked to a higher risk of stomach cancer. "
                     "And international research bodies class salt preserved food as a possible risk factor."}),
            ("H", "Keep it in proportion. The link is put down to the salt, and the damage it does to the stomach lining, not to the fermentation.", {}),
            ("H", "And it was seen at typical Korean intake levels, which are much higher than in the West. "
                  "As an occasional side, there's no real concern.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 180, "emoji": "📈", "title": "High intake, higher risk",
             "body": "salt-pickled vegetables, Korea", "at": [1, "Korea"]},
            {"type": "check", "x": 220, "y": 450, "w": 1000, "ok": False, "text": "Blame: the salt", "at": [2, "salt"]},
            {"type": "check", "x": 220, "y": 580, "w": 1000, "ok": True, "text": "Not the fermentation", "at": [2, "fermentation"]},
            {"type": "pill", "x": 720, "y": 750, "text": "as an occasional side: no real concern", "color": "green", "at": [3, "occasional"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Other Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Like any fermented food, kimchi contains histamine and tyramine made during fermentation. "
                  "People sensitive to histamine may get headaches, itching or a stuffy nose.",
             {"say": "Like any fermented food, kimchi contains histamine and tie-ra-meen made during fermentation. "
                     "People sensitive to histamine may get headaches, itching or a stuffy nose."}),
            ("H", "And anyone taking MAOI medications should avoid it.",
             {"say": "And anyone taking M A O I medications should avoid it."}),
            ("H", "It's also high in FODMAPs, thanks to lots of garlic and onion, so it can trigger symptoms in irritable bowel syndrome. "
                  "And the gochugaru can make heartburn and reflux worse in people prone to them.",
             {"say": "It's also high in fod-maps, thanks to lots of garlic and onion, so it can trigger symptoms in irritable bowel syndrome. "
                     "And the go-choo-gah-roo can make heartburn and reflux worse in people prone to them."}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1300, "ok": False, "text": "Histamine and tyramine", "at": [0, "histamine"]},
            {"type": "check", "x": 160, "y": 330, "w": 1300, "ok": False, "text": "On MAOI drugs? Avoid it", "at": [1, "medications"]},
            {"type": "check", "x": 160, "y": 460, "w": 1300, "ok": False, "text": "High FODMAP: may upset IBS", "at": [2, "irritable"]},
            {"type": "check", "x": 160, "y": 590, "w": 1300, "ok": False, "text": "Spicy: heartburn, reflux", "at": [2, "heartburn"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Here's a common mistake: kimchi isn't vegetarian or vegan by default. "
                  "Most traditional recipes contain fish sauce or salted shrimp. Vegan versions exist, but check the label.", {}),
            ("P", "Told you. Shrimp. Hiding in the cabbage.", {"mood": "smug"}),
            ("H", "People with a weakened immune system should ask their doctor first, as with any food with live cultures.", {}),
            ("H", "And canned or pasteurized kimchi loses its live bacteria. It's still a tasty fermented vegetable, "
                  "but without the probiotic benefit. Look for a chilled product in the fridge section.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 190, "w": 1000, "h": 170, "emoji": "🐟", "title": "Not vegan by default",
             "body": "fish sauce or salted shrimp", "at": 0, "fill": "#FEF3C7"},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 170, "emoji": "🩺", "title": "Weak immune system?",
             "body": "ask your doctor first", "at": [2, "immune"]},
            {"type": "card", "x": 720, "y": 650, "w": 1000, "h": 170, "emoji": "🥫", "title": "Pasteurized: no probiotics",
             "body": "buy it chilled", "at": [3, "pasteurized"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "How to Eat It", "emoji": "🥢", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "The traditional way is as banchan, a side dish: a spoonful or two next to rice and a main dish.",
             {"say": "The traditional way is as bahn-chahn, a side dish: a spoonful or two next to rice and a main dish."}),
            ("H", "Kimchi jjigae is a sour kimchi stew with tofu and meat. It's the classic use for kimchi that has turned too sour.",
             {"say": "Kimchi chee-geh is a sour kimchi stew with tofu and meat. It's the classic use for kimchi that has turned too sour."}),
            ("H", "Kimchi fried rice is one of the most popular Korean dishes. "
                  "And it works with eggs, on toast and in sandwiches, because the acidity cuts through fat.", {}),
            ("P", "Kimchi on toast? Now we're talking. Sprinkle a few seeds on top, too.", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "card", "x": 480, "y": 220, "w": 640, "h": 160, "emoji": "🍚", "title": "Banchan", "body": "a side dish", "at": 0},
            {"type": "card", "x": 1140, "y": 220, "w": 600, "h": 160, "emoji": "🍲", "title": "Kimchi jjigae", "body": "stew", "at": [1, "stew"]},
            {"type": "card", "x": 480, "y": 440, "w": 640, "h": 160, "emoji": "🍳", "title": "Fried rice", "at": [2, "fried"]},
            {"type": "card", "x": 1140, "y": 440, "w": 600, "h": 160, "emoji": "🥪", "title": "Eggs, toast", "at": [2, "toast"]},
            {"type": "pill", "x": 810, "y": 640, "text": "acidity cuts through fat", "color": "green", "at": [2, "acidity"]},
        ]},
        {"pip": PIP_C, "lines": [
            ("H", "One thing to know. Heating kimchi above forty-five to fifty degrees Celsius kills the probiotic bacteria.", {}),
            ("H", "The basic nutrition and the flavor stay, but the probiotic benefit is lost. If you're after the probiotics, eat it cold.", {}),
            ("P", "Cold kimchi for the bacteria, hot kimchi for the stew. Everyone wins.", {"mood": "happy"}),
        ], "els": [
            T("Above 45–50°C", 520, 170, 72, at=[0, "forty"], font="fredoka", weight=700, color="red"),
            T("probiotics gone", 520, 260, 44, at=[0, "kills"], color="muted"),
            T("Eat it cold", 1400, 170, 72, at=[1, "cold"], font="fredoka", weight=700, color="#0EA5E9"),
            T("keeps the bacteria", 1400, 260, 44, at=[1, "cold"], color="muted"),
            E("🔥", 520, 450, 160, at=[0, "Heating"]),
            E("❄️", 1400, 450, 160, at=[1, "cold"]),
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: kimchi is fermented vegetables with plant-based, dairy-free probiotics, plus fiber, vitamin K and vitamin C, at fifteen calories per hundred grams.", {}),
            ("H", "Two: the main downside is sodium, five hundred to eleven hundred milligrams per hundred grams.", {}),
            ("H", "Three: eat it the way it's eaten in Korea, as a thirty to fifty gram side, not a main portion. And eat it cold to keep the bacteria.", {}),
            ("H", "Four: if you're vegetarian, check the label, because most traditional versions contain fish sauce.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Dairy-free probiotics, 15 calories", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": False, "text": "Sodium: 500–1,100 mg per 100 g", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "A 30–50 g side, eaten cold", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Vegetarian? Check for fish sauce", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So kimchi: spicy, sour, full of tiny helpers. Just go easy on the portion.", {"mood": "smug"}),
            ("H", "Wise words, Pip.", {}),
            ("P", "A spoonful a day keeps the boredom away!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Remember: a side, not a main!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/kimchi", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
