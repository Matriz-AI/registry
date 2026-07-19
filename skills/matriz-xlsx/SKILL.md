---
name: matriz-xlsx
description: Create, edit, analyze, and validate XLSX spreadsheets. Use when the task involves Excel workbooks, formulas, tables, charts, budgets, models, data cleaning, spreadsheet formatting, workbook audit, or visual and formula quality assurance.
---

# XLSX workflows

Inspect the workbook before editing it. Preserve existing formulas, named ranges, tables, conditional formats, and chart dependencies unless a change requires an update.

## Build and edit

- Separate inputs, calculations, and outputs. Use formulas for derived values rather than hard-coding computed results.
- Store dates and numbers as typed spreadsheet values with appropriate number formats.
- Use clear sheet names, descriptive headers, and a consistent structure that another person can audit.
- Extend tables, formulas, validations, conditional formats, and chart ranges when adding data to an existing model.
- Prefer small, readable formulas and helper cells over opaque nested expressions.

## Analyze and verify

1. Inspect representative cells for values, formulas, references, and number formats.
2. Scan for formula errors such as `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, and `#N/A`.
3. Recalculate with an available spreadsheet engine when possible.
4. Render each changed worksheet or export it to PDF for visual review; fix clipped headers, unreadable columns, broken charts, and inconsistent formatting.

## Safety

- Do not replace formulas with values unless the user explicitly requests a static export.
- Do not modify hidden sheets, workbook protection, external connections, or macros without explicit approval.
- For financial models, make assumptions visible, cite source data, and preserve an auditable calculation trail.
