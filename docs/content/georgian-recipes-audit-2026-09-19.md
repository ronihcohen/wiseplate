# Georgian recipe collection audit — 2026-09-19

## Scope

This audit covers `content/recipes/georgia/`: one Hebrew collection page and exactly ten recipes. It records selection rationale, source checks, Israeli substitutions, kosher/safety decisions, and calorie arithmetic. Values are editorial estimates, not laboratory measurements.

## Selection and source verification

The official Georgian National Tourism Administration food guides identify khinkali and khachapuri as national/signature foods; its regional guide distinguishes common Imeretian khachapuri from the popular boat-shaped Ajarian version. Its “Top 11” guide includes khinkali, Ajarian khachapuri, lobio and chakapuli and describes the latter as lamb/veal with tarragon, sour plums and white wine. The official cuisine and ritual-food guides also describe chakhokhbili, walnut kharcho, pkhali and walnut vegetable assortments.

Primary/official references:

* Georgia Travel, “Georgian Cuisine”: https://georgia.travel/georgian-cuisine
* Georgia Travel, “Why Georgia — Delicious Cuisine”: https://georgia.travel/why-georgia-delicious-cuisine
* Georgia Travel, “Top 11 Georgian Food”: https://georgia.travel/top-eleven-georgian-food
* Georgia Travel, “Khinkali”: https://georgia.travel/khinkali
* Georgia Travel, “Chakapuli”: https://georgia.travel/chakapuli
* Georgia Travel, “Chakhokhbili”: https://georgia.travel/chakhokhbili
* Georgia Travel, “Georgian Ritual Foods”: https://georgia.travel/georgian-ritual-foods
* Georgia Travel, “Imeretian Khachapuri”: https://georgia.travel/imeretian-khachapuri
* Georgia Travel, “Khachapuri — True Symbol of Georgian Cuisine”: https://georgia.travel/get-a-taste-of-khachapuri
* Georgia Travel, “Pkhali — Georgia's Versatile Vegan Appetiser” (also documents walnut eggplant rolls): https://georgia.travel/pkhali-georgias-versatile-vegan-appetiser
* Georgia Travel, “A Guide to Vegetarian Georgian Food”: https://georgia.travel/a-guide-to-vegetarian-georgian-food
* Georgia Travel, “Churchkhela”: https://georgia.travel/churchkhela
* Georgia Travel, “Tatara”: https://georgia.travel/tatara
* Georgia Travel, “Mingrelian Walnut Kharcho”: https://georgia.travel/mingrelian-walnut-kharcho

Additional technique cross-checks:

* JDC-Eshel, *Cooking Up a Story*, includes a Georgian-Jewish khinkali contribution and supports the dish's Israeli community context: https://www.thejoint.org.il/wp-content/uploads/2020/09/Cooking-up-a-story.pdf
* Saveur, “Georgian Beef Kharcho with Walnuts”, used to cross-check the documented soup/stew spectrum and walnut technique: https://www.saveur.com/recipes/georgian-beef-kharcho-recipe/
* USDA FoodData Central, generic ingredient energy references: https://fdc.nal.usda.gov/
* Israeli packaged-food labels should override generic database values when a specific brand is used.

The ten selected dishes are: Ajarian khachapuri, Imeretian khachapuri, khinkali, lobio, badrijani nigvzit, spinach pkhali, chakhokhbili, chakapuli, kharcho and churchkhela. This gives recognizable restaurant foods plus vegetable, legume, soup, stew and sweet coverage without relying on pork or obscure offal.

## Israeli availability and substitutions

* Imeretian cheese/sulguni: use real sulguni from Georgian delis when available. The documented supermarket blend is dry mozzarella + feta + ricotta, which approximates stretch, salt/acidity and moisture but is explicitly described as a substitute.
* Tkemali/tklapi: imported tkemali is sold in Georgian/Eastern European delis. Sour green plums plus lemon are the seasonal substitute. Tomato alone is not presented as equivalent.
* Khmeli suneli: available in spice shops; the recipes name coriander/fenugreek components so readers are not dependent on a variable commercial mix.
* Tarragon, walnuts, coriander, parsley, eggplant, red beans, grape juice, lamb and beef are ordinary Israeli market/supermarket ingredients.

## Kosher and food-safety review

* Both khachapuri recipes are clearly labeled dairy; all meat dishes contain no dairy. The collection tells kosher readers not to combine them in one meal and to verify certification on cheese, wine and imported sauces.
* Khinkali uses beef and lamb, not the pork blends found in some non-Jewish versions. Ground meat is cooked to 71°C.
* Chicken is cooked to 74°C. Runny egg is flagged as unsuitable for pregnant people, small children and immunocompromised diners.
* Walnut allergens are explicitly called out in pkhali, badrijani, lobio, kharcho and churchkhela.
* Churchkhela gives humidity, clean hanging, mold and discard guidance; no visual-only guarantee of safety is made.

## Calorie calculations

Energy was calculated from raw ingredient weights and divided by declared yield. Rounded values reflect label/database variation. Spices and herbs under about 50 kcal per full recipe are included in the rounding margin unless listed.

| Recipe | Approximate energy calculation | Published value |
|---|---|---:|
| Ajarian khachapuri | flour 1,820 + sugar 46 + oil 265 + mozzarella 1,120 + feta 530 + ricotta 260 + eggs 288 + butter 287 = 4,616 kcal / 4 | 1,150 |
| Imeretian khachapuri | flour 2,184 + yogurt 120 + oil 265 + mozzarella 1,260 + feta 663 + ricotta 348 + egg 72 + butter 143 = 5,055 / 6 | 840 |
| Khinkali | flour 2,548 + beef 1,290 + lamb 846 + onion 80 = 4,764 / 8 | 600 |
| Lobio | dry beans 1,665 + walnuts 654 + oil 265 + onion/seasoning about 200 = 2,784 / 6 | 465 |
| Badrijani | eggplant 375 + absorbed oil 1,061 + walnuts 1,962 + onion/pomegranate about 165 = 3,563 / 8 | 445 |
| Spinach pkhali | spinach 276 + walnuts 1,962 + onion/pomegranate about 125 = 2,363 / 8 | 295 |
| Chakhokhbili | skinless chicken thighs about 2,700 + oil 265 + onions 160 + tomatoes 216 + aromatics = about 3,360 / 6 | 560 |
| Chakapuli | trimmed lamb about 3,000 + wine 310 + plums 230 + herbs/aromatics about 120 = 3,660 / 6 | 610 |
| Kharcho | beef 2,250 + rice 720 + walnuts 1,308 + oil 265 + onion/tkemali/tomato about 220 = 4,763 / 8 | 595 |
| Churchkhela | walnuts 3,270 + 80% of grape-juice/flour batter (1,688) = 4,958 / 20 | 250 |

Key uncertainty ranges:

* Meat cut and fat percentage: typically ±10%–20%.
* Cheese brand and fat percentage: ±8%–15%.
* Eggplant oil absorption: largest uncertainty; the recipe publishes the assumed 120 g and a baked comparison.
* Churchkhela coating retention: assumed 80%; weighing finished dry pieces is more accurate.

## Text QA checklist

* Exactly 10 recipes and one `_index.md`.
* Every page has title, SEO title, description, tags, featured image, cuisine/category, ISO-8601 times, numeric yield and calories.
* Every recipe includes overview, timing/yield/difficulty, ingredients, substitutions, numbered method, nutrition table, tips, summary, internal collection links and four FAQs.
* Hebrew naming is consistent: חצ'פורי, חינקלי, לוביו, פחאלי, בדריג'ני ניגווזית, צ'אחוחבילי, צ'אקאפולי, חרצ'ו, צ'ורצ'חלה.
* No recipe mixes dairy and meat. Alcohol, allergens, ground-meat/chicken temperatures and runny-egg risk are addressed.
* Featured-image paths are unique and use 1200×630 WebP project assets.
