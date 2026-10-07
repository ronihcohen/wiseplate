"""Shrimp explainer (English), based on https://wiseplate.blog/food/shrimp/

Numbers are the article's: cooked shrimp per 100 g, edible part, no sauce,
breading or frying (USDA FDC 175180, rounded), a 150 g serving, and selenium
and B12 from a separate USDA record (mixed species, moist heat, FDC 171971).
Keep them in sync with content/food/shrimp.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Shrimp: Is the Cholesterol a Problem?"
SLUG = "shrimp"
ARTICLE = "https://wiseplate.blog/en/food/shrimp/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "SHRIMP", "top_size": 210, "bottom": "CHOLESTEROL?", "bottom_size": 160,
         "badge": "24 g", "badge_label": "protein in\n99 calories", "badge_color": "#0EA5E9",
         "scatter": "🍤", "hero": "🦐", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "protein":  {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "chol":     {"bpm": 92, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.55},
    "benefits": {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "allergy":  {"bpm": 96, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.6, "swing": 0.1},
    "added":    {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "farm":     {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#ECFEFF", "protein": "#E0F2FE", "chol": "#F1F5F9", "benefits": "#ECFDF5",
    "allergy": "#FEE2E2", "added": "#FEF3C7", "farm": "#ECFCCB", "howto": "#FFEDD5",
    "outro": "#ECFEFF",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Ahoy! Pip the pumpkin seed here. I've never seen the ocean, but today the ocean came to me.", {"mood": "happy", "wave": True}),
            ("P", "Our guest is pink, curly, and very popular. It's shrimp!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🦐", 960, 200, 160, at=[1, "shrimp"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today it's shrimp, also called prawns. We'll look at its amazing protein numbers, the big cholesterol question, "
                  "and the downsides that actually matter.", {}),
            ("P", "Cholesterol drama? I brought popcorn. Well, pumpkin seeds.", {"mood": "smug"}),
        ], "els": [
            E("🦐", 420, 330, 200, at=[0, "shrimp"], wobble=True),
            T("Shrimp", 640, 300, 140, at=[0, "shrimp"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "💪", "title": "The protein", "at": [0, "protein"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🔎", "title": "Cholesterol", "at": [0, "cholesterol"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "⚠️", "title": "The real downsides", "at": [0, "downsides"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "protein", "title": "A Protein Powerhouse", "emoji": "💪", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Here's the headline. One hundred grams of cooked shrimp gives about twenty-four grams of protein, for about ninety-nine calories.", {}),
            ("H", "A one hundred fifty gram serving comes to about thirty-six grams of protein, and around one hundred forty-nine calories.", {}),
            ("H", "That's for the edible part, cooked, with no sauce, breading or frying. Other products and cooking methods can differ.", {}),
            ("P", "Twenty-four grams of protein in ninety-nine calories? That's... efficient. I'm a little jealous.", {"mood": "surprised"}),
        ], "els": [
            T("Cooked, per 100 g (USDA)", 720, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 450, "y": 400, "w": 480, "h": 300, "value": 24, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "twenty"]},
            {"type": "stat", "x": 1000, "y": 400, "w": 480, "h": 300, "value": 99, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "ninety"]},
            {"type": "pill", "x": 720, "y": 650, "text": "150 g serving: 36 g protein, 149 calories", "color": "green", "at": [1, "serving"]},
            {"type": "pill", "x": 720, "y": 750, "text": "no sauce, breading or frying", "color": "orange", "at": [2, "sauce"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "The rest of the label, per hundred grams: zero point three grams of fat, only zero point one of it saturated, "
                  "and zero point two grams of carbs.", {}),
            ("H", "Plus two hundred thirty-seven milligrams of phosphorus, one hundred eleven milligrams of sodium, "
                  "and one hundred eighty-nine milligrams of cholesterol. Hold on to that last number.", {}),
        ], "els": [
            T("Per 100 g cooked", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 330, "y": 370, "w": 400, "h": 260, "value": 0.3, "decimals": 1, "unit": " g", "label": "fat", "emoji": "🫒", "at": [0, "fat"]},
            {"type": "stat", "x": 760, "y": 370, "w": 400, "h": 260, "value": 0.1, "decimals": 1, "unit": " g", "label": "sat. fat", "emoji": "🧈", "at": [0, "saturated"]},
            {"type": "stat", "x": 1190, "y": 370, "w": 400, "h": 260, "value": 0.2, "decimals": 1, "unit": " g", "label": "carbs", "emoji": "🍞", "at": [0, "carbs"]},
            {"type": "stat", "x": 330, "y": 680, "w": 400, "h": 260, "value": 237, "unit": " mg", "label": "phosphorus", "emoji": "🦴", "at": [1, "phosphorus"]},
            {"type": "stat", "x": 760, "y": 680, "w": 400, "h": 260, "value": 111, "unit": " mg", "label": "sodium", "emoji": "🧂", "at": [1, "sodium"]},
            {"type": "stat", "x": 1190, "y": 680, "w": 400, "h": 260, "value": 189, "unit": " mg", "label": "cholesterol", "emoji": "❓", "at": [1, "cholesterol"], "color": "orange"},
        ], "pip_hide": True},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "chol", "title": "The Cholesterol Question", "emoji": "🔎", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "For decades, many people avoided shrimp because of its cholesterol. "
                  "The idea was that cholesterol in food turns straight into cholesterol in your blood.", {}),
            ("H", "The evidence changed that picture. Your body makes most of the cholesterol in your blood itself, in the liver. "
                  "And it adjusts: when you eat more, the liver makes less.", {}),
            ("P", "The liver adjusts? Smart liver.", {"mood": "surprised"}),
        ], "els": [
            T("Old idea", 450, 180, 64, at=0, font="fredoka", weight=700, color="red", strike=[1, "changed"]),
            T("food cholesterol = blood cholesterol", 450, 260, 40, at=0, color="muted"),
            {"type": "card", "x": 720, "y": 480, "w": 1000, "h": 180, "emoji": "🫀", "title": "The liver makes most of it",
             "body": "eat more, and it makes less", "at": [1, "liver"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "In twenty fifteen, the U S Dietary Guidelines dropped the numeric limit on dietary cholesterol, "
                  "which had been three hundred milligrams a day. They found not enough evidence to support it.",
             {"say": "In twenty fifteen, the U S Dietary Guidelines dropped the numeric limit on dietary cholesterol, "
                     "which had been three hundred milligrams a day. They found not enough evidence to support it."}),
            ("H", "And for shrimp specifically: controlled trials that fed people large amounts of shrimp found a modest rise in LDL, "
                  "but also a rise in HDL. So the ratio between them, a more informative risk marker, barely changed.",
             {"say": "And for shrimp specifically: controlled trials that fed people large amounts of shrimp found a modest rise in L D L, "
                     "but also a rise in H D L. So the ratio between them, a more informative risk marker, barely changed."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 180, "emoji": "📜", "title": "2015: the 300 mg limit dropped",
             "body": "US Dietary Guidelines", "at": 0},
            T("Shrimp trials", 720, 490, 56, at=[1, "trials"], font="fredoka", weight=700, color="green"),
            {"type": "pill", "x": 330, "y": 600, "text": "LDL: a bit up", "color": "orange", "at": [1, "modest"]},
            {"type": "pill", "x": 660, "y": 600, "text": "HDL: up too", "color": "ok", "at": [1, "also"]},
            {"type": "pill", "x": 1110, "y": 600, "text": "ratio: barely changed", "color": "green", "at": [1, "ratio"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Plus, shrimp is very low in saturated fat. And saturated fat is the dietary factor with a much stronger effect on LDL.",
             {"say": "Plus, shrimp is very low in saturated fat. And saturated fat is the dietary factor with a much stronger effect on L D L."}),
            ("H", "The caveat: some people are hyper-responders, and dietary cholesterol does affect them noticeably. "
                  "People with familial hypercholesterolemia, or very high LDL, should talk to their doctor, not generalize from this video.",
             {"say": "The caveat: some people are hyper responders, and dietary cholesterol does affect them noticeably. "
                     "People with familial hyper-cholesterol-emia, or very high L D L, should talk to their doctor, not generalize from this video."}),
            ("P", "So for most people, shrimp gets a pass. For some, ask a doctor first.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 240, "w": 1000, "h": 180, "emoji": "🧈", "title": "Very low saturated fat",
             "body": "the bigger driver of LDL", "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 500, "w": 1000, "h": 190, "emoji": "🩺", "title": "Hyper-responders",
             "body": "very high LDL or familial: ask your doctor", "at": [1, "hyper"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "benefits", "title": "More Good Stuff", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "That protein-to-calorie ratio is a real advantage for weight management, building muscle, and calorie-limited diets. "
                  "And it's complete protein, with all the essential amino acids.", {}),
            ("H", "Next: astaxanthin. It's the carotenoid that turns shrimp pinkish orange when cooked. It's a very strong antioxidant, "
                  "studied for oxidative stress, skin health, and muscle function after exercise.",
             {"say": "Next: asta-zanthin. It's the carotenoid that turns shrimp pinkish orange when cooked. It's a very strong antioxidant, "
                     "studied for oxidative stress, skin health, and muscle function after exercise."}),
            ("H", "But most of that research used high-dose supplements, not food amounts. So you can't apply it directly to eating shrimp.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 160, "emoji": "💪", "title": "Complete protein, few calories", "at": 0},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 180, "emoji": "🌸", "title": "Astaxanthin",
             "body": "the pink color · a strong antioxidant", "at": [1, "astaxanthin"]},
            {"type": "pill", "x": 720, "y": 680, "text": "studied mostly as high-dose supplements", "color": "orange", "at": [2, "supplements"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Minerals and vitamins: in a separate U S D A record, for mixed shrimp species cooked with moist heat, "
                  "there are about fifty micrograms of selenium, and one point seven micrograms of vitamin B12, per hundred grams.",
             {"say": "Minerals and vitamins: in a separate U S D A record, for mixed shrimp species cooked with moist heat, "
                     "there are about fifty micrograms of selenium, and one point seven micrograms of vitamin B 12, per hundred grams."}),
            ("H", "Selenium is needed for an enzyme called glutathione peroxidase, and for making thyroid hormones.",
             {"say": "Selenium is needed for an enzyme called glue-ta-thigh-own per-ox-i-dase, and for making thyroid hormones."}),
            ("H", "Seafood is also a major source of iodine, which many people in the West don't get enough of. "
                  "And shrimp is a good source of copper and zinc too.", {}),
        ], "els": [
            T("Per 100 g (a separate USDA record)", 760, 150, 50, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 470, "y": 380, "w": 480, "h": 280, "value": 50, "unit": " mcg", "label": "selenium", "emoji": "🛡️", "at": [0, "fifty"]},
            {"type": "stat", "x": 1050, "y": 380, "w": 480, "h": 280, "value": 1.7, "decimals": 1, "unit": " mcg", "label": "vitamin B12", "emoji": "⚡", "at": [0, "B12"]},
            {"type": "pill", "x": 760, "y": 600, "text": "selenium: antioxidant enzyme + thyroid", "color": "green", "at": [1, "thyroid"]},
            {"type": "pill", "x": 520, "y": 720, "text": "iodine", "color": "#0EA5E9", "at": [2, "iodine"]},
            {"type": "pill", "x": 1000, "y": 720, "text": "copper + zinc", "color": "#B45309", "at": [2, "copper"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "allergy", "title": "Allergy: The Big One", "emoji": "🚨", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the downsides, and the biggest one is allergy. Shellfish allergy is one of the most serious and common allergies in adults.", {}),
            ("H", "The main allergen is tropomyosin, a muscle protein. Reactions can be anaphylactic and life-threatening.",
             {"say": "The main allergen is tro-po-my-o-sin, a muscle protein. Reactions can be ana-fil-actic and life threatening."}),
            ("H", "Unlike many childhood allergies, it tends to last a lifetime.", {}),
        ], "els": [
            T("#1 Shellfish allergy", 720, 170, 80, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 720, "y": 400, "w": 1000, "h": 180, "emoji": "🧬", "title": "Tropomyosin",
             "body": "a muscle protein · the main allergen", "at": [1, "tropomyosin"]},
            {"type": "banner", "x": 720, "y": 630, "text": "Can be life-threatening", "color": "#DC2626", "at": [1, "anaphylactic"]},
            {"type": "pill", "x": 720, "y": 780, "text": "often lifelong", "color": "orange", "at": [2, "lifetime"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "There's also cross-reactivity with other crustaceans. And sometimes even with dust mites and cockroaches, "
                  "which carry a similar tropomyosin.",
             {"say": "There's also cross reactivity with other crustaceans. And sometimes even with dust mites and cockroaches, "
                     "which carry a similar tro-po-my-o-sin."}),
            ("P", "Cockroaches?! I did not need that mental image.", {"mood": "worried", "jump": True}),
        ], "els": [
            T("Cross-reactions", 720, 190, 72, at=0, font="fredoka", weight=700, color="green"),
            E("🦀", 400, 430, 150, at=[0, "crustaceans"]),
            T("other crustaceans", 400, 550, 40, at=[0, "crustaceans"], font="fredoka", weight=600),
            E("🦠", 760, 430, 150, at=[0, "dust"]),
            T("dust mites", 760, 550, 40, at=[0, "dust"], font="fredoka", weight=600),
            E("🪳", 1120, 430, 150, at=[0, "cockroaches"]),
            T("cockroaches", 1120, 550, 40, at=[0, "cockroaches"], font="fredoka", weight=600),
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "added", "title": "What Gets Added", "emoji": "🏷️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch two: sodium. Fresh shrimp has about one hundred ten to one hundred fifty milligrams per hundred grams.", {}),
            ("H", "But frozen and processed shrimp are often treated with brine, or polyphosphates to keep them moist. "
                  "That can push sodium up to five hundred milligrams or more. Read the label.",
             {"say": "But frozen and processed shrimp are often treated with brine, or poly-phosphates to keep them moist. "
                     "That can push sodium up to five hundred milligrams or more. Read the label."}),
        ], "els": [
            T("#2 Sodium per 100 g", 760, 170, 70, at=0, font="fredoka", weight=700, color="red"),
            {"type": "bars", "x": 200, "y": 350, "w": 1200, "row_h": 130, "max": 520, "unit": " mg", "rows": [
                {"label": "Fresh", "value": 150, "text": "110 to 150 mg", "color": "#16A34A", "at": [0, "Fresh"]},
                {"label": "Processed", "value": 500, "text": "500+ mg", "color": "#EF4444", "at": [1, "five"]},
            ]},
            {"type": "pill", "x": 760, "y": 680, "text": "brine and polyphosphates add salt", "color": "orange", "at": [1, "brine"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch three: sulfites. Shrimp is sometimes treated with sulfites to stop it turning black, a process called melanosis.",
             {"say": "Catch three: sulfites. Shrimp is sometimes treated with sulfites to stop it turning black, a process called mela-no-sis."}),
            ("H", "People sensitive to sulfites, especially people with asthma, may react. Most countries require it on the label.", {}),
            ("P", "Sulfites, polyphosphates... shrimp has more additives than a sports drink.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 760, "y": 300, "w": 1100, "h": 190, "emoji": "⚫", "title": "#3 Sulfites",
             "body": "stop the shrimp turning black", "at": 0},
            {"type": "card", "x": 760, "y": 560, "w": 1100, "h": 190, "emoji": "🫁", "title": "Asthma? Watch out",
             "body": "usually on the label", "at": [1, "asthma"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "farm", "title": "Farming and Safety", "emoji": "🌊", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch four: farming. Most shrimp on the market is raised on sea farms, mainly in Southeast Asia.", {}),
            ("H", "There have been reports of antibiotic use, crowding and poor conditions, plus environmental damage from clearing mangrove forests.", {}),
            ("H", "Labels like A S C or B A P mark stricter standards.",
             {"say": "Labels like A S C, or B A P, mark stricter standards."}),
        ], "els": [
            T("#4 Shrimp farming", 760, 170, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "pill", "x": 480, "y": 340, "text": "antibiotics", "color": "orange", "at": [1, "antibiotic"]},
            {"type": "pill", "x": 820, "y": 340, "text": "crowding", "color": "orange", "at": [1, "crowding"]},
            {"type": "pill", "x": 1160, "y": 340, "text": "mangroves", "color": "orange", "at": [1, "mangrove"]},
            {"type": "card", "x": 760, "y": 560, "w": 1000, "h": 180, "emoji": "✅", "title": "Look for ASC or BAP",
             "body": "stricter standards", "at": [2, "Labels"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch five, which is mostly good news: mercury levels in shrimp are low. "
                  "The F D A lists it among the safer choices for pregnant women.",
             {"say": "Catch five, which is mostly good news: mercury levels in shrimp are low. "
                     "The F D A lists it among the safer choices for pregnant women."}),
            ("H", "But undercooked shrimp carries a risk of bacteria, like Vibrio.",
             {"say": "But undercooked shrimp carries a risk of bacteria, like Vib-ree-oh."}),
            ("H", "And two more. Overcooking turns shrimp rubbery fast. And shrimp isn't kosher, since it has no fins or scales. "
                  "That matters to some viewers.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 210, "w": 1300, "ok": True, "text": "Mercury: low, FDA safer choice", "at": [0, "mercury"]},
            {"type": "check", "x": 160, "y": 340, "w": 1300, "ok": False, "text": "Undercooked: bacteria risk", "at": [1, "undercooked"]},
            {"type": "check", "x": 160, "y": 470, "w": 1300, "ok": False, "text": "Overcooked: rubbery", "at": [2, "rubbery"]},
            {"type": "check", "x": 160, "y": 600, "w": 1300, "ok": False, "text": "Not kosher", "at": [2, "kosher"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "Cook It Right", "emoji": "🍳", "scenes": [
        {"pip": PIP_C, "lines": [
            ("H", "Cooking shrimp right takes just two to three minutes in total. The giveaway is the shape.", {}),
            ("H", "Done shrimp curls into the letter C. If it closes into a tight O, it's overcooked and rubbery.", {}),
            ("P", "C for cooked. O for... oh no. I love it.", {"mood": "happy", "jump": True}),
        ], "els": [
            T("2 to 3 minutes", 960, 150, 90, at=0, font="fredoka", weight=700, color="green"),
            T("C", 520, 330, 220, at=[1, "C."], font="fredoka", weight=700, color="#16A34A"),
            T("perfect", 520, 470, 48, at=[1, "C."], font="fredoka", weight=600, color="#16A34A"),
            T("O", 1400, 330, 220, at=[1, "O,"], font="fredoka", weight=700, color="#DC2626"),
            T("overcooked", 1400, 470, 48, at=[1, "O,"], font="fredoka", weight=600, color="#DC2626"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "When buying, check the label for polyphosphates or brine. They add sodium, and water you pay for by weight. "
                  "Dry-packed shrimp is better, and A S C or B A P labels mean better farming standards.",
             {"say": "When buying, check the label for poly-phosphates or brine. They add sodium, and water you pay for by weight. "
                     "Dry packed shrimp is better, and A S C or B A P labels mean better farming standards."}),
            ("H", "Frozen is often the better buy. Most fresh shrimp at the counter was thawed anyway. "
                  "Individually quick frozen shrimp, thawed at home, is usually fresher.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 1000, "h": 170, "emoji": "🏷️", "title": "Skip polyphosphates, brine",
             "body": "they add sodium and water weight", "at": 0},
            {"type": "card", "x": 720, "y": 430, "w": 1000, "h": 150, "emoji": "📦", "title": "Dry-packed is better", "at": [0, "Dry"]},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 170, "emoji": "🧊", "title": "Frozen is often fresher",
             "body": "counter shrimp was usually thawed", "at": [1, "Frozen"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And the classic pairing: olive oil, garlic and lemon. It works for nutrition too. "
                  "Shrimp is almost fat-free, so it benefits from some healthy fat alongside.", {}),
            ("H", "In pregnancy, shrimp is considered a safe choice for mercury, as long as it's well cooked.", {}),
        ], "els": [
            E("🫒", 340, 330, 150, at=[0, "olive"]),
            T("olive oil", 340, 450, 42, at=[0, "olive"], font="fredoka", weight=600),
            E("🧄", 720, 330, 150, at=[0, "garlic"]),
            T("garlic", 720, 450, 42, at=[0, "garlic"], font="fredoka", weight=600),
            E("🍋", 1100, 330, 150, at=[0, "lemon"]),
            T("lemon", 1100, 450, 42, at=[0, "lemon"], font="fredoka", weight=600),
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 170, "emoji": "🤰", "title": "Pregnancy: fine, if well cooked",
             "body": "low in mercury", "at": [1, "pregnancy"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: shrimp has one of the best protein-to-calorie ratios out there. Twenty-four grams of protein in ninety-nine calories.", {}),
            ("H", "Two: it adds selenium, iodine, B12 and astaxanthin, with almost no saturated fat.",
             {"say": "Two: it adds selenium, iodine, B 12, and asta-zanthin, with almost no saturated fat."}),
            ("H", "Three: the old cholesterol fear has faded a lot, though hyper-responders should ask a doctor.", {}),
            ("H", "Four: the real downsides are allergy, which is serious and common in adults, and added sodium and sulfites in processed shrimp.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "24 g protein in 99 calories", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Selenium, iodine, B12, astaxanthin", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Cholesterol fear has faded", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Watch: allergy, sodium, sulfites", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So shrimp: tiny, pink, and packed with protein. Kind of like me, but from the sea.", {"mood": "smug"}),
            ("H", "If you say so, Pip.", {}),
            ("P", "Land and sea, united!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Remember, C, not O!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/shrimp", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
