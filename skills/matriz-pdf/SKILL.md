---
name: matriz-pdf
description: Read, create, edit, merge, split, annotate, redact, extract, and validate PDF files. Use when a task involves PDF documents, forms, page manipulation, text or table extraction, visual review, secure redaction, or publication-ready PDF output.
---

# PDF workflows

Keep originals immutable and work from copies. Use `pypdf` for document structure, `pdfplumber` for extraction, and `reportlab` for new PDF generation when appropriate.

## Choose the operation

- Read or extract: inspect page count, text, metadata, links, annotations, and tables before making conclusions.
- Create: build a layout with explicit page geometry, type hierarchy, margins, and page numbering.
- Edit: merge, split, rotate, reorder, stamp, or annotate pages without rasterizing the whole document unless necessary.
- Forms: inspect field names and types before filling values. Preserve unrelated fields and calculate appearances when needed.
- Redact: remove the underlying content and related metadata; placing a rectangle over text is never a valid redaction.

## Verification gate

1. Check page count, metadata, and intended structural changes with a PDF parser.
2. Render every changed page to PNG using Poppler or an equivalent renderer.
3. Inspect visual output for clipped text, incorrect rotation, broken fonts, layer artifacts, unreadable tables, and incorrect page order.
4. For extracted data, cross-check representative values against the rendered page rather than trusting text extraction alone.

## Delivery rules

- Use descriptive final filenames and preserve the requested PDF version.
- Remove temporary page images and working copies unless the user asks to retain them.
- State if a signature, encryption setting, or form appearance could not be preserved exactly.
