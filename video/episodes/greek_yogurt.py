"""Greek yogurt explainer (English), based on https://wiseplate.blog/food/greek-yogurt/

Numbers are the article's: rounded USDA examples per 100 g, plain Greek yogurt
about 2% fat (FDC 170903) vs plain regular whole-milk yogurt about 3.25% fat
(FDC 171284). Not uniform values for every brand. Keep them in sync with
content/food/greek-yogurt.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Greek Yogurt: What Makes It Greek?"
SLUG = "greek-yogurt"
ARTICLE = "https://wiseplate.blog/food/greek-yogurt/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "THICK YOGURT", "top_size": 150, "bottom": "WORTH IT?", "bottom_size": 190,
         "badge": "20 g", "badge_label": "protein\nper cup", "badge_color": "#0EA5E9",
         "scatter": "🥛", "hero": "🥄", "mood": "surprised"}

MUSIC = {
    "intro":   {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "strain":  {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "numbers": {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "updown":  {"bpm": 104, "root": 62, "prog": ["vi", "IV", "I", "V"], "density": 0.65, "swing": 0.1},
    "cultures": {"bpm": 92, "root": 69, "prog": ["I", "iii", "IV", "V"], "density": 0.55, "inst": "musicbox", "drums": False},
    "benefits": {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "catches": {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "howto":   {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":   {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#F0F9FF", "strain": "#FEF3C7", "numbers": "#ECFDF5", "updown": "#E0F2FE",
    "cultures": "#F5F3FF", "benefits": "#ECFCCB", "catches": "#FEE2E2", "howto": "#FFEDD5",
    "outro": "#F0F9FF",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hey! Over here! It's me, Pip, your favorite pumpkin seed.", {"mood": "happy", "wave": True}),
            ("P", "Today I'm a guest reviewer, because people keep sprinkling me on this stuff. Greek yogurt!",
             {"mood": "happy", "jump": True}),
        ], "els": [
            E("🥛", 960, 200, 160, at=[1, "yogurt"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "That's right. Today it's Greek yogurt: what actually makes it Greek, how it really compares "
                  "to regular yogurt, and what to look for on the label.", {}),
            ("P", "I just want to know if it's worthy of me.", {"mood": "smug"}),
            ("H", "Let's find out. Spoons ready.", {}),
        ], "els": [
            E("🥛", 420, 330, 200, at=[0, "Greek"], wobble=True),
            T("Greek Yogurt", 640, 300, 120, at=[0, "Greek"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🏺", "title": "What makes it Greek", "at": [0, "makes"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "⚖️", "title": "Greek vs regular", "at": [0, "compares"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "🏷️", "title": "Reading the label", "at": [0, "label"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "strain", "title": "It's All About the Strain", "emoji": "🏺", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So what is Greek yogurt? It's simply yogurt that has been strained to remove the whey. "
                  "That's the watery liquid that separates from the curds.", {}),
            ("H", "Straining out that liquid is what makes it so much thicker than regular yogurt.", {}),
            ("P", "So it's yogurt that went to the gym and lost the water weight.", {"mood": "smug"}),
        ], "els": [
            T("Greek yogurt = strained yogurt", 720, 190, 70, at=0, font="fredoka", weight=700, color="green"),
            E("🥛", 360, 450, 170, at=[0, "yogurt"]),
            {"type": "arrow", "x1": 480, "y1": 450, "x2": 640, "y2": 450, "at": [0, "strained"]},
            T("strain", 560, 390, 40, at=[0, "strained"], color="muted"),
            {"type": "card", "x": 950, "y": 450, "w": 480, "h": 150, "emoji": "💧", "title": "Whey", "body": "the watery part", "at": [0, "whey."]},
            {"type": "card", "x": 720, "y": 700, "w": 760, "h": 150, "emoji": "🥄", "title": "Thicker, creamier texture", "at": [1, "thicker"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "But here's a detail most people miss. When the whey drains away, some of the calcium leaves with it.", {}),
            ("H", "So straining doesn't concentrate everything equally. Some things go up, and some things go down.", {}),
            ("P", "A plot twist! In a yogurt cup!", {"mood": "surprised", "jump": True}),
        ], "els": [
            {"type": "card", "x": 720, "y": 280, "w": 900, "h": 170, "emoji": "🦴", "title": "Some calcium leaves with the whey",
             "at": [0, "calcium"], "fill": "#FEF3C7"},
            {"type": "pill", "x": 470, "y": 560, "text": "some things go up", "color": "ok", "at": [1, "up,"]},
            {"type": "pill", "x": 980, "y": 560, "text": "some go down", "color": "orange", "at": [1, "down."]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And one more thing: the word Greek on the cup doesn't, by itself, promise fewer calories or more calcium. "
                  "The sugar, calcium and calories also depend on the fat percentage and the recipe of each product.", {}),
        ], "els": [
            {"type": "banner", "x": 720, "y": 250, "text": "\"Greek\" is not a guarantee", "color": "#F97316", "at": 0},
            {"type": "card", "x": 420, "y": 520, "w": 460, "h": 140, "emoji": "🧈", "title": "Fat %", "at": [0, "fat"]},
            {"type": "card", "x": 1000, "y": 520, "w": 460, "h": 140, "emoji": "📜", "title": "Recipe", "at": [0, "recipe"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "numbers", "title": "Greek vs Regular", "emoji": "📊", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's put numbers on it. These are rounded examples from U.S. Department of Agriculture records, per one hundred grams.",
             {"say": "Let's put numbers on it. These are rounded examples from U S Department of Agriculture records, per one hundred grams."}),
            ("H", "On one side, plain Greek yogurt, about two percent fat. On the other, plain regular yogurt, about three point two five percent fat.", {}),
            ("H", "Calories: seventy-three versus sixty-one. Protein: ten grams versus three and a half. That's the big one.", {}),
            ("H", "Calcium: one hundred fifteen milligrams versus one hundred twenty-one. Sodium: thirty-four versus forty-six. "
                  "And total sugars: three point six grams versus four point seven.", {}),
            ("P", "Ten grams of protein versus three and a half? Okay, I'm impressed.", {"mood": "surprised"}),
        ], "els": [
            T("Per 100 g (USDA examples)", 760, 150, 52, at=0, font="fredoka", weight=600, color="green"),
            {"type": "versus", "x": 120, "y": 330, "w": 1440, "row_h": 118, "names": ["Greek, ~2% fat", "Regular, ~3.25% fat"],
             "at": [1, "Greek"], "rows": [
                {"label": "Calories", "a": 73, "b": 61, "at": [2, "Calories"]},
                {"label": "Protein", "a": 10, "b": 3.5, "unit": " g", "decimals": 1, "at": [2, "Protein"]},
                {"label": "Calcium", "a": 115, "b": 121, "unit": " mg", "at": [3, "Calcium"]},
                {"label": "Sodium", "a": 34, "b": 46, "unit": " mg", "at": [3, "Sodium"]},
                {"label": "Sugars", "a": 3.6, "b": 4.7, "unit": " g", "decimals": 1, "at": [3, "sugars"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Two caveats. These aren't values for every brand. And the fat percentages differ, "
                  "so this comparison doesn't measure the effect of straining alone.", {}),
            ("H", "That same Greek yogurt also gives about two grams of fat and four grams of carbs per hundred grams. "
                  "A two hundred gram cup comes to about twenty grams of protein and around one hundred forty-six calories, before toppings.", {}),
            ("P", "Before toppings. Meaning before me.", {"mood": "smug", "wave": True}),
        ], "els": [
            {"type": "pill", "x": 720, "y": 180, "text": "not every brand · different fat %", "color": "orange", "at": [0, "brand"]},
            {"type": "stat", "x": 290, "y": 500, "w": 400, "h": 300, "value": 200, "unit": " g", "label": "one cup", "emoji": "🥛", "at": [1, "cup"]},
            {"type": "stat", "x": 740, "y": 500, "w": 400, "h": 300, "value": 20, "unit": " g", "label": "protein", "emoji": "💪", "at": [1, "twenty"]},
            {"type": "stat", "x": 1190, "y": 500, "w": 400, "h": 300, "value": 146, "unit": "", "label": "calories", "emoji": "🔥", "at": [1, "forty"]},
            T("before toppings", 740, 720, 44, at=[1, "toppings"], color="muted"),
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "updown", "title": "Straining: Ups and Downs", "emoji": "⚖️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Straining is the whole story, and it pushes things in two opposite directions.", {}),
            ("H", "What goes up: protein, about ten grams versus three and a half in our example, though the gap varies between products. "
                  "And thickness, which makes it a great stand-in for sour cream and mayonnaise.", {}),
            ("H", "What goes down: lactose. Some of it drains out with the liquid. But Greek yogurt is not necessarily lactose-free. "
                  "And calcium, some of which leaves with the whey. Some products are fortified, so check the label.", {}),
        ], "els": [
            T("Goes up", 420, 180, 64, at=[0, "opposite"], font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 420, "y": 360, "w": 600, "h": 150, "emoji": "💪", "title": "Protein", "body": "gap varies by product", "at": [1, "protein,"]},
            {"type": "card", "x": 420, "y": 560, "w": 600, "h": 150, "emoji": "🥄", "title": "Thickness", "body": "a sour cream swap", "at": [1, "thickness"]},
            T("Goes down", 1080, 180, 64, at=[0, "opposite"], font="fredoka", weight=700, color="orange"),
            {"type": "card", "x": 1080, "y": 360, "w": 600, "h": 150, "emoji": "🥛", "title": "Lactose", "body": "but not lactose-free", "at": [2, "lactose."]},
            {"type": "card", "x": 1080, "y": 560, "w": 600, "h": 150, "emoji": "🦴", "title": "Calcium", "body": "some brands fortify it", "at": [2, "calcium,"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Now, a sneaky one. Some products sold as Greek-style yogurt aren't strained at all.", {}),
            ("H", "Instead, they're thickened with concentrated milk protein, starch or stabilizers. "
                  "They're cheaper to make, but they don't have the same nutrition profile.", {}),
            ("H", "The giveaway is a long ingredient list that includes thickeners.", {}),
            ("P", "An impostor yogurt! I demand to see its ingredient list.", {"mood": "worried", "jump": True}),
        ], "els": [
            T("\"Greek-style\"", 720, 190, 96, at=[0, "style"], font="fredoka", weight=700, color="red"),
            T("not always strained", 720, 290, 48, at=[0, "strained"], color="muted"),
            {"type": "card", "x": 420, "y": 480, "w": 520, "h": 140, "emoji": "🌽", "title": "Starch", "at": [1, "starch"]},
            {"type": "card", "x": 1020, "y": 480, "w": 560, "h": 140, "emoji": "🧪", "title": "Stabilizers", "at": [1, "stabilizers"]},
            {"type": "banner", "x": 720, "y": 720, "text": "Clue: long ingredient list", "color": "#DC2626", "at": [2, "giveaway"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "cultures", "title": "Live Cultures, Decoded", "emoji": "🦠", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Next, the live cultures. All yogurt starts as pasteurized milk. Then bacterial cultures are added to ferment it, "
                  "mainly Lactobacillus bulgaricus and Streptococcus thermophilus.",
             {"say": "Next, the live cultures. All yogurt starts as pasteurized milk. Then bacterial cultures are added to ferment it, "
                     "mainly Lacto-bacillus bulgaricus, and Strepto-coccus thermophilus."}),
            ("H", "People often mix this up: pasteurizing comes first, so it doesn't cancel the fermentation.", {}),
            ("P", "First a hot bath, then the bacteria party. Got it.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 330, "y": 300, "w": 500, "h": 150, "emoji": "🔥", "title": "1. Pasteurize", "at": [0, "pasteurized"]},
            {"type": "arrow", "x1": 600, "y1": 300, "x2": 690, "y2": 300, "at": [0, "Then"]},
            {"type": "card", "x": 920, "y": 300, "w": 440, "h": 150, "emoji": "🦠", "title": "2. Ferment", "at": [0, "ferment"]},
            T("L. bulgaricus", 720, 500, 52, at=[0, "bulgaricus"], font="fredoka", weight=600, color="#7C3AED"),
            T("S. thermophilus", 720, 580, 52, at=[0, "thermophilus"], font="fredoka", weight=600, color="#7C3AED"),
            {"type": "pill", "x": 720, "y": 740, "text": "pasteurizing comes first", "color": "ok", "at": [1, "first"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The question that really matters is whether the product was heat-treated after fermentation. "
                  "That extends shelf life, but it kills the cultures.", {}),
            ("H", "Products that skip that step usually carry a label like, contains live and active cultures.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 280, "w": 1000, "h": 170, "emoji": "♨️", "title": "Heated after fermenting?",
             "body": "longer shelf life, but the cultures die", "at": [0, "heat"]},
            {"type": "banner", "x": 720, "y": 560, "text": "Look for: \"live and active cultures\"", "color": "#16A34A", "at": [1, "live"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And an important caveat. The classic yogurt bacteria aren't necessarily probiotic in the strict sense. "
                  "They don't necessarily survive the stomach and settle in your gut.", {}),
            ("H", "Strains shown to be probiotic, like Lactobacillus acidophilus or Bifidobacterium, are added on purpose, "
                  "and named on the package.",
             {"say": "Strains shown to be probiotic, like Lacto-bacillus acidophilus, or Bifido-bacterium, are added on purpose, "
                     "and named on the package."}),
            ("H", "In fact, yogurt's best-supported effect on digestion is helping to break down lactose. There, the evidence is good.", {}),
            ("P", "So the bacteria are helpful, just not superheroes. Like me, but less crunchy.", {"mood": "smug"}),
        ], "els": [
            {"type": "check", "x": 140, "y": 230, "w": 1300, "ok": False, "text": "Classic cultures = probiotic? Not necessarily", "at": [0, "probiotic"]},
            {"type": "check", "x": 140, "y": 370, "w": 1300, "ok": True, "text": "Probiotic strains are named on the pack", "at": [1, "named"]},
            {"type": "check", "x": 140, "y": 510, "w": 1300, "ok": True, "text": "Best evidence: helps break down lactose", "at": [2, "lactose"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "benefits", "title": "The Good Stuff", "emoji": "💪", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the benefits. Number one is protein density. Ten grams per hundred grams, for just seventy-three calories. "
                  "That's one of the best protein-to-calorie ratios among dairy foods.", {}),
            ("H", "Most of that protein is casein, which breaks down slowly and releases amino acids over several hours. "
                  "That makes it a good fit for staying full, and for eating before bed.", {}),
            ("P", "A slow-release snack. Very fancy.", {"mood": "happy"}),
        ], "els": [
            {"type": "stat", "x": 330, "y": 380, "w": 420, "h": 300, "value": 10, "unit": " g", "label": "protein / 100 g", "emoji": "💪", "at": [0, "Ten"]},
            {"type": "stat", "x": 810, "y": 380, "w": 420, "h": 300, "value": 73, "unit": "", "label": "calories / 100 g", "emoji": "🔥", "at": [0, "seventy"]},
            {"type": "card", "x": 570, "y": 700, "w": 900, "h": 160, "emoji": "🐢", "title": "Casein: slow release",
             "body": "amino acids over several hours", "at": [1, "casein"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Fullness has actually been tested. Trials compared high-protein Greek yogurt with snacks of the same calories, "
                  "and found people felt fuller and ate less at the next meal.", {}),
            ("H", "Lactose tolerance: some people with lactose intolerance handle yogurt better than milk. "
                  "But it depends on the person and on the amount.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 300, "w": 1100, "h": 190, "emoji": "😌", "title": "Fuller, ate less next meal",
             "body": "vs snacks with the same calories", "at": [0, "fuller"]},
            {"type": "card", "x": 720, "y": 560, "w": 1100, "h": 190, "emoji": "🥛", "title": "Often easier than milk",
             "body": "for some people · depends on you and the amount", "at": [1, "better"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "It also brings meaningful amounts of vitamin B12, riboflavin, which is vitamin B2, and phosphorus.", {}),
            ("H", "Sodium is low, only about thirty to forty milligrams per hundred grams. "
                  "Compare that with cottage cheese, at around three hundred sixty-four.", {}),
            ("H", "And it's flexible in the kitchen. It can replace sour cream, mayonnaise or cream in dips and sauces, "
                  "with less fat and more protein.", {}),
            ("P", "Vitamins, low salt, and it does dips. Fine. You may have my sprinkle.", {"mood": "smug", "jump": True}),
        ], "els": [
            {"type": "pill", "x": 300, "y": 190, "text": "B12", "color": "#8B5CF6", "at": [0, "B12"]},
            {"type": "pill", "x": 600, "y": 190, "text": "B2 (riboflavin)", "color": "#0EA5E9", "at": [0, "riboflavin"]},
            {"type": "pill", "x": 960, "y": 190, "text": "phosphorus", "color": "#14B8A6", "at": [0, "phosphorus"]},
            T("Sodium per 100 g", 760, 320, 52, at=[1, "Sodium"], font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 430, "w": 1200, "row_h": 92, "max": 364, "unit": " mg", "rows": [
                {"label": "Greek yogurt", "value": 34, "color": "#16A34A", "at": [1, "thirty"]},
                {"label": "Cottage", "value": 364, "color": "#EF4444", "at": [1, "cottage"]},
            ]},
            {"type": "card", "x": 760, "y": 750, "w": 1100, "h": 150, "emoji": "🥣", "title": "Swaps for sour cream, mayo, cream",
             "at": [2, "replace"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Alright, the catches. First: sugar in the flavored versions. They often have ten to fifteen grams of sugar per hundred grams.", {}),
            ("H", "But careful. Total sugars include the natural sugar in milk and fruit, plus any added sugar. "
                  "So not all the sugar in the cup is added sugar. Check the ingredient list and the sugar per hundred grams.", {}),
        ], "els": [
            T("#1 Sugar in flavored cups", 760, 160, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "stat", "x": 470, "y": 440, "w": 500, "h": 300, "value": 3.6, "decimals": 1, "unit": " g", "label": "plain, per 100 g", "emoji": "🥛", "at": [0, "flavored"], "color": "ok"},
            {"type": "stat", "x": 1050, "y": 440, "w": 500, "h": 300, "value": 15, "unit": " g", "label": "flavored: 10 to 15 g", "emoji": "🍓", "at": [0, "fifteen"], "color": "red"},
            {"type": "pill", "x": 760, "y": 720, "text": "total sugars = milk + fruit + added", "color": "orange", "at": [1, "Total"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Second: calcium. More protein does not guarantee more calcium. Our U.S.D.A. example has one hundred fifteen milligrams per hundred grams, "
                  "and the product you buy may be different.",
             {"say": "Second: calcium. More protein does not guarantee more calcium. Our U S D A example has one hundred fifteen milligrams per hundred grams, "
                     "and the product you buy may be different."}),
            ("H", "Third: price and sustainability. It takes three to four liters of milk to make one kilogram. "
                  "The leftover whey used to be a real environmental problem, though today it's used for protein powders and animal feed.", {}),
        ], "els": [
            {"type": "card", "x": 760, "y": 250, "w": 1100, "h": 180, "emoji": "🦴", "title": "#2 Calcium",
             "body": "more protein ≠ more calcium · check your product", "at": 0},
            {"type": "card", "x": 760, "y": 510, "w": 1100, "h": 180, "emoji": "🥛", "title": "#3 Price: 3 to 4 L milk per kg",
             "body": "leftover whey now goes to protein powder, feed", "at": [1, "liters"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Fourth: milk protein allergy. Unlike lactose intolerance, it means avoiding dairy completely. "
                  "Straining concentrates the casein, and doesn't make it any less allergenic.", {}),
            ("H", "And fifth: saturated fat. Ten percent Greek yogurt has a significant amount. "
                  "The zero to five percent versions are common, and work for most uses.", {}),
            ("P", "And sixth: not enough pumpkin seeds on top. That's a catch too.", {"mood": "smug", "jump": True}),
        ], "els": [
            {"type": "card", "x": 760, "y": 250, "w": 1100, "h": 180, "emoji": "🚫", "title": "#4 Milk protein allergy",
             "body": "avoid fully · straining doesn't help", "at": 0},
            {"type": "card", "x": 760, "y": 510, "w": 1100, "h": 180, "emoji": "🧈", "title": "#5 Saturated fat in 10%",
             "body": "0 to 5% versions suit most uses", "at": 1},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "How to Use It", "emoji": "🥄", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So how should you use it? The single most useful move: buy plain, and sweeten it at home.", {}),
            ("H", "Plain yogurt, plus fresh fruit, plus cinnamon or a little honey, gives you the same experience "
                  "with about a third of the sugar.", {}),
            ("P", "And a sprinkle of pumpkin seeds. I'm just saying.", {"mood": "happy", "wave": True}),
        ], "els": [
            T("Buy plain, sweeten at home", 720, 180, 72, at=[0, "plain"], font="fredoka", weight=700, color="green"),
            E("🥛", 280, 420, 160, at=[1, "Plain"]),
            T("+", 450, 420, 100, at=[1, "fruit"], font="fredoka", weight=700, color="orange"),
            E("🍓", 610, 420, 160, at=[1, "fruit"]),
            T("+", 780, 420, 100, at=[1, "cinnamon"], font="fredoka", weight=700, color="orange"),
            E("🍯", 950, 420, 160, at=[1, "honey"]),
            T("cinnamon or a little honey", 950, 540, 38, at=[1, "honey"], color="muted"),
            {"type": "banner", "x": 720, "y": 720, "text": "About 1/3 of the sugar", "color": "#16A34A", "at": [1, "third"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "On the label, look for a short ingredient list: just milk and cultures. "
                  "Look for live and active cultures. And skip starch or thickeners, the sign of a Greek-style product that wasn't really strained.", {}),
            ("H", "If yogurt is a main calcium source for you, check how much it actually provides. "
                  "Other sources include hard cheese, whole tahini, and tofu made with calcium sulfate.", {}),
        ], "els": [
            {"type": "check", "x": 140, "y": 200, "w": 1300, "ok": True, "text": "Short list: milk + cultures", "at": [0, "short"]},
            {"type": "check", "x": 140, "y": 330, "w": 1300, "ok": True, "text": "\"Live and active cultures\"", "at": [0, "active"]},
            {"type": "check", "x": 140, "y": 460, "w": 1300, "ok": False, "text": "Starch or thickeners", "at": [0, "starch"]},
            {"type": "card", "x": 790, "y": 690, "w": 1300, "h": 170, "emoji": "🧀", "title": "Calcium: hard cheese, tahini, tofu",
             "body": "whole tahini · tofu made with calcium sulfate", "at": [1, "Other"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "In cooking, it's a great swap for sour cream and mayo. But don't boil it. The milk protein curdles and turns grainy.", {}),
            ("H", "Add it at the end, with the heat off, or stabilize it with a spoonful of cornstarch.", {}),
            ("H", "And before bed, a cup gives about twenty grams of slow-release casein. "
                  "For people who train, that practice makes sense based on how casein works.", {}),
            ("P", "Goodnight, yogurt. Goodnight, gains.", {"mood": "sleepy"}),
        ], "els": [
            {"type": "card", "x": 740, "y": 220, "w": 1000, "h": 170, "emoji": "🫕", "title": "Don't boil it",
             "body": "the protein curdles and goes grainy", "at": [0, "boil"], "fill": "#FEE2E2"},
            {"type": "card", "x": 740, "y": 430, "w": 1000, "h": 170, "emoji": "🥄", "title": "Heat off, or a spoon of cornstarch",
             "body": "add it at the end", "at": [1, "end,"]},
            {"type": "card", "x": 740, "y": 640, "w": 1000, "h": 170, "emoji": "🌙", "title": "Before bed: ~20 g casein",
             "body": "a fit for people who train", "at": [2, "bed,"], "fill": "#E0E7FF"},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: Greek yogurt is strained, so it's thicker, and usually higher in protein per hundred grams.", {}),
            ("H", "Two: there's no fixed ratio between products for protein, lactose or calcium.", {}),
            ("H", "Three: to compare, check the values per hundred grams, the fat percentage, and the added sugar.", {}),
            ("H", "Four: plain is best. You control what goes on top.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Strained: thicker, usually more protein", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "No fixed ratio between brands", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Compare per 100 g, fat %, added sugar", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Buy plain, top it yourself", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So, verdict: is Greek yogurt worthy of me?", {"mood": "surprised"}),
            ("H", "Plain, strained, and topped with a measured handful of you? I'd say it's a match.", {}),
            ("P", "A perfect couple!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Go strain something!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article + sources: wiseplate.blog/food/greek-yogurt", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
