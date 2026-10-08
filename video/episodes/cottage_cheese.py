"""Cottage cheese explainer (English), based on https://wiseplate.blog/en/food/cottage-cheese/

Numbers are the article's: 5% cottage cheese per 100 g unless a line says
otherwise (the 3% version, a 250 g container, the per-100 g comparison table
of dairy protein sources). Keep them in sync with content/food/cottage-cheese.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Cottage Cheese: Great Protein, but Low Calcium?"
SLUG = "cottage-cheese"
ARTICLE = "https://wiseplate.blog/en/food/cottage-cheese/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "COTTAGE CHEESE", "top_size": 120, "bottom": "LOW CALCIUM?", "bottom_size": 130,
         "badge": "11 g", "badge_label": "protein in\n98 calories", "badge_color": "#0EA5E9",
         "scatter": "🥛", "hero": "🧀", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "made":     {"bpm": 104, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.65, "swing": 0.15},
    "inside":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "casein":   {"bpm": 84, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "protein":  {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "calcium":  {"bpm": 96, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.6},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "faceoff":  {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#F0F9FF", "made": "#FEF9C3", "inside": "#ECFDF5", "casein": "#1E1B4B",
    "protein": "#E0F2FE", "calcium": "#F1F5F9", "catches": "#FEE2E2", "faceoff": "#ECFCCB",
    "howto": "#FFEDD5", "outro": "#F0F9FF",
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
            ("P", "Hi there! Pip the pumpkin seed here, guest reviewer and part-time snack.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest is white, lumpy, and lives in a little tub. It's cottage cheese!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🥛", 960, 200, 160, at=[1, "cottage"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today: cottage cheese. How it's made, why its protein is the slow kind, "
                  "a calcium surprise, and its main downside, the salt.", {}),
            ("P", "A slow protein and a surprise? I'm on the edge of my shell.", {"mood": "smug"}),
        ], "els": [
            E("🥛", 400, 330, 200, at=[0, "cottage"], wobble=True),
            T("Cottage cheese", 580, 300, 120, at=[0, "cottage"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🌙", "title": "The slow protein", "at": [0, "slow"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🦴", "title": "A calcium surprise", "at": [0, "calcium"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "🧂", "title": "The salt", "at": [0, "salt"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "made", "title": "How It's Made", "emoji": "🥛", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Cottage cheese is a fresh, unaged cheese. And it's made from two basic ingredients: "
                  "milk, and a bacterial culture. Some products add a little cream at the end.", {}),
            ("H", "Step one, souring. Lactic acid bacteria are added to the milk and lower its pH. "
                  "Sometimes a small amount of coagulating enzyme goes in too.",
             {"say": "Step one, souring. Lactic acid bacteria are added to the milk and lower its P H. "
                     "Sometimes a small amount of coagulating enzyme goes in too."}),
            ("H", "Step two, curdling. At the low pH, the milk protein casein loses its stability and curdles. "
                  "It separates from the liquid, which is the whey.",
             {"say": "Step two, curdling. At the low P H, the milk protein kay-seen loses its stability and curdles. "
                     "It separates from the liquid, which is the whey."}),
        ], "els": [
            E("🥛", 420, 230, 130, at=[0, "milk"]),
            T("milk", 420, 330, 44, at=[0, "milk"], font="fredoka", weight=600),
            T("+", 620, 240, 90, at=[0, "bacterial"], font="fredoka", weight=700, color="muted"),
            E("🦠", 820, 230, 130, at=[0, "bacterial"]),
            T("culture", 820, 330, 44, at=[0, "bacterial"], font="fredoka", weight=600),
            {"type": "pill", "x": 1180, "y": 260, "text": "+ a little cream", "color": "#0EA5E9", "at": [0, "cream"]},
            {"type": "card", "x": 720, "y": 510, "w": 1000, "h": 150, "emoji": "1️⃣", "title": "Souring: the pH drops", "at": [1, "souring"]},
            {"type": "card", "x": 720, "y": 700, "w": 1000, "h": 150, "emoji": "2️⃣", "title": "Curdling: casein meets whey", "at": [2, "curdling"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Step three is the one that sets cottage cheese apart. The curd is cut into granules and rinsed with water. "
                  "That removes extra acidity and lactose, and gives the mild flavor and the granular texture.", {}),
            ("H", "Step four, the dressing. The granules are mixed with a little milk or cream, "
                  "which sets the final fat percentage: three, five, or nine percent.", {}),
            ("P", "They rinse it? I've never been rinsed. I've been roasted.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 180, "emoji": "3️⃣", "title": "Cut and rinse",
             "body": "the step that makes it cottage cheese", "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 450, "w": 1000, "h": 180, "emoji": "4️⃣", "title": "The dressing",
             "body": "a little milk or cream", "at": [1, "dressing"]},
            {"type": "pill", "x": 470, "y": 640, "text": "3%", "color": "green", "at": [1, "three"]},
            {"type": "pill", "x": 720, "y": 640, "text": "5%", "color": "green", "at": [1, "five"]},
            {"type": "pill", "x": 970, "y": 640, "text": "9%", "color": "green", "at": [1, "nine"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And what doesn't happen: no pressing, and no aging. That's why it holds a lot of water, "
                  "keeps only a short time, and counts as a fresh cheese.", {}),
            ("H", "A quality cottage cheese has a short ingredient list: milk, cream, culture and salt.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 220, "w": 1240, "ok": False, "text": "No pressing", "at": [0, "pressing"]},
            {"type": "check", "x": 160, "y": 350, "w": 1240, "ok": False, "text": "No aging", "at": [0, "aging"]},
            {"type": "pill", "x": 780, "y": 480, "text": "lots of water · short shelf life · a fresh cheese", "color": "#0EA5E9", "at": [0, "water"]},
            {"type": "card", "x": 780, "y": 680, "w": 1100, "h": 170, "emoji": "🏷️", "title": "Milk, cream, culture, salt",
             "body": "a short label is a good sign", "at": [1, "ingredient"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "inside", "title": "What's in the Tub", "emoji": "📊", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Here's the label. One hundred grams of five percent cottage cheese gives about ninety-eight calories, "
                  "eleven grams of protein, four point three grams of fat, and three point four grams of carbs.", {}),
            ("H", "In the three percent version, calories drop to about eighty, and fat to about three grams.", {}),
        ], "els": [
            T("5% cottage cheese, per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 280, "y": 380, "w": 290, "h": 280, "value": 98, "label": "calories", "emoji": "🔥", "at": [0, "ninety"], "vsize": 84},
            {"type": "stat", "x": 610, "y": 380, "w": 290, "h": 280, "value": 11, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "eleven"], "vsize": 84},
            {"type": "stat", "x": 940, "y": 380, "w": 290, "h": 280, "value": 4.3, "decimals": 1, "unit": " g", "label": "fat", "emoji": "🧈", "at": [0, "fat"], "vsize": 84},
            {"type": "stat", "x": 1270, "y": 380, "w": 290, "h": 280, "value": 3.4, "decimals": 1, "unit": " g", "label": "carbs", "emoji": "🍞", "at": [0, "carbs"], "vsize": 84},
            {"type": "pill", "x": 760, "y": 680, "text": "3% version: about 80 calories, 3 g fat", "color": "#0EA5E9", "at": [1, "three"]},
        ], "pip_hide": True},
        {"pip": PIP_S, "lines": [
            ("H", "There's more in the tub. One hundred grams provide about one hundred sixty milligrams of phosphorus, "
                  "and about nine micrograms of selenium.", {}),
            ("H", "Plus vitamin B12 and riboflavin, which is B2, in significant amounts. About zero point four micrograms of B12 per hundred grams.",
             {"say": "Plus vitamin B 12 and riboflavin, which is B 2, in significant amounts. About zero point four micrograms of B 12 per hundred grams."}),
            ("P", "Phosphorus, selenium, B12. Not bad for something that looks like a cloud.",
             {"say": "Phosphorus, selenium, B 12. Not bad for something that looks like a cloud.", "mood": "happy"}),
        ], "els": [
            T("Per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 400, "y": 400, "w": 420, "h": 280, "value": 160, "unit": " mg", "label": "phosphorus", "emoji": "🦴", "at": [0, "sixty"]},
            {"type": "stat", "x": 860, "y": 400, "w": 420, "h": 280, "value": 9, "unit": " mcg", "label": "selenium", "emoji": "🛡️", "at": [0, "nine"]},
            {"type": "stat", "x": 1320, "y": 400, "w": 420, "h": 280, "value": 0.4, "decimals": 1, "unit": " mcg", "label": "vitamin B12", "emoji": "⚡", "at": [1, "zero"]},
            {"type": "pill", "x": 760, "y": 650, "text": "plus riboflavin (B2)", "color": "green", "at": [1, "riboflavin"]},
        ], "pip_hide": True},
        {"pip": PIP_R, "lines": [
            ("H", "And it's relatively low in lactose. Most of the lactose drains off with the whey, "
                  "leaving about two to three grams per hundred grams.", {}),
            ("H", "So some people with mild lactose intolerance tolerate it better than milk. "
                  "Aged hard cheeses contain even less, though.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "🥛", "title": "Lactose: 2 to 3 g",
             "body": "per 100 g · most drains off with the whey", "at": [0, "lactose"]},
            {"type": "card", "x": 720, "y": 500, "w": 1000, "h": 190, "emoji": "🙂", "title": "Mild intolerance?",
             "body": "often tolerated better than milk", "at": [1, "mild"], "fill": "#DCFCE7"},
            {"type": "pill", "x": 720, "y": 690, "text": "aged hard cheeses: even less lactose", "color": "orange", "at": [1, "Aged"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "casein", "title": "The Slow Protein", "emoji": "🌙", "dark": True, "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Milk protein comes in two types. Whey, about twenty percent, and casein, about eighty percent.",
             {"say": "Milk protein comes in two types. Whey, about twenty percent, and kay-seen, about eighty percent."}),
            ("H", "In cottage cheese the ratio is even more extreme. Most of the whey is drained off, "
                  "so the protein that's left is almost entirely casein.",
             {"say": "In cottage cheese the ratio is even more extreme. Most of the whey is drained off, "
                     "so the protein that's left is almost entirely kay-seen."}),
        ], "els": [
            T("Milk protein", 720, 170, 72, at=0, font="fredoka", weight=700, color="#FDE68A"),
            {"type": "ring", "x": 460, "y": 450, "r": 130, "value": 20, "label": "whey", "color": "#38BDF8", "at": [0, "Whey"]},
            {"type": "ring", "x": 980, "y": 450, "r": 130, "value": 80, "label": "casein", "color": "#FBBF24", "at": [0, "eighty"]},
            {"type": "banner", "x": 720, "y": 720, "text": "Cottage cheese: almost all casein", "color": "#F59E0B", "at": [1, "entirely"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Why it matters: whey protein is absorbed quickly. It gives a sharp, short rise in amino acids in the blood.", {}),
            ("H", "Casein forms a clot in the acidic stomach and breaks down slowly. "
                  "That means a steady release of amino acids over hours.",
             {"say": "Kay-seen forms a clot in the acidic stomach and breaks down slowly. "
                     "That means a steady release of amino acids over hours."}),
            ("P", "Fast whey, slow casein. The tortoise and the hare, but with cheese.", {"mood": "smug",
             "say": "Fast whey, slow kay-seen. The tortoise and the hare, but with cheese."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "🐇", "title": "Whey: fast",
             "body": "a sharp, short rise in amino acids", "at": [0, "whey"], **DARK},
            {"type": "card", "x": 720, "y": 510, "w": 1000, "h": 190, "emoji": "🐢", "title": "Casein: slow",
             "body": "a clot in the stomach · released over hours", "at": [1, "clot"], **DARK},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "That's the logic behind eating cottage cheese before bed.", {}),
            ("H", "Several trials found that about thirty to forty grams of casein before sleep raises muscle protein synthesis "
                  "during the night, and improves recovery.",
             {"say": "Several trials found that about thirty to forty grams of kay-seen before sleep raises muscle protein synthesis "
                     "during the night, and improves recovery."}),
            ("H", "The caveat: the evidence isn't conclusive about how big the effect on muscle growth is over time. "
                  "But the mechanism is well established.", {}),
        ], "els": [
            E("🛏️", 440, 250, 150, at=[0, "bed"]),
            T("Before bed", 540, 250, 80, at=[0, "bed"], font="fredoka", weight=700, color="#FDE68A", anchor="l"),
            {"type": "card", "x": 720, "y": 470, "w": 1000, "h": 180, "emoji": "💪", "title": "30 to 40 g casein",
             "body": "more muscle protein synthesis overnight", "at": [1, "thirty"], **DARK},
            {"type": "pill", "x": 720, "y": 680, "text": "long-term muscle gain: not conclusive", "color": "orange", "at": [2, "conclusive"]},
            {"type": "pill", "x": 720, "y": 790, "text": "the mechanism: well established", "color": "green", "at": [2, "mechanism"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "protein", "title": "Protein per Calorie", "emoji": "💪", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Its big advantage is one of the best protein-to-calorie ratios on the market. "
                  "Eleven grams of protein in ninety-eight calories, or in about eighty calories in the three percent version.", {}),
            ("H", "Hard cheeses have twenty-five grams of protein, but around four hundred calories. "
                  "That makes cottage cheese a clear advantage for weight management.", {}),
            ("P", "Four hundred calories? Hard cheese, we need to talk.", {"mood": "surprised"}),
        ], "els": [
            T("Per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "versus", "x": 160, "y": 360, "w": 1300, "row_h": 170, "label_w": 300,
             "names": ["Cottage 5%", "Hard cheese"], "at": [1, "Hard"], "rows": [
                 {"label": "Protein", "a": 11, "b": 25, "unit": " g", "at": [1, "twenty"]},
                 {"label": "Calories", "a": 98, "b": 400, "unit": "", "at": [1, "four"]},
             ]},
            {"type": "pill", "x": 760, "y": 740, "text": "a clear advantage for weight management", "color": "green", "at": [1, "weight"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "It's a complete protein with high biological value, with all the essential amino acids. "
                  "And it's rich in leucine, the amino acid that switches on the mTOR pathway for building muscle protein.",
             {"say": "It's a complete protein with high biological value, with all the essential amino acids. "
                     "And it's rich in loo-seen, the amino acid that switches on the M tor pathway for building muscle protein."}),
            ("H", "Then there's satiety. High protein plus lots of water fills you up for few calories. "
                  "Studies compared cottage cheese with eggs for breakfast, and found similar satiety.", {}),
            ("P", "As filling as eggs. The eggs did not see that coming.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 180, "emoji": "🧬", "title": "Complete protein",
             "body": "rich in leucine, which drives mTOR", "at": 0},
            {"type": "card", "x": 720, "y": 470, "w": 1000, "h": 180, "emoji": "😌", "title": "Very filling",
             "body": "protein + water, few calories", "at": [1, "satiety"], "fill": "#DCFCE7"},
            E("🥚", 560, 700, 110, at=[1, "eggs"]),
            T("=", 720, 700, 80, at=[1, "similar"], font="fredoka", weight=700, color="green"),
            E("🥛", 880, 700, 110, at=[1, "similar"]),
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "calcium", "title": "The Calcium Surprise", "emoji": "🦴", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Now the most surprising point, and it runs against intuition. Cottage cheese is low in calcium.", {}),
            ("H", "It has only about eighty to ninety milligrams per hundred grams. "
                  "Less than milk, at one hundred twenty, and much less than yellow cheese, at seven hundred to nine hundred.", {}),
            ("P", "Wait, what? A dairy product that's low in calcium?", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("Calcium per 100 g", 760, 160, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 160, "y": 330, "w": 1300, "row_h": 130, "max": 1300, "unit": " mg", "rows": [
                {"label": "Cottage", "value": 90, "text": "80 to 90 mg", "color": "#F97316", "at": [1, "eighty"]},
                {"label": "Milk", "value": 120, "text": "120 mg", "color": "#0EA5E9", "at": [1, "milk"]},
                {"label": "Yellow cheese", "value": 900, "text": "700 to 900 mg", "color": "#16A34A", "at": [1, "yellow"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The reason: a large part of the calcium in milk is bound to the whey and to the soluble casein, "
                  "and it drains out during production.",
             {"say": "The reason: a large part of the calcium in milk is bound to the whey and to the soluble kay-seen, "
                     "and it drains out during production."}),
            ("H", "So cottage cheese is an excellent source of protein, but not a major source of calcium, "
                  "despite the popular belief.", {}),
            ("P", "Great protein, so-so calcium. Noted.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "💧", "title": "It drains out",
             "body": "with the whey and soluble casein", "at": [0, "drains"]},
            {"type": "check", "x": 220, "y": 500, "w": 1000, "ok": True, "text": "Excellent protein source", "at": [1, "excellent"]},
            {"type": "check", "x": 220, "y": 630, "w": 1000, "ok": False, "text": "Not a major calcium source", "at": [1, "major"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Salty Side", "emoji": "🧂", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "The main downside is sodium. One hundred grams have about three hundred thirty to four hundred milligrams.", {}),
            ("H", "A whole two hundred fifty gram container may give about nine hundred milligrams. "
                  "That's close to half the daily recommendation.", {}),
            ("H", "The salt isn't only for flavor. It's part of the production process, and of preservation. "
                  "Reduced-sodium versions exist, and they're the better pick for people with high blood pressure.", {}),
        ], "els": [
            T("#1 Sodium", 760, 160, 80, at=0, font="fredoka", weight=700, color="red"),
            {"type": "stat", "x": 470, "y": 400, "w": 520, "h": 280, "text": "330-400 mg", "value": 0, "label": "per 100 g",
             "emoji": "🧂", "at": [0, "three"], "color": "orange", "vsize": 84},
            {"type": "stat", "x": 1050, "y": 400, "w": 520, "h": 280, "value": 900, "unit": " mg", "label": "a 250 g container",
             "emoji": "🥛", "at": [1, "container"], "color": "red"},
            {"type": "pill", "x": 760, "y": 640, "text": "close to half the daily recommendation", "color": "red", "at": [1, "half"]},
            {"type": "pill", "x": 760, "y": 760, "text": "high blood pressure? choose reduced-sodium", "color": "green", "at": [2, "Reduced"]},
        ], "pip_hide": True},
        {"pip": PIP_S, "lines": [
            ("H", "Catch two: flavored versions. With sweet add-ins like fruit or vanilla, "
                  "they usually have eight to twelve grams of sugar per hundred grams. That's triple the carbs. Read the labels.", {}),
            ("H", "Catch three: milk protein allergy. Unlike lactose intolerance, it's an immune reaction to casein, "
                  "and it means complete avoidance. Cottage cheese is especially rich in casein.",
             {"say": "Catch three: milk protein allergy. Unlike lactose intolerance, it's an immune reaction to kay-seen, "
                     "and it means complete avoidance. Cottage cheese is especially rich in kay-seen."}),
            ("P", "Fruit on the bottom, sugar on the top. Sneaky.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 760, "y": 260, "w": 1100, "h": 190, "emoji": "🍓", "title": "#2 Flavored: 8 to 12 g sugar",
             "body": "per 100 g · triple the carbs", "at": 0, "fill": "#FEF3C7"},
            {"type": "card", "x": 760, "y": 510, "w": 1100, "h": 190, "emoji": "🚫", "title": "#3 Milk protein allergy",
             "body": "an immune reaction to casein: avoid it", "at": [1, "allergy"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Catch four: a short shelf life. As a fresh, unaged cheese, it spoils fairly fast. "
                  "Eat it within a few days of opening, and keep it in the fridge.", {}),
            ("H", "And catch five: additives. Some products contain stabilizers, thickeners or preservatives. "
                  "A short ingredient list is better.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "🧊", "title": "#4 Short shelf life",
             "body": "a few days after opening · keep it cold", "at": 0},
            {"type": "card", "x": 720, "y": 510, "w": 1000, "h": 190, "emoji": "🏷️", "title": "#5 Additives",
             "body": "stabilizers, thickeners, preservatives", "at": [1, "additives"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "faceoff", "title": "Dairy Face-Off", "emoji": "⚖️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "How does it compare with other dairy protein sources? Per hundred grams, sodium tells the story.", {}),
            ("H", "Five percent cottage cheese, three hundred sixty-four milligrams. Greek yogurt, thirty-four. "
                  "White cheese, three hundred. Milk, forty-three. And yellow cheese, six hundred twenty.", {}),
        ], "els": [
            T("Sodium per 100 g", 760, 150, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 160, "y": 290, "w": 1300, "row_h": 115, "max": 800, "unit": " mg", "rows": [
                {"label": "Cottage 5%", "value": 364, "color": "#F97316", "at": [1, "sixty"]},
                {"label": "Greek yogurt", "value": 34, "color": "#16A34A", "at": [1, "Greek"]},
                {"label": "White cheese", "value": 300, "color": "#F59E0B", "at": [1, "White"]},
                {"label": "Milk 3%", "value": 43, "color": "#16A34A", "at": [1, "Milk"]},
                {"label": "Yellow cheese", "value": 620, "color": "#EF4444", "at": [1, "yellow"]},
            ]},
        ], "pip_hide": True},
        {"pip": PIP_R, "lines": [
            ("H", "So, cottage cheese or Greek yogurt? They're similar in protein, eleven grams against ten.", {}),
            ("H", "Greek yogurt wins on sodium, which is much lower, and it has live cultures. "
                  "Cottage cheese wins on slow-release casein. Both are excellent.",
             {"say": "Greek yogurt wins on sodium, which is much lower, and it has live cultures. "
                     "Cottage cheese wins on slow release kay-seen. Both are excellent."}),
            ("P", "A tie! Everybody gets a trophy. Except hard cheese.", {"mood": "happy", "jump": True}),
        ], "els": [
            T("11 g vs 10 g protein", 720, 170, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 420, "y": 450, "w": 620, "h": 230, "emoji": "🥣", "title": "Greek yogurt",
             "body": "less sodium, live cultures", "at": [1, "Greek"]},
            {"type": "card", "x": 1070, "y": 450, "w": 620, "h": 230, "emoji": "🥛", "title": "Cottage",
             "body": "slow-release casein", "at": [1, "Cottage"]},
            {"type": "banner", "x": 720, "y": 710, "text": "Both are excellent", "color": "#16A34A", "at": [1, "Both"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "howto", "title": "How to Eat It", "emoji": "🥄", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "A reasonable serving is one hundred fifty to two hundred fifty grams. "
                  "That's sixteen to twenty-seven grams of protein. Just keep an eye on the sodium adding up.", {}),
            ("H", "Before bed, one hundred fifty to two hundred grams gives about twenty grams of casein. "
                  "It's a practice with a solid mechanism, for athletes and anyone doing resistance training.",
             {"say": "Before bed, one hundred fifty to two hundred grams gives about twenty grams of kay-seen. "
                     "It's a practice with a solid mechanism, for athletes and anyone doing resistance training."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 250, "w": 1000, "h": 190, "emoji": "🥄", "title": "150 to 250 g a serving",
             "body": "16 to 27 g protein · watch the sodium", "at": 0},
            {"type": "card", "x": 720, "y": 500, "w": 1000, "h": 190, "emoji": "🌙", "title": "Before bed: 150 to 200 g",
             "body": "about 20 g casein", "at": [1, "bed"]},
            {"type": "pill", "x": 720, "y": 690, "text": "for athletes and resistance training", "color": "green", "at": [1, "athletes"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Balance the calcium. If cottage cheese is a main protein source for you, get calcium elsewhere: "
                  "yogurt, hard cheese, whole tahini, tofu set with calcium sulfate, or kale.",
             {"say": "Balance the calcium. If cottage cheese is a main protein source for you, get calcium elsewhere: "
                     "yogurt, hard cheese, whole ta-hee-nee, tofu set with calcium sulfate, or kale."}),
            ("P", "Tahini is made of seeds. I'm just saying.", {"mood": "smug", "say": "Ta-hee-nee is made of seeds. I'm just saying."}),
        ], "els": [
            T("Calcium from elsewhere", 760, 160, 64, at=0, font="fredoka", weight=700, color="green"),
            E("🥣", 260, 380, 120, at=[0, "yogurt"]),
            T("yogurt", 260, 480, 40, at=[0, "yogurt"], font="fredoka", weight=600),
            E("🧀", 530, 380, 120, at=[0, "hard"]),
            T("hard cheese", 530, 480, 40, at=[0, "hard"], font="fredoka", weight=600),
            E("🫙", 800, 380, 120, at=[0, "tahini"]),
            T("whole tahini", 800, 480, 40, at=[0, "tahini"], font="fredoka", weight=600),
            E("🍢", 1070, 380, 120, at=[0, "tofu"]),
            T("tofu", 1070, 480, 40, at=[0, "tofu"], font="fredoka", weight=600),
            {"type": "pill", "x": 760, "y": 640, "text": "tofu: the kind set with calcium sulfate", "color": "#0EA5E9", "at": [0, "sulfate"]},
            E("🥬", 1340, 380, 120, at=[0, "kale"]),
            T("kale", 1340, 480, 40, at=[0, "kale"], font="fredoka", weight=600),
        ], "pip_hide": True},
        {"pip": PIP_R, "lines": [
            ("H", "Prefer plain over flavored, and add your own fresh fruit, walnuts or cinnamon. "
                  "That gives you full control over the sugar.", {}),
            ("H", "For a filling meal, try cottage cheese with vegetables, olive oil and whole-grain bread. "
                  "It's balanced and very satisfying.", {}),
            ("H", "And with high blood pressure, choosing reduced sodium matters more than the fat percentage.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 180, "emoji": "🍓", "title": "Plain + your own toppings",
             "body": "fruit, walnuts or cinnamon", "at": 0},
            {"type": "card", "x": 720, "y": 460, "w": 1000, "h": 180, "emoji": "🥗", "title": "A filling meal",
             "body": "vegetables, olive oil, whole-grain bread", "at": [1, "filling"], "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 690, "w": 1000, "h": 180, "emoji": "🩺", "title": "Sodium over fat %",
             "body": "for high blood pressure", "at": [2, "blood"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 9
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: cottage cheese is one of the most efficient protein sources for its calories. Eleven grams of protein in about ninety-eight calories.", {}),
            ("H", "Two: its protein is almost all slow-release casein, which suits eating it before bed.",
             {"say": "Two: its protein is almost all slow release kay-seen, which suits eating it before bed."}),
            ("H", "Three: it's low in calcium compared with other dairy, so it doesn't replace them for that.", {}),
            ("H", "Four: it's high in sodium, its main practical downside. A reduced-salt version helps.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "11 g protein in 98 calories", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Slow casein, good before bed", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": False, "text": "Low in calcium", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": False, "text": "High in sodium: go reduced-salt", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So cottage cheese: lumpy, loyal, and full of slow protein. I respect a snack that takes its time.", {"mood": "smug"}),
            ("H", "Very wise, Pip.", {}),
            ("P", "Wise Plate, wise seed!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the details, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the details, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Check the sodium on the label!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/cottage-cheese", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
