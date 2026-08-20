# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Wise Plate** is a Hugo-based static site — a Hebrew-language scientific knowledge base covering nutrition, supplements, and sports performance. All content is in Hebrew (`languageCode = 'he'`).

## Commands

```bash
hugo                    # Build site → outputs to ./public/
hugo server -D          # Dev server with drafts at http://localhost:1313
hugo new content/<path> # Scaffold a new content file from archetype
```

No package.json, Makefile, or other build tooling — pure Hugo.

## Architecture

### Content Sections

| Directory | Purpose |
|---|---|
| `content/food/` | Individual food and ingredient articles (~162 files) |
| `content/food/supplements/` | Vitamins, minerals, and performance supplements (~30 files) |
| `content/compare/` | Side-by-side comparisons of related foods/nutrients (~17 files) |
| `content/run/` | Running gear and technique articles (~5 files) |

### Article Structure

All articles follow a consistent pattern:

**Front matter** (YAML):
```yaml
---
title: "Hebrew title"           # the H1/nav label
seo_title: "Hebrew title: ..."  # optional; overrides <title> only
date: 2024-01-01T00:00:00+02:00
lastmod: 2024-01-01T00:00:00+02:00  # optional
tags: ["tag1", "tag2"]
featured_image: ""
description: "Brief Hebrew summary"  # becomes <meta name=description>
---
```

`seo_title` is a custom param rendered by `layouts/partials/head.html`. It lets
an article target the phrasing people search for without changing the visible
H1. Prefer it over contorting `title`.

**Body structure:**
1. H2 title (repeats front matter title)
2. Opening context paragraph — for a food, name it in English and note any
   common Hebrew variant (e.g. קפיר/כפיר, שרימפס/חסילונים)
3. Nutrition table (`### ערך תזונתי`)
4. `### יתרונות` (Advantages) — bullet points with citations/reasoning
5. `### חסרונות` (Disadvantages/Risks) — balanced counterpoints
6. Optional: comparison tables, dosage guidelines, cooking tips
7. `### שימוש מעשי` and `### סיכום`
8. `### שאלות ותשובות נפוצות` — see the FAQ format note below

### FAQ blocks feed FAQPage schema — format matters

`layouts/partials/head.html` parses Q&A pairs out of the prose and emits
`FAQPage` JSON-LD. It matches two shapes, and in both the answer must sit on
the **immediately following line** — a blank line between them silently drops
the pair from the schema:

```markdown
**שאלה: ...?**
תשובה: ...
```

Two or more pairs are required before any schema is emitted. 141 articles
currently rely on this.

### Internal Linking

Articles cross-reference each other using Hugo relative paths, e.g. `/food/supplements/selenium/`. Food articles often link into the supplements sub-section.

Two topics deliberately live in both trees: the **food** page covers the
dietary/culinary angle and the **supplement** page covers doses and clinical
use. Keep their titles distinct and cross-link them both ways, or they compete
for the same queries:

- `/food/iron/` (ברזל) ↔ `/food/supplements/iron/` (תוסף ברזל)
- `/food/turmeric/` (כורכום) ↔ `/food/supplements/turmeric/` (תוסף כורכומין)

### Layouts

There is no theme; `layouts/` holds the site's own templates (9 files):
`_default/baseof.html`, `_default/single.html`, `_default/list.html`,
`index.html`, `sitemap.xml`, and partials (`head.html`, `nav.html`,
`footer.html`, `article-card.html`).

`head.html` is where the SEO surface lives — `<title>`/`seo_title`, meta
description, canonical, robots, Open Graph, and JSON-LD for Article,
CollectionPage, BreadcrumbList and FAQPage. Tag pages listing fewer than
`min_term_pages` articles are noindexed there and excluded from the sitemap.

`public/` is generated output and should not be edited directly. Deploys run
from `.github/workflows/hugo.yml`.
