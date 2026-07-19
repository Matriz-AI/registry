---
name: matriz-pptx
description: Create, edit, review, and validate PowerPoint PPTX presentations. Use when the task involves PowerPoint slides, presentation templates, speaker-facing decks, layouts, charts, slide notes, visual storytelling, or slide rendering and quality assurance.
---

# PPTX workflows

Start by identifying the audience, purpose, and visual source. Preserve an existing template whenever one is supplied; otherwise define one deliberate visual system before building slides.

## Build and edit

- Use PowerPoint-native text, shapes, tables, charts, and images. Keep important content editable.
- Establish slide size, margins, title hierarchy, body type scale, and a restrained color system before authoring.
- Make each slide communicate one main idea. Prefer concise labels and visuals over dense prose.
- For template edits, retain the template's layout, font roles, spacing, footer elements, and color treatment unless the user asks to restyle.
- Use speaker notes only when requested. Do not expose internal planning notes on visible slides.

## Charts and assets

- Keep chart values traceable to supplied data and label units, dates, and sources clearly.
- Use images with suitable aspect ratio and crop intentionally. Do not reuse copyrighted visuals without permission.
- Add diagrams only when they make a relationship easier to understand than a short list.

## Verification gate

1. Inspect slide structure for missing titles, placeholders, inaccessible contrast, and unexpected overflow.
2. Render every slide to images and inspect them at full size.
3. Fix overlap, clipping, awkward wrapping, unbalanced composition, and chart label issues before delivery.
4. Preserve the source deck and export a separate result unless an in-place edit is requested.

## Bundled scripts

- `scripts/inspect_pptx.py`: report slide size, visible text, shape counts, and notes.
- `scripts/add_slide.py`: append an editable title-and-body slide.
- `scripts/validate_pptx.py`: flag empty slides and off-canvas shapes.
- `scripts/clean_pptx.py`: remove notes and/or review comments only on explicit request.
- `render_pptx.py`: create slide PNGs (and optionally a PDF), using LibreOffice first and Microsoft PowerPoint as a local fallback.
