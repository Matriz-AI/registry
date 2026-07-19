---
name: matriz-docx
description: Create, edit, review, compare, and validate Word DOCX documents. Use when the task involves DOCX files, Word templates, reports, proposals, contracts, forms, comments, tracked revisions, document metadata, or layout-sensitive Word output.
---

# DOCX workflows

Use a task-local working copy. Preserve the original file unless the user explicitly asks for an in-place change.

## Choose the workflow

- Create: use `python-docx` for paragraphs, styles, tables, headers, footers, images, and section settings.
- Edit: inspect existing styles and apply the smallest possible change. Preserve unrelated content, numbering, and document properties.
- Review: extract text and structure first; use an OOXML-level change only when the high-level library cannot represent the requested feature.
- Compare or redline: keep both source documents, state the comparison scope, and verify the result structurally and visually.

## Authoring rules

- Use semantic headings and real numbered or bulleted lists; never simulate hierarchy with manual spaces or symbols.
- Set page size, margins, font hierarchy, table widths, and paragraph spacing deliberately.
- Use tables only for repeated comparable information. Let rows expand instead of clipping text.
- Keep source links, citations, and file metadata human-readable.
- For comments, revisions, fields, or content controls, inspect the document package before changing OOXML and retain every required relationship and content type.

## Verification gate

1. Reopen the produced DOCX and inspect headings, paragraphs, tables, headers, footers, and metadata.
2. Render it with LibreOffice in headless mode when available.
3. Inspect every rendered page for overflow, broken tables, missing glyphs, accidental page breaks, and header/footer drift.
4. Repeat after every layout-sensitive change. Deliver only the DOCX unless the user requests a PDF or preview.

## Safety

- Do not accept tracked changes, remove comments, scrub metadata, or redact text unless the user explicitly requests it.
- Treat visual redaction as insufficient. Remove sensitive content from document XML, comments, headers, footers, properties, and embedded objects before delivery.
