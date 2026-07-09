---
name: officecli
description: Use when creating, inspecting, validating, or modifying Office documents in .docx, .xlsx, or .pptx format, especially for CLI-based Word, Excel, or PowerPoint automation, rendered previews, document issues, structured JSON, or Office QA.
---

# OfficeCLI

## Overview

OfficeCLI is the project adapter for command-line work on Word, Excel, and PowerPoint files. Use it as a thin wrapper around the external `officecli` binary; do not clone or vendor the OfficeCLI source tree into this repository.

Canonical upstream references:
- `https://github.com/iOfficeAI/OfficeCLI`
- `https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/SKILL.md`

## When to Use

- A task creates, reads, edits, validates, or visually checks `.docx`, `.xlsx`, or `.pptx`.
- The user asks for Word, Excel, PowerPoint, Office, DOCX, XLSX, PPTX, slides, workbook, spreadsheet, deck, rendered preview, screenshot, or formatting QA.
- A document needs structured inspection with `get --json`, selector search with `query`, or a render/check loop with `view html`, `view screenshot`, `view issues`, or `validate`.

## When NOT to Use

- The main deliverable is LaTeX, Markdown, Python code, PDF paper parsing, or a web app.
- A spreadsheet task needs heavy pandas/openpyxl data modeling; use `xlsx` first and OfficeCLI only for Office-native inspection/QA.
- A slide design task needs the existing bespoke `pptx` workflow; OfficeCLI can still be used for preview, DOM edits, and validation.
- `officecli` is missing and the user has not approved installation/network access.

## Quick Reference

| Need | Command pattern |
|---|---|
| Check availability | `officecli --version` |
| Discover syntax | `officecli help`, `officecli help docx paragraph`, `officecli help xlsx cell`, `officecli help pptx shape` |
| Create | `officecli create file.docx` / `file.xlsx` / `file.pptx` |
| Read outline/text | `officecli view file.pptx outline`, `officecli view file.docx text` |
| Inspect structure | `officecli get file.docx / --depth 2 --json` |
| Search | `officecli query file.docx 'paragraph:contains("draft")'` |
| Modify | `officecli set file.docx / --find draft --replace final` |
| Add content | `officecli add file.pptx / --type slide --prop title="Title"` |
| Verify | `officecli validate file.docx`, `officecli view file.docx issues` |
| Save/release | `officecli close file.docx` |

## Core Pattern

1. **Check the binary first.** Run `officecli --version`. If it is unavailable, stop and tell the user. Only install after explicit approval for network/system changes. On Windows, prefer an official release or the upstream installer; do not run installer commands silently.
2. **Ask OfficeCLI for syntax.** When property names, value formats, selectors, or element types are uncertain, run `officecli help ...` instead of guessing.
3. **Use the highest safe layer.** Prefer read/inspect commands first, then DOM operations (`set`, `add`, `remove`, `move`, `query`, `get`). Use raw XML only when the DOM layer cannot express the edit.
4. **Respect project file rules.** Never write to `02_du-lieu-tho/` except by the project-approved intake/freeze workflow. Never write to `06_nop-bai/`. Put experiments and smoke tests in `scratch/`.
5. **Verify after edits.** Run `officecli validate <file>` and `officecli view <file> issues`. For visual deliverables, render with `view html` or `view screenshot` when available.
6. **Flush at boundaries.** For longer sessions, use `officecli open <file>` before a batch of edits and `officecli close <file>` before non-OfficeCLI tools read the file.

## Project Routing

- `.docx`: use OfficeCLI for protocol updates, issue checks, rendered previews, and targeted text/format edits. If OfficeCLI is unavailable, fall back to zip/XML or Python only after noting the fallback.
- `.xlsx`: use OfficeCLI for workbook inspection, cell edits, validation, and visual QA. Use `xlsx` for pandas/openpyxl formula-heavy work.
- `.pptx`: use OfficeCLI for outline extraction, shape inspection, DOM edits, and preview/validation. Use `pptx` for full deck design workflows when its templates/scripts are a better fit.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Guessing a property name | Run `officecli help <format> <element>` first. |
| Editing a frozen raw-data file | Copy to an allowed analysis location before modifying. |
| Leaving resident state unflushed | Run `officecli close <file>` before using Python, Word, LibreOffice, git diff artifacts, or delivery steps. |
| Treating OfficeCLI as installed everywhere | Check `officecli --version` at the start of each Office task. |
| Using raw XML too early | Try `get`, `query`, `set`, `add`, and `remove` first. |

## Red Flags

- An install command would download or execute code without user approval.
- A command targets `02_du-lieu-tho/` for modification or `06_nop-bai/` for any non-final output.
- The task needs AHP, TOPSIS, Likert, or literature synthesis; route to the project-specific skill instead.
- Validation or issue checks fail after an edit; fix or report the failure before declaring completion.
