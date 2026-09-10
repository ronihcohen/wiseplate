# Search Console content-gap audit — 2026-09-04

## Scope and limitations

- Property: Wise Plate (`wiseplate.blog`)
- Search type: Google Web Search
- Stable 30-day window: 2026-08-03 through 2026-09-01
- The three trailing days were excluded to avoid incomplete Search Console data.
- Search Console provides top rows and does not guarantee a complete raw dataset. Detailed query counts are omitted from this public repository.

## Decision

The data did not justify a wholly new article. It revealed two cases where useful content already existed but did not clearly match the search language:

1. Searches about the benefits of cocoa were reaching the general food index instead of the existing cacao-nibs article.
2. The red, green and black lentil comparison received substantial visibility without clicks. Its strongest visible query asked for the English name of red/orange lentils, but that answer appeared late in the article.

Creating a second generic cocoa page would overlap heavily with the cacao-nibs article and could split relevance between two URLs. The safer response is to broaden and clarify the existing page.

## Changes

- Expanded the cacao-nibs page to cover the terminology and practical differences between cocoa powder, whole beans and nibs.
- Reframed its title, description, introduction and FAQ around the generic cocoa-benefits intent.
- Added a direct internal link from the food index to strengthen discovery of the page.
- Added the English names for orange/red lentils near the start of the comparison page and aligned its title, description and FAQ with that intent.

## Validation plan

After Google recrawls both pages and at least two stable weeks have accumulated:

- Compare impressions, clicks and CTR for each changed page with this 30-day baseline.
- Confirm that generic cocoa queries resolve to `/food/cacao-nibs/` rather than `/food/`.
- Check whether the lentil page retains first-page visibility for English-name queries while gaining clicks.
- Review query overlap before considering any separate cocoa article.
