# Yemenite recipe verification — 2026-09-19

## Scope and cultural checks

Ten Hebrew recipes were prepared under `/recipes/yemen/`: Yemenite chicken soup, jachnun, kubaneh, malawach, lahuh, saluf, zhug, hilbeh, asid and zalabia. They represent Jewish-Yemenite cooking familiar in Israel without claiming that Sana'a, Aden, Shar'ab and rural traditions are identical. Israeli commercial conventions are labeled: margarine in pareve jachnun, supermarket hawaij blends, domestic ovens instead of a tabun, and baking-paper methods.

Dish identity and techniques were checked primarily against the ANU Museum FOODISH Yemenite community recipes and the Association for Society and Culture, Documentation and Research (Yemenite Jewish Heritage). FOODISH's museum recipes document jachnun stretching and overnight baking, kubaneh with samneh/clarified butter, malawach lamination, family asid, chicken soup, and everyday savory zalabia. The heritage association's documentation was used for the breadth and names of Yemenite breads. Recipes were normalized to metric weights and safe domestic cooking instructions.

## Nutrition method

Calories use raw ingredient weights and typical USDA FoodData Central values, divided by the declared yield and rounded. Flour: 364 kcal/100 g; semolina: 360; sugar: 387; butter/ghee: about 717; margarine: about 717; oil: 884; fenugreek seed: 323. Chicken soup assumes about 800 g edible cooked-equivalent meat and skin from 1.4 kg bone-in thighs/drumsticks. Herbs, vegetables and spices are counted when material. Water and salt are zero.

| Recipe | Approx. kcal per full recipe | Yield | Published kcal | Main uncertainty |
|---|---:|---:|---:|---|
| Hilbeh | 323 | 20 tbsp | 15 | final whipped volume and drained solids |
| Zhug | 1,225 | ~30 tbsp | 40 | oil retained on herbs/container |
| Lahuh | 2,350 | 12 | 195 | pan oil |
| Zalabia | 3,900 | 18 | 215 | assumes 120 g frying oil absorbed |
| Kubaneh | 3,825 | 12 | 320 | butter left on bowl/surfaces |
| Saluf | 3,175 | 10 | 320 | flour used for handling |
| Yemenite chicken soup | 2,760 | 8 | 345 | edible chicken yield and skin |
| Asid | 2,170 | 6 | 360 | served sauce/butter excluded |
| Malawach | 4,670 | 10 | 470 | pan fat and lamination losses |
| Jachnun | 6,220 | 12 | 520 | spread fat; accompaniments excluded |

These are recipe estimates, not laboratory measurements. Package labels should replace generic values for a specific margarine or flour. Egg, grated tomato, zhug and other optional accompaniments are not included unless the recipe says otherwise.

## Israeli availability and safety

All ingredients are sold in ordinary Israeli supermarkets or neighborhood spice shops: white and whole-wheat flour, semolina, dry yeast, butter/ghee or margarine, chicken pieces, potatoes, cilantro, parsley, green chilies, fenugreek powder and hawaij for soup. Every overnight dough recipe specifies an oven-safe covered pot and a low oven, not an improvised hotplate setup. Chicken is cooked to at least 74°C in the thickest piece; cooked food is refrigerated within two hours. Frying recipes specify gradual loading and oil around 170–175°C.

## SEO image production

Eleven original images were generated with the built-in image generator, one call per final asset, and saved as optimized 1200×630 WebP files. The shared prompt set used the `photorealistic-natural` taxonomy and specified: recipe/collection SEO feature image; authentic dish-specific form and ingredients; wide landscape editorial food framing; warm natural side-window light; realistic homemade texture; no people, text, logos or watermarks; and explicit exclusions that prevent confusion with Moroccan, Georgian or generic commercial food styling. Each dish prompt added its defining visual constraint — open fermentation holes for lahuh, cylinders and accompaniments for jachnun, pull-apart crumb for kubaneh, coarse herbs for zhug, aerated foam for hilbeh, and flat irregular fried rounds for savory zalabia. A contact-sheet review confirmed distinct subjects, plausible textures and consistent framing.

## Validation

- Hugo `0.146.0` production build completed successfully: 1,032 pages.
- Exactly 10 recipe Markdown files and 10 dish images are present, plus the collection page and collection image.
- Every recipe has all required frontmatter fields, eight content sections, a nutrition table and four FAQ entries.
- Rendered pages contain both Recipe and FAQPage JSON-LD.
- All local content links resolve; all 11 images are sRGB WebP at 1200×630.

## Sources

- https://foodish.anumuseum.org.il/recipe/yemenite-jachnun/
- https://foodish.anumuseum.org.il/recipe/kubaneh/
- https://foodish.anumuseum.org.il/recipe/%D7%9E%D7%9C%D7%90%D7%95%D7%95%D7%97/
- https://foodish.anumuseum.org.il/community-recipe/jewish-yemenite-aseed/
- https://foodish.anumuseum.org.il/community-recipe/grandmas-yemenite-chicken-soup/
- https://foodish.anumuseum.org.il/community-recipe/yemanite-zalabiyeh/
- https://foodish.anumuseum.org.il/recipe/spice-mix-for-yemeni-soup/
- https://teman.org.il/content/9954
- https://fdc.nal.usda.gov/
- https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/safe-temperature-chart
