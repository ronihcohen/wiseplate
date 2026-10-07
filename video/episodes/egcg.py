"""EGCG explainer (English), based on https://wiseplate.blog/food/egcg/

Numbers are the article's: EGCG per cup by tea type, the 200-400 mg/day
range (3-5 cups or a standardized supplement), the 800 mg/day caution line
for concentrated extracts, and the study figures it quotes. Keep them in sync
with content/food/egcg.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "EGCG: Green Tea's Fat Burner?"
SLUG = "egcg"
ARTICLE = "https://wiseplate.blog/en/food/egcg/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "EGCG", "top_size": 220, "bottom": "FAT BURNER?", "bottom_size": 180,
         "badge": "800 mg", "badge_size": 80, "badge_label": "the liver\ncaution line", "badge_color": "#DC2626",
         "scatter": "🍵", "hero": "🍵", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "what":     {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "cup":      {"bpm": 90, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "fat":      {"bpm": 120, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "heart":    {"bpm": 104, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.65, "swing": 0.1},
    "lab":      {"bpm": 96, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.55},
    "absorb":   {"bpm": 108, "root": 65, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#F0FDF4", "what": "#ECFDF5", "cup": "#F7FEE7", "fat": "#FFEDD5",
    "heart": "#FFE4E6", "lab": "#F5F3FF", "absorb": "#E0F2FE", "catches": "#FEE2E2",
    "outro": "#F0FDF4",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


EGCG_SAY = "E G C G"

CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hi! Pip the pumpkin seed here. Today's guest is... wait, where is it? I can't see anything.", {"mood": "surprised", "wave": True}),
            ("P", "Oh! It's a molecule. A tiny one, from green tea. Its name is E G C G!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🍵", 960, 200, 160, at=[1, "molecule"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today it's EGCG, the star compound of green tea. What it is, how much is in your cup, "
                  "the fat-burning claim, and why the supplement version needs some caution.",
             {"say": "Today it's E G C G, the star compound of green tea. What it is, how much is in your cup, "
                     "the fat burning claim, and why the supplement version needs some caution."}),
            ("P", "Finally, someone smaller than me. I'm going to enjoy this.", {"mood": "smug"}),
        ], "els": [
            E("🍵", 420, 330, 200, at=0, wobble=True),
            T("EGCG", 640, 300, 150, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "☕", "title": "How much per cup", "at": [0, "cup"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "🔥", "title": "The fat-burning claim", "at": [0, "fat"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "⚠️", "title": "Supplement caution", "at": [0, "supplement"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "what", "title": "What Is EGCG?", "emoji": "🧪", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "EGCG stands for epigallocatechin gallate. It's an antioxidant from the catechin group, "
                  "and the most active and most studied compound in green tea.",
             {"say": "E G C G stands for epi-gallo-catechin gallate. It's an antioxidant from the catechin group, "
                     "and the most active and most studied compound in green tea."}),
            ("H", "About thirty percent of the dry weight of a green tea leaf is catechins. And EGCG is the dominant one, "
                  "about fifty to sixty percent of all the catechins in the leaf.",
             {"say": "About thirty percent of the dry weight of a green tea leaf is catechins. And E G C G is the dominant one, "
                     "about fifty to sixty percent of all the catechins in the leaf."}),
            ("P", "Epigallo... cate... I'll just call it Greg.", {"mood": "smug"}),
        ], "els": [
            T("Epigallocatechin gallate", 720, 180, 70, at=0, font="fredoka", weight=700, color="green"),
            {"type": "ring", "x": 420, "y": 520, "r": 160, "value": 30, "color": "#16A34A", "label": "of the dry leaf", "at": [1, "thirty"]},
            T("catechins", 420, 720, 46, at=[1, "catechins."], font="fredoka", weight=600, color="green"),
            {"type": "ring", "x": 1030, "y": 520, "r": 160, "value": 55, "color": "#0EA5E9", "label": "of catechins", "at": [1, "fifty"]},
            T("EGCG: 50 to 60%", 1030, 720, 46, at=[1, "fifty"], font="fredoka", weight=600, color="#0369A1"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "When a supplement label promises green tea extract, the extract is usually standardized by its percentage of EGCG.",
             {"say": "When a supplement label promises green tea extract, the extract is usually standardized by its percentage of E G C G."}),
            ("H", "Catechins are a sub-family of polyphenols, the protective compounds plants make for themselves.", {}),
            ("H", "What makes EGCG special is a combo: strong antioxidant power, and the ability to cross the blood-brain barrier. "
                  "But it has one big weakness: your body absorbs it poorly.",
             {"say": "What makes E G C G special is a combo: strong antioxidant power, and the ability to cross the blood brain barrier. "
                     "But it has one big weakness: your body absorbs it poorly."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 150, "emoji": "💊", "title": "Extracts: standardized by % EGCG", "at": 0},
            {"type": "card", "x": 720, "y": 380, "w": 1000, "h": 150, "emoji": "🌿", "title": "Polyphenols > catechins > EGCG", "at": [1, "polyphenols"]},
            {"type": "check", "x": 220, "y": 590, "w": 1000, "ok": True, "text": "Strong antioxidant", "at": [2, "antioxidant"]},
            {"type": "check", "x": 220, "y": 710, "w": 1000, "ok": True, "text": "Crosses the blood-brain barrier", "at": [2, "barrier"]},
            {"type": "check", "x": 220, "y": 830, "w": 1000, "ok": False, "text": "Poorly absorbed", "at": [2, "poorly"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "cup", "title": "How Much Is in Your Cup?", "emoji": "☕", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "So how much EGCG is in a cup? It depends a lot on the tea.",
             {"say": "So how much E G C G is in a cup? It depends a lot on the tea."}),
            ("H", "Matcha: seventy to one hundred thirty milligrams. Japanese gyokuro: sixty to ninety. Regular green tea: twenty to fifty. "
                  "White tea: ten to thirty. And black tea, only about five, because it gets oxidized during production.",
             {"say": "Matcha: seventy to one hundred thirty milligrams. Japanese gyo-kuro: sixty to ninety. Regular green tea: twenty to fifty. "
                     "White tea: ten to thirty. And black tea, only about five, because it gets oxidized during production."}),
        ], "els": [
            T("EGCG per cup", 760, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 200, "y": 290, "w": 1200, "row_h": 108, "max": 130, "unit": " mg", "rows": [
                {"label": "Matcha", "value": 130, "text": "70 to 130 mg", "color": "#16A34A", "at": [1, "Matcha"]},
                {"label": "Gyokuro", "value": 90, "text": "60 to 90 mg", "color": "#65A30D", "at": [1, "gyokuro"]},
                {"label": "Green tea", "value": 50, "text": "20 to 50 mg", "color": "#84CC16", "at": [1, "Regular"]},
                {"label": "White tea", "value": 30, "text": "10 to 30 mg", "color": "#CBD5E1", "at": [1, "White"]},
                {"label": "Black tea", "value": 5, "text": "~5 mg", "color": "#78350F", "at": [1, "black"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Why is matcha so high? With matcha, you drink the whole ground leaf, not just water that soaked in it. "
                  "Studies show one cup of matcha equals about three to ten cups of regular green tea in catechins and EGCG.",
             {"say": "Why is matcha so high? With matcha, you drink the whole ground leaf, not just water that soaked in it. "
                     "Studies show one cup of matcha equals about three to ten cups of regular green tea in catechins and E G C G."}),
            ("H", "And a heat warning. EGCG breaks down fast in boiling water. For the most catechins, "
                  "use water at seventy to eighty degrees Celsius, and steep the leaves for one to three minutes.",
             {"say": "And a heat warning. E G C G breaks down fast in boiling water. For the most catechins, "
                     "use water at seventy to eighty degrees Celsius, and steep the leaves for one to three minutes."}),
            ("P", "Boiling water ruins it? Tea is more delicate than I thought.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 180, "emoji": "🍵", "title": "1 matcha ≈ 3 to 10 green teas",
             "body": "you drink the whole leaf", "at": 0},
            {"type": "card", "x": 450, "y": 540, "w": 560, "h": 180, "emoji": "♨️", "title": "Not boiling", "body": "EGCG breaks down", "at": [1, "boiling"], "fill": "#FEE2E2"},
            {"type": "card", "x": 1030, "y": 540, "w": 560, "h": 180, "emoji": "🌡️", "title": "70 to 80°C", "body": "steep 1 to 3 minutes", "at": [1, "seventy"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The amount used in most clinical studies is two hundred to four hundred milligrams a day. "
                  "That's three to five cups of green tea, or a standardized supplement.", {}),
        ], "els": [
            T("The studied dose", 720, 140, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 720, "y": 360, "w": 640, "h": 320, "value": 400, "unit": " mg", "label": "studied: 200 to 400 mg a day", "emoji": "🎯", "at": [0, "two"]},
            {"type": "pill", "x": 720, "y": 650, "text": "= 3 to 5 cups of green tea", "color": "green", "at": [0, "cups"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "fat", "title": "The Fat-Burner Science", "emoji": "🔥", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now, the famous fat-burning claim. Here's how it works. EGCG blocks an enzyme called C O M T, "
                  "whose job is to break down the hormone noradrenaline.",
             {"say": "Now, the famous fat burning claim. Here's how it works. E G C G blocks an enzyme called C O M T, "
                     "whose job is to break down the hormone nor-adrenaline."}),
            ("H", "With that enzyme blocked, noradrenaline stays high for longer. And noradrenaline is what tells fat cells "
                  "to break down fat and release it into the blood as fuel.",
             {"say": "With that enzyme blocked, nor-adrenaline stays high for longer. And nor-adrenaline is what tells fat cells "
                     "to break down fat and release it into the blood as fuel."}),
        ], "els": [
            {"type": "card", "x": 330, "y": 300, "w": 440, "h": 160, "emoji": "🍵", "title": "EGCG", "at": 0},
            {"type": "arrow", "x1": 560, "y1": 300, "x2": 660, "y2": 300, "at": [0, "blocks"]},
            {"type": "card", "x": 900, "y": 300, "w": 440, "h": 160, "emoji": "🚫", "title": "COMT", "body": "blocked", "at": [0, "blocks"]},
            {"type": "card", "x": 330, "y": 600, "w": 520, "h": 160, "emoji": "⚡", "title": "Noradrenaline", "body": "stays high longer", "at": [1, "longer"]},
            {"type": "arrow", "x1": 600, "y1": 600, "x2": 700, "y2": 600, "at": [1, "tells"]},
            {"type": "card", "x": 960, "y": 600, "w": 480, "h": 160, "emoji": "🔥", "title": "Fat released", "body": "as fuel", "at": [1, "release"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Studies show EGCG works especially well together with caffeine. The pair raised resting metabolism by about four percent.", {}),
            ("H", "But does it help you lose weight without exercise? Not in a meaningful way. EGCG helps release fatty acids into the blood, "
                  "but if you don't burn them, your body just stores them again.", {}),
            ("H", "It opens the door. But you still have to walk through it, ideally at a run.", {}),
            ("P", "So it's a fat-burner... if you do the burning. Sneaky.", {"mood": "smug"}),
        ], "els": [
            T("EGCG + caffeine", 450, 200, 64, at=0, font="fredoka", weight=700, color="green"),
            {"type": "stat", "x": 450, "y": 430, "w": 460, "h": 280, "value": 4, "unit": "%", "label": "metabolism boost", "emoji": "⚡", "at": [0, "four"]},
            {"type": "card", "x": 1050, "y": 330, "w": 560, "h": 200, "emoji": "🛋️", "title": "No exercise?",
             "body": "fat gets stored again", "at": [1, "exercise"], "fill": "#FEE2E2"},
            {"type": "banner", "x": 760, "y": 760, "text": "It opens the door. You walk through.", "color": "#16A34A", "at": [2, "door"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "heart", "title": "Heart, Sugar, Inflammation", "emoji": "❤️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Heart health. Meta-analyses of observational studies show that regularly drinking three to five cups of green tea a day "
                  "is linked to about a ten to twenty percent lower risk of stroke and coronary heart disease.", {}),
            ("H", "That's a statistical link, not proven cause and effect.", {}),
            ("H", "The proposed mechanisms: EGCG protects LDL from oxidation, an early step in hardening of the arteries. "
                  "It boosts nitric oxide in blood vessels, lowering systolic blood pressure by two to three points on average. "
                  "And it reduces platelet clumping, in the same direction as low-dose aspirin, but much weaker.",
             {"say": "The proposed mechanisms: E G C G protects L D L from oxidation, an early step in hardening of the arteries. "
                     "It boosts nitric oxide in blood vessels, lowering systolic blood pressure by two to three points on average. "
                     "And it reduces platelet clumping, in the same direction as low dose aspirin, but much weaker."}),
        ], "els": [
            {"type": "card", "x": 760, "y": 200, "w": 1100, "h": 160, "emoji": "🍵", "title": "3 to 5 cups: 10 to 20% lower risk",
             "body": "stroke and heart disease · observational", "at": 0},
            {"type": "pill", "x": 760, "y": 410, "text": "a link, not proven cause", "color": "orange", "at": [1, "link"]},
            {"type": "check", "x": 210, "y": 530, "w": 1100, "ok": True, "text": "Protects LDL from oxidation", "at": [2, "oxidation"]},
            {"type": "check", "x": 210, "y": 650, "w": 1100, "ok": True, "text": "Systolic BP: 2 to 3 points lower", "at": [2, "systolic"]},
            {"type": "check", "x": 210, "y": 770, "w": 1100, "ok": True, "text": "Less platelet clumping (mild)", "at": [2, "platelet"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Blood sugar. EGCG slows the gut enzymes alpha-amylase and alpha-glucosidase, which break carbs into glucose. "
                  "So sugar enters the blood more slowly, without big spikes.",
             {"say": "Blood sugar. E G C G slows the gut enzymes alpha amylase and alpha glucosidase, which break carbs into glucose. "
                     "So sugar enters the blood more slowly, without big spikes."}),
            ("H", "It also helps move GLUT4 glucose transporters to muscle cell membranes. And in clinical trials in type 2 diabetes, "
                  "four hundred milligrams a day led to a slight drop in H b A one C after twelve weeks.",
             {"say": "It also helps move GLUT 4 glucose transporters to muscle cell membranes. And in clinical trials in type 2 diabetes, "
                     "four hundred milligrams a day led to a slight drop in H b A 1 C after twelve weeks."}),
            ("H", "And inflammation: EGCG inhibits NF kappa B, the immune system's main inflammation switch, "
                  "and the COX-2 enzyme, the same target as ibuprofen, but more mildly.",
             {"say": "And inflammation: E G C G inhibits N F kappa B, the immune system's main inflammation switch, "
                     "and the cox 2 enzyme, the same target as ibuprofen, but more mildly."}),
        ], "els": [
            {"type": "card", "x": 760, "y": 200, "w": 1100, "h": 160, "emoji": "🍞", "title": "Slower carb breakdown",
             "body": "fewer sugar spikes", "at": 0},
            {"type": "card", "x": 760, "y": 400, "w": 1100, "h": 160, "emoji": "🩸", "title": "400 mg/day: slight HbA1c drop",
             "body": "type 2 diabetes · 12 weeks", "at": [1, "four"]},
            {"type": "card", "x": 760, "y": 600, "w": 1100, "h": 160, "emoji": "🧯", "title": "Calms inflammation switches",
             "body": "NF-kB and COX-2 · milder than ibuprofen", "at": [2, "inflammation"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "lab", "title": "Brain and Cancer: Mostly Lab", "emoji": "🔬", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "EGCG is one of the few polyphenols that crosses the blood-brain barrier.",
             {"say": "E G C G is one of the few polyphenols that crosses the blood brain barrier."}),
            ("H", "In the lab, it slows the clumping of beta-amyloid and tau, the two hallmarks of Alzheimer's. "
                  "In mice with Alzheimer's mutations, plaques dropped by up to fifty percent.", {}),
            ("H", "In animal models of Parkinson's, it protected dopamine neurons from oxidative damage. "
                  "And it raises B D N F, a protein often called fertilizer for brain cells.",
             {"say": "In animal models of Parkinson's, it protected dopamine neurons from oxidative damage. "
                     "And it raises B D N F, a protein often called fertilizer for brain cells."}),
            ("H", "But most of this evidence is still preclinical. In people, there's only an epidemiological link, not proven cause.", {}),
        ], "els": [
            T("Brain", 720, 160, 80, at=0, font="fredoka", weight=700, color="green"),
            {"type": "card", "x": 720, "y": 320, "w": 1000, "h": 150, "emoji": "🐭", "title": "Up to 50% fewer plaques", "body": "Alzheimer's mice", "at": [1, "mice"]},
            {"type": "card", "x": 720, "y": 500, "w": 1000, "h": 150, "emoji": "🧠", "title": "Neurons protected", "body": "Parkinson's models", "at": [2, "Parkinson's"]},
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 150, "emoji": "🌱", "title": "More BDNF", "body": "brain cell fertilizer", "at": [2, "B"]},
            {"type": "banner", "x": 720, "y": 850, "text": "Mostly preclinical", "color": "#F97316", "at": [3, "preclinical"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Cancer? Dozens of lab and animal studies showed EGCG can block new blood vessels that feed tumors, "
                  "trigger programmed death in cancer cells, and protect D N A from oxidative damage.",
             {"say": "Cancer? Dozens of lab and animal studies showed E G C G can block new blood vessels that feed tumors, "
                     "trigger programmed death in cancer cells, and protect D N A from oxidative damage."}),
            ("H", "But human studies haven't reached clear conclusions like the lab did. The direction is promising, nothing more yet.", {}),
            ("H", "And here's the big gap. Most impressive EGCG results came from cell cultures, at concentrations you can't reach in the body through food.",
             {"say": "And here's the big gap. Most impressive E G C G results came from cell cultures, at concentrations you can't reach in the body through food."}),
            ("P", "So EGCG is a superhero... in a petri dish.", {"mood": "smug", "say": "So E G C G is a superhero... in a petri dish."}),
        ], "els": [
            T("Cancer: lab and animals", 720, 160, 70, at=0, font="fredoka", weight=700, color="green"),
            {"type": "pill", "x": 400, "y": 290, "text": "fewer tumor vessels", "color": "green", "at": [0, "vessels"]},
            {"type": "pill", "x": 760, "y": 370, "text": "cancer cell death", "color": "green", "at": [0, "death"]},
            {"type": "pill", "x": 1100, "y": 290, "text": "DNA protection", "color": "green", "at": [0, "protect"]},
            {"type": "check", "x": 210, "y": 500, "w": 1100, "ok": False, "text": "Clear results in people", "at": [1, "human"]},
            {"type": "card", "x": 760, "y": 720, "w": 1100, "h": 170, "emoji": "🧫", "title": "The lab gap",
             "body": "doses food can't reach in the body", "at": [2, "gap"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "absorb", "title": "The Absorption Problem", "emoji": "🚪", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "The bad news: EGCG is absorbed very poorly. Most of it breaks down in the gut or leaves the body.",
             {"say": "The bad news: E G C G is absorbed very poorly. Most of it breaks down in the gut or leaves the body."}),
            ("H", "How to improve it? Vitamin C, from lemon or orange, can raise absorption up to five times. "
                  "Piperine, from black pepper, helps too, like it does with turmeric.",
             {"say": "How to improve it? Vitamin C, from lemon or orange, can raise absorption up to five times. "
                     "Pie-per-een, from black pepper, helps too, like it does with turmeric."}),
            ("H", "Taking a supplement on an empty stomach also improves absorption, but it raises the risk of side effects. More on that soon.", {}),
        ], "els": [
            T("Poorly absorbed", 720, 160, 80, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 450, "y": 380, "w": 560, "h": 180, "emoji": "🍋", "title": "Vitamin C", "body": "up to 5× absorption", "at": [1, "Vitamin"], "fill": "#DCFCE7"},
            {"type": "card", "x": 1030, "y": 380, "w": 560, "h": 180, "emoji": "🌶️", "title": "Black pepper", "body": "piperine helps", "at": [1, "pepper"], "fill": "#DCFCE7"},
            {"type": "card", "x": 740, "y": 650, "w": 1000, "h": 170, "emoji": "⚠️", "title": "Empty stomach",
             "body": "better absorbed, more side effects", "at": [2, "empty"], "fill": "#FEF3C7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And milk? Casein, the milk protein, binds catechins into complexes that are absorbed less.", {}),
            ("H", "European studies found that adding milk to black tea wiped out the improvement in blood vessel function seen with plain tea. "
                  "A similar effect probably happens with green tea, though that wasn't tested directly.", {}),
            ("P", "Milk in tea cancels the benefit? The British are not going to like this.", {"mood": "worried", "jump": True}),
        ], "els": [
            E("🥛", 440, 330, 170, at=0),
            T("+", 640, 330, 110, at=0, font="fredoka", weight=700, color="orange"),
            E("🍵", 840, 330, 170, at=0),
            T("casein binds catechins", 640, 480, 50, at=[0, "binds"], font="fredoka", weight=600, color="green"),
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 180, "emoji": "🫖", "title": "Black tea + milk",
             "body": "the blood vessel benefit disappeared", "at": [1, "wiped"], "fill": "#FEE2E2"},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Now the side effects, which matter most with concentrated supplements, not the drink.", {}),
            ("H", "The biggest one: liver toxicity. Concentrated green tea extracts have been linked to cases of acute liver damage. "
                  "It's rare, but well documented, and it led European health authorities to look at limiting EGCG doses in supplements.",
             {"say": "The biggest one: liver toxicity. Concentrated green tea extracts have been linked to cases of acute liver damage. "
                     "It's rare, but well documented, and it led European health authorities to look at limiting E G C G doses in supplements."}),
            ("H", "The risk rises above eight hundred milligrams of EGCG a day, on an empty stomach, and with alcohol. "
                  "To be clear: no liver damage has been documented from drinking normal amounts of tea.",
             {"say": "The risk rises above eight hundred milligrams of E G C G a day, on an empty stomach, and with alcohol. "
                     "To be clear: no liver damage has been documented from drinking normal amounts of tea."}),
        ], "els": [
            T("#1 Liver: the big one", 760, 150, 72, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 760, "y": 330, "w": 1100, "h": 170, "emoji": "💊", "title": "Concentrated extracts",
             "body": "rare, documented liver damage", "at": [1, "liver"]},
            {"type": "pill", "x": 330, "y": 580, "text": "800+ mg a day", "color": "red", "at": [2, "eight"]},
            {"type": "pill", "x": 760, "y": 580, "text": "empty stomach", "color": "red", "at": [2, "empty"]},
            {"type": "pill", "x": 1150, "y": 580, "text": "alcohol", "color": "red", "at": [2, "alcohol"]},
            {"type": "banner", "x": 760, "y": 740, "text": "Normal tea drinking: no documented harm", "color": "#16A34A", "at": [2, "drinking"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Two: nausea and stomach pain on an empty stomach. Catechins irritate the stomach lining. "
                  "The fix: take it after a light meal, or with a big glass of water.", {}),
            ("H", "Three: iron. EGCG binds plant iron and cuts its absorption by about twenty-five to fifty percent. "
                  "That matters for vegetarians, vegans and anyone with anemia. Keep tea and iron-rich meals a couple of hours apart.",
             {"say": "Three: iron. E G C G binds plant iron and cuts its absorption by about twenty five to fifty percent. "
                     "That matters for vegetarians, vegans and anyone with anemia. Keep tea and iron rich meals a couple of hours apart."}),
        ], "els": [
            {"type": "card", "x": 760, "y": 280, "w": 1100, "h": 190, "emoji": "🤢", "title": "#2 Nausea on an empty stomach",
             "body": "take it after a light meal", "at": 0},
            {"type": "card", "x": 760, "y": 540, "w": 1100, "h": 190, "emoji": "🩸", "title": "#3 Iron: 25 to 50% less absorbed",
             "body": "keep a couple of hours apart", "at": 1},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Four: drug interactions. EGCG may weaken bortezomib, a chemotherapy drug. It can affect blood thinners like warfarin, "
                  "may raise blood levels of rosuvastatin, and can interact with drugs broken down by C Y P enzymes.",
             {"say": "Four: drug interactions. E G C G may weaken bortezomib, a chemotherapy drug. It can affect blood thinners like warfarin, "
                     "may raise blood levels of rosu-va-statin, and can interact with drugs broken down by C Y P enzymes."}),
            ("H", "Five: many extracts also contain caffeine, which can cause restlessness and poor sleep. "
                  "And six: EGCG supplements aren't recommended in pregnancy or breastfeeding, and EGCG may interfere with folic acid metabolism.",
             {"say": "Five: many extracts also contain caffeine, which can cause restlessness and poor sleep. "
                     "And six: E G C G supplements aren't recommended in pregnancy or breastfeeding, and E G C G may interfere with folic acid metabolism."}),
            ("P", "Lots of fine print for something so tiny.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 760, "y": 230, "w": 1100, "h": 180, "emoji": "💉", "title": "#4 Drug interactions",
             "body": "chemo, warfarin, rosuvastatin, CYP drugs", "at": 0},
            {"type": "card", "x": 760, "y": 460, "w": 1100, "h": 160, "emoji": "☕", "title": "#5 Hidden caffeine", "at": 1},
            {"type": "card", "x": 760, "y": 670, "w": 1100, "h": 180, "emoji": "🤰", "title": "#6 Pregnancy, breastfeeding",
             "body": "no supplements · folic acid", "at": [1, "pregnancy"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "Tea or Supplement?", "emoji": "✅", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So, tea or supplement? Green tea, or matcha, wins. In nature, EGCG comes wrapped with other compounds that help keep it stable.",
             {"say": "So, tea or supplement? Green tea, or matcha, wins. In nature, E G C G comes wrapped with other compounds that help keep it stable."}),
            ("H", "And remember, tea isn't just EGCG. It also has caffeine, L-theanine, other catechins and minerals. "
                  "The population studies looked at the whole drink, not EGCG on its own. So tea findings don't automatically apply to an EGCG capsule.",
             {"say": "And remember, tea isn't just E G C G. It also has caffeine, L theanine, other catechins and minerals. "
                     "The population studies looked at the whole drink, not E G C G on its own. So tea findings don't automatically apply to an E G C G capsule."}),
        ], "els": [
            {"type": "card", "x": 450, "y": 300, "w": 560, "h": 200, "emoji": "🍵", "title": "Tea or matcha", "body": "the winner", "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 1030, "y": 300, "w": 560, "h": 200, "emoji": "💊", "title": "Capsule", "body": "use with care", "at": [0, "supplement"], "fill": "#FEF3C7"},
            {"type": "banner", "x": 740, "y": 620, "text": "Tea ≠ EGCG alone", "color": "#475569", "at": [1, "isn't"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: EGCG is green tea's main catechin. A cup has twenty to fifty milligrams, matcha much more.",
             {"say": "One: E G C G is green tea's main catechin. A cup has twenty to fifty milligrams, matcha much more."}),
            ("H", "Two: it nudges fat release, blood sugar and blood vessels, but mostly modestly, and much of the evidence is from the lab.", {}),
            ("H", "Three: it's poorly absorbed. Vitamin C helps, milk hurts.", {}),
            ("H", "Four: drinking tea is safe. Concentrated extracts above eight hundred milligrams a day are where the liver risk lives.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "Cup: 20 to 50 mg · matcha: more", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Real but modest effects", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Add lemon, skip the milk", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Tea: safe · extracts 800+ mg: risky", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So EGCG is tiny, powerful, and best enjoyed in a nice warm cup. Not boiling!", {"mood": "happy",
             "say": "So E G C G is tiny, powerful, and best enjoyed in a nice warm cup. Not boiling!"}),
            ("H", "Seventy to eighty degrees, Pip.", {}),
            ("P", "Tea party!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Go put the kettle on, but not too hot!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/egcg", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
