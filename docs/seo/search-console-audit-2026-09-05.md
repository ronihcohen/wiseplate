# Search Console content audit — 2026-09-05

Changes prepared for review against the current `master` of `wiseplate.blog`; not deployed. This public record deliberately excludes private Search Console metrics, query rows and inspection links. Detailed evidence and the private report are in the existing ignored `google/` directory.

## Evidence and decisions

The audit compared stable 28-day and 90-day windows ending 2026-09-02, including previous periods and a year-earlier check. Search Console showed growth before these edits; that growth is not an outcome of this work. Returned queries are incomplete, and country/device differences make a single site-wide CTR benchmark misleading. The year-earlier response did not support a useful seasonal comparison.

Five pages had identifiable opportunities to answer existing search intent more directly:

| Page | Change |
|---|---|
| `content/food/greek-yogurt.md` | Definition and comparison with regular yogurt moved near the opening; description clarified; nutrition records made comparable and product differences qualified. Existing SEO title retained. |
| `content/food/pumpkin-seeds.md` | Practical disadvantages and serving context moved early; title and description aligned; mixed nutritional preparations corrected using one roasted, unsalted, shelled-seed record. |
| `content/food/shrimp.md` | Hebrew synonym added to titles; cooked protein and calorie answer made explicit; table moved earlier; micronutrient sources distinguished. |
| `content/food/chickpeas.md` | Direct carbohydrate/protein answer and distinction between chickpea grains and hummus spread; inaccurate calorie percentages removed. |
| `content/compare/red-green-black-lentils.md` | English-name table moved early, translation FAQ added and search title shortened. |

`content/food/_index.md` adds contextual links to the relevant foods and comparison. Existing URLs and the targeted articles' original heading IDs are retained. Kefir's article and metadata remain unchanged because the evidence did not identify a comparable content problem there.

The section template now suppresses the empty-state message when child sections exist. Collection structured data follows visible child-section and article cards in the same order. Article bylines distinguish publication from a later update date, consistent with structured dates.

## Sources and limits

Nutrition corrections use [USDA Greek yogurt](https://fdc.nal.usda.gov/food-details/170903/nutrients), [regular yogurt](https://fdc.nal.usda.gov/food-details/171284/nutrients), [roasted pumpkin seeds](https://fdc.nal.usda.gov/food-details/170557/nutrients), [cooked shrimp](https://fdc.nal.usda.gov/food-details/175180/nutrients), [the separately identified shrimp micronutrient record](https://fdc.nal.usda.gov/food-details/171971/nutrients) and [cooked chickpeas](https://fdc.nal.usda.gov/food-details/173757/nutrients). These represent specified foods, not every retail product. This was not a comprehensive medical review of all site content.

Sampled URL inspections reported indexing allowed, successful fetches and matching canonicals. A stale sitemap download timestamp does not establish an indexing failure, and its deprecated indexed-count field was not treated as the site's indexed-page count. An empty search-appearance response likewise does not prove rich results are absent.

Recipe localization was separately requested during this work. Its scope and sources are recorded in [the recipe review](../content/recipe-localization-2026-09-05.md); those changes are not presented as findings from Search Console. The initial checkout lacked recipe photos. Before opening the PR, the branch was rebased onto `9963d69`, retaining the recipe images and favicon updates already merged upstream. No images or ratings are added by this PR; rendered image metadata is checked after integration. Search Console outcomes remain unmeasured.

## Verification and follow-up

Final build and acceptance results are recorded below after validation. No indexing request, sitemap resubmission or deployment has been performed.

After deployment, record the deployed commit, deployment time and confirmed recrawl separately. Compare equivalent stable 28-day windows, retaining the same query/page cohort and Israel/mobile versus Israel/desktop filters. Read clicks, impressions, CTR and position together, alongside page totals and broader site movement. Small samples may require a longer observation period. No ranking improvement, traffic gain or business conversion is claimed from these unpublished changes.

### Final local acceptance — 2026-09-05

- After integration with master `9963d69`, CI-pinned Hugo 0.146.0 production/minified build passed, with destination cleanup.
- All 50 upstream recipe images are retained in front matter, emitted in Recipe JSON-LD and resolve to existing static files; favicon assets are unchanged.
- All 553 generated HTML pages have one H1, one canonical and parseable JSON-LD.
- All 50 Recipe objects match source ingredient and instruction counts, yield, total time and modification date; each recipe retains FAQ structured data and has a local-ingredient alternatives section.
- All 336 sitemap URLs resolve. No broken internal path or fragment targets were found. Original heading IDs from the initial audit build are retained in the reviewed page trees.
- All 10 CollectionPage lists match visible cards in count and order. All 261 Article/Recipe bylines match structured publication/modification dates.
- Sampled desktop and mobile views were inspected for Hebrew layout, descriptions and date labels, including the revised amba page. This is visual sampling, not a performance or accessibility certification.
- `git diff --check` passed. Private Search Console evidence and the detailed private report remain ignored by Git.

Prepared as a pull request; no merge or deployment has been performed. Changes in analytics cannot yet be attributed to this work.
