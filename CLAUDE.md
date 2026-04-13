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
| `content/food/` | Individual food and ingredient articles (~184 files) |
| `content/food/supplements/` | Vitamins, minerals, and performance supplements (~29 files) |
| `content/compare/` | Side-by-side comparisons of related foods/nutrients (~19 files) |
| `content/run/` | Running gear and technique articles |

### Article Structure

All articles follow a consistent pattern:

**Front matter** (YAML):
```yaml
---
title: "Hebrew title"
date: 2024-01-01T00:00:00+02:00
tags: ["tag1", "tag2"]
featured_image: ""
description: "Brief Hebrew summary"
---
```

**Body structure:**
1. H2 title (repeats front matter title)
2. Opening context paragraph
3. `### יתרונות` (Advantages) — bullet points with citations/reasoning
4. `### חסרונות` (Disadvantages/Risks) — balanced counterpoints
5. Optional: comparison tables, dosage guidelines, cooking tips
6. Practical conclusions

### Internal Linking

Articles cross-reference each other using Hugo relative paths, e.g. `/food/supplements/selenium/`. Food articles often link into the supplements sub-section.

### No Theme/Layouts

`hugo.toml` specifies no theme and `layouts/` is empty — Hugo's built-in default rendering is used. `public/` is the generated output and should not be edited directly.
