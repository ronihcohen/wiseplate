"""Kefir explainer (English), based on https://wiseplate.blog/food/kefir/

Facts and numbers are the article's (content/food/kefir.md and its English
translation content/food/kefir.en.md). Nutrition is per 1 cup (about 240 ml)
of cow's-milk kefir; % daily value figures are the article's approximations.
Strain counts compare factory yogurt (2-5), commercial kefir (7-9) and
homemade kefir from grains (30 to 60+). Alcohol is % by volume.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Kefir: Ancient, Immortal and a Little Bit Boozy?"
SLUG = "kefir"
ARTICLE = "https://wiseplate.blog/en/food/kefir/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

MUSIC = {
    "intro":      {"bpm": 112, "root": 62, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "grains":     {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "history":    {"bpm": 94, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.6, "swing": 0.1},
    "cup":        {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "probiotics": {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "benefits":   {"bpm": 90, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.5, "drums": True},
    "quirks":     {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "alcohol":    {"bpm": 76, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.45, "inst": "musicbox", "drums": False},
    "howto":      {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":      {"bpm": 112, "root": 62, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {
    "intro": "#F0F9FF", "grains": "#FEF3C7", "history": "#FFEDD5", "cup": "#ECFDF5",
    "probiotics": "#E0F2FE", "benefits": "#F1F5F9", "quirks": "#FEE2E2", "alcohol": "#1E1B4B",
    "howto": "#ECFCCB", "outro": "#F0F9FF",
}

THUMB = {
    "top": "IMMORTAL", "bottom": "GRAINS?!", "bottom_size": 200,
    "badge": "60+", "badge_label": "microbe strains\nin homemade kefir", "badge_color": "#0EA5E9",
    "bg": ("#F0F9FF", "#7DD3FC"), "pip_mood": "surprised",
    "props": [("🥛", 1800, 540, 240, 0.15), ("🦠", 1780, 170, 170, 0.2), ("🦠", 1820, 900, 150, -0.3),
              ("🫙", 1010, 900, 220, 0.1)],
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


DARK = {"fill": "#312E81", "title_color": "white"}

CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hey! Down here! It's me, Pip. Yes, the pumpkin seed. I'm back.",
             {"mood": "happy", "wave": True}),
            ("P", "But today I'm just a guest reviewer, because the star of the show isn't a seed. It's a drink.",
             {"mood": "surprised", "jump": True}),
        ], "els": []},
        {"pip": PIP_R, "lines": [
            ("H", "Pip is right. Today we're talking about kefir: a tangy, fizzy, fermented milk drink. "
                  "Where it comes from, what's inside, what the science says, and the downsides nobody prints on the bottle.", {}),
            ("P", "Including the alcohol. Yes, really. Stay tuned.", {"mood": "smug"}),
        ], "els": [
            E("🥛", 420, 300, 200, at=[0, "kefir"], wobble=True),
            T("Kefir", 620, 300, 140, at=[0, "kefir"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 500, "w": 640, "h": 110, "emoji": "🏔️", "title": "Where it's from", "at": [0, "Where"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🔬", "title": "What science says", "at": [0, "science"]},
            {"type": "card", "x": 760, "y": 800, "w": 640, "h": 110, "emoji": "⚠️", "title": "The downsides", "at": [0, "downsides"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "grains", "title": "Grains That Aren't Grains", "emoji": "🌾", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Kefir comes from the Caucasus Mountains, between the Black Sea and the Caspian Sea.", {}),
            ("H", "It's made by adding kefir grains to milk, usually from cows, goats or sheep.", {}),
            ("P", "Grains? Like wheat? Finally, a fellow plant!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🏔️", 300, 270, 170, at=[0, "Caucasus"]),
            T("The Caucasus", 440, 250, 96, at=[0, "Caucasus"], font="fredoka", weight=700, color="green", anchor="l"),
            T("between the Black Sea and the Caspian Sea", 760, 380, 44, at=[0, "Black"], color="muted"),
            {"type": "card", "x": 500, "y": 640, "w": 560, "h": 160, "emoji": "⚪", "title": "Kefir grains",
             "at": [1, "grains"]},
            T("+", 860, 640, 110, at=[1, "milk"], font="fredoka", weight=700, color="orange"),
            E("🐄", 1000, 640, 120, at=[1, "cows"]),
            E("🐐", 1150, 640, 120, at=[1, "goats"]),
            E("🐑", 1300, 640, 120, at=[1, "sheep"]),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Sorry, Pip. Kefir grains aren't grains at all. They're colonies of bacteria and yeasts living together, "
                  "known as a SCOBY: a symbiotic culture of bacteria and yeast.",
             {"say": "Sorry, Pip. Kefir grains aren't grains at all. They're colonies of bacteria and yeasts living together, "
                     "known as a scoby: a symbiotic culture of bacteria and yeast."}),
            ("H", "They look like tiny cauliflower florets.", {}),
            ("P", "So they're not grains. They're a tiny city. I feel betrayed.", {"mood": "worried"}),
        ], "els": [
            {"type": "banner", "x": 760, "y": 170, "text": "NOT real grains", "color": "#DC2626", "at": [0, "all"]},
            {"type": "card", "x": 470, "y": 370, "w": 520, "h": 150, "emoji": "🦠", "title": "Bacteria", "at": [0, "bacteria"]},
            {"type": "card", "x": 1050, "y": 370, "w": 520, "h": 150, "emoji": "🍞", "title": "Yeasts", "at": [0, "yeasts"]},
            {"type": "card", "x": 760, "y": 580, "w": 1100, "h": 170, "emoji": "🏙️", "title": "SCOBY",
             "body": "Symbiotic Culture Of Bacteria and Yeast", "at": [0, "symbiotic"]},
            T("look like tiny cauliflower florets", 760, 760, 48, at=[1, "cauliflower"], color="ink", weight=600),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "There are two main types. Milk kefir is the classic: tangy, like a drinkable natural yogurt, "
                  "with protein, calcium and B vitamins.", {}),
            ("H", "Water kefir is fermented in sugar water, coconut water or fruit juice. It has no dairy at all, "
                  "so it's vegan and lactose-free. Some people call it probiotic champagne.", {}),
            ("P", "Probiotic champagne. Fancy. Does it come with a tiny monocle?", {"mood": "happy"}),
        ], "els": [
            E("🥛", 420, 260, 170, at=[0, "Milk"]),
            T("Milk kefir", 420, 400, 64, at=[0, "Milk"], font="fredoka", weight=700, color="green"),
            T("tangy, drinkable", 420, 470, 40, at=[0, "tangy"], color="muted"),
            {"type": "pill", "x": 420, "y": 560, "text": "protein · calcium · B vitamins", "color": "green", "at": [0, "protein"]},
            T("vs", 760, 330, 100, at=[1, "Water"], font="fredoka", weight=700, color="orange"),
            E("🥥", 1100, 260, 170, at=[1, "Water"]),
            T("Water kefir", 1100, 400, 64, at=[1, "Water"], font="fredoka", weight=700, color="#0369A1"),
            T("sugar water, coconut water, juice", 1100, 470, 36, at=[1, "sugar"], color="muted"),
            {"type": "pill", "x": 1100, "y": 560, "text": "no dairy · vegan · lactose-free", "color": "#0EA5E9", "at": [1, "dairy"]},
            {"type": "banner", "x": 760, "y": 750, "text": "“probiotic champagne”", "color": "#8B5CF6", "at": [1, "champagne"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "history", "title": "A 3,600-Year-Old Drink", "emoji": "📜", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Kefir is one of the oldest fermented drinks around. Kefir cheese was found on Bronze Age mummies "
                  "in China, about three thousand six hundred years old.", {}),
            ("H", "It's the oldest cheese ever found, and DNA analysis confirmed it was made with kefir grains.",
             {"say": "It's the oldest cheese ever found, and D N A analysis confirmed it was made with kefir grains."}),
            ("P", "Mummy cheese. That was not on my bingo card.", {"mood": "surprised"}),
        ], "els": [
            {"type": "stat", "x": 400, "y": 400, "w": 460, "h": 330, "value": 3600, "unit": "", "label": "years old",
             "emoji": "🏺", "at": [0, "thousand"]},
            {"type": "card", "x": 1030, "y": 320, "w": 620, "h": 170, "emoji": "🧀", "title": "Xiaohe cemetery",
             "body": "Tarim Basin, China", "at": [0, "China"]},
            {"type": "card", "x": 1030, "y": 530, "w": 620, "h": 170, "emoji": "🏆", "title": "Oldest cheese",
             "body": "ever found", "at": [1, "oldest"]},
            {"type": "pill", "x": 760, "y": 760, "text": "DNA: made with kefir grains", "color": "green", "at": [1, "DNA"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "In the Caucasus, Ossetian tribes hung milk in goatskin bags in doorways, "
                  "so everyone walking past would knock the bag and keep it fermenting.", {}),
            ("H", "The grains, called the Grains of the Prophet, were a symbol of wealth and were never given to outsiders. For centuries.", {}),
            ("P", "Knock knock. Who's there? Fermentation.", {"mood": "smug"}),
        ], "els": [
            E("🚪", 330, 330, 190, at=[0, "doorways"], wobble=True),
            {"type": "card", "x": 900, "y": 330, "w": 900, "h": 180, "emoji": "🐐", "title": "Goatskin bags",
             "body": "hung in doorways · knocked in passing", "at": [0, "goatskin"]},
            {"type": "card", "x": 760, "y": 580, "w": 1100, "h": 180, "emoji": "🤫", "title": "“Grains of the Prophet”",
             "body": "a symbol of wealth · never given to outsiders", "at": [1, "Prophet"]},
            {"type": "pill", "x": 760, "y": 770, "text": "kept secret for centuries", "color": "orange", "at": [1, "centuries"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Then came the wildest chapter. In the early nineteen hundreds, a Moscow dairy sent a young employee, "
                  "Irina Sakharova, to charm a local prince into giving her grains.", {}),
            ("H", "He refused. Then tribesmen kidnapped her so she would marry him. "
                  "She was rescued, and the case reached Tsar Nicholas the Second.", {}),
            ("H", "His ruling? The prince owed Irina ten pounds of kefir grains. "
                  "And in September nineteen oh eight, kefir went on sale in Moscow.", {}),
            ("P", "Kidnapping, a tsar, and a payout in kefir. Somebody make this a movie!", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("The Irina Sakharova affair", 760, 160, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 430, "y": 320, "w": 620, "h": 140, "emoji": "🏭", "title": "Moscow dairy",
             "body": "sends Irina for grains", "at": [0, "Irina"]},
            {"type": "card", "x": 1090, "y": 320, "w": 620, "h": 140, "emoji": "🤴", "title": "The prince",
             "body": "says no", "at": [1, "refused"]},
            {"type": "card", "x": 430, "y": 500, "w": 620, "h": 140, "emoji": "🐎", "title": "Kidnapped",
             "body": "then rescued", "at": [1, "kidnapped"]},
            {"type": "card", "x": 1090, "y": 500, "w": 620, "h": 140, "emoji": "👑", "title": "The tsar rules",
             "body": "pay 10 lb of grains", "at": [2, "ten"]},
            {"type": "banner", "x": 760, "y": 720, "text": "Sept 1908: kefir on sale in Moscow", "color": "#F97316",
             "at": [2, "September"]},
        ], "pip_hide": True},
        {"pip": PIP_R, "lines": [
            ("H", "Now the strangest part. Scientists found over fifty species of microbes in kefir grains, "
                  "yet nobody can build the grains from scratch in a lab.", {}),
            ("H", "The grains also have no programmed cell death. Feed them fresh milk and they keep growing: "
                  "by more than five hundred percent in two weeks, under ideal conditions.", {}),
            ("P", "Immortal milk pets. Okay, that's genuinely cooler than me.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 760, "y": 210, "w": 1100, "h": 150, "emoji": "🧪", "title": "50+ species of microbes",
             "body": "and still impossible to rebuild in a lab", "at": [0, "fifty"]},
            {"type": "card", "x": 500, "y": 470, "w": 620, "h": 190, "emoji": "♾️", "title": "No cell death",
             "body": "keeps growing on milk", "at": [1, "death"]},
            {"type": "stat", "x": 1120, "y": 470, "w": 520, "h": 300, "value": 500, "unit": "%", "label": "growth in 2 weeks (ideal)",
             "emoji": "📈", "at": [1, "five"]},
            {"type": "banner", "x": 760, "y": 760, "text": "Biologically “immortal”", "color": "#8B5CF6", "at": [1, "ideal"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "cup", "title": "What's in a Cup?", "emoji": "🥛", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So what's in a cup? Our serving is one cup, about two hundred forty milliliters, of cow's milk kefir.", {}),
            ("H", "On average, you get one hundred to one hundred twenty calories, about nine grams of complete protein, "
                  "and seven to ten grams of carbs.", {}),
            ("P", "Ranges? Kefir, commit to something!", {"mood": "smug"}),
            ("H", "Fat: five to eight grams in whole-milk kefir, under two in low-fat.", {}),
        ], "els": [
            {"type": "pill", "x": 760, "y": 170, "text": "1 cup ≈ 240 ml · cow's milk kefir", "color": "green", "at": [0, "cup"]},
            {"type": "stat", "x": 330, "y": 420, "w": 400, "h": 300, "value": 0, "text": "100–120", "vsize": 84,
             "label": "calories", "emoji": "🔥", "at": [1, "calories"]},
            {"type": "stat", "x": 760, "y": 420, "w": 400, "h": 300, "value": 9, "unit": " g", "label": "complete protein",
             "emoji": "💪", "at": [1, "protein"]},
            {"type": "stat", "x": 1190, "y": 420, "w": 400, "h": 300, "value": 0, "text": "7–10 g", "vsize": 90,
             "label": "carbs", "emoji": "🍞", "at": [1, "carbs"]},
            {"type": "card", "x": 760, "y": 720, "w": 1100, "h": 150, "emoji": "🧈", "title": "Fat: 5–8 g whole, under 2 g low-fat",
             "at": [3, "Fat"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Now vitamins and minerals, as percent of the daily value.", {}),
            ("H", "Vitamin B12, close to thirty percent. Riboflavin, that's vitamin B2, about twenty-five. "
                  "Calcium, about twenty. And phosphorus, about twenty.",
             {"say": "Vitamin B 12, close to thirty percent. Riboflavin, that's vitamin B 2, about twenty-five. "
                     "Calcium, about twenty. And phosphorus, about twenty."}),
            ("P", "Thirty percent B12? Okay, I'm officially jealous.", {"mood": "worried", "say": "Thirty percent B 12? Okay, I'm officially jealous."}),
            ("H", "That B12 is great news for vegetarians. Not vegans, though: it's still milk.",
             {"say": "That B 12 is great news for vegetarians. Not vegans, though: it's still milk."}),
        ], "els": [
            T("% Daily Value per cup", 760, 175, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 260, "y": 300, "w": 1000, "row_h": 105, "max": 34, "rows": [
                {"label": "B12", "value": 30, "text": "~30%", "color": "#8B5CF6", "at": [1, "B12"]},
                {"label": "Riboflavin", "value": 25, "text": "~25%", "color": "#F97316", "at": [1, "Riboflavin"]},
                {"label": "Calcium", "value": 20, "text": "~20%", "color": "#0EA5E9", "at": [1, "Calcium"]},
                {"label": "Phosphorus", "value": 20, "text": "~20%", "color": "#14B8A6", "at": [1, "phosphorus"]},
            ]},
            {"type": "pill", "x": 760, "y": 790, "text": "great for vegetarians (not vegans)", "color": "green", "at": [3, "vegetarians"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "probiotics", "title": "Probiotic Powerhouse", "emoji": "🦠", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Now the headline benefit: probiotics. A typical factory-made yogurt has about two to five strains of bacteria.", {}),
            ("H", "Store-bought kefir usually has seven to nine. And homemade kefir from real grains can have thirty, up to more than sixty.", {}),
            ("P", "Sixty roommates in one cup. And I thought my pumpkin was crowded.", {"mood": "surprised"}),
        ], "els": [
            T("Microbe strains", 760, 175, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 230, "y": 340, "w": 1080, "row_h": 140, "max": 62, "suffix": "", "rows": [
                {"label": "Yogurt", "value": 5, "text": "2–5", "color": "#94A3B8", "at": [0, "yogurt"]},
                {"label": "Store kefir", "value": 9, "text": "7–9", "color": "#0EA5E9", "at": [1, "Store"]},
                {"label": "Homemade", "value": 60, "text": "30–60+", "color": "#8B5CF6", "at": [1, "homemade"]},
            ]},
            T("homemade = kefir from real grains", 760, 800, 38, at=[1, "grains"], color="muted"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And it's not just the number. Unlike yogurt, kefir also contains beneficial yeasts, which yogurt doesn't have at all.", {}),
            ("H", "That richness helps balance the gut microbiome, supports metabolism, and helps reduce inflammation.", {}),
        ], "els": [
            {"type": "check", "x": 120, "y": 230, "w": 1300, "ok": False, "text": "Yogurt: bacteria only", "at": [0, "yogurt"]},
            {"type": "check", "x": 120, "y": 370, "w": 1300, "ok": True, "text": "Kefir: bacteria + beneficial yeasts", "at": [0, "yeasts"]},
            {"type": "card", "x": 300, "y": 640, "w": 440, "h": 120, "emoji": "⚖️", "title": "Gut balance", "at": [1, "balance"]},
            {"type": "card", "x": 780, "y": 640, "w": 440, "h": 120, "emoji": "⚡", "title": "Metabolism", "at": [1, "metabolism"]},
            {"type": "card", "x": 1260, "y": 640, "w": 440, "h": 120, "emoji": "🧯", "title": "Inflammation", "at": [1, "inflammation"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "This also explains kefir's lactose trick. The bacteria break much of the lactose down into lactic acid, "
                  "and kefir brings live lactase enzymes too.", {}),
            ("H", "In one clinical study, kefir cut breath hydrogen, a marker of undigested lactose, threefold compared with regular milk. "
                  "And gas symptoms dropped by half.", {}),
            ("P", "Kefir: the dairy that does the digesting for you.", {"mood": "smug"}),
        ], "els": [
            T("The lactose trick", 760, 170, 72, at=0, font="fredoka", weight=700, color="green"),
            {"type": "pill", "x": 760, "y": 270, "text": "lactose becomes lactic acid + live lactase", "color": "green", "at": [0, "lactic"]},
            {"type": "stat", "x": 500, "y": 520, "w": 500, "h": 300, "value": 3, "unit": "×", "label": "less breath hydrogen",
             "emoji": "🌬️", "at": [1, "threefold"]},
            {"type": "stat", "x": 1050, "y": 520, "w": 500, "h": 300, "value": 50, "unit": "%", "label": "fewer gas symptoms",
             "emoji": "💨", "at": [1, "half"]},
            {"type": "pill", "x": 760, "y": 790, "text": "most lactose-intolerant people do fine", "color": "ok", "at": [1, "half"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "benefits", "title": "Benefits, Fact-Checked", "emoji": "🔎", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now, the other benefits, fact-checked.", {}),
            ("H", "Bones: kefir pairs calcium with vitamin K2, made during fermentation, which helps send calcium into bone. "
                  "And that calcium is absorbed better than from regular milk.",
             {"say": "Bones: kefir pairs calcium with vitamin K 2, made during fermentation, which helps send calcium into bone. "
                     "And that calcium is absorbed better than from regular milk."}),
            ("H", "Cholesterol: several clinical studies linked regular kefir to lower LDL, the bad cholesterol.",
             {"say": "Cholesterol: several clinical studies linked regular kefir to lower L D L, the bad cholesterol."}),
            ("P", "Ooh, actual human studies. Fancy.", {"mood": "happy"}),
        ], "els": [
            T("How strong is the evidence?", 760, 170, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 760, "y": 380, "w": 1100, "h": 190, "emoji": "🦴", "title": "Bones: calcium + vitamin K2",
             "body": "and better calcium absorption than plain milk", "at": [1, "Bones"]},
            {"type": "card", "x": 760, "y": 640, "w": 1100, "h": 190, "emoji": "❤️", "title": "Cholesterol: lower LDL",
             "body": "linked in several clinical studies", "at": [2, "Cholesterol"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Blood sugar: some small clinical studies suggest better control. Promising, but it needs bigger studies.", {}),
            ("H", "Mood: about ninety percent of your serotonin is made in the gut, and regular probiotics like kefir "
                  "have been linked to less anxiety and stress.", {}),
            ("H", "Germs: kefir strains, and its sugar kefiran, held back Salmonella, H. pylori and Candida. But mostly in lab studies.",
             {"say": "Germs: kefir strains, and its sugar, keffy-ran, held back Salmonella, H. pylori and Candida. But mostly in lab studies."}),
        ], "els": [
            {"type": "check", "x": 120, "y": 230, "w": 1420, "ok": True, "text": "Blood sugar: small clinical studies", "at": [0, "Blood"]},
            {"type": "check", "x": 120, "y": 370, "w": 1420, "ok": True, "text": "Mood: linked via the gut-brain axis", "at": [1, "Mood"]},
            {"type": "check", "x": 120, "y": 510, "w": 1420, "ok": True, "text": "Germs: Salmonella, H. pylori, Candida", "at": [2, "Salmonella"]},
            {"type": "pill", "x": 760, "y": 660, "text": "promising, needs bigger studies", "color": "orange", "at": [0, "Promising"]},
            {"type": "pill", "x": 760, "y": 760, "text": "germ-fighting: mostly lab studies", "color": "orange", "at": [2, "lab"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And then the big claims. Anti-cancer effects, and help with asthma and allergies, come mainly from lab and animal studies.", {}),
            ("H", "So no treatment recommendation can be drawn from them.", {}),
            ("P", "Translation: cool science, not a cure. Got it.", {"mood": "worried"}),
        ], "els": [
            {"type": "check", "x": 120, "y": 260, "w": 1300, "ok": False, "text": "Cancer: lab and animal studies only", "at": [0, "cancer"]},
            {"type": "check", "x": 120, "y": 400, "w": 1300, "ok": False, "text": "Asthma & allergies: animal studies", "at": [0, "asthma"]},
            {"type": "banner", "x": 760, "y": 620, "text": "Interesting, not a cure", "color": "#475569", "at": [1, "treatment"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "quirks", "title": "The Downsides", "emoji": "⚠️", "scenes": [
        {"pip": PIP_C, "lines": [
            ("H", "Alright. Kefir has real downsides, and some of them matter a lot for certain people.", {}),
            ("P", "As a fellow superfood, I prefer the word... quirks.", {"mood": "smug"}),
        ], "els": [
            T("Downsides", 960, 140, 100, at=0, font="fredoka", weight=700, color="red", strike=[1, "quirks"]),
            T("Quirks", 960, 255, 84, at=[1, "quirks"], font="fredoka", weight=700, color="green", rot=-0.06),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Quirk number one, and almost everyone gets it: bloating, gas and rumbling "
                  "for a few days up to two weeks, while your gut adjusts.", {}),
            ("H", "The fix: start with a quarter cup a day for a week, then double it. "
                  "Jump straight to a full cup, and you'll almost always feel it.", {}),
            ("P", "Go slow. Respect the ferment.", {"mood": "smug", "jump": True}),
        ], "els": [
            T("#1 The adjustment period", 760, 170, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 760, "y": 380, "w": 1100, "h": 190, "emoji": "🎈", "title": "Bloating, gas, rumbling",
             "body": "a few days to about two weeks", "at": [0, "bloating"]},
            {"type": "card", "x": 760, "y": 640, "w": 1100, "h": 190, "emoji": "🥄", "title": "Start with 1/4 cup a day",
             "body": "for a week, then double it", "at": [1, "quarter"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Number two: the taste. Real kefir is sour, a little fizzy, and slightly yeasty, like beer or sourdough.", {}),
            ("H", "Number three: added sugar. Flavored kefir often has twelve to twenty grams of sugar per cup. Read the label and pick plain.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 300, "w": 1100, "h": 190, "emoji": "🍋", "title": "#2 Sour taste",
             "body": "tangy · fizzy · a bit yeasty", "at": 0},
            {"type": "card", "x": 760, "y": 560, "w": 1100, "h": 190, "emoji": "🍓", "title": "#3 Added sugar",
             "body": "flavored: 12–20 g per cup · pick plain", "at": 1},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Number four: histamine. Kefir is rich in it. If you're sensitive, it can cause headaches, "
                  "itching, flushing or a stuffy nose. Longer ferments have more.", {}),
            ("H", "Kefir also contains tyramine. If you take M A O inhibitors, a type of antidepressant, "
                  "avoid fermented foods like kefir unless your doctor says otherwise.",
             {"say": "Kefir also contains tyramine. If you take M A O inhibitors, a type of antidepressant, "
                     "avoid fermented foods like kefir unless your doctor says otherwise."}),
        ], "els": [
            {"type": "card", "x": 760, "y": 300, "w": 1100, "h": 190, "emoji": "🤧", "title": "#4 Histamine",
             "body": "headaches · itching · flushing · stuffy nose", "at": 0},
            {"type": "pill", "x": 760, "y": 450, "text": "longer ferment = more histamine", "color": "orange", "at": [0, "Longer"]},
            {"type": "card", "x": 760, "y": 640, "w": 1100, "h": 190, "emoji": "💊", "title": "Tyramine + MAOI drugs",
             "body": "avoid unless your doctor says otherwise", "at": [1, "tyramine"], "fill": "#FEE2E2"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Number five: kefir is usually fine with lactose intolerance, but it is not safe "
                  "if you're allergic to milk protein. Water kefir is the alternative.", {}),
            ("H", "Severely weakened immunity? Check with a doctor. Kidney disease? Ask a renal dietitian. "
                  "It's not for babies under one. And keep it two hours apart from antibiotics.", {}),
            ("P", "That's a lot of fine print for a cup of milk.", {"mood": "worried"}),
        ], "els": [
            {"type": "check", "x": 120, "y": 190, "w": 1360, "ok": True, "text": "Lactose intolerance: usually fine", "at": [0, "lactose"]},
            {"type": "check", "x": 120, "y": 320, "w": 1360, "ok": False, "text": "Milk protein allergy: not safe", "at": [0, "allergic"]},
            {"type": "card", "x": 450, "y": 520, "w": 640, "h": 140, "emoji": "🩺", "title": "Weak immunity",
             "body": "ask your doctor", "at": [1, "immunity"]},
            {"type": "card", "x": 1130, "y": 520, "w": 640, "h": 140, "emoji": "🫘", "title": "Kidney disease",
             "body": "ask a renal dietitian", "at": [1, "kidney"]},
            {"type": "card", "x": 450, "y": 700, "w": 640, "h": 140, "emoji": "👶", "title": "Babies under 1",
             "body": "not for them", "at": [1, "babies"]},
            {"type": "card", "x": 1130, "y": 700, "w": 640, "h": 140, "emoji": "💊", "title": "Antibiotics",
             "body": "keep 2+ hours apart", "at": [1, "antibiotics"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "alcohol", "title": "The Alcohol Surprise", "emoji": "🍺", "dark": True, "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Here's the downside people know least about. Kefir's yeasts make carbon dioxide, and alcohol. Yogurt has none.", {}),
            ("P", "Wait. Kefir is a party drink?", {"mood": "surprised", "jump": True}),
            ("H", "Not quite. Store-bought kefir usually has zero point zero five to zero point five percent, like fresh orange juice.", {}),
            ("H", "But a long, warm homemade ferment in a sealed jar can reach about one to two percent, sometimes more.", {}),
        ], "els": [
            T("Yeasts make CO2 + alcohol", 760, 170, 64, at=[0, "yeasts"], font="fredoka", weight=700, color="#FDE68A"),
            {"type": "stat", "x": 470, "y": 470, "w": 560, "h": 320, "value": 0, "text": "0.05–0.5%", "vsize": 84,
             "label": "store-bought", "emoji": "🏪", "at": [2, "Store"], "color": "#16A34A"},
            T("≈ fresh orange juice or bread", 470, 700, 36, at=[2, "orange"], color="#C7D2FE"),
            {"type": "stat", "x": 1100, "y": 470, "w": 560, "h": 320, "value": 0, "text": "1–2%+", "vsize": 96,
             "label": "homemade, long + warm", "emoji": "🫙", "at": [3, "homemade"], "color": "#EA580C"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Who should care? People who avoid alcohol for religion, addiction, or belief.", {}),
            ("H", "And in pregnancy, for maximum caution, choose pasteurized store-bought kefir. Homemade isn't pasteurized, which matters even more.", {}),
            ("H", "Driving? Not a concern. To keep alcohol low at home: ferment for less time, somewhere cooler, under a cloth.", {}),
            ("P", "Short, cool, and breathable. Like my ideal vacation.", {"mood": "sleepy"}),
        ], "els": [
            {"type": "card", "x": 470, "y": 220, "w": 640, "h": 150, "emoji": "🙏", "title": "Avoiding alcohol",
             "body": "religion · addiction · belief", "at": [0, "avoid"], **DARK},
            {"type": "card", "x": 1100, "y": 220, "w": 500, "h": 150, "emoji": "🤰", "title": "Pregnancy",
             "body": "pick pasteurized", "at": [1, "pregnancy"], **DARK},
            {"type": "pill", "x": 760, "y": 380, "text": "driving: not a real concern", "color": "ok", "at": [2, "Driving"]},
            T("Less alcohol at home:", 760, 500, 52, at=[2, "low"], font="fredoka", weight=600, color="#FDE68A"),
            {"type": "card", "x": 330, "y": 660, "w": 420, "h": 140, "emoji": "⏱️", "title": "Shorter", "at": [2, "less"], **DARK},
            {"type": "card", "x": 770, "y": 660, "w": 420, "h": 140, "emoji": "❄️", "title": "Cooler", "at": [2, "cooler"], **DARK},
            {"type": "card", "x": 1210, "y": 660, "w": 420, "h": 140, "emoji": "🧺", "title": "Cloth cover", "at": [2, "cloth"], **DARK},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "howto", "title": "How to Use It", "emoji": "🥣", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "In Eastern Europe, kefir is an everyday staple: at breakfast, in school meals, even in cold soups.", {}),
            ("H", "Try it in a smoothie with banana and berries, or instead of yogurt in dressings and marinades, where its acidity tenderizes meat.", {}),
        ], "els": [
            E("🍳", 330, 270, 150, at=[0, "breakfast"]),
            T("breakfast", 330, 380, 42, at=[0, "breakfast"], font="fredoka", weight=600),
            E("🏫", 760, 270, 150, at=[0, "school"]),
            T("school meals", 760, 380, 42, at=[0, "school"], font="fredoka", weight=600),
            E("🥣", 1190, 270, 150, at=[0, "soups"]),
            T("cold soups", 1190, 380, 42, at=[0, "soups"], font="fredoka", weight=600),
            {"type": "card", "x": 330, "y": 640, "w": 420, "h": 170, "emoji": "🍌", "title": "Smoothie", "at": [1, "smoothie"]},
            {"type": "card", "x": 770, "y": 640, "w": 420, "h": 170, "emoji": "🥗", "title": "Dressings", "at": [1, "dressings"]},
            {"type": "card", "x": 1210, "y": 640, "w": 420, "h": 170, "emoji": "🍖", "title": "Marinades", "at": [1, "marinades"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "You can bake with it like buttermilk. But heat above forty-five degrees Celsius, one hundred thirteen Fahrenheit, "
                  "destroys most of the probiotics. The protein and calcium stay.", {}),
            ("H", "Drain it through cheesecloth for twelve to twenty-four hours, and you get a soft kefir cheese, like labneh.",
             {"say": "Drain it through cheesecloth for twelve to twenty-four hours, and you get a soft kefir cheese, like lab-nay."}),
            ("P", "Kefir cheese! The mummies would be proud.", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "card", "x": 460, "y": 260, "w": 680, "h": 170, "emoji": "🧁", "title": "Baking",
             "body": "use it like buttermilk", "at": [0, "bake"]},
            {"type": "card", "x": 760, "y": 470, "w": 1100, "h": 170, "emoji": "🔥", "title": "Above 45°C / 113°F",
             "body": "probiotics gone · protein & calcium stay", "at": [0, "Celsius"], "fill": "#FEE2E2"},
            {"type": "card", "x": 760, "y": 690, "w": 1100, "h": 170, "emoji": "🧀", "title": "Kefir cheese",
             "body": "drain 12–24 hours · like labneh", "at": [1, "cheesecloth"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "How much? About a cup a day, starting with a quarter cup.", {}),
            ("H", "Got grains? Feed them fresh milk every twenty-four hours at room temperature. "
                  "On vacation, they keep in a cup of milk in the fridge for up to three weeks.", {}),
            ("P", "Even immortal pets need a sitter.", {"mood": "smug"}),
        ], "els": [
            {"type": "stat", "x": 400, "y": 400, "w": 460, "h": 330, "value": 0, "text": "1 cup", "vsize": 100,
             "label": "a day (start with 1/4)", "emoji": "🥛", "at": [0, "cup"]},
            {"type": "card", "x": 1020, "y": 320, "w": 720, "h": 170, "emoji": "🍼", "title": "Feed every 24 h",
             "body": "fresh milk · 20–25°C", "at": [1, "twenty"]},
            {"type": "card", "x": 1020, "y": 540, "w": 720, "h": 170, "emoji": "🧊", "title": "Vacation mode",
             "body": "up to 3 weeks in the fridge", "at": [1, "vacation"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 9
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: kefir is a probiotic powerhouse, with yeasts that yogurt lacks.", {}),
            ("H", "Two: a cup brings protein, calcium, B12 and riboflavin.",
             {"say": "Two: a cup brings protein, calcium, B 12 and riboflavin."}),
            ("H", "Three: some benefits are still only lab and animal findings.", {}),
            ("H", "Four: start with a quarter cup, pick it plain, and know the downsides.", {}),
        ], "els": [
            {"type": "check", "x": 120, "y": 200, "w": 1400, "ok": True, "text": "Probiotic powerhouse: bacteria + yeasts", "at": 1},
            {"type": "check", "x": 120, "y": 340, "w": 1400, "ok": True, "text": "Protein, calcium, B12, riboflavin", "at": 2},
            {"type": "check", "x": 120, "y": 480, "w": 1400, "ok": True, "text": "Some benefits: lab & animal only", "at": 3},
            {"type": "check", "x": 120, "y": 620, "w": 1400, "ok": True, "text": "Start with 1/4 cup, pick plain", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("H", "So, Pip. Your verdict as our guest reviewer?", {}),
            ("P", "Ancient, immortal, and full of roommates. Five stars. Grudgingly.", {"mood": "smug"}),
            ("P", "Just don't tell the other seeds.", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 1},
            E("⭐", 760, 170, 90, at=[1, "Five"]),
            E("⭐", 860, 170, 90, at=[1, "Five"]),
            E("⭐", 960, 170, 90, at=[1, "Five"]),
            E("⭐", 1060, 170, 90, at=[1, "Five"]),
            E("⭐", 1160, 170, 90, at=[1, "Five"]),
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For all the details, read the full article "
                  "at wiseplate dot blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For all the details, read the full article "
                     "at wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Start with a quarter cup!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/kefir", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
