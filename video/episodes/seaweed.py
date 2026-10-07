"""Seaweed explainer (English), based on https://wiseplate.blog/food/seaweed/

Numbers are the article's: iodine in micrograms (mcg) per gram of DRIED
seaweed, adult intake 150 mcg/day, safe upper limit 1,100 mcg/day. Keep them
in sync with content/food/seaweed.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Seaweed: Superfood or Iodine Overload?"
SLUG = "seaweed"
ARTICLE = "https://wiseplate.blog/en/food/seaweed/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "SEAWEED", "top_size": 190, "bottom": "TOO MUCH IODINE?", "bottom_size": 130,
         "badge": "2,500", "badge_size": 120, "badge_label": "mcg iodine\nin 1 g kelp", "badge_color": "#0EA5E9",
         "scatter": "🌊", "hero": "🍙", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 110, "root": 62, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "meet":     {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "iodine":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "goodies":  {"bpm": 116, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.8, "bright": 1.3},
    "b12":      {"bpm": 84, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howmuch":  {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "careful":  {"bpm": 96, "root": 64, "prog": ["vi", "IV", "I", "V"], "density": 0.6},
    "outro":    {"bpm": 110, "root": 62, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#ECFEFF", "meet": "#E0F2FE", "iodine": "#F0FDFA", "goodies": "#ECFCCB",
    "b12": "#1E1B4B", "catches": "#FEE2E2", "howmuch": "#E0F2FE", "careful": "#FEF3C7",
    "outro": "#ECFEFF",
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
            ("P", "Ahoy! Pip the pumpkin seed here. Today I'm going to the beach. Well, under it.", {"mood": "happy", "wave": True}),
            ("P", "Our guest has no roots, no seeds, and lives in the ocean. Rude. It's seaweed!", {"mood": "surprised", "jump": True}),
        ], "els": [
            E("🌊", 960, 200, 160, at=[1, "ocean"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today: seaweed. Why it's the richest food source of iodine, what else it brings, "
                  "and why that same iodine is also its biggest catch.", {}),
            ("H", "Then the practical part: how much you can actually eat in a day.", {}),
            ("P", "A superfood with a warning label. My favorite kind of drama.", {"mood": "smug"}),
        ], "els": [
            E("🌿", 420, 330, 200, at=0, wobble=True),
            T("Seaweed", 640, 300, 140, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🧂", "title": "Iodine", "at": [0, "iodine"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "⚠️", "title": "The catch", "at": [0, "catch"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "📏", "title": "How much a day", "at": [1, "much"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "meet", "title": "Meet the Sea Vegetables", "emoji": "🌊", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Seaweed, also called sea vegetables, includes types like nori, wakame, kelp, dulse and chlorella. "
                  "It's been eaten in Asia for thousands of years.",
             {"say": "Seaweed, also called sea vegetables, includes types like nori, wah-kah-meh, kelp, dulse and chlorella. "
                     "It's been eaten in Asia for thousands of years."}),
            ("H", "In the West it's been getting more attention lately, because of a mineral profile you won't find in most land foods.", {}),
        ], "els": [
            T("Sea vegetables", 760, 170, 60, at=0, font="fredoka", weight=600, color="green"),
            {"type": "pill", "x": 340, "y": 330, "text": "nori", "color": "green", "at": [0, "nori"]},
            {"type": "pill", "x": 620, "y": 330, "text": "wakame", "color": "#0EA5E9", "at": [0, "wakame"]},
            {"type": "pill", "x": 900, "y": 330, "text": "kelp", "color": "#92400E", "at": [0, "kelp"]},
            {"type": "pill", "x": 1150, "y": 330, "text": "dulse", "color": "#DC2626", "at": [0, "dulse"]},
            {"type": "pill", "x": 760, "y": 440, "text": "chlorella", "color": "#14B8A6", "at": [0, "chlorella"]},
            {"type": "card", "x": 760, "y": 660, "w": 1000, "h": 170, "emoji": "🏯", "title": "Thousands of years in Asia",
             "at": [0, "Asia"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Biologically, seaweeds photosynthesize, and they soak up minerals from the sea in very high concentrations.", {}),
            ("H", "Hundreds of species are eaten, and each one has a different mix of pigments, polysaccharides and minerals.",
             {"say": "Hundreds of species are eaten, and each one has a different mix of pigments, polly-sack-a-rides and minerals."}),
            ("P", "So it's basically a sponge that went to culinary school.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 170, "emoji": "☀️", "title": "Photosynthesis", "at": 0},
            {"type": "card", "x": 720, "y": 430, "w": 1000, "h": 170, "emoji": "🧲", "title": "Soaks up sea minerals",
             "at": [0, "minerals"]},
            {"type": "card", "x": 720, "y": 650, "w": 1000, "h": 170, "emoji": "🎨", "title": "Hundreds of species",
             "body": "pigments · polysaccharides · minerals", "at": [1, "Hundreds"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "iodine", "title": "The Iodine King", "emoji": "🧂", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Here's the big one. Seaweed is the richest natural food source of iodine.", {}),
            ("H", "Iodine is essential for your thyroid. It's needed to make the thyroid hormones T3 and T4, "
                  "and for brain development in babies, before and after birth.",
             {"say": "Iodine is essential for your thyroid. It's needed to make the thyroid hormones T 3 and T 4, "
                     "and for brain development in babies, before and after birth."}),
            ("H", "An adult needs one hundred fifty micrograms a day. The safe upper limit is one thousand one hundred.", {}),
        ], "els": [
            T("Iodine", 720, 180, 120, at=0, font="fredoka", weight=700, color="#0EA5E9"),
            {"type": "pill", "x": 470, "y": 340, "text": "thyroid: T3 + T4", "color": "#7C3AED", "at": [1, "thyroid"]},
            {"type": "pill", "x": 1000, "y": 340, "text": "baby brains", "color": "#EC4899", "at": [1, "brain"]},
            {"type": "stat", "x": 470, "y": 620, "w": 460, "h": 280, "value": 150, "unit": " mcg", "label": "you need a day",
             "emoji": "✅", "at": [2, "fifty"]},
            {"type": "stat", "x": 1000, "y": 620, "w": 460, "h": 280, "value": 1100, "unit": " mcg", "label": "safe upper limit",
             "emoji": "🛑", "at": [2, "limit"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Now look how much the types differ. Iodine in micrograms, per gram of dried seaweed.", {}),
            ("H", "Dulse: ten to thirty. Nori: sixteen to forty-three. Wakame: forty to eighty.", {}),
            ("H", "And kombu, or kelp: five hundred to two thousand five hundred. In a single gram.", {}),
            ("P", "Kelp, buddy. That bar is leaving the screen.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("Iodine per 1 g dried (mcg)", 760, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 160, "y": 300, "w": 1300, "row_h": 130, "max": 3200, "unit": "", "rows": [
                {"label": "Dulse", "value": 30, "text": "10–30", "color": "#DC2626", "at": [1, "Dulse"]},
                {"label": "Nori", "value": 43, "text": "16–43", "color": "#16A34A", "at": [1, "Nori"]},
                {"label": "Wakame", "value": 80, "text": "40–80", "color": "#0EA5E9", "at": [1, "Wakame"]},
                {"label": "Kelp", "value": 2500, "text": "500–2,500", "color": "#92400E", "at": [2, "kombu"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "That's the whole story of seaweed in one chart. Nori and wakame give you a useful amount. "
                  "One gram of kelp can be more than twice the upper limit.", {}),
            ("H", "The gap between types is a hundredfold or more. So with seaweed, the question is never just how much. "
                  "It's which one.", {}),
            ("P", "Which one. Got it. Not all seaweed is created equal. Unlike seeds, who are all perfect.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 450, "y": 300, "w": 560, "h": 200, "emoji": "🍙", "title": "Nori, wakame",
             "body": "a useful amount", "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 1060, "y": 300, "w": 560, "h": 200, "emoji": "🟤", "title": "1 g kelp",
             "body": "over 2× the upper limit", "at": [0, "kelp"], "fill": "#FEE2E2"},
            {"type": "banner", "x": 760, "y": 620, "text": "Not how much. Which one.", "color": "#0EA5E9", "at": [1, "which"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "goodies", "title": "The Other Goodies", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Beyond iodine: fucoidan. It's a sulfated polysaccharide found only in brown seaweeds, like kelp and wakame.",
             {"say": "Beyond iodine: foo-coy-dan. It's a sulfated polly-sack-a-ride found only in brown seaweeds, like kelp and wah-kah-meh."}),
            ("H", "It's been studied for antiviral, anti-tumor and anti-clotting activity. "
                  "And early evidence suggests it supports natural killer cells in the immune system.", {}),
            ("H", "Early evidence, mind you. Not proven treatments.", {}),
        ], "els": [
            T("Fucoidan", 720, 180, 110, at=0, font="fredoka", weight=700, color="#92400E"),
            T("brown seaweeds only: kelp, wakame", 720, 290, 46, at=[0, "brown"], color="muted"),
            {"type": "pill", "x": 380, "y": 430, "text": "antiviral", "color": "#0EA5E9", "at": [1, "antiviral"]},
            {"type": "pill", "x": 730, "y": 430, "text": "anti-tumor", "color": "#7C3AED", "at": [1, "tumor"]},
            {"type": "pill", "x": 1100, "y": 430, "text": "anti-clotting", "color": "#DC2626", "at": [1, "clotting"]},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 170, "emoji": "🛡️", "title": "Natural killer cells",
             "body": "early evidence, not proven", "at": [1, "killer"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Then carrageenan and alginates, polysaccharides from red and red-brown seaweeds. "
                  "They can bind heavy metals and slow their absorption in the gut. A gentle detox effect.",
             {"say": "Then carra-geenan and al-gin-ates, polly-sack-a-rides from red and red brown seaweeds. "
                     "They can bind heavy metals and slow their absorption in the gut. A gentle detox effect."}),
            ("H", "And pigments. Fucoxanthin, a carotenoid found only in brown seaweed, is anti-inflammatory, "
                  "with early anti-cancer activity in studies.",
             {"say": "And pigments. Foo-co-zanthin, a carotenoid found only in brown seaweed, is anti inflammatory, "
                     "with early anti cancer activity in studies."}),
            ("H", "And phycocyanin, in blue-green algae like spirulina, is an antioxidant and anti-inflammatory.",
             {"say": "And fy-co-sigh-a-nin, in blue green algae like spirulina, is an antioxidant and anti inflammatory."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1100, "h": 170, "emoji": "🧲", "title": "Carrageenan + alginates",
             "body": "bind heavy metals in the gut", "at": 0},
            {"type": "card", "x": 720, "y": 450, "w": 1100, "h": 170, "emoji": "🟫", "title": "Fucoxanthin",
             "body": "anti-inflammatory · early studies", "at": [1, "pigments"]},
            {"type": "card", "x": 720, "y": 670, "w": 1100, "h": 170, "emoji": "🔵", "title": "Phycocyanin",
             "body": "antioxidant · spirulina", "at": [2, "spirulina"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "And the sea minerals. Around fifty-six different minerals, in a highly available form.", {}),
            ("H", "Magnesium, calcium, iron, potassium, manganese and selenium, at levels higher than most land foods.", {}),
            ("H", "Plus, seaweed is very low in calories, and has soluble fiber.", {}),
            ("P", "Fifty-six minerals. I have, like, four. And I'm proud of them.", {"mood": "worried"}),
        ], "els": [
            {"type": "stat", "x": 400, "y": 380, "w": 440, "h": 320, "value": 56, "unit": "", "label": "sea minerals",
             "emoji": "🌊", "at": 0},
            {"type": "pill", "x": 860, "y": 250, "text": "magnesium", "color": "#14B8A6", "at": [1, "Magnesium"]},
            {"type": "pill", "x": 1220, "y": 250, "text": "calcium", "color": "#0EA5E9", "at": [1, "calcium"]},
            {"type": "pill", "x": 860, "y": 350, "text": "iron", "color": "#DC2626", "at": [1, "iron"]},
            {"type": "pill", "x": 1180, "y": 350, "text": "potassium", "color": "#F59E0B", "at": [1, "potassium"]},
            {"type": "pill", "x": 860, "y": 450, "text": "manganese", "color": "#7C3AED", "at": [1, "manganese"]},
            {"type": "pill", "x": 1210, "y": 450, "text": "selenium", "color": "#16A34A", "at": [1, "selenium"]},
            {"type": "card", "x": 760, "y": 720, "w": 1000, "h": 150, "emoji": "🪶", "title": "Low calories + soluble fiber",
             "at": [2, "calories"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "b12", "title": "The B12 Myth", "emoji": "🌱", "dark": True, "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now, a popular claim, especially among vegans: seaweed is a source of vitamin B12.", {}),
            ("H", "Some seaweeds do contain B12. But most of it is in the form of analogs. Inactive look-alikes.", {}),
            ("H", "Those analogs compete with real B12, and may even block its absorption.", {}),
            ("P", "Fake B12 that gets in the way of real B12? That's sabotage.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("Vitamin B12?", 720, 190, 110, at=0, font="fredoka", weight=700, color="#FDE68A"),
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 170, "emoji": "🎭", "title": "Mostly inactive analogs",
             "at": [1, "analogs"], **DARK},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 170, "emoji": "🚧", "title": "May block real B12",
             "at": [2, "block"], **DARK},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "So the bottom line for vegans: don't rely on seaweed for B12. Take a separate B12 supplement.", {}),
            ("P", "Seaweed: great at iodine, terrible at B12. Nobody's perfect. Except me.", {"mood": "smug"}),
        ], "els": [
            {"type": "check", "x": 160, "y": 300, "w": 1300, "ok": False, "text": "Seaweed as your B12 source", "at": 0},
            {"type": "check", "x": 160, "y": 440, "w": 1300, "ok": True, "text": "A separate B12 supplement", "at": [0, "supplement"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch one, and it's the big one: too much iodine. Too much is as risky as too little.", {}),
            ("H", "Going over one thousand one hundred micrograms a day, usually from kelp, can trigger an overactive thyroid, "
                  "a goiter, and even a reactive underactive thyroid.", {}),
            ("H", "Nori, the sushi seaweed, is the relatively safe type for daily eating.", {}),
        ], "els": [
            {"type": "banner", "x": 760, "y": 200, "text": "Too much = as risky as too little", "color": "#DC2626", "at": 0},
            {"type": "card", "x": 760, "y": 410, "w": 1100, "h": 180, "emoji": "🦋", "title": "Over 1,100 mcg a day",
             "body": "overactive thyroid · goiter · underactive", "at": [1, "thousand"]},
            {"type": "card", "x": 760, "y": 640, "w": 1100, "h": 180, "emoji": "🍣", "title": "Nori: relatively safe daily",
             "at": [2, "Nori"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch two: heavy metals. Seaweed absorbs arsenic, lead, cadmium and mercury from the water. "
                  "How much depends a lot on where it grows.", {}),
            ("H", "So buy brands that test for quality, from clean waters, like Japan, Ireland or Norway.", {}),
            ("H", "Catch three: sodium. Processed, dried and seasoned products, like nori snacks, can have a lot of added salt.", {}),
            ("H", "Catch four: fucoidan has anti-clotting activity. Eating a lot of it while on warfarin needs medical advice.", {}),
            ("P", "Ocean gossip: it picks up everything around it. Choose your seaweed's neighborhood carefully.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 760, "y": 200, "w": 1100, "h": 160, "emoji": "🏭", "title": "#2 Heavy metals",
             "body": "arsenic · lead · cadmium · mercury", "at": 0},
            {"type": "card", "x": 760, "y": 380, "w": 1100, "h": 140, "emoji": "🧪", "title": "Tested · clean waters",
             "body": "Japan · Ireland · Norway", "at": [1, "brands"], "fill": "#DCFCE7"},
            {"type": "card", "x": 760, "y": 560, "w": 1100, "h": 160, "emoji": "🧂", "title": "#3 Sodium",
             "body": "seasoned nori snacks", "at": [2, "sodium"]},
            {"type": "card", "x": 760, "y": 740, "w": 1100, "h": 160, "emoji": "💊", "title": "#4 Warfarin",
             "body": "a lot of fucoidan? ask first", "at": [3, "warfarin"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "howmuch", "title": "How Much a Day?", "emoji": "📏", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So how much seaweed can you eat a day? It depends almost entirely on the type.", {}),
            ("H", "Nori: one to three sheets a day. That's the safest. Each sheet gives sixteen to forty-three micrograms of iodine.", {}),
            ("H", "Wakame: about a tablespoon dried, roughly two grams. A daily bowl of miso soup is perfectly fine.",
             {"say": "Wah-kah-meh: about a tablespoon dried, roughly two grams. A daily bowl of miso soup is perfectly fine."}),
            ("H", "Dulse: about two to three grams a day. It's relatively low in iodine.", {}),
        ], "els": [
            T("Safe daily amounts", 720, 160, 60, at=0, font="fredoka", weight=600, color="green"),
            {"type": "card", "x": 720, "y": 330, "w": 1100, "h": 160, "emoji": "🍙", "title": "Nori: 1 to 3 sheets",
             "body": "16–43 mcg iodine per sheet", "at": [1, "Nori"], "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 520, "w": 1100, "h": 160, "emoji": "🍜", "title": "Wakame: 1 tablespoon",
             "body": "about 2 g dried · miso soup is fine", "at": [2, "tablespoon"], "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 710, "w": 1100, "h": 160, "emoji": "🟥", "title": "Dulse: 2 to 3 g",
             "body": "relatively low iodine", "at": [3, "Dulse"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Kombu and kelp: not for every day. Once or twice a week at most, in small amounts. "
                  "One gram can have two thousand five hundred micrograms, more than twice the upper limit.", {}),
            ("H", "And kelp supplements: avoid them unless a doctor tells you to. "
                  "They're the most common cause of iodine excess.", {}),
            ("P", "Kelp pills. The villain of today's episode. Dun dun dun.", {"mood": "worried", "jump": True}),
        ], "els": [
            {"type": "card", "x": 720, "y": 280, "w": 1100, "h": 190, "emoji": "🟤", "title": "Kombu / kelp: 1 to 2× a week",
             "body": "small amounts · 1 g can be 2,500 mcg", "at": 0, "fill": "#FEF3C7"},
            {"type": "card", "x": 720, "y": 540, "w": 1100, "h": 190, "emoji": "💊", "title": "Kelp supplements: avoid",
             "body": "#1 cause of iodine excess", "at": [1, "supplements"], "fill": "#FEE2E2"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The rule of thumb: nori and wakame, in normal food amounts, are safe every day, "
                  "and give you just about the iodine you want.", {}),
            ("H", "Kelp and kombu are a seasoning and a soup base. Not a portion. With those, you measure.", {}),
            ("H", "How often overall? Two to four times a week, in moderate amounts, is plenty for the benefits "
                  "without worrying about too much iodine.", {}),
        ], "els": [
            {"type": "card", "x": 450, "y": 300, "w": 560, "h": 200, "emoji": "✅", "title": "Nori, wakame",
             "body": "food amounts, daily", "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 1060, "y": 300, "w": 560, "h": 200, "emoji": "🥄", "title": "Kelp, kombu",
             "body": "seasoning: measure it", "at": [1, "seasoning"], "fill": "#FEF3C7"},
            {"type": "banner", "x": 760, "y": 620, "text": "2 to 4 times a week", "color": "#0EA5E9", "at": [2, "Two"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "careful", "title": "Who Should Be Careful", "emoji": "🦋", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Some people need extra care. Anyone diagnosed with a thyroid condition, like Hashimoto's, Graves', "
                  "or a multinodular goiter. Anyone on thyroid medication. And pregnant women.",
             {"say": "Some people need extra care. Anyone diagnosed with a thyroid condition, like Hashi-moto's, Graves', "
                     "or a multi-nodular goiter. Anyone on thyroid medication. And pregnant women."}),
            ("H", "For them, even a moderate excess of iodine can upset the thyroid. So talk to your doctor.", {}),
            ("H", "In pregnancy and breastfeeding, the recommended intake rises to two hundred twenty to two hundred ninety micrograms. "
                  "But the upper limit stays about the same. Nori and wakame in moderation are fine. Be careful with kelp.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 210, "w": 1100, "h": 160, "emoji": "🦋", "title": "Thyroid conditions",
             "body": "Hashimoto's · Graves' · nodules", "at": 0},
            {"type": "card", "x": 760, "y": 390, "w": 1100, "h": 140, "emoji": "💊", "title": "Thyroid medication",
             "at": [0, "medication"]},
            {"type": "card", "x": 760, "y": 570, "w": 1100, "h": 160, "emoji": "🤰", "title": "Pregnancy: 220–290 mcg",
             "body": "nori, wakame OK · careful with kelp", "at": [0, "pregnant"]},
            {"type": "banner", "x": 760, "y": 790, "text": "Ask your doctor", "color": "#7C3AED", "at": [1, "doctor"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Signs of too much iodine: a metallic taste in the mouth, burning in the mouth and throat, and more saliva.", {}),
            ("H", "Over the long run, changes in thyroid function, which show up on a blood test.", {}),
            ("P", "Metal mouth. Not the superpower I was hoping for.", {"mood": "worried"}),
        ], "els": [
            T("Too much iodine?", 720, 170, 64, at=0, font="fredoka", weight=700, color="#DC2626"),
            {"type": "check", "x": 160, "y": 300, "w": 1300, "ok": False, "text": "Metallic taste", "at": [0, "metallic"]},
            {"type": "check", "x": 160, "y": 420, "w": 1300, "ok": False, "text": "Burning mouth and throat", "at": [0, "burning"]},
            {"type": "check", "x": 160, "y": 540, "w": 1300, "ok": False, "text": "More saliva", "at": [0, "saliva"]},
            {"type": "card", "x": 720, "y": 740, "w": 1000, "h": 150, "emoji": "🩸", "title": "Long run: check thyroid blood test",
             "at": [1, "blood"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Two quick ones. Is the nori in sushi enough for iodine? One sheet gives sixteen to forty-three micrograms, "
                  "about ten to twenty-nine percent of a day's needs. Two to four sheets a week is a decent contribution.", {}),
            ("H", "And roasted nori snacks? Fine for snacking, but check the sodium and the oil. "
                  "Versions with olive oil and low salt are the better pick.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 280, "w": 1100, "h": 200, "emoji": "🍣", "title": "1 sheet = 10–29% of a day",
             "body": "2 to 4 sheets a week helps", "at": 0},
            {"type": "card", "x": 720, "y": 560, "w": 1100, "h": 200, "emoji": "🫒", "title": "Nori snacks: check the label",
             "body": "olive oil, low salt", "at": [1, "snacks"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: seaweed is the richest food source of iodine, plus fucoidan and a lot of sea minerals.", {}),
            ("H", "Two: the type matters most. Nori and wakame are everyday foods. Kelp and kombu are a seasoning you measure.", {}),
            ("H", "Three: buy from tested sources, and skip kelp supplements unless a doctor says otherwise.", {}),
            ("H", "Four: seaweed isn't a B12 source. Vegans, take a supplement.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Top iodine source + sea minerals", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Nori, wakame daily · kelp measured", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Tested sources · no kelp pills", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": False, "text": "Not a B12 source", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So seaweed: iodine royalty, mineral hoarder, and kelp is the cousin you keep an eye on.", {"mood": "happy"}),
            ("H", "Couldn't have said it better, Pip.", {}),
            ("P", "Land seeds and sea plants, united!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Pick your seaweed wisely!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/seaweed", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
