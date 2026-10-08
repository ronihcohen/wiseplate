"""Green tea explainer (English), based on https://wiseplate.blog/en/food/green-tea/

Numbers are the article's: caffeine per 240 ml cup (and by brewing method and
tea type), EGCG per cup vs per extract capsule, the EFSA 800 mg/day caution
line for extract, brewing temperatures in °C, and the study figures it quotes.
Keep them in sync with content/food/green-tea.md. The EGCG episode
(egcg.py) covers the molecule in depth; this one stays with the tea article.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Green Tea: How Much Caffeine, and Is the Extract Safe?"
SLUG = "green-tea"
ARTICLE = "https://wiseplate.blog/en/food/green-tea/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "GREEN TEA", "top_size": 170, "bottom": "TEA OR PILL?", "bottom_size": 150,
         "badge": "20-45", "badge_size": 100, "badge_label": "mg caffeine\nper cup", "badge_color": "#16A34A",
         "scatter": "🍃", "hero": "🍵", "mood": "surprised"}

MUSIC = {
    "intro":    {"bpm": 108, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.7, "swing": 0.12},
    "bush":     {"bpm": 96, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.6, "swing": 0.15},
    "caffeine": {"bpm": 118, "root": 62, "prog": ["I", "V", "IV", "V"], "density": 0.85, "bright": 1.3},
    "extract":  {"bpm": 94, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.55},
    "types":    {"bpm": 104, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "benefits": {"bpm": 112, "root": 69, "prog": ["vi", "IV", "I", "V"], "density": 0.75, "swing": 0.1},
    "catches":  {"bpm": 104, "root": 70, "prog": ["I", "bVII", "IV", "I"], "density": 0.7, "swing": 0.2},
    "brew":     {"bpm": 84, "root": 65, "prog": ["I", "IV", "vi", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "outro":    {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#F0FDF4", "bush": "#ECFDF5", "caffeine": "#FEF3C7", "extract": "#F1F5F9",
    "types": "#F7FEE7", "benefits": "#ECFCCB", "catches": "#FEE2E2", "brew": "#E0F2FE",
    "outro": "#F0FDF4",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


EGCG = "E G C G"

CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hi! Pip the pumpkin seed here. Seeds don't usually drink tea, but today I'm making an exception.",
             {"mood": "happy", "wave": True}),
            ("P", "Our guest is a drink with thousands of studies behind it. It's green tea!", {"mood": "happy", "jump": True}),
        ], "els": [
            E("🍵", 960, 200, 160, at=[1, "green"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today: green tea. How much caffeine is really in a cup, why the extract is not the same as the drink, "
                  "which kind to buy, and how to brew it so it isn't bitter.", {}),
            ("P", "Green, popular and full of leaves. I see a lot of myself in it.", {"mood": "smug"}),
        ], "els": [
            E("🍵", 420, 330, 200, at=[0, "green"], wobble=True),
            T("Green Tea", 620, 300, 130, at=[0, "green"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 680, "h": 110, "emoji": "☕", "title": "Caffeine per cup", "at": [0, "caffeine"]},
            {"type": "card", "x": 760, "y": 650, "w": 680, "h": 110, "emoji": "💊", "title": "Tea vs extract", "at": [0, "extract"]},
            {"type": "card", "x": 760, "y": 780, "w": 680, "h": 110, "emoji": "🌡️", "title": "Brew it right", "at": [0, "brew"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "bush", "title": "One Bush, Three Teas", "emoji": "🌿", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Green tea, Camellia sinensis, is one of the most studied drinks in the world. "
                  "It comes from Japan and China, where it's been drunk for thousands of years, as a drink and as a medicine.", {}),
            ("H", "Here's the surprise: green tea, black tea and white tea all come from exactly the same bush.", {}),
            ("P", "Same bush? So it's a family drama. I love it.", {"mood": "surprised", "jump": True}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 900, "h": 150, "emoji": "🌿", "title": "Camellia sinensis",
             "body": "one of the most studied drinks", "at": 0},
            {"type": "card", "x": 720, "y": 400, "w": 900, "h": 150, "emoji": "🗾", "title": "Japan and China",
             "body": "a drink and a medicine", "at": [0, "Japan"]},
            T("one bush:", 720, 580, 52, at=[1, "same"], color="muted"),
            {"type": "pill", "x": 400, "y": 700, "text": "green", "color": "#16A34A", "at": [1, "green"]},
            {"type": "pill", "x": 720, "y": 700, "text": "black", "color": "#7C2D12", "at": [1, "black"]},
            {"type": "pill", "x": 1040, "y": 700, "text": "white", "color": "#94A3B8", "at": [1, "white"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The only difference is what happens to the leaf after picking. For green tea, the leaf is steamed or pan-fired right away. "
                  "That switches off an enzyme called polyphenol oxidase, and stops oxidation.", {}),
            ("H", "So the catechins, a group of polyphenols behind most of its benefits, are kept almost entirely, "
                  "instead of turning into theaflavins, like in black tea.",
             {"say": "So the cat-eh-kins, a group of polyphenols behind most of its benefits, are kept almost entirely, "
                     "instead of turning into thee-a-flay-vins, like in black tea."}),
        ], "els": [
            {"type": "card", "x": 400, "y": 300, "w": 520, "h": 180, "emoji": "🍃", "title": "Fresh leaf", "at": 0},
            {"type": "arrow", "x1": 690, "y1": 300, "x2": 800, "y2": 300, "at": [0, "steamed"]},
            {"type": "card", "x": 1080, "y": 300, "w": 520, "h": 180, "emoji": "♨️", "title": "Steamed",
             "body": "oxidation stopped", "at": [0, "steamed"]},
            {"type": "card", "x": 400, "y": 620, "w": 520, "h": 180, "emoji": "🍵", "title": "Green tea",
             "body": "catechins kept", "at": [1, "catechins"], "fill": "#DCFCE7"},
            {"type": "card", "x": 1080, "y": 620, "w": 520, "h": 180, "emoji": "🫖", "title": "Black tea",
             "body": "now theaflavins", "at": [1, "black"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "caffeine", "title": "How Much Caffeine?", "emoji": "☕", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Is there caffeine in green tea? Yes. A two hundred forty milliliter cup usually has twenty to forty-five milligrams.", {}),
            ("H", "That's a third to a half of a cup of drip coffee, at ninety-five to one hundred sixty-five milligrams. "
                  "Matcha has more, about sixty to seventy, because you drink the whole ground leaf.", {}),
        ], "els": [
            T("Caffeine per cup", 720, 160, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 300, "y": 430, "w": 380, "h": 300, "value": 0, "text": "20-45 mg", "vsize": 80,
             "label": "green tea", "emoji": "🍵", "at": [0, "twenty"]},
            {"type": "stat", "x": 720, "y": 430, "w": 380, "h": 300, "value": 0, "text": "95-165 mg", "vsize": 70,
             "label": "drip coffee", "emoji": "☕", "color": "#92400E", "at": [1, "drip"]},
            {"type": "stat", "x": 1140, "y": 430, "w": 380, "h": 300, "value": 0, "text": "60-70 mg", "vsize": 80,
             "label": "matcha", "emoji": "🟢", "at": [1, "Matcha"]},
            {"type": "banner", "x": 720, "y": 760, "text": "A third to a half of coffee", "color": "#16A34A", "at": [1, "third"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "The exact amount depends less on the type of tea, and more on how you make it.", {}),
            ("H", "One minute at seventy degrees Celsius: fifteen to twenty milligrams. Two to three minutes at eighty: twenty-five to thirty-five. "
                  "Four minutes in boiling water: forty to fifty.", {}),
            ("H", "A teaspoon of matcha: sixty to seventy. And decaf green tea: just two to five.", {}),
            ("P", "So the kettle is the boss. Noted.", {"mood": "smug"}),
        ], "els": [
            T("Caffeine per cup, by brewing", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 180, "y": 270, "w": 1260, "row_h": 115, "max": 70, "unit": " mg", "rows": [
                {"label": "1 min, 70°C", "value": 20, "text": "15-20 mg", "color": "#84CC16", "at": [1, "One"]},
                {"label": "2-3 min, 80°C", "value": 35, "text": "25-35 mg", "color": "#16A34A", "at": [1, "Two"]},
                {"label": "4 min, boiling", "value": 50, "text": "40-50 mg", "color": "#F59E0B", "at": [1, "Four"]},
                {"label": "Matcha", "value": 70, "text": "60-70 mg", "color": "#15803D", "at": [2, "matcha"]},
                {"label": "Decaf", "value": 5, "text": "2-5 mg", "color": "#94A3B8", "at": [2, "decaf"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And green tea's caffeine comes with a partner: L-theanine. It slows the caffeine's absorption and softens its effect.",
             {"say": "And green tea's caffeine comes with a partner: L theanine. It slows the caffeine's absorption and softens its effect."}),
            ("H", "So you get moderate, lasting alertness, instead of a sharp spike and then a crash. "
                  "That's why many people tolerate green tea even when coffee makes them jittery or anxious.", {}),
            ("H", "Decaf green tea keeps most of the catechins, but loses that alertness. And the method matters: "
                  "carbon dioxide decaf keeps EGCG much better than the solvent ethyl acetate, which can remove up to about seventy percent of the catechins.",
             {"say": "Decaf green tea keeps most of the cat-eh-kins, but loses that alertness. And the method matters: "
                     "carbon dioxide decaf keeps " + EGCG + " much better than the solvent ethyl acetate, which can remove up to about seventy percent of the cat-eh-kins."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 150, "emoji": "🧘", "title": "L-theanine: calm, lasting alertness",
             "at": [0, "theanine"]},
            {"type": "card", "x": 400, "y": 420, "w": 560, "h": 150, "emoji": "📈", "title": "No spike", "at": [1, "spike"]},
            {"type": "card", "x": 1040, "y": 420, "w": 560, "h": 150, "emoji": "📉", "title": "No crash", "at": [1, "crash"]},
            {"type": "card", "x": 400, "y": 680, "w": 560, "h": 180, "emoji": "🫧", "title": "CO2 decaf",
             "body": "keeps EGCG", "at": [2, "carbon"], "fill": "#DCFCE7"},
            {"type": "card", "x": 1040, "y": 680, "w": 560, "h": 180, "emoji": "🧪", "title": "Ethyl acetate",
             "body": "up to ~70% lost", "at": [2, "ethyl"], "fill": "#FEE2E2"},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "extract", "title": "Tea vs Extract", "emoji": "💊", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Green tea extract is the catechins from the leaf, concentrated into a powder or a capsule. "
                  "And it's not the same as drinking tea. The difference isn't only strength.",
             {"say": "Green tea extract is the cat-eh-kins from the leaf, concentrated into a powder or a capsule. "
                     "And it's not the same as drinking tea. The difference isn't only strength."}),
            ("H", "A cup of green tea gives about fifty to one hundred milligrams of EGCG. "
                  "A capsule usually gives two hundred to four hundred, and sometimes as much as seven hundred.",
             {"say": "A cup of green tea gives about fifty to one hundred milligrams of " + EGCG + ". "
                     "A capsule usually gives two hundred to four hundred, and sometimes as much as seven hundred."}),
            ("H", "So one capsule equals four to ten cups.", {}),
            ("P", "Ten cups in one pill? That's not tea, that's a tea-nado.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("EGCG per serving", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 180, "y": 300, "w": 1260, "row_h": 130, "max": 700, "unit": " mg", "rows": [
                {"label": "A cup", "value": 100, "text": "50-100 mg", "color": "#16A34A", "at": [1, "cup"]},
                {"label": "A capsule", "value": 400, "text": "200-400 mg", "color": "#F59E0B", "at": [1, "capsule"]},
                {"label": "Strong ones", "value": 700, "text": "up to 700", "color": "#DC2626", "at": [1, "seven"]},
            ]},
            {"type": "banner", "x": 760, "y": 740, "text": "1 capsule = 4 to 10 cups", "color": "#DC2626", "at": [2, "four"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Now, the liver problem. The European Food Safety Authority, EFSA, found that eight hundred milligrams of EGCG a day or more, "
                  "from extract, is linked to raised liver enzymes.",
             {"say": "Now, the liver problem. The European Food Safety Authority, E F S A, found that eight hundred milligrams of " + EGCG +
                     " a day or more, from extract, is linked to raised liver enzymes."}),
            ("H", "Dozens of cases of acute liver injury have been linked to green tea extract supplements. "
                  "Mainly when taken on an empty stomach, where blood EGCG jumps three to five times higher.",
             {"say": "Dozens of cases of acute liver injury have been linked to green tea extract supplements. "
                     "Mainly when taken on an empty stomach, where blood " + EGCG + " jumps three to five times higher."}),
            ("H", "But the tea itself? The same review found no concern with drinking green tea, even in large amounts. "
                  "The difference is the concentration, and how fast it's absorbed.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 170, "emoji": "⚠️", "title": "800 mg+ a day from extract",
             "body": "EFSA: raised liver enzymes", "at": [0, "eight"], "fill": "#FEE2E2"},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 170, "emoji": "🍽️", "title": "Empty stomach: 3-5× higher",
             "body": "dozens of liver injury cases", "at": [1, "empty"], "fill": "#FEE2E2"},
            {"type": "card", "x": 720, "y": 630, "w": 1000, "h": 170, "emoji": "🍵", "title": "The drink: no concern",
             "body": "even in large amounts", "at": [2, "tea"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "What does work? Studies with a real metabolic effect mostly used two hundred fifty to five hundred milligrams of EGCG a day, "
                  "usually with caffeine. The weight effect was consistent, but small: about one to one and a half kilos over twelve weeks.",
             {"say": "What does work? Studies with a real metabolic effect mostly used two hundred fifty to five hundred milligrams of " + EGCG +
                     " a day, usually with caffeine. The weight effect was consistent, but small: about one to one and a half kilos over twelve weeks."}),
            ("H", "The practical takeaway: three to four cups of tea a day give a similar range of EGCG, without the liver risk.",
             {"say": "The practical takeaway: three to four cups of tea a day give a similar range of " + EGCG + ", without the liver risk."}),
            ("H", "And if you take extract anyway: not on an empty stomach, not above four hundred milligrams of EGCG a day, "
                  "and not alongside drugs that are processed by the liver.",
             {"say": "And if you take extract anyway: not on an empty stomach, not above four hundred milligrams of " + EGCG + " a day, "
                     "and not alongside drugs that are processed by the liver."}),
            ("P", "Or, hear me out: just drink the tea.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 150, "emoji": "⚖️", "title": "~1-1.5 kg in 12 weeks",
             "at": [0, "kilos"]},
            {"type": "banner", "x": 720, "y": 370, "text": "3-4 cups a day: no liver risk", "color": "#16A34A", "at": [1, "three"]},
            T("Taking extract anyway?", 720, 500, 48, at=[2, "anyway"], font="fredoka", weight=600, color="muted"),
            {"type": "check", "x": 140, "y": 590, "w": 1300, "ok": False, "text": "On an empty stomach", "at": [2, "empty"]},
            {"type": "check", "x": 140, "y": 700, "w": 1300, "ok": False, "text": "Over 400 mg EGCG a day", "at": [2, "four"]},
            {"type": "check", "x": 140, "y": 810, "w": 1300, "ok": False, "text": "With liver-processed drugs", "at": [2, "drugs"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "types", "title": "Which Green Tea?", "emoji": "🍵", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Five Japanese green teas, from most caffeine to least.", {}),
            ("H", "Matcha: the highest EGCG, because you drink the whole leaf, and sixty to seventy milligrams of caffeine.",
             {"say": "Matcha: the highest " + EGCG + ", because you drink the whole leaf, and sixty to seventy milligrams of caffeine."}),
            ("H", "Gyokuro: high, about thirty-five. It's grown in the shade, the richest in L-theanine, sweet and mellow.",
             {"say": "Gyo-kuro: high, about thirty-five. It's grown in the shade, the richest in L theanine, sweet and mellow."}),
            ("H", "Sencha: medium-high, about thirty. Bancha: low, about ten, good after a meal or in the evening. "
                  "And hojicha: roasted, low, seven to ten, with almost no bitterness. Fine for kids and evenings.",
             {"say": "Sen-cha: medium high, about thirty. Ban-cha: low, about ten, good after a meal or in the evening. "
                     "And ho-ji-cha: roasted, low, seven to ten, with almost no bitterness. Fine for kids and evenings."}),
        ], "els": [
            T("Caffeine per cup", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "bars", "x": 180, "y": 270, "w": 1260, "row_h": 115, "max": 70, "unit": " mg", "rows": [
                {"label": "Matcha", "value": 70, "text": "60-70 mg", "color": "#15803D", "at": [1, "Matcha"]},
                {"label": "Gyokuro", "value": 35, "text": "~35 mg", "color": "#16A34A", "at": [2, "Gyo"]},
                {"label": "Sencha", "value": 30, "text": "~30 mg", "color": "#22C55E", "at": [3, "Sen"]},
                {"label": "Bancha", "value": 10, "text": "~10 mg", "color": "#84CC16", "at": [3, "Ban"]},
                {"label": "Hojicha", "value": 10, "text": "7-10 mg", "color": "#B45309", "at": [3, "ho-ji"]},
            ]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The practical pick for most people is whole-leaf Japanese sencha. It gives most of the benefit, at a reasonable price.",
             {"say": "The practical pick for most people is whole leaf Japanese sen-cha. It gives most of the benefit, at a reasonable price."}),
            ("H", "Matcha is better if you want the maximum and you're willing to pay. But choose a ceremonial grade and a known source. "
                  "Because you drink the whole leaf, you also get any heavy metals and fluoride it absorbed.", {}),
            ("H", "And whole leaves beat tea bags. Bags usually hold dust and low-grade leaf fragments that lost some of their volatile oils. "
                  "Whole leaves give more catechins and a cleaner flavor.",
             {"say": "And whole leaves beat tea bags. Bags usually hold dust and low grade leaf fragments that lost some of their volatile oils. "
                     "Whole leaves give more cat-eh-kins and a cleaner flavor."}),
            ("P", "Whole and natural. Like a certain seed I know.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 170, "emoji": "🏆", "title": "Best everyday: sencha",
             "body": "whole leaf · great value", "at": [0, "sencha"], "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 170, "emoji": "🍵", "title": "Matcha: ceremonial grade",
             "body": "known source · whole leaf, metals too", "at": [1, "ceremonial"]},
            {"type": "card", "x": 400, "y": 660, "w": 560, "h": 170, "emoji": "🍃", "title": "Whole leaves",
             "body": "more catechins", "at": [2, "Whole"], "fill": "#DCFCE7"},
            {"type": "card", "x": 1040, "y": 660, "w": 560, "h": 170, "emoji": "🧺", "title": "Tea bags",
             "body": "dust and fragments", "at": [2, "dust"], "fill": "#FEE2E2"},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "benefits", "title": "The Benefits", "emoji": "⭐", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Benefit one: EGCG, epigallocatechin gallate. It's the main catechin, about fifty to sixty percent of the leaf's total, "
                  "and one of the most powerful known antioxidants.",
             {"say": "Benefit one: " + EGCG + ", epi-gallo-catechin gallate. It's the main cat-eh-kin, about fifty to sixty percent of the leaf's total, "
                     "and one of the most powerful known antioxidants."}),
            ("H", "It inhibits oxidative enzymes, reduces inflammation, and is linked to activity against tumor growth in lab studies.", {}),
            ("H", "Benefit two: caffeine plus L-theanine. Caffeine boosts alertness, focus and metabolic rate. "
                  "L-theanine, an amino acid almost unique to tea, increases alpha brain waves and balances the caffeine. "
                  "Together: calm alertness.",
             {"say": "Benefit two: caffeine plus L theanine. Caffeine boosts alertness, focus and metabolic rate. "
                     "L theanine, an amino acid almost unique to tea, increases alpha brain waves and balances the caffeine. "
                     "Together: calm alertness."}),
        ], "els": [
            {"type": "ring", "x": 400, "y": 330, "r": 150, "value": 60, "color": "#16A34A", "label": "of catechins", "at": [0, "fifty"]},
            {"type": "pill", "x": 1040, "y": 220, "text": "antioxidant", "color": "green", "at": [0, "antioxidants"]},
            {"type": "pill", "x": 1040, "y": 310, "text": "less inflammation", "color": "#0EA5E9", "at": [1, "inflammation"]},
            {"type": "pill", "x": 1040, "y": 400, "text": "lab: anti-tumor", "color": "#8B5CF6", "at": [1, "tumor"]},
            {"type": "card", "x": 720, "y": 680, "w": 1000, "h": 190, "emoji": "🧠", "title": "Caffeine + L-theanine",
             "body": "calm alertness", "at": [2, "theanine"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Benefit three: the heart. Large studies in Japan, like the Ohsaki study with about forty thousand people, "
                  "linked three to five cups a day with lower heart disease deaths and fewer strokes.",
             {"say": "Benefit three: the heart. Large studies in Japan, like the Oh-saki study with about forty thousand people, "
                     "linked three to five cups a day with lower heart disease deaths and fewer strokes."}),
            ("H", "Catechins reduce LDL oxidation, and improve how the lining of blood vessels works.",
             {"say": "Cat-eh-kins reduce L D L oxidation, and improve how the lining of blood vessels works."}),
            ("H", "Benefit four: fat metabolism. EGCG blocks an enzyme called COMT, so a fat-mobilizing signal lasts longer. "
                  "The effect is real but modest: about three to four percent of daily energy use. Not the fat burning the marketing promises.",
             {"say": "Benefit four: fat metabolism. " + EGCG + " blocks an enzyme called C O M T, so a fat mobilizing signal lasts longer. "
                     "The effect is real but modest: about three to four percent of daily energy use. Not the fat burning the marketing promises."}),
            ("P", "Three percent. So I still have to actually move. Rude.", {"mood": "worried"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1000, "h": 170, "emoji": "❤️", "title": "3-5 cups: healthier heart",
             "body": "Ohsaki study · ~40,000 people", "at": [0, "Ohsaki"]},
            {"type": "card", "x": 720, "y": 420, "w": 1000, "h": 170, "emoji": "🩸", "title": "Less LDL oxidation",
             "body": "better blood-vessel lining", "at": [1, "LDL"]},
            {"type": "card", "x": 720, "y": 630, "w": 1000, "h": 170, "emoji": "🔥", "title": "+3-4% energy use",
             "body": "real, but modest", "at": [2, "three"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And three more. Regular tea drinking has been linked to better fasting glucose, and a better insulin response to a meal.", {}),
            ("H", "EGCG has been studied for protecting the brain against Alzheimer's and Parkinson's. But that evidence is still early, mostly from models.",
             {"say": EGCG + " has been studied for protecting the brain against Alzheimer's and Parkinson's. But that evidence is still early, mostly from models."}),
            ("H", "And your teeth: catechins inhibit Streptococcus mutans, the main bacterium behind cavities. The leaf's natural fluoride helps too.",
             {"say": "And your teeth: cat-eh-kins inhibit Strep-to-coccus mew-tans, the main bacterium behind cavities. The leaf's natural fluoride helps too."}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 1000, "h": 170, "emoji": "🩺", "title": "Blood sugar and insulin",
             "body": "linked to improvements", "at": 0},
            {"type": "card", "x": 720, "y": 430, "w": 1000, "h": 170, "emoji": "🧠", "title": "Brain: early evidence",
             "body": "mostly from models", "at": [1, "brain"], "fill": "#FEF3C7"},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 170, "emoji": "🦷", "title": "Fewer cavity bacteria",
             "body": "plus natural fluoride", "at": [2, "teeth"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Catch one: iron. Tannins and catechins bind plant iron and cut its absorption by twenty-five to fifty percent. "
                  "That's the biggest downside if you're prone to anemia.",
             {"say": "Catch one: iron. Tannins and cat-eh-kins bind plant iron and cut its absorption by twenty-five to fifty percent. "
                     "That's the biggest downside if you're prone to anemia."}),
            ("H", "The fix is simple: drink tea between meals, at least an hour apart, not with them.", {}),
            ("H", "Catch two: sleep. If you're sensitive to caffeine, skip it after two p.m. "
                  "Caffeine's half-life is five to six hours for most people, and up to nine for slow metabolizers.",
             {"say": "Catch two: sleep. If you're sensitive to caffeine, skip it after two P M. "
                     "Caffeine's half life is five to six hours for most people, and up to nine for slow metabolizers."}),
            ("P", "Nine hours? That's longer than my nap schedule.", {"mood": "sleepy"}),
        ], "els": [
            {"type": "card", "x": 760, "y": 220, "w": 1100, "h": 180, "emoji": "🩸", "title": "#1 Blocks plant iron: 25-50%",
             "body": "biggest issue if prone to anemia", "at": 0},
            {"type": "banner", "x": 760, "y": 400, "text": "Drink between meals, 1 hour apart", "color": "#16A34A", "at": [1, "between"]},
            {"type": "card", "x": 760, "y": 640, "w": 1100, "h": 180, "emoji": "😴", "title": "#2 Sleep: none after 2 p.m.",
             "body": "half-life 5-6 h, up to 9 h", "at": 2},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Catch three: fluoride. The tea leaf absorbs it from the soil, and it builds up most in the older leaves used for cheap tea. "
                  "More than eight to ten cups a day for years has been linked to fluoride buildup in the bones. At two to four cups, the risk is negligible.", {}),
            ("H", "Catch four: concentrated extract and the liver. The risk is in the supplements, not in the drink.", {}),
            ("H", "Catch five: drugs. Green tea contains vitamin K and may interfere with warfarin. "
                  "And catechins affect liver enzymes and the absorption of some drugs, including nadolol and some statins.",
             {"say": "Catch five: drugs. Green tea contains vitamin K and may interfere with warfarin. "
                     "And cat-eh-kins affect liver enzymes and the absorption of some drugs, including nad-o-lol and some statins."}),
        ], "els": [
            {"type": "card", "x": 760, "y": 230, "w": 1100, "h": 180, "emoji": "🦴", "title": "#3 Fluoride: 8-10+ cups for years",
             "body": "2-4 cups: negligible risk", "at": 0},
            {"type": "card", "x": 760, "y": 460, "w": 1100, "h": 180, "emoji": "💊", "title": "#4 Extract and the liver",
             "body": "supplements, not the drink", "at": 1},
            {"type": "card", "x": 760, "y": 690, "w": 1100, "h": 180, "emoji": "⚕️", "title": "#5 Warfarin, nadolol, statins",
             "body": "vitamin K · drug absorption", "at": 2},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "And catch six: bitterness. Boiling water pulls too many tannins and catechins out of the leaf. "
                  "It's the most common reason people say they don't like green tea.",
             {"say": "And catch six: bitterness. Boiling water pulls too many tannins and cat-eh-kins out of the leaf. "
                     "It's the most common reason people say they don't like green tea."}),
            ("P", "So green tea isn't bitter. It's just been treated badly.", {"mood": "worried"}),
        ], "els": [
            E("🫖", 520, 400, 220, at=0, wobble=True),
            T("#6 Boiling water", 1000, 340, 64, at=[0, "Boiling"], font="fredoka", weight=700, color="#DC2626"),
            T("= bitter tea", 1000, 440, 64, at=[0, "bitter"], font="fredoka", weight=700, color="#DC2626"),
            {"type": "banner", "x": 720, "y": 700, "text": "#1 reason people dislike it", "color": "#F59E0B", "at": [0, "common"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "brew", "title": "Brew It Right", "emoji": "🌡️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "So here's how to brew it. Temperature: seventy to eighty degrees Celsius. "
                  "Boil, then wait three to five minutes, or add a little cold water to the kettle. For matcha, seventy to seventy-five.", {}),
            ("H", "Time: two to three minutes for sencha, one to two for gyokuro. Longer mostly adds bitterness.",
             {"say": "Time: two to three minutes for sen-cha, one to two for gyo-kuro. Longer mostly adds bitterness."}),
            ("H", "Amount: a teaspoon, two to three grams, per two hundred milliliters.", {}),
        ], "els": [
            {"type": "stat", "x": 300, "y": 400, "w": 380, "h": 320, "value": 0, "text": "70-80°C", "vsize": 84,
             "label": "158-176°F", "emoji": "🌡️", "at": [0, "seventy"]},
            {"type": "stat", "x": 720, "y": 400, "w": 380, "h": 320, "value": 0, "text": "2-3 min", "vsize": 84,
             "label": "sencha", "emoji": "⏱️", "at": [1, "Time"]},
            {"type": "stat", "x": 1140, "y": 400, "w": 380, "h": 320, "value": 0, "text": "2-3 g", "vsize": 84,
             "label": "per 200 ml", "emoji": "🥄", "at": [2, "teaspoon"]},
            T("matcha 70-75°C · gyokuro 1-2 min", 720, 680, 44, at=[1, "gyokuro"], color="muted"),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Re-steep: whole leaves are good for two, even three brews. The second one is richer in L-theanine, and mellower.",
             {"say": "Re steep: whole leaves are good for two, even three brews. The second one is richer in L theanine, and mellower."}),
            ("H", "Add lemon. Vitamin C stabilizes catechins in the gut, and significantly increases how much you absorb. A real upgrade, not just flavor.",
             {"say": "Add lemon. Vitamin C stabilizes cat-eh-kins in the gut, and significantly increases how much you absorb. A real upgrade, not just flavor."}),
            ("H", "But skip the milk. Milk proteins bind some of the catechins.",
             {"say": "But skip the milk. Milk proteins bind some of the cat-eh-kins."}),
            ("H", "And iced green tea? It keeps its benefits. A long cold brew even pulls out less caffeine and less bitterness.", {}),
            ("P", "Lemon yes, milk no, ice welcome. My kind of rules.", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "card", "x": 720, "y": 190, "w": 1000, "h": 140, "emoji": "🔁", "title": "Re-steep 2-3 times", "at": 0, "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 360, "w": 1000, "h": 140, "emoji": "🍋", "title": "Add lemon", "at": [1, "lemon"], "fill": "#DCFCE7"},
            {"type": "card", "x": 720, "y": 530, "w": 1000, "h": 140, "emoji": "🥛", "title": "Skip the milk", "at": [2, "milk"], "fill": "#FEE2E2"},
            {"type": "card", "x": 720, "y": 700, "w": 1000, "h": 140, "emoji": "🧊", "title": "Iced: still good", "at": [3, "iced"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: two to four cups a day is one of the simplest, best-supported additions to your diet.", {}),
            ("H", "Two: whole-leaf sencha or matcha, brewed at eighty degrees, not boiling.",
             {"say": "Two: whole leaf sen-cha or matcha, brewed at eighty degrees, not boiling."}),
            ("H", "Three: drink it between meals, not with them, so it doesn't block iron.", {}),
            ("H", "Four: be careful with concentrated extracts. That's where the real risk is, not in the drink.", {}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "2-4 cups a day", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Sencha or matcha, 80°C, not boiling", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Between meals, for your iron", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": True, "text": "Careful with extracts", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So green tea: calm energy, a happy heart, and it only turns bitter if you boil it. Relatable.", {"mood": "smug"}),
            ("H", "Very relatable, Pip.", {}),
            ("P", "Cheers! Cup raised, seed approved!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article with all the sources, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article with all the sources, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Don't boil the leaves!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/green-tea", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
