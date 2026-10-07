# Search Console audit — 2026-10-07

Changes prepared for review on `claude/seo-tag-hubs-descriptions`; not deployed. Like the earlier audits, this public record leaves out Search Console metrics and query rows.

## Evidence and decisions

The export covers web search for the last 3 months, ending in early October. Most of that window comes before the September 4–5 snippet and content changes, so the export can't yet show whether those changes worked. The pages they targeted (shrimp, Greek yogurt, chickpeas, kefir, pumpkin seeds, sesame, lentil comparison) were therefore left alone.

This pass targets pages that have real search demand, have never been revised for it, and rank on page one or near it for a specific question that the page answered only in passing or not at all:

| Page | Change |
|---|---|
| `content/food/tofu.md` | The opening now states what tofu is made of in one sentence. FAQ pairs added for what it is made of and how much protein it has. |
| `content/food/pecans.md` | FAQ pairs added for calories per single nut and for disadvantages, both taken from the article's existing figures. |
| `content/food/mango.md` | FAQ pair added for sugar content per 100 g and per medium mango. |
| `content/food/red-meat.md` | FAQ pair added defining red meat and whether chicken or turkey count as red meat. |
| `content/food/cinnamon.md` | FAQ pair added for calories per teaspoon and per 100 g. |

Each new answer reuses numbers already in its article. The new pecan figure, about 1.5 g and 10 kcal per half, follows from the USDA serving of 1 oz = 19 halves.

The same branch also carries technical fixes found by auditing the built site. Tag hubs are now linked from articles, tag pages have their own descriptions, over-long or generic descriptions were tightened, and a tag-URL collision that sometimes corrupted a built page is fixed. Those fixes don't depend on the Search Console data.

## Follow-up

After deployment, compare equivalent 28-day windows for the pages above, against the same queries, and do the same for the September 4–5 pages once enough post-change data exists. No ranking or traffic gain is claimed.
