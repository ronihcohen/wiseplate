"""Rye bread explainer (English), based on https://wiseplate.blog/en/food/rye-bread/

Numbers are the article's: whole rye bread per 100 g (calories, protein, fat,
carbs, fiber), magnesium and zinc per 100 g of whole rye FLOUR with % daily
value, GI ranges, commercial sodium per 100 g, the rye-type table (GI and fiber
per 100 g) and 1 to 3 slices of 30 to 40 g a day. Keep them in sync with
content/food/rye-bread.md.

Lines are (speaker, caption text, options). Speaker "H" is the host, "P" is
Pip. options["say"] overrides what the TTS reads (for pronunciation).
Element "at" is a line index, or [line, "word"] to trigger on a word.
"""

TITLE = "Rye Bread: Is It Really Better Than Wheat?"
SLUG = "rye-bread"
ARTICLE = "https://wiseplate.blog/en/food/rye-bread/"

VOICES = {
    "H": {"voice": "af_heart", "speed": 1.0, "name": "Host"},
    "P": {"voice": "am_puck", "speed": 1.08, "name": "Pip"},
}

PIP_R = {"x": 1660, "y": 640, "size": 300}     # Pip parked on the right
PIP_C = {"x": 960, "y": 560, "size": 420}      # Pip centre stage
PIP_S = {"x": 1720, "y": 700, "size": 220}     # Pip small, bottom right

THUMB = {"top": "RYE BREAD", "top_size": 170, "bottom": "BEATS WHEAT?", "bottom_size": 126,
         "badge": "6.2 g", "badge_size": 110, "badge_label": "fiber\nper 100 g", "badge_color": "#B45309",
         "scatter": "🌾", "hero": "🍞", "mood": "surprised"}

MUSIC = {
    "intro":   {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.75, "swing": 0.12},
    "meet":    {"bpm": 100, "root": 65, "prog": ["I", "vi", "IV", "V"], "density": 0.65, "swing": 0.15},
    "heart":   {"bpm": 96, "root": 63, "prog": ["I", "iii", "IV", "V"], "density": 0.6},
    "sugar":   {"bpm": 108, "root": 67, "prog": ["I", "IV", "vi", "V"], "density": 0.7},
    "gut":     {"bpm": 116, "root": 62, "prog": ["I", "bVII", "IV", "I"], "density": 0.8, "swing": 0.1},
    "catches": {"bpm": 104, "root": 70, "prog": ["vi", "IV", "I", "V"], "density": 0.65, "swing": 0.2},
    "loaf":    {"bpm": 84, "root": 69, "prog": ["I", "vi", "IV", "V"], "density": 0.5, "inst": "musicbox", "drums": False},
    "howto":   {"bpm": 110, "root": 60, "prog": ["IV", "I", "V", "vi"], "density": 0.7, "swing": 0.1},
    "outro":   {"bpm": 112, "root": 60, "prog": ["I", "V", "vi", "IV"], "density": 0.8, "swing": 0.12},
}

BG = {  # background tint per chapter
    "intro": "#FEF3C7", "meet": "#FFF7ED", "heart": "#FFE4E6", "sugar": "#ECFDF5",
    "gut": "#ECFCCB", "catches": "#FEE2E2", "loaf": "#FDF4E3", "howto": "#FFEDD5",
    "outro": "#FEF3C7",
}


def T(text, x, y, size=64, at=0, **kw):
    return {"type": "text", "text": text, "x": x, "y": y, "size": size, "at": at, **kw}


def E(ch, x, y, size=140, at=0, **kw):
    return {"type": "emoji", "ch": ch, "x": x, "y": y, "size": size, "at": at, **kw}


CHAPTERS = [
    # ------------------------------------------------------------------ 0
    {"key": "intro", "title": "Meet Pip", "card": False, "scenes": [
        {"pip": {"x": 960, "y": 1500, "size": 420}, "pip_to": PIP_C, "dur_min": 3, "lines": [
            ("P", "Hello, hello! Pip the pumpkin seed here. Today I'm reviewing a fellow plant product. A grain, in fact.", {"mood": "happy", "wave": True}),
            ("P", "It's dark, it's dense, and it's a little bit sour. Just like my uncle. It's rye bread!", {"mood": "smug", "jump": True}),
        ], "els": [
            E("🍞", 960, 200, 160, at=[1, "rye"], wobble=True),
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Today it's rye bread. We'll look at what's in it, why its fiber is special, how it treats your blood sugar and your gut, "
                  "and the catches, starting with gluten.", {}),
            ("P", "A bread with a fan club. Let's see if it deserves one.", {"mood": "smug"}),
        ], "els": [
            E("🌾", 420, 330, 200, at=[0, "rye"], wobble=True),
            T("Rye bread", 620, 300, 130, at=[0, "rye"], font="fredoka", weight=700, color="green", anchor="l"),
            {"type": "card", "x": 760, "y": 520, "w": 640, "h": 110, "emoji": "🌀", "title": "Special fiber", "at": [0, "fiber"]},
            {"type": "card", "x": 760, "y": 650, "w": 640, "h": 110, "emoji": "📉", "title": "Blood sugar", "at": [0, "blood"]},
            {"type": "card", "x": 760, "y": 780, "w": 640, "h": 110, "emoji": "⚠️", "title": "The catches", "at": [0, "catches"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 1
    {"key": "meet", "title": "The Northern Grain", "emoji": "🌾", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Rye bread is made from a grain called Secale cereale. It's a national standard in Scandinavia, Germany and Eastern Europe, "
                  "where it has been part of the traditional diet for hundreds of years.",
             {"say": "Rye bread is made from a grain called Seck-a-lee seer-ee-ah-lee. It's a national standard in Scandinavia, Germany and Eastern Europe, "
                     "where it has been part of the traditional diet for hundreds of years."}),
            ("H", "While wheat took over most of the world, rye kept its place there. And not by chance. "
                  "Nutritionally, it shows a better profile for chronic health than white wheat breads, and even many whole wheat breads.", {}),
            ("P", "Hundreds of years of loyalty. Respect. I know a thing or two about being an underrated snack.", {"mood": "happy"}),
        ], "els": [
            T("Secale cereale", 720, 170, 72, at=0, font="fredoka", weight=700, color="green"),
            E("🇸🇪", 400, 360, 120, at=[0, "Scandinavia"]),
            T("Scandinavia", 400, 460, 40, at=[0, "Scandinavia"], font="fredoka", weight=600),
            E("🇩🇪", 720, 360, 120, at=[0, "Germany"]),
            T("Germany", 720, 460, 40, at=[0, "Germany"], font="fredoka", weight=600),
            E("🌍", 1040, 360, 120, at=[0, "Eastern"]),
            T("Eastern Europe", 1040, 460, 40, at=[0, "Eastern"], font="fredoka", weight=600),
            {"type": "card", "x": 720, "y": 680, "w": 1080, "h": 180, "emoji": "🏆", "title": "Better profile than wheat",
             "body": "white bread, and many whole wheat breads", "at": [1, "Nutritionally"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Here are the numbers. One hundred grams of whole rye bread has about two hundred sixty calories, "
                  "eight point five grams of protein, and one point seven grams of fat.", {}),
            ("H", "Plus forty-eight grams of carbohydrates, and six point two grams of dietary fiber. That's significantly more fiber than wheat breads.", {}),
            ("H", "But the numbers are only part of the story.", {}),
        ], "els": [
            T("Whole rye bread, per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 330, "y": 380, "w": 400, "h": 270, "value": 260, "unit": "", "label": "calories", "emoji": "🔥", "at": [0, "sixty"]},
            {"type": "stat", "x": 760, "y": 380, "w": 400, "h": 270, "value": 8.5, "decimals": 1, "unit": " g", "label": "protein", "emoji": "💪", "at": [0, "protein"]},
            {"type": "stat", "x": 1190, "y": 380, "w": 400, "h": 270, "value": 1.7, "decimals": 1, "unit": " g", "label": "fat", "emoji": "🫒", "at": [0, "fat"]},
            {"type": "stat", "x": 540, "y": 690, "w": 400, "h": 270, "value": 48, "unit": " g", "label": "carbs", "emoji": "🍞", "at": [1, "carbohydrates"]},
            {"type": "stat", "x": 980, "y": 690, "w": 400, "h": 270, "value": 6.2, "decimals": 1, "unit": " g", "label": "fiber", "emoji": "🌾", "at": [1, "fiber"], "color": "orange"},
        ], "pip_hide": True},
    ]},
    # ------------------------------------------------------------------ 2
    {"key": "heart", "title": "Fiber for Your Heart", "emoji": "❤️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "The star of rye is its fiber. It's rich in fibers from the arabinoxylan family, and it also has a moderate amount of beta-glucan.",
             {"say": "The star of rye is its fiber. It's rich in fibers from the arra-bino-zylan family, and it also has a moderate amount of beta gloo-can."}),
            ("H", "These fibers form a thick, viscous gel in the small intestine. The gel binds bile salts, so less of them get reabsorbed.", {}),
            ("H", "That forces the liver to use up cholesterol to make new bile.", {}),
            ("P", "So the fiber makes the liver clean up. I love a bread with a plan.", {"mood": "surprised"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1000, "h": 180, "emoji": "🌀", "title": "Arabinoxylans",
             "body": "plus some beta-glucan", "at": [0, "arabinoxylan"]},
            {"type": "pill", "x": 400, "y": 420, "text": "viscous gel", "color": "green", "at": [1, "gel"]},
            {"type": "arrow", "x1": 570, "y1": 420, "x2": 680, "y2": 420, "at": [1, "binds"], "color": "orange"},
            {"type": "pill", "x": 900, "y": 420, "text": "binds bile salts", "color": "orange", "at": [1, "binds"]},
            {"type": "card", "x": 720, "y": 640, "w": 1000, "h": 180, "emoji": "🫀", "title": "Liver uses cholesterol",
             "body": "to make new bile", "at": [2, "liver"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "The U S Food and Drug Administration recognized a health claim for beta-glucan from oats and barley, for reducing heart disease risk. "
                  "In rye, though, the effect is mainly put down to the arabinoxylans.",
             {"say": "The U S Food and Drug Administration recognized a health claim for beta gloo-can from oats and barley, for reducing heart disease risk. "
                     "In rye, though, the effect is mainly put down to the arra-bino-zylans."}),
            ("H", "And Nordic intervention studies found a moderate drop in LDL cholesterol when people swapped wheat bread for whole rye bread.",
             {"say": "And Nordic intervention studies found a moderate drop in L D L cholesterol when people swapped wheat bread for whole rye bread."}),
            ("P", "Moderate. Not magic. Noted.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 220, "w": 1040, "h": 180, "emoji": "📜", "title": "FDA claim: oat, barley",
             "body": "beta-glucan · heart disease risk", "at": 0},
            {"type": "pill", "x": 720, "y": 400, "text": "in rye: mainly arabinoxylans", "color": "green", "at": [0, "rye"]},
            {"type": "card", "x": 720, "y": 620, "w": 1040, "h": 180, "emoji": "📉", "title": "LDL: a moderate drop",
             "body": "wheat bread swapped for whole rye", "at": [1, "LDL"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 3
    {"key": "sugar", "title": "Gentle on Blood Sugar", "emoji": "📉", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Next, blood sugar. Most rye breads have a glycemic index, or GI, of forty-five to sixty-five. White bread sits at sixty-five to eighty-five.",
             {"say": "Next, blood sugar. Most rye breads have a glycemic index, or G I, of forty-five to sixty-five. White bread sits at sixty-five to eighty-five."}),
            ("H", "But the bigger difference is the overall glucose profile. The rise is spread over a longer time, it's less sharp, "
                  "and the drop that follows is gentler too.", {}),
        ], "els": [
            T("Glycemic index (GI)", 760, 170, 66, at=0, font="fredoka", weight=700, color="green"),
            {"type": "bars", "x": 250, "y": 340, "w": 1150, "row_h": 130, "max": 90, "unit": "", "rows": [
                {"label": "Rye bread", "value": 65, "text": "45-65", "color": "#B45309", "at": [0, "forty"]},
                {"label": "White bread", "value": 85, "text": "65-85", "color": "#EF4444", "at": [0, "White"]},
            ]},
            {"type": "pill", "x": 520, "y": 640, "text": "slower rise", "color": "green", "at": [1, "longer"]},
            {"type": "pill", "x": 860, "y": 640, "text": "less sharp", "color": "green", "at": [1, "sharp"]},
            {"type": "pill", "x": 1200, "y": 640, "text": "gentler drop", "color": "green", "at": [1, "gentler"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Swedish and Finnish intervention studies found that whole rye bread leads to a significantly lower insulin response than white wheat bread.", {}),
            ("H", "That matters for managing insulin resistance, and for the risk of type 2 diabetes.", {}),
            ("P", "Low and slow. Like a good barbecue, but for blood sugar.", {"mood": "happy"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 240, "w": 1000, "h": 180, "emoji": "🇫🇮", "title": "Lower insulin response",
             "body": "whole rye vs white wheat bread", "at": [0, "insulin"]},
            {"type": "card", "x": 720, "y": 500, "w": 1000, "h": 180, "emoji": "🩸", "title": "Why it matters",
             "body": "insulin resistance · type 2 diabetes risk", "at": [1, "matters"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Rye also beats wheat on fullness. The viscous fibers slow down how fast the stomach empties, so glucose is released slowly and steadily.", {}),
            ("H", "In studies, a breakfast with rye bread was linked to eating fewer calories over the next eight hours, "
                  "compared with a similar breakfast with white wheat bread.", {}),
            ("H", "To be clear, it doesn't burn fat. But that lasting fullness may help you eat a bit less overall. It's a tool in a broader plan, not a solution by itself.", {}),
            ("P", "Not a fat burner. Just a very persuasive breakfast.", {"mood": "smug"}),
        ], "els": [
            T("Stays with you", 720, 170, 72, at=0, font="fredoka", weight=700, color="green"),
            E("🍞", 420, 380, 150, at=[1, "breakfast"]),
            {"type": "arrow", "x1": 540, "y1": 380, "x2": 760, "y2": 380, "at": [1, "fewer"], "color": "orange"},
            T("fewer calories", 1020, 350, 50, at=[1, "fewer"], font="fredoka", weight=700, color="green"),
            T("over the next 8 hours", 1020, 415, 40, at=[1, "eight"], color="muted"),
            {"type": "card", "x": 720, "y": 640, "w": 1040, "h": 180, "emoji": "🚫", "title": "Not a fat burner",
             "body": "a tool in a broader plan", "at": [2, "burn"], "fill": "#FEF3C7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 4
    {"key": "gut", "title": "Gut Bugs and Minerals", "emoji": "🦠", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Back to those arabinoxylans. They aren't digested in the small intestine, so they reach the large intestine intact.",
             {"say": "Back to those arra-bino-zylans. They aren't digested in the small intestine, so they reach the large intestine intact."}),
            ("H", "There they feed beneficial bacteria, especially Bifidobacterium and Lactobacillus species.",
             {"say": "There they feed beneficial bacteria, especially Biffy-doe-bacterium and Lacto-bacillus species."}),
            ("H", "That boosts short-chain fatty acids, especially butyrate. It's the main fuel for the cells lining the colon, "
                  "and it's been linked to protection against inflammation in the gut.",
             {"say": "That boosts short chain fatty acids, especially bew-tir-ate. It's the main fuel for the cells lining the colon, "
                     "and it's been linked to protection against inflammation in the gut."}),
            ("P", "Feeding the good bugs. Rye bread runs a restaurant down there.", {"mood": "surprised"}),
        ], "els": [
            T("A prebiotic", 720, 170, 72, at=0, font="fredoka", weight=700, color="green"),
            E("🦠", 400, 360, 130, at=[1, "Bifidobacterium"]),
            T("Bifidobacterium", 400, 465, 40, at=[1, "Bifidobacterium"], font="fredoka", weight=600),
            E("🦠", 1040, 360, 130, at=[1, "Lactobacillus"]),
            T("Lactobacillus", 1040, 465, 40, at=[1, "Lactobacillus"], font="fredoka", weight=600),
            {"type": "card", "x": 720, "y": 680, "w": 1040, "h": 180, "emoji": "🔥", "title": "Butyrate",
             "body": "main fuel for the colon's lining", "at": [2, "butyrate"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Rye also has a high concentration of lignans. These are polyphenols that gut bacteria turn into enterolactone and enterodiol, "
                  "compounds with mild plant-estrogen activity.",
             {"say": "Rye also has a high concentration of lig-nans. These are polyphenols that gut bacteria turn into entero-lactone and entero-dial, "
                     "compounds with mild plant estrogen activity."}),
            ("H", "Epidemiological studies, mainly from the Nordic countries where people eat a lot of rye, "
                  "link high blood levels of enterolactone to a lower risk of breast and prostate cancer.",
             {"say": "Epidemiological studies, mainly from the Nordic countries where people eat a lot of rye, "
                     "link high blood levels of entero-lactone to a lower risk of breast and prostate cancer."}),
            ("H", "Keep in mind: these are population studies that show a link.", {}),
        ], "els": [
            {"type": "card", "x": 720, "y": 210, "w": 1040, "h": 180, "emoji": "🌿", "title": "Lignans",
             "body": "turned into enterolactone by gut bacteria", "at": [0, "lignans"]},
            {"type": "card", "x": 720, "y": 450, "w": 1040, "h": 180, "emoji": "📊", "title": "Nordic studies",
             "body": "high enterolactone, lower cancer risk", "at": [1, "Nordic"]},
            {"type": "pill", "x": 720, "y": 650, "text": "population studies: a link, not proof", "color": "orange", "at": [2, "population"]},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "And minerals. One hundred grams of whole rye flour has about one hundred fifteen milligrams of magnesium, "
                  "twenty-nine percent of the daily value, and three point seven milligrams of zinc, thirty-four percent.", {}),
            ("H", "Both are critical for enzyme function, hormone regulation and joint health.", {}),
            ("P", "Magnesium and zinc? Those are MY thing! Okay, I'll share the spotlight. A little.", {"mood": "surprised", "jump": True}),
        ], "els": [
            T("Whole rye flour, per 100 g", 760, 150, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "stat", "x": 500, "y": 400, "w": 480, "h": 300, "value": 115, "unit": " mg", "label": "magnesium", "emoji": "⚡", "at": [0, "magnesium"]},
            {"type": "stat", "x": 1060, "y": 400, "w": 480, "h": 300, "value": 3.7, "decimals": 1, "unit": " mg", "label": "zinc", "emoji": "🛡️", "at": [0, "zinc"]},
            {"type": "pill", "x": 500, "y": 610, "text": "29% DV", "color": "green", "at": [0, "twenty"]},
            {"type": "pill", "x": 1060, "y": 610, "text": "34% DV", "color": "green", "at": [0, "thirty"]},
            {"type": "pill", "x": 780, "y": 740, "text": "enzymes · hormones · joints", "color": "orange", "at": [1, "enzyme"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 5
    {"key": "catches", "title": "The Catches", "emoji": "⚠️", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Now the downsides. The big one: rye contains gluten. Its gluten protein is called secalin, rather than gliadin as in wheat.",
             {"say": "Now the downsides. The big one: rye contains gluten. Its gluten protein is called seck-a-lin, rather than glya-din as in wheat."}),
            ("H", "People with celiac disease must avoid rye bread completely. "
                  "People with non-celiac gluten sensitivity may react to rye less than they react to wheat.",
             {"say": "People with see-liac disease must avoid rye bread completely. "
                     "People with non see-liac gluten sensitivity may react to rye less than they react to wheat."}),
            ("P", "So it's not gluten-free. Good to clear that up.", {"mood": "worried"}),
        ], "els": [
            T("#1 It has gluten", 720, 170, 80, at=0, font="fredoka", weight=700, color="red"),
            {"type": "card", "x": 720, "y": 390, "w": 1000, "h": 180, "emoji": "🧬", "title": "Secalin",
             "body": "rye's version of wheat's gliadin", "at": [0, "secalin"]},
            {"type": "banner", "x": 720, "y": 600, "text": "Celiac: avoid completely", "color": "#DC2626", "at": [1, "celiac"]},
            {"type": "pill", "x": 720, "y": 760, "text": "gluten sensitivity: may react less than to wheat", "color": "orange", "at": [1, "sensitivity"]},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Two: phytic acid. Like any whole grain, rye has phytic acid, which reduces mineral absorption.",
             {"say": "Two: fy-tic acid. Like any whole grain, rye has fy-tic acid, which reduces mineral absorption."}),
            ("H", "Fermentation, like in rye sourdough, cuts phytic acid considerably. So sourdough rye breads are the best for bioavailability.",
             {"say": "Fermentation, like in rye sourdough, cuts fy-tic acid considerably. So sourdough rye breads are the best for bio-availability."}),
            ("P", "Phytic acid. My old nemesis. We seeds have it too, so no judgment here.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 230, "w": 1000, "h": 180, "emoji": "🔒", "title": "#2 Phytic acid",
             "body": "reduces mineral absorption", "at": 0},
            {"type": "card", "x": 720, "y": 490, "w": 1000, "h": 180, "emoji": "🫙", "title": "Sourdough cuts it",
             "body": "the best pick for absorbing minerals", "at": [1, "sourdough"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_S, "lines": [
            ("H", "Three: taste. Rye bread is dense, with an earthy, sour, strong flavor. That's a cultural drawback more than a nutritional one, "
                  "but it does put people off.", {}),
            ("H", "Four: sodium. Many commercial rye breads have four hundred to six hundred milligrams of sodium per hundred grams. "
                  "Read labels, choose breads with less salt, or bake your own.", {}),
            ("H", "And five: FODMAPs. Rye contains fructans, a type of FODMAP that can cause bloating, gas and discomfort in people with IBS. "
                  "They're advised to check with a dietitian before adding rye.",
             {"say": "And five: fod-maps. Rye contains fructans, a type of fod-map that can cause bloating, gas and discomfort in people with I B S. "
                     "They're advised to check with a dietitian before adding rye."}),
        ], "els": [
            {"type": "check", "x": 160, "y": 210, "w": 1300, "ok": False, "text": "#3 Dense, strong, sour taste", "at": [0, "Three"]},
            {"type": "check", "x": 160, "y": 350, "w": 1300, "ok": False, "text": "#4 Sodium: 400-600 mg per 100 g", "at": [1, "sodium"]},
            {"type": "check", "x": 160, "y": 490, "w": 1300, "ok": False, "text": "#5 Fructans: tricky with IBS", "at": [2, "fructans"]},
            {"type": "pill", "x": 810, "y": 650, "text": "read the label · ask a dietitian", "color": "orange", "at": [2, "dietitian"]},
        ]},
    ]},
    # ------------------------------------------------------------------ 6
    {"key": "loaf", "title": "Pick Your Loaf", "emoji": "🍞", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Not all rye bread is the same. Pumpernickel, which is one hundred percent rye, has a GI of about fifty to fifty-five, "
                  "and seven to eight grams of fiber per hundred grams. Nutritionally, it's the top pick.",
             {"say": "Not all rye bread is the same. Pumper-nickel, which is one hundred percent rye, has a G I of about fifty to fifty-five, "
                     "and seven to eight grams of fiber per hundred grams. Nutritionally, it's the top pick."}),
            ("H", "Rye sourdough, eighty to one hundred percent rye, has a GI of about forty-five to fifty-five, the same fiber, and less phytic acid. Also a favorite.",
             {"say": "Rye sourdough, eighty to one hundred percent rye, has a G I of about forty-five to fifty-five, the same fiber, and less fy-tic acid. Also a favorite."}),
            ("H", "Whole rye bread, seventy to one hundred percent rye, sits at about fifty-five to sixty-five, with six to seven grams of fiber. Very good.",
             {"say": "Whole rye bread, seventy to one hundred percent rye, sits at about fifty-five to sixty-five, with six to seven grams of fiber. Very good."}),
            ("H", "And light rye, only thirty to fifty percent rye, is about sixty-five to seventy, with four to five grams of fiber. "
                  "Easier to like, but less ideal.", {}),
        ], "els": [
            T("GI and fiber per 100 g", 760, 140, 56, at=0, font="fredoka", weight=600, color="green"),
            {"type": "check", "x": 160, "y": 270, "w": 1300, "ok": True, "text": "Pumpernickel: GI ~50-55, 7-8 g", "at": [0, "Pumpernickel"]},
            {"type": "check", "x": 160, "y": 400, "w": 1300, "ok": True, "text": "Rye sourdough: GI ~45-55, 7-8 g", "at": [1, "sourdough"]},
            {"type": "check", "x": 160, "y": 530, "w": 1300, "ok": True, "text": "Whole rye: GI ~55-65, 6-7 g", "at": [2, "Whole"]},
            {"type": "check", "x": 160, "y": 660, "w": 1300, "ok": False, "text": "Light rye: GI ~65-70, 4-5 g", "at": [3, "light"]},
        ]},
        {"pip": PIP_C, "lines": [
            ("H", "The rule of thumb: the darker and the more whole the loaf, the better.", {}),
            ("P", "Dark, dense and whole. Finally, a bread that gets me.", {"mood": "happy", "jump": True}),
        ], "els": [
            T("Darker + more whole = better", 960, 170, 76, at=0, font="fredoka", weight=700, color="green"),
        ]},
    ]},
    # ------------------------------------------------------------------ 7
    {"key": "howto", "title": "How to Eat It", "emoji": "🥑", "scenes": [
        {"pip": PIP_R, "lines": [
            ("H", "Rye bread goes especially well with raw tahini, smoked salmon, goat cheese, avocado and herbs. "
                  "These add healthy fats and protein to its complex carbs.", {}),
            ("H", "And add some vitamin C, like tomato or pepper. That increases how much iron you absorb from the rye.", {}),
        ], "els": [
            E("🐟", 300, 280, 130, at=[0, "salmon"]),
            T("smoked salmon", 300, 380, 38, at=[0, "salmon"], font="fredoka", weight=600),
            E("🧀", 620, 280, 130, at=[0, "goat"]),
            T("goat cheese", 620, 380, 38, at=[0, "goat"], font="fredoka", weight=600),
            E("🥑", 940, 280, 130, at=[0, "avocado"]),
            T("avocado", 940, 380, 38, at=[0, "avocado"], font="fredoka", weight=600),
            E("🌿", 1240, 280, 130, at=[0, "herbs"]),
            T("tahini, herbs", 1240, 380, 38, at=[0, "herbs"], font="fredoka", weight=600),
            {"type": "card", "x": 720, "y": 620, "w": 1040, "h": 180, "emoji": "🍅", "title": "Add vitamin C",
             "body": "tomato or pepper: more iron absorbed", "at": [1, "vitamin"], "fill": "#DCFCE7"},
        ]},
        {"pip": PIP_R, "lines": [
            ("H", "Can you eat it every day? Yes. One to three slices a day, about thirty to forty grams each, is a reasonable amount for most people.", {}),
            ("H", "All that fiber may cause some fermentation and bloating at first, so increase it gradually.", {}),
            ("H", "And rye versus whole wheat? In many ways whole rye wins, with more fiber, a lower insulin response, and more lignans. "
                  "But both are far better than white bread, and eating both is a good approach.",
             {"say": "And rye versus whole wheat? In many ways whole rye wins, with more fiber, a lower insulin response, and more lig-nans. "
                     "But both are far better than white bread, and eating both is a good approach."}),
            ("P", "Rye and wheat, best friends. Nobody tell white bread.", {"mood": "smug"}),
        ], "els": [
            {"type": "card", "x": 720, "y": 200, "w": 1040, "h": 170, "emoji": "🍞", "title": "1 to 3 slices a day",
             "body": "30 to 40 g each", "at": [0, "slices"]},
            {"type": "card", "x": 720, "y": 410, "w": 1040, "h": 170, "emoji": "🐢", "title": "Start slow",
             "body": "fiber can cause bloating at first", "at": [1, "gradually"], "fill": "#FEF3C7"},
            {"type": "card", "x": 720, "y": 620, "w": 1040, "h": 170, "emoji": "🤝", "title": "Rye and whole wheat",
             "body": "both far better than white bread", "at": [2, "both"], "fill": "#DCFCE7"},
        ]},
    ]},
    # ------------------------------------------------------------------ 8
    {"key": "outro", "title": "The Bottom Line", "emoji": "✅", "scenes": [
        {"pip": PIP_S, "lines": [
            ("H", "Let's wrap it up.", {}),
            ("H", "One: whole rye bread has six point two grams of fiber per hundred grams, more than wheat breads, mostly arabinoxylans.",
             {"say": "One: whole rye bread has six point two grams of fiber per hundred grams, more than wheat breads, mostly arra-bino-zylans."}),
            ("H", "Two: a moderate drop in LDL in Nordic studies, and a gentler blood sugar and insulin response.",
             {"say": "Two: a moderate drop in L D L in Nordic studies, and a gentler blood sugar and insulin response."}),
            ("H", "Three: it feeds good gut bacteria, and brings lignans, magnesium and zinc.",
             {"say": "Three: it feeds good gut bacteria, and brings lig-nans, magnesium and zinc."}),
            ("H", "Four: it has gluten, so it's out for celiac disease. Watch the sodium, and go slow if you have IBS. "
                  "And choose dark, whole or sourdough rye.",
             {"say": "Four: it has gluten, so it's out for see-liac disease. Watch the sodium, and go slow if you have I B S. "
                     "And choose dark, whole or sourdough rye."}),
        ], "els": [
            {"type": "check", "x": 160, "y": 200, "w": 1340, "ok": True, "text": "6.2 g fiber per 100 g", "at": 1},
            {"type": "check", "x": 160, "y": 340, "w": 1340, "ok": True, "text": "Kinder to LDL and blood sugar", "at": 2},
            {"type": "check", "x": 160, "y": 480, "w": 1340, "ok": True, "text": "Gut bugs, lignans, minerals", "at": 3},
            {"type": "check", "x": 160, "y": 620, "w": 1340, "ok": False, "text": "Gluten, sodium, FODMAPs", "at": 4},
        ]},
        {"pip": PIP_C, "lines": [
            ("P", "So rye bread: dark, dense, and quietly brilliant. Just like a certain pumpkin seed I know.", {"mood": "smug"}),
            ("H", "Subtle, Pip.", {}),
            ("P", "Seeds and grains, together forever!", {"mood": "happy", "jump": True}),
        ], "els": [
            {"type": "confetti", "at": 2},
        ]},
        {"pip": {"x": 1500, "y": 560, "size": 340}, "endscreen": True, "dur_min": 16, "lines": [
            ("H", "This video is for general education, not medical advice. For the full article, "
                  "visit wiseplate.blog. Thanks for watching!",
             {"say": "This video is for general education, not medical advice. For the full article, "
                     "visit wise plate dot blog. Thanks for watching!"}),
            ("P", "Bye! Remember: the darker, the better!", {"mood": "happy", "wave": True}),
        ], "els": [
            {"type": "logo", "x": 330, "y": 230, "size": 150, "at": 0},
            T("wiseplate.blog", 450, 230, 76, at=0, font="fredoka", weight=700, color="green", anchor="l"),
            T("Full article: wiseplate.blog/en/food/rye-bread", 760, 350, 38, at=[0, "article"], color="muted"),
            T("Not medical advice", 760, 410, 34, at=0, color="muted"),
            {"type": "endslot", "x": 470, "y": 700, "w": 620, "h": 350, "at": [0, "Thanks"]},
            {"type": "endslot", "x": 1100, "y": 700, "w": 0, "h": 0, "at": [0, "Thanks"], "subscribe": True},
        ]},
    ]},
]
