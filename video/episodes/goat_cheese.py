"""Goat cheese explainer (English), based on https://wiseplate.blog/en/food/goat-cheese/

Numbers are the article's: soft (fresh) goat cheese per 100 g, a 50 g serving
for saturated fat, lactose as a percentage of goat's versus cow's milk, and
sodium ranges per 100 g for aged and brined cheeses. Keep them in sync with
content/food/goat-cheese.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Goat Cheese: Easier to Digest Than Cow's Milk Cheese?"
SLUG = "goat-cheese"
ARTICLE = "https://wiseplate.blog/en/food/goat-cheese/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "GOAT CHEESE", "top_size": 140, "bottom": "EASIER?", "bottom_size": 200,
         "badge": "4.2%", "badge_label": "lactose\n(cow: 4.7%)", "badge_color": "#16A34A", "badge_size": 110,
         "scatter": "🧀", "hero": "🐐", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "roots":    {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "inside":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "digest":   {"bpm": 96, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.6},
    "mct":      {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "benefits": {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "types":    {"bpm": 84, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FAFAF9", "roots": "#FEF3C7", "inside": "#ECFDF5", "digest": "#E0F2FE",
    "mct": "#FFEDD5", "benefits": "#ECFCCB", "catches": "#FEE2E2", "types": "#F5F3FF",
    "howto": "#FFF7ED", "outro": "#FAFAF9",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hello! Pip the pumpkin seed here, your favorite guest reviewer.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest is soft, tangy, and comes from a goat. It's goat cheese!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🐐", 960, 200, 160, at=[1, "goat"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today: goat cheese. What's in it, why some people find it easier to digest than cow's milk cheese, "
                  "its medium-chain fats, and the catches worth knowing.", {}),
            ("P", "A cheese from a goat that climbs mountains. I'm already impressed.", {"mood": "smug"}),
        ], "els": [
            E("🐐", 400, 330, 200, at=[0, "goat"], wobble=True),
            T("Goat cheese", 580, 300, 130, at=[0, "goat"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🫧", "title": "Easier to digest?", "at": [0, "digest"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "⚡", "title": "Medium-chain fats", "at": [0, "medium"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "⚠️", "title": "The catches", "at": [0, "catches"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "roots", "title": "An Ancient Cheese", "emoji": "🐐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Goat cheese is also known by its French name, chèvre, from the French word for goat.",
             {"say": "Goat cheese is also known by its French name, shev, from the French word for goat."}),
            ("H", "It's one of the oldest dairy foods in human culture. Its production predates cow's milk cheeses by thousands of years.", {}),
            ("H", "In the Middle East and around the Mediterranean, it's been a staple for ages, and not by chance.", {}),
            ("P", "Thousands of years? Respect your elders, everyone.", {"mood": "surprised"}),
        ], "els": [
            T("Chèvre", 720, 220, 130, at=[0, "French"], font="fredoka", weight=700, color="green"),
            T("French for goat", 720, 340, 48, at=[0, "word"], color="muted"),
            {"type": "card", "x": 720, "y": 520, "w": 1000, "h": 180, "emoji": "🏺", "title": "One of the oldest dairy foods",
             "body": "older than cow's milk cheese", "at": [1, "oldest"]},
            {"type": "pill", "x": 720, "y": 720, "text": "a Middle East and Mediterranean staple", "color": "#0EA5E9", "at": [2, "Mediterranean"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Nutritionally, goat's milk and its products differ from cow's milk in ways that matter.", {}),
            ("H", "They can change how available the nutrients are to your body, and how well people who struggle with dairy tolerate it.", {}),
        ], "els": [
            E("🐐", 450, 300, 170, at=[0, "goat's"]),
            T("vs", 720, 300, 80, at=[0, "cow's"], font="fredoka", weight=700, color="muted"),
            E("🐄", 990, 300, 170, at=[0, "cow's"]),
            {"type": "pill", "x": 720, "y": 540, "text": "how available the nutrients are", "color": "green", "at": [1, "available"]},
            {"type": "pill", "x": 720, "y": 660, "text": "how well dairy is tolerated", "color": "green", "at": [1, "tolerate"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "inside", "title": "What's Inside", "emoji": "📊", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "One hundred grams of soft, fresh goat cheese contains about two hundred sixty-four calories, "
                  "eighteen grams of protein, and twenty-one grams of fat.", {}),
            ("H", "Plus just zero point one grams of carbs, and one hundred forty milligrams of calcium.", {}),
            ("P", "Twenty-one grams of fat. This cheese doesn't do diets.", {"mood": "smug"}),
        ], "els": [
            T("Soft goat cheese, per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 470, "y": 360, "w": 420, "h": 260, "value": 264, "label": "calories", "emoji": "🔥", "at": [0, "sixty"]},
            {"type": "stat", "x": 920, "y": 360, "w": 420, "h": 260, "value": 18, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "eighteen"]},
            {"type": "stat", "x": 1370, "y": 360, "w": 420, "h": 260, "value": 21, "unit": " g", "label": "fat", "emoji": "🧈", "at": [0, "fat"]},
            {"type": "stat", "x": 470, "y": 670, "w": 420, "h": 260, "value": 0.1, "decimals": 1, "unit": " g", "label": "carbs", "emoji": "🍞", "at": [1, "carbs"]},
            {"type": "stat", "x": 920, "y": 670, "w": 420, "h": 260, "value": 140, "unit": " mg", "label": "calcium", "emoji": "🦴", "at": [1, "calcium"]},
        ], "pip_hide": True},
        {"pip": PIP_R, "lines": [
            ("H", "And aged goat cheeses? They hold less moisture, so everything is more concentrated.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 330, "w": 1000, "h": 190, "emoji": "⏳", "title": "Aged goat cheese",
             "body": "less moisture · more concentrated nutrients", "at": [0, "aged"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "digest", "title": "Easier to Digest?", "emoji": "🫧", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "First, the fat. Goat's milk has much smaller fat globules than cow's milk.", {}),
            ("H", "Smaller globules mean more total surface area, so lipase, the enzyme that digests fat, works more efficiently.",
             {"say": "Smaller globules mean more total surface area, so lie-pace, the enzyme that digests fat, works more efficiently."}),
            ("H", "The result is faster, more efficient digestion. That may explain why many people who feel heavy after cow's milk cheese "
                  "report easier digestion with goat cheese.", {}),
        ], "els": [
            T("Smaller fat globules", 720, 170, 70, at=0, font="fredoka", weight=700, color="green"),
            E("🫧", 450, 370, 170, at=[0, "smaller"]),
            T("goat", 450, 490, 44, at=[0, "smaller"], font="fredoka", weight=600),
            E("🟡", 990, 370, 170, at=[0, "cow's"]),
            T("cow", 990, 490, 44, at=[0, "cow's"], font="fredoka", weight=600),
            {"type": "pill", "x": 720, "y": 620, "text": "more surface area for lipase", "color": "#0EA5E9", "at": [1, "surface"]},
            {"type": "pill", "x": 720, "y": 740, "text": "many report easier digestion", "color": "green", "at": [2, "report"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Then the protein. Goat's milk is low in alpha-s1 casein, the dominant protein in cow's milk, "
                  "and relatively rich in beta-casein.",
             {"say": "Then the protein. Goat's milk is low in alpha S 1 kay-seen, the dominant protein in cow's milk, "
                     "and relatively rich in beta kay-seen."}),
            ("H", "Add slightly less lactose, four point two percent in goat's milk against four point seven in cow's milk, "
                  "and a softer curd that forms in the stomach.", {}),
            ("H", "Together, that means some people who are sensitive to cow's milk tolerate goat's milk products better.", {}),
            ("P", "Some people. Not everyone. I'm writing that down.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 170, "emoji": "🧬", "title": "Low in alpha-s1 casein",
             "body": "richer in beta-casein", "at": 0},
            {"type": "bars", "x": 160, "y": 400, "w": 1300, "row_h": 110, "max": 6, "unit": "%", "decimals": 1, "rows": [
                {"label": "Goat", "value": 4.2, "color": "#16A34A", "at": [1, "four"]},
                {"label": "Cow", "value": 4.7, "color": "#94A3B8", "at": [1, "seven"]},
            ]},
            T("lactose in the milk", 720, 590, 40, at=[1, "lactose"], color="muted"),
            {"type": "pill", "x": 720, "y": 690, "text": "a softer curd in the stomach", "color": "#0EA5E9", "at": [1, "softer"]},
            {"type": "pill", "x": 720, "y": 800, "text": "some sensitive people do better", "color": "green", "at": [2, "some"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "What about lactose intolerance? Often goat cheese works, especially aged goat cheese. "
                  "Aging breaks down most of the lactose, and even fresh soft cheese is relatively low in it.", {}),
            ("H", "But everyone is different. Start with small amounts and see how you react.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "⏳", "title": "Lactose intolerant?",
             "body": "often fine, especially aged cheese", "at": 0},
            {"type": "card", "x": 720, "y": 510, "w": 1000, "h": 190, "emoji": "🥄", "title": "Start small",
             "body": "everyone is different", "at": [1, "small"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "mct", "title": "Medium-Chain Fats", "emoji": "⚡", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Goat's milk is richer than cow's milk in medium-chain triglycerides, or MCTs. "
                  "Fats like caproic, caprylic and capric acid.",
             {"say": "Goat's milk is richer than cow's milk in medium chain triglycerides, or M C Ts. "
                     "Fats like ka-pro-ick, ka-prill-ick, and ka-prick acid."}),
            ("P", "Caproic, caprylic, capric. Say that three times fast. I can't.", {"mood": "smug", "say": "Ka-pro-ick, ka-prill-ick, ka-prick. Say that three times fast. I can't."}),
        ], "els": [
            T("MCTs", 720, 200, 120, at=0, font="fredoka", weight=700, color="green"),
            T("medium-chain triglycerides", 720, 310, 46, at=0, color="muted"),
            {"type": "pill", "x": 400, "y": 470, "text": "caproic", "color": "orange", "at": [0, "caproic"]},
            {"type": "pill", "x": 720, "y": 470, "text": "caprylic", "color": "orange", "at": [0, "caprylic"]},
            {"type": "pill", "x": 1040, "y": 470, "text": "capric", "color": "orange", "at": [0, "capric"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "These fats are absorbed directly into the liver and used for quick energy, "
                  "similar to the fats in coconut oil.", {}),
            ("H", "Studies show that MCT intake is associated with faster use for energy, and a reduced tendency to store fat.",
             {"say": "Studies show that M C T intake is associated with faster use for energy, and a reduced tendency to store fat."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 250, "w": 1000, "h": 190, "emoji": "⚡", "title": "Straight to the liver",
             "body": "used for quick energy", "at": [0, "liver"]},
            E("🥥", 420, 470, 110, at=[0, "coconut"]),
            T("like coconut oil", 520, 470, 46, at=[0, "coconut"], font="fredoka", weight=600, anchor="l"),
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 180, "emoji": "📈", "title": "Linked in studies",
             "body": "faster energy use · less fat storage", "at": [1, "associated"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "benefits", "title": "More Good Stuff", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Calcium. Goat cheese provides highly bioavailable calcium, for bone density, muscle function and nerve conduction.",
             {"say": "Calcium. Goat cheese provides highly bio-available calcium, for bone density, muscle function and nerve conduction."}),
            ("H", "And organic acids made during fermentation, like lactic acid in aged cheeses, help calcium absorption.", {}),
            ("H", "Aged goat cheeses, like goat gouda, goat kashkaval, or the French Crottin de Chavignol, "
                  "contain live cultures that survived aging.",
             {"say": "Aged goat cheeses, like goat gouda, goat kash-ka-val, or the French cro-tan de sha-vee-nyol, "
                     "contain live cultures that survived aging."}),
            ("H", "They may be a modest probiotic source for a balanced gut. Though not every aged cheese has live bacteria in significant amounts.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 170, "emoji": "🦴", "title": "Bioavailable calcium",
             "body": "bones, muscles, nerves", "at": 0},
            {"type": "pill", "x": 720, "y": 360, "text": "lactic acid helps absorption", "color": "green", "at": [1, "lactic"]},
            {"type": "card", "x": 720, "y": 540, "w": 1000, "h": 170, "emoji": "🦠", "title": "Live cultures in aged cheese",
             "body": "a modest probiotic source, maybe", "at": [2, "Aged"]},
            {"type": "pill", "x": 720, "y": 710, "text": "not every aged cheese has them", "color": "orange", "at": [3, "not"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Tryptophan. Goat cheese is rich in this amino acid, the building block of serotonin, "
                  "which regulates mood, sleep and appetite.",
             {"say": "Tryptophan. Goat cheese is rich in this amino acid, the building block of sero-tonin, "
                     "which regulates mood, sleep and appetite."}),
            ("H", "Like other dairy cheeses, it gives a good amount of tryptophan for a fairly small serving.", {}),
            ("H", "And vitamins. Goat's milk has more vitamin A and riboflavin, B2, than cow's milk. "
                  "Vitamin A supports vision, immunity and epithelial tissue. B2 helps with energy metabolism and making ATP.",
             {"say": "And vitamins. Goat's milk has more vitamin A and riboflavin, B 2, than cow's milk. "
                     "Vitamin A supports vision, immunity and epi-thee-lial tissue. B 2 helps with energy metabolism and making A T P."}),
            ("P", "Mood, sleep, vision, energy. Goat cheese has a busy schedule.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 180, "emoji": "😊", "title": "Tryptophan",
             "body": "building block of serotonin", "at": 0},
            {"type": "pill", "x": 400, "y": 390, "text": "mood", "color": "#8B5CF6", "at": [0, "mood"]},
            {"type": "pill", "x": 720, "y": 390, "text": "sleep", "color": "#8B5CF6", "at": [0, "sleep"]},
            {"type": "pill", "x": 1040, "y": 390, "text": "appetite", "color": "#8B5CF6", "at": [0, "appetite"]},
            {"type": "card", "x": 450, "y": 620, "w": 560, "h": 190, "emoji": "👁️", "title": "Vitamin A",
             "body": "vision · immunity", "at": [2, "vitamin A"]},
            {"type": "card", "x": 1060, "y": 620, "w": 560, "h": 190, "emoji": "⚡", "title": "B2",
             "body": "energy · ATP", "at": [2, "riboflavin"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch one: saturated fat. A fifty gram serving of soft goat cheese has about seven grams of it.", {}),
            ("H", "That's about a third of the recommended daily ceiling of around twenty grams. "
                  "If you're cutting saturated fat for heart reasons, count it in your daily total.", {}),
        ], "els": [
            T("#1 Saturated fat", 760, 160, 76, at=0, font="fredoka", weight=700, color="red"),
            {"type": "stat", "x": 500, "y": 420, "w": 480, "h": 280, "value": 7, "unit": " g", "label": "in a 50 g serving",
             "emoji": "🧈", "at": [0, "seven"], "color": "orange"},
            {"type": "stat", "x": 1060, "y": 420, "w": 520, "h": 280, "text": "about 1/3", "value": 0, "label": "of the ~20 g daily ceiling", "emoji": "📏", "at": [1, "third"], "color": "red", "vsize": 90},
            {"type": "pill", "x": 760, "y": 700, "text": "heart reasons? count it in your daily total", "color": "red", "at": [1, "heart"]},
        ], "pip_hide": True},
        {"pip": PIP_R, "lines": [
            ("H", "Catch two: it's not for milk protein allergy, the I g E kind. Even if it's better tolerated, "
                  "goat cheese still has milk proteins that can trigger a reaction.",
             {"say": "Catch two: it's not for milk protein allergy, the I G E kind. Even if it's better tolerated, "
                     "goat cheese still has milk proteins that can trigger a reaction."}),
            ("H", "Lactose intolerance usually doesn't rule out aged cheeses. But a milk protein allergy means complete avoidance.", {}),
            ("P", "Intolerance and allergy are not the same thing. Got it.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 250, "w": 1000, "h": 190, "emoji": "🚫", "title": "#2 Milk protein allergy",
             "body": "IgE-mediated: avoid it completely", "at": 0},
            {"type": "check", "x": 220, "y": 500, "w": 1000, "ok": True, "text": "Lactose intolerance: often OK", "at": [1, "Lactose"]},
            {"type": "check", "x": 220, "y": 630, "w": 1000, "ok": False, "text": "Milk protein allergy: no", "at": [1, "allergy"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch three: it's calorie dense. About two hundred sixty-four calories per hundred grams for soft cheese, "
                  "and four hundred plus for hard aged cheese. It's easy to eat more than you meant to.", {}),
            ("H", "Catch four: sodium varies. Aged and brined cheeses, like feta-style goat cheese, "
                  "can have four hundred to eight hundred milligrams per hundred grams. With high blood pressure, choose soft, less salty ones.", {}),
            ("H", "And catch five: like all dairy, it raises animal welfare and environmental questions. "
                  "Its footprint is lower than beef, and usually lower than industrial cow's milk cheese.", {}),
        ], "els": [
            {"type": "bars", "x": 160, "y": 210, "w": 1300, "row_h": 110, "max": 600, "unit": "", "rows": [
                {"label": "Soft", "value": 264, "text": "264 cal", "color": "#F59E0B", "at": [0, "sixty"]},
                {"label": "Hard aged", "value": 400, "text": "400+ cal", "color": "#EF4444", "at": [0, "plus"]},
            ]},
            {"type": "card", "x": 760, "y": 520, "w": 1100, "h": 170, "emoji": "🧂", "title": "Aged or brined: 400-800 mg",
             "body": "sodium per 100 g · pick soft, less salty", "at": [1, "sodium"], "fill": "#FEF3C7"},
            {"type": "card", "x": 760, "y": 720, "w": 1100, "h": 150, "emoji": "🌍", "title": "Lower footprint than beef",
             "at": [2, "footprint"]},
        ], "pip_hide": True},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "types", "title": "Types of Goat Cheese", "emoji": "🧀", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Goat cheese comes in many types. Fresh soft cheese: high moisture, low lactose, and low sodium.", {}),
            ("H", "Bûcheron: medium moisture, very low lactose, and medium sodium.",
             {"say": "Boosh-ron: medium moisture, very low lactose, and medium sodium."}),
            ("H", "Hard aged cheese: low moisture, negligible lactose, the most concentrated nutrients, and high sodium.", {}),
            ("H", "And feta-style cheese: medium moisture, low lactose, and very high sodium.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 190, "w": 1200, "h": 150, "emoji": "🥛", "title": "Fresh soft: low sodium",
             "at": [0, "Fresh"], "fill": "#DCFCE7"},
            {"type": "card", "x": 760, "y": 370, "w": 1200, "h": 150, "emoji": "🪵", "title": "Bûcheron: very low lactose",
             "at": [1, "medium"]},
            {"type": "card", "x": 760, "y": 550, "w": 1200, "h": 150, "emoji": "🧀", "title": "Hard aged: lactose negligible",
             "at": [2, "Hard"]},
            {"type": "card", "x": 760, "y": 730, "w": 1200, "h": 150, "emoji": "🧂", "title": "Feta-style: very high sodium",
             "at": [3, "feta"], "fill": "#FEE2E2"},
        ], "pip_hide": True},
        {"pip": PIP_R, "lines": [
            ("H", "Speaking of feta: how is it different? Traditional feta is made from sheep's milk, sometimes mixed with goat's milk. "
                  "Goat cheese is made from goat's milk only.", {}),
            ("H", "Feta's texture is different, and it's saltier, because it's made in brine. Both are rich in protein and calcium.", {}),
            ("P", "Sheep, goats... I'm the only one here who grew on a vine.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 420, "y": 300, "w": 620, "h": 220, "emoji": "🐑", "title": "Feta",
             "body": "sheep's (+ goat) milk", "at": [0, "sheep's"]},
            {"type": "card", "x": 1070, "y": 300, "w": 620, "h": 220, "emoji": "🐐", "title": "Goat cheese",
             "body": "goat's milk only", "at": [0, "only"]},
            {"type": "pill", "x": 420, "y": 500, "text": "saltier: made in brine", "color": "orange", "at": [1, "brine"]},
            {"type": "banner", "x": 760, "y": 690, "text": "Both: protein + calcium", "color": "#16A34A", "at": [1, "Both"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "howto", "title": "How to Eat It", "emoji": "🍯", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Soft goat cheese goes great with honey, walnuts, tomatoes and leafy greens. "
                  "That balances the fat with antioxidants and phytochemicals.",
             {"say": "Soft goat cheese goes great with honey, walnuts, tomatoes and leafy greens. "
                     "That balances the fat with antioxidants and fighto-chemicals."}),
            ("H", "Aged goat cheese is excellent on sourdough bread with olive oil.", {}),
        ], "els": [
            T("Soft goat cheese +", 760, 150, 64, at=0, font="fredoka", weight=700, color="green"),
            E("🍯", 340, 330, 130, at=[0, "honey"]),
            T("honey", 340, 440, 42, at=[0, "honey"], font="fredoka", weight=600),
            E("🌰", 620, 330, 130, at=[0, "walnuts"]),
            T("walnuts", 620, 440, 42, at=[0, "walnuts"], font="fredoka", weight=600),
            E("🍅", 900, 330, 130, at=[0, "tomatoes"]),
            T("tomatoes", 900, 440, 42, at=[0, "tomatoes"], font="fredoka", weight=600),
            E("🥬", 1180, 330, 130, at=[0, "leafy"]),
            T("leafy greens", 1180, 440, 42, at=[0, "leafy"], font="fredoka", weight=600),
            {"type": "card", "x": 760, "y": 660, "w": 1100, "h": 170, "emoji": "🍞", "title": "Aged: on sourdough",
             "body": "with olive oil", "at": [1, "sourdough"]},
        ], "pip_hide": True},
        {"pip": PIP_R, "lines": [
            ("H", "How much a day? In a balanced diet, thirty to fifty grams of soft cheese, or twenty to thirty grams of aged cheese, "
                  "about one or two slices, is a reasonable amount.", {}),
            ("H", "Count it as part of your total dairy, and your total saturated fat for the day.", {}),
            ("P", "Thirty grams. That's about the size of a seed's ego. Mine, specifically.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 250, "w": 1000, "h": 180, "emoji": "🥛", "title": "Soft: 30 to 50 g",
             "at": [0, "thirty"]},
            {"type": "card", "x": 720, "y": 470, "w": 1000, "h": 180, "emoji": "🧀", "title": "Aged: 20 to 30 g",
             "body": "about 1 to 2 slices", "at": [0, "twenty"]},
            {"type": "pill", "x": 720, "y": 680, "text": "count it in daily dairy + saturated fat", "color": "orange", "at": [1, "Count"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 9
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: goat cheese has a unique profile, with smaller fat globules, a different casein makeup, and a little less lactose.",
             {"say": "One: goat cheese has a unique profile, with smaller fat globules, a different kay-seen makeup, and a little less lactose."}),
            ("H", "Two: that can make it easier for some people who are sensitive to cow's milk, or have digestive trouble.", {}),
            ("H", "Three: it brings protein, calcium and medium-chain fats.", {}),
            ("H", "Four: it's rich in fat and calories, and aged or brined types can be salty. Small portions, eaten well, work best.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Smaller fat globules, different casein", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Easier for some sensitive people", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Protein, calcium, MCTs", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": False, "text": "Fat, calories, salt: small portions", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So goat cheese: ancient, tangy, and gentle on some tummies. Honestly? A legend.", {"mood": "smug"}),
            ("H", "High praise from a seed.", {}),
            ("P", "The highest!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the details, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the details, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Keep your portions small and your cheese tangy!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/goat-cheese", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
