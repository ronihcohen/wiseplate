"""Salmon explainer (English), based on https://wiseplate.blog/en/food/salmon/

Numbers are the article's: cooked Atlantic salmon per 100 g, farmed versus
wild (omega-3 = EPA+DHA, vitamin D in IU, mercury in ppm), a 150-180 g home
fillet, and cooking temperatures in degrees Celsius. Keep them in sync with
content/food/salmon.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Salmon: Farmed or Wild?"
SLUG = "salmon"
ARTICLE = "https://wiseplate.blog/en/food/salmon/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "SALMON", "top_size": 200, "bottom": "FARMED OR WILD?", "bottom_size": 110,
         "badge": "25 g", "badge_label": "protein\nper 100 g", "badge_color": "#F97316",
         "scatter": "🐟", "hero": "🍣", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "protein":  {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "versus":   {"bpm": 104, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.7, "swing": 0.15},
    "omega":    {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "vitd":     {"bpm": 114, "root": 64, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "bright": 1.2},
    "mercury":  {"bpm": 84, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "catches":  {"bpm": 98, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.65, "swing": 0.2},
    "howto":    {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FFF1EC", "protein": "#FFE4D6", "versus": "#E0F2FE", "omega": "#ECFDF5",
    "vitd": "#FEF9C3", "mercury": "#1E3A5F", "catches": "#FEE2E2", "howto": "#FFEDD5",
    "outro": "#FFF1EC",
}

DARK = {"fill": "#1E40AF", "title_color": "white"}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hi there! Pip the pumpkin seed here, your favorite guest reviewer.", {"mood": "happy", "wave": True}),
            ("P", "Today's guest swims upstream, comes in pink, and costs a fortune. It's salmon!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🐟", 960, 200, 160, at=[1, "salmon"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Salmon is one of the most studied and most eaten fish in the world. "
                  "We'll look at its protein, the big farmed versus wild question, the omega-3, "
                  "and the downsides worth knowing.", {}),
            ("P", "Farmed versus wild? A fish fight! I'm staying out of the water.", {"mood": "smug"}),
        ], "els": [
            E("🐟", 420, 330, 200, at=[0, "Salmon"], wobble=True),
            T("Salmon", 640, 300, 140, at=[0, "Salmon"], font="fredoka", weight=700, color="#EA580C", anchor="l"),
            {"type": "card", "x": 760, "y": 480, "w": 640, "h": 96, "emoji": "💪", "title": "The protein", "at": [0, "protein"]},
            {"type": "card", "x": 760, "y": 588, "w": 640, "h": 96, "emoji": "⚖️", "title": "Farmed vs wild", "at": [0, "farmed"]},
            {"type": "card", "x": 760, "y": 696, "w": 640, "h": 96, "emoji": "🫀", "title": "The omega-3", "at": [0, "omega"]},
            {"type": "card", "x": 760, "y": 804, "w": 640, "h": 96, "emoji": "⚠️", "title": "The downsides", "at": [0, "downsides"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "protein", "title": "A Rare Combo", "emoji": "💪", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "First, protein. Cooked salmon has twenty-two to twenty-five grams of protein per hundred grams, "
                  "depending on the variety and how it's cooked.", {}),
            ("H", "A typical home fillet of one hundred fifty to one hundred eighty grams gives about thirty-four to forty-two grams. "
                  "That's a full protein serving for a meal.", {}),
            ("P", "Forty-two grams in one fillet? I'd need a whole field of pumpkins for that.", {"mood": "surprised"}),
        ], "els": [
            T("Cooked salmon", 720, 160, 60, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 450, "y": 420, "w": 520, "h": 300, "value": 0, "text": "22-25 g", "label": "protein per 100 g",
             "emoji": "💪", "at": [0, "twenty"]},
            {"type": "stat", "x": 1010, "y": 420, "w": 520, "h": 300, "value": 0, "text": "34-42 g", "label": "per 150-180 g fillet",
             "emoji": "🍽️", "at": [1, "fillet"]},
            {"type": "pill", "x": 720, "y": 690, "text": "a full protein serving", "color": "green", "at": [1, "full"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "It's a complete protein of high biological value, with all nine essential amino acids, "
                  "including enough leucine to stimulate muscle protein synthesis.",
             {"say": "It's a complete protein of high biological value, with all nine essential amino acids, "
                     "including enough loo-seen to stimulate muscle protein synthesis."}),
            ("H", "But what makes salmon special is the combination. It gives complete protein, long-chain omega-3, "
                  "and vitamin D, all in significant amounts.", {}),
            ("H", "That's rare. Most protein sources don't give omega-3. And most plant omega-3 is ALA, "
                  "which the body turns into EPA and DHA at an efficiency of only a few percent.",
             {"say": "That's rare. Most protein sources don't give omega-3. And most plant omega-3 is A L A, "
                     "which the body turns into E P A and D H A at an efficiency of only a few percent."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 190, "w": 1000, "h": 140, "emoji": "🧬", "title": "All 9 essential amino acids", "at": 0},
            T("The rare combo", 720, 340, 56, at=[1, "combination"], font="fredoka", weight=700, color="#EA580C"),
            {"type": "pill", "x": 330, "y": 450, "text": "protein", "color": "green", "at": [1, "complete"]},
            {"type": "pill", "x": 720, "y": 450, "text": "omega-3", "color": "#0EA5E9", "at": [1, "long"]},
            {"type": "pill", "x": 1110, "y": 450, "text": "vitamin D", "color": "#EAB308", "at": [1, "vitamin"]},
            {"type": "card", "x": 720, "y": 650, "w": 1000, "h": 170, "emoji": "🌱", "title": "Plant ALA",
             "body": "turned into EPA and DHA: only a few %", "at": [2, "plant"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "versus", "title": "Farmed vs Wild", "emoji": "⚖️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Now the most common question: farmed or wild? Here's cooked Atlantic salmon, per hundred grams.", {}),
            ("H", "Calories: two hundred six for farmed, one hundred eighty for wild. "
                  "Protein: twenty-two point one grams versus twenty-five point four.", {}),
            ("H", "Total fat: twelve point four grams versus eight point one. "
                  "Saturated fat: two point five versus one point three. And zero carbs in both.", {}),
        ], "els": [
            T("Cooked Atlantic salmon, per 100 g", 720, 150, 50, at=0, font="fredoka", weight=600, color="green"),
            {"type": "versus", "x": 120, "y": 340, "w": 1340, "row_h": 125, "names": ["Farmed", "Wild"],
             "color_a": "#EA580C", "color_b": "#0EA5E9", "at": [0, "Atlantic"], "rows": [
                {"label": "Calories", "a": 206, "b": 180, "at": [1, "Calories"]},
                {"label": "Protein", "a": 22.1, "b": 25.4, "unit": " g", "decimals": 1, "at": [1, "Protein"]},
                {"label": "Fat", "a": 12.4, "b": 8.1, "unit": " g", "decimals": 1, "at": [2, "Total"]},
                {"label": "Sat. fat", "a": 2.5, "b": 1.3, "unit": " g", "decimals": 1, "at": [2, "Saturated"]},
            ]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Omega-3, as EPA plus DHA: two thousand to two thousand three hundred milligrams in farmed, "
                  "and one thousand two hundred to one thousand seven hundred in wild.",
             {"say": "Omega-3, as E P A plus D H A: two thousand to two thousand three hundred milligrams in farmed, "
                     "and one thousand two hundred to one thousand seven hundred in wild."}),
            ("H", "Vitamin D: about five hundred twenty-five I U in farmed, and six hundred to nine hundred ninety in wild.",
             {"say": "Vitamin D: about five hundred twenty-five I U in farmed, and six hundred to nine hundred ninety in wild."}),
            ("H", "Vitamin B12: three point two versus four point four micrograms. Selenium: thirty-six versus forty-one micrograms. "
                  "Potassium: three hundred eighty-four versus six hundred twenty-eight milligrams.",
             {"say": "Vitamin B 12: three point two versus four point four micrograms. Selenium: thirty-six versus forty-one micrograms. "
                     "Potassium: three hundred eighty-four versus six hundred twenty-eight milligrams."}),
            ("H", "And mercury? About zero point zero two p p m in both.",
             {"say": "And mercury? About zero point zero two P P M in both."}),
        ], "els": [
            {"type": "versus", "x": 120, "y": 250, "w": 1340, "row_h": 122, "names": ["Farmed", "Wild"],
             "color_a": "#EA580C", "color_b": "#0EA5E9", "at": 0, "rows": [
                {"label": "Omega-3", "a": 2300, "b": 1700, "a_text": "2,000-2,300 mg", "b_text": "1,200-1,700 mg", "at": [0, "Omega"]},
                {"label": "Vitamin D", "a": 525, "b": 990, "a_text": "~525 IU", "b_text": "600-990 IU", "at": [1, "Vitamin"]},
                {"label": "B12", "a": 3.2, "b": 4.4, "unit": " mcg", "decimals": 1, "at": [2, "B12"]},
                {"label": "Selenium", "a": 36, "b": 41, "unit": " mcg", "at": [2, "Selenium"]},
                {"label": "Potassium", "a": 384, "b": 628, "unit": " mg", "at": [2, "Potassium"]},
            ]},
            {"type": "pill", "x": 720, "y": 860, "text": "mercury: ~0.02 ppm in both", "color": "green", "at": [3, "mercury"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "So here's the twist. Farmed salmon is fattier, about twelve grams of fat versus eight. "
                  "And omega-3 sits in the fat, so farmed salmon actually gives more EPA and DHA per serving, not less.",
             {"say": "So here's the twist. Farmed salmon is fattier, about twelve grams of fat versus eight. "
                     "And omega-3 sits in the fat, so farmed salmon actually gives more E P A and D H A per serving, not less."}),
            ("H", "Wild salmon is leaner and higher in protein, and it gives one and a half to two times the vitamin D.", {}),
            ("P", "Wait, the farm fish wins on omega-3? Plot twist of the century.", {"mood": "surprised", "jump": True}),
        ], "els": [
            {"type": "card", "x": 720, "y": 260, "w": 1000, "h": 190, "emoji": "🏭", "title": "Farmed: fattier",
             "body": "so more EPA + DHA per serving", "at": [0, "Farmed"]},
            {"type": "card", "x": 720, "y": 520, "w": 1000, "h": 190, "emoji": "🌊", "title": "Wild: leaner",
             "body": "more protein, 1.5 to 2x the vitamin D", "at": [1, "Wild"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Farmed salmon has a worse omega-6 to omega-3 ratio, because its feed is based on vegetable oils. "
                  "Still, the ratio stays favorable compared with almost any other protein source.", {}),
            ("H", "Older studies found more PCBs and dioxins in farmed salmon. Feed rules have changed since then and narrowed the gap a lot. "
                  "Health authorities agree the omega-3 benefit outweighs the risk in both types.",
             {"say": "Older studies found more P C Bs and dye-ox-ins in farmed salmon. Feed rules have changed since then and narrowed the gap a lot. "
                     "Health authorities agree the omega-3 benefit outweighs the risk in both types."}),
            ("H", "And the pink color comes from astaxanthin, an antioxidant pigment. Wild salmon gets it from krill and algae. "
                  "In farmed salmon it's added to the feed. Chemically, it's the same molecule.",
             {"say": "And the pink color comes from asta-zanthin, an antioxidant pigment. Wild salmon gets it from krill and algae. "
                     "In farmed salmon it's added to the feed. Chemically, it's the same molecule."}),
        ], "els": [
            {"type": "check", "x": 160, "y": 210, "w": 1300, "ok": False, "text": "Omega-6 to 3 ratio: worse in farmed", "at": [0, "ratio"]},
            {"type": "pill", "x": 810, "y": 320, "text": "still favorable vs most proteins", "color": "green", "at": [0, "Still"]},
            {"type": "check", "x": 160, "y": 460, "w": 1300, "ok": True, "text": "PCBs, dioxins: gap narrowed", "at": [1, "Feed"]},
            {"type": "pill", "x": 810, "y": 570, "text": "benefit outweighs risk in both", "color": "green", "at": [1, "outweighs"]},
            {"type": "card", "x": 810, "y": 760, "w": 1100, "h": 150, "emoji": "🌸", "title": "Astaxanthin: same molecule",
             "at": [2, "pink"], "fill": "#FFE4E6"},
        ]},
        {"pip": PIP_C, "lines": [
            ("H", "The bottom line on this one: both are a good choice. Farmed is cheaper, easier to find, and gives more omega-3 per serving.", {}),
            ("H", "Wild is leaner, richer in vitamin D, and more sustainable, but a lot more expensive.", {}),
            ("P", "So no losers. Just two fish and a very confused shopper.", {"mood": "happy"}),
        ], "els": [
            T("Both are a good choice", 960, 150, 80, at=0, font="fredoka", weight=700, color="green"),
            {"type": "pill", "x": 480, "y": 290, "text": "Farmed: more omega-3", "color": "#EA580C", "at": [0, "Farmed"]},
            {"type": "pill", "x": 1440, "y": 290, "text": "Wild: more vitamin D", "color": "#0EA5E9", "at": [1, "Wild"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "omega", "title": "Heart and Brain", "emoji": "🫀", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Let's talk omega-3. EPA and DHA are the biologically active forms. "
                  "The plant ALA from flax seeds and walnuts converts in the body at only five to ten percent.",
             {"say": "Let's talk omega-3. E P A and D H A are the biologically active forms. "
                     "The plant A L A from flax seeds and walnuts converts in the body at only five to ten percent."}),
            ("H", "One serving of salmon covers the recommendation of two hundred fifty to five hundred milligrams a day.", {}),
            ("P", "Five to ten percent? Hey, seeds are trying our best.", {"mood": "worried"}),
        ], "els": [
            {"type": "bars", "x": 200, "y": 260, "w": 1200, "row_h": 130, "max": 100, "unit": "%", "rows": [
                {"label": "EPA, DHA", "value": 100, "text": "ready to use", "color": "#0EA5E9", "at": [0, "active"]},
                {"label": "Plant ALA", "value": 10, "text": "5-10% converted", "color": "#F59E0B", "at": [0, "flax"]},
            ]},
            {"type": "card", "x": 720, "y": 620, "w": 1000, "h": 170, "emoji": "🐟", "title": "One serving covers it",
             "body": "250-500 mg a day recommended", "at": [1, "serving"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Heart health: in large cohort studies, eating oily fish twice a week is consistently linked to lower cardiovascular mortality.", {}),
            ("H", "The mechanisms seen: triglycerides down by fifteen to thirty percent, less inflammation, and a steadier heart rhythm.",
             {"say": "The mechanisms seen: try-glis-er-ides down by fifteen to thirty percent, less inflammation, and a steadier heart rhythm."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 1000, "h": 190, "emoji": "🫀", "title": "Oily fish twice a week",
             "body": "linked to lower cardiovascular mortality", "at": [0, "twice"]},
            {"type": "check", "x": 170, "y": 470, "w": 1100, "ok": True, "text": "Triglycerides: down 15-30%", "at": [1, "triglycerides"]},
            {"type": "check", "x": 170, "y": 600, "w": 1100, "ok": True, "text": "Less inflammation", "at": [1, "inflammation"]},
            {"type": "check", "x": 170, "y": 730, "w": 1100, "ok": True, "text": "Steadier heart rhythm", "at": [1, "rhythm"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And the brain. DHA is a key building block of nerve cell membranes and the retina.",
             {"say": "And the brain. D H A is a key building block of nerve cell membranes and the retina."}),
            ("H", "It matters most in pregnancy and infancy, for the development of the brain and vision.", {}),
            ("P", "Brain food. Finally, something we can both be smart about.", {"mood": "smug"}),
        ], "els": [
            E("🧠", 450, 330, 190, at=[0, "brain"]),
            T("nerve cells", 450, 480, 46, at=[0, "nerve"], font="fredoka", weight=600),
            E("👁️", 1000, 330, 190, at=[0, "retina"]),
            T("retina", 1000, 480, 46, at=[0, "retina"], font="fredoka", weight=600),
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 170, "emoji": "🤰", "title": "Pregnancy and infancy",
             "body": "brain and vision development", "at": [1, "pregnancy"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "vitd", "title": "The Vitamin D Bonus", "emoji": "☀️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Vitamin D is the sneaky star. Salmon is one of the few truly dietary sources of it.", {}),
            ("H", "A one hundred fifty gram serving of wild salmon may give over one thousand I U. "
                  "That's more than the recommended daily intake.",
             {"say": "A one hundred fifty gram serving of wild salmon may give over one thousand I U. "
                     "That's more than the recommended daily intake."}),
            ("H", "On top of that, salmon brings selenium and vitamin B12 in significant amounts.",
             {"say": "On top of that, salmon brings selenium and vitamin B 12 in significant amounts."}),
            ("P", "A fish that brings its own sunshine. Show-off.", {"mood": "smug"}),
        ], "els": [
            E("☀️", 360, 330, 220, at=0, wobble=True),
            T("one of the few food sources", 900, 300, 50, at=[0, "few"], font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 900, "y": 470, "w": 620, "h": 280, "value": 0, "text": "1,000+ IU", "label": "in 150 g of wild salmon",
             "emoji": "🌊", "at": [1, "thousand"]},
            {"type": "pill", "x": 900, "y": 700, "text": "more than the daily intake", "color": "#EAB308", "at": [1, "more"]},
            {"type": "pill", "x": 520, "y": 820, "text": "selenium", "color": "#0EA5E9", "at": [2, "selenium"]},
            {"type": "pill", "x": 900, "y": 820, "text": "B12", "color": "#7C3AED", "at": [2, "B12"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "mercury", "title": "Low on Mercury", "emoji": "🌡️", "dark": True, "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Mercury is where salmon really shines. It has about zero point zero two p p m, among the lowest in fish, "
                  "and six to seventeen times less than tuna.",
             {"say": "Mercury is where salmon really shines. It has about zero point zero two P P M, among the lowest in fish, "
                     "and six to seventeen times less than tuna."}),
            ("H", "Why? Salmon is a short-lived fish, and not a predator at the top of the food chain. "
                  "So it's considered safe even in pregnancy.", {}),
            ("P", "Low mercury, high omega-3. Okay, salmon, I see you.", {"mood": "happy"}),
        ], "els": [
            T("Mercury", 720, 160, 80, at=0, font="fredoka", weight=700, color="white"),
            {"type": "card", "x": 450, "y": 380, "w": 520, "h": 200, "emoji": "🐟", "title": "~0.02 ppm",
             "body": "salmon", "at": [0, "zero"], **DARK},
            {"type": "card", "x": 1030, "y": 380, "w": 520, "h": 200, "emoji": "🐋", "title": "6-17x more",
             "body": "tuna", "at": [0, "tuna"], "fill": "#7F1D1D", "title_color": "white"},
            {"type": "card", "x": 720, "y": 650, "w": 1000, "h": 190, "emoji": "⏳", "title": "Short-lived, not a top predator",
             "body": "considered safe even in pregnancy", "at": [1, "short"], **DARK},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the downsides. Catch one: price. Salmon is one of the most expensive protein sources.", {}),
            ("H", "Sardines and mackerel give a similar amount of omega-3 at a fraction of the price.", {}),
            ("P", "Sardines, the budget superhero. Small, cheap and mighty. Sounds like someone I know.", {"mood": "smug"}),
        ], "els": [
            T("#1 Price", 720, 180, 90, at=0, font="fredoka", weight=700, color="red"),
            E("💸", 720, 340, 160, at=[0, "expensive"]),
            {"type": "card", "x": 720, "y": 600, "w": 1000, "h": 190, "emoji": "🐟", "title": "Sardines and mackerel",
             "body": "similar omega-3, a fraction of the price", "at": [1, "Sardines"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Catch two: smoked salmon. A hundred grams of cold-smoked salmon has six hundred to one thousand two hundred milligrams of sodium.", {}),
            ("H", "And cold smoking doesn't cook the fish, so there's a risk of listeria. "
                  "Pregnant women should avoid cold-smoked salmon, unless it's been thoroughly heated.",
             {"say": "And cold smoking doesn't cook the fish, so there's a risk of liss-teer-ee-a. "
                     "Pregnant women should avoid cold smoked salmon, unless it's been thoroughly heated."}),
        ], "els": [
            T("#2 Smoked salmon", 720, 170, 80, at=0, font="fredoka", weight=700, color="red"),
            {"type": "stat", "x": 720, "y": 400, "w": 760, "h": 280, "value": 0, "text": "600-1,200 mg", "label": "sodium per 100 g, cold-smoked",
             "emoji": "🧂", "color": "orange", "at": [0, "sodium"]},
            {"type": "card", "x": 720, "y": 700, "w": 1000, "h": 180, "emoji": "🤰", "title": "Pregnant? Avoid it",
             "body": "listeria risk, unless thoroughly heated", "at": [1, "Pregnant"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Catch three: sustainability. Intensive farming in sea cages causes local pollution, sea lice, and fish escaping into the wild.", {}),
            ("H", "And wild salmon stocks in the Atlantic Ocean are in poor shape. "
                  "An A S C label for farming, or M S C for wild fishing, points to better practices.",
             {"say": "And wild salmon stocks in the Atlantic Ocean are in poor shape. "
                     "An A S C label for farming, or M S C for wild fishing, points to better practices."}),
            ("H", "Catch four: fish allergy. It's one of the major allergens, and reactions can be severe.", {}),
        ], "els": [
            T("#3 Sustainability", 720, 160, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "pill", "x": 400, "y": 290, "text": "pollution", "color": "orange", "at": [0, "pollution"]},
            {"type": "pill", "x": 720, "y": 290, "text": "sea lice", "color": "orange", "at": [0, "lice"]},
            {"type": "pill", "x": 1060, "y": 290, "text": "escapes", "color": "orange", "at": [0, "escaping"]},
            {"type": "card", "x": 720, "y": 470, "w": 1000, "h": 170, "emoji": "✅", "title": "Look for ASC or MSC",
             "body": "Atlantic wild stocks are in poor shape", "at": [1, "label"], "fill": "#DCFCE7"},
            {"type": "banner", "x": 720, "y": 700, "text": "#4 Fish allergy: can be severe", "color": "#DC2626", "at": [2, "allergy"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Catch five: raw fish. Salmon sushi and sashimi may contain a parasitic worm, which causes anisakiasis.",
             {"say": "Catch five: raw fish. Salmon sushi and sashimi may contain a parasitic worm, which causes an-ee-sa-kye-a-sis."}),
            ("H", "Commercial freezing kills it: minus twenty degrees Celsius for a week, or minus thirty-five for fifteen hours. "
                  "So don't use fresh salmon from the counter for homemade sushi.", {}),
            ("P", "A worm?! I'm a seed. Worms are my natural enemy.", {"mood": "worried", "jump": True}),
            ("H", "And catch six: overcooking. Long, high heat oxidizes some of the omega-3. "
                  "Gentle baking, steaming or brief grilling beat long frying.", {}),
        ], "els": [
            T("#5 Raw salmon", 720, 150, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 720, "y": 330, "w": 1000, "h": 180, "emoji": "🧊", "title": "-20°C for a week",
             "body": "or -35°C for 15 hours", "at": [1, "freezing"]},
            {"type": "pill", "x": 720, "y": 500, "text": "no counter salmon for homemade sushi", "color": "orange", "at": [1, "counter"]},
            {"type": "card", "x": 720, "y": 710, "w": 1000, "h": 170, "emoji": "🔥", "title": "#6 Overcooking",
             "body": "oxidizes some of the omega-3", "at": [3, "overcooking"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "Cook It Right", "emoji": "🍳", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So how much? Twice a week, a one hundred twenty to one hundred eighty gram serving. "
                  "That's the official advice of most health organizations for oily fish.", {}),
            ("H", "Best method: bake at one hundred sixty to one hundred eighty degrees Celsius, "
                  "until the inside reaches fifty to fifty-two degrees. That's medium.", {}),
            ("H", "Above sixty degrees, the fish dries out and the fat runs out.", {}),
            ("P", "Dry salmon. The saddest thing in any kitchen.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 170, "emoji": "📅", "title": "Twice a week",
             "body": "120-180 g per serving", "at": [0, "Twice"]},
            {"type": "stat", "x": 450, "y": 530, "w": 520, "h": 260, "value": 0, "text": "160-180°C", "label": "oven",
             "emoji": "🔥", "at": [1, "bake"]},
            {"type": "stat", "x": 1010, "y": 530, "w": 520, "h": 260, "value": 0, "text": "50-52°C", "label": "inside (medium)",
             "emoji": "🌡️", "at": [1, "inside"]},
            {"type": "pill", "x": 720, "y": 760, "text": "above 60°C: dry", "color": "red", "at": [2, "sixty"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Keep the skin on. The fat layer under it is especially rich in omega-3, and cooking skin side down protects it.", {}),
            ("H", "Canned salmon is a cheap, excellent option. Especially the kind with soft bones, which adds a good amount of calcium.", {}),
            ("H", "And cheaper choices of the same quality: sardines, with fourteen hundred to fifteen hundred milligrams of omega-3, and mackerel. "
                  "Both are smaller, even lower in mercury, and much cheaper.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 160, "emoji": "🍳", "title": "Skin on, skin side down", "at": [0, "skin"]},
            {"type": "card", "x": 720, "y": 410, "w": 1000, "h": 170, "emoji": "🥫", "title": "Canned salmon",
             "body": "soft bones add calcium", "at": [1, "Canned"]},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 190, "emoji": "🐟", "title": "Sardines and mackerel",
             "body": "sardines: 1,400-1,500 mg omega-3", "at": [2, "sardines"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: salmon gives twenty-two to twenty-five grams of protein per hundred grams, "
                  "and one thousand two hundred to two thousand three hundred milligrams of omega-3.", {}),
            ("H", "Two: it's one of the few real food sources of vitamin D, with especially low mercury.", {}),
            ("H", "Three: farmed versus wild matters less than people think. "
                  "Farmed gives more omega-3, wild gives more protein and vitamin D.", {}),
            ("H", "Four: two servings a week cover the recommendation. "
                  "And if the price puts you off, sardines give a similar benefit at a third of the price.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "22-25 g protein, lots of omega-3", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Vitamin D, very low mercury", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Farmed or wild: both are good", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Twice a week, or try sardines", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So salmon: pink, rich, and famous. Basically a celebrity fish.", {"mood": "smug"}),
            ("H", "And you, Pip?", {}),
            ("P", "Green, tiny, and humble. But I'll share the spotlight. Just this once.", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Keep the skin on!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/salmon", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
