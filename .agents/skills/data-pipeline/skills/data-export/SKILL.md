---
name: data-export
description: Formats and writes finalized data to Excel (multi-sheet), CSV, or JSON. Configures frozen headers, auto-width columns, and formatting. Do not use to transform or aggregate data.
---
# Skill: Data Export

You are responsible for the final presentation and storage of the data. Your primary tool is the multi-sheet Excel writer, which creates professional, analyst-ready deliverables.

## Core Directives
1. **Separation of Concerns:** Do not alter the data (no math, no row-dropping) during this phase. Only format and write it.
2. **Standard Workbook Structure:** When generating an analytical Excel report, try to include the following sheets if the data is available: `summary`, `aggregated_data`, `cleaned_data`, `raw_data`, `data_dictionary`, `source_log`, `validation_report`.
3. **Professional Formatting:** Freeze the top row. Auto-adjust column widths. No decorative colors or styling unless explicitly requested by the user.

## Capabilities
All tools are executable CLI scripts. Run them with `--help` to view arguments.
- **`scripts/export_data.py`**: A robust Excel multi-sheet writer that takes multiple CSVs and compiles them into a single `.xlsx` workbook with proper formatting. (Also handles basic CSV/JSON conversion if needed).

## References
- `references/output_schema_template.md`: Guide for structuring final deliverables.
- `references/data_dictionary_template.md`: How to build a data dictionary sheet.
- `references/error_taxonomy.md`: Standard nomenclature for flagging data issues.
- `references/data_quality_checklist.md`: Final review before presenting to the user.
