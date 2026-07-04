# Workflow: Data Pipeline Orchestration

**Trigger:** `/pipeline` or `/pipeline [goal]`

This workflow orchestrates the complete data lifecycle: collect → clean → validate → aggregate/synthesize → export → document.

## Sequence

1. **Understand the objective:** Determine the question to answer, required fields, candidate sources, time range, output format, and whether the user wants raw, cleaned, aggregated, or an analytical report.
2. **CHECKPOINT 1 — Confirm scope:** Present the intended sources, the proposed output schema, and the output format. Wait for user approval. (Ask clarifying questions *only* here. If the request is clear, proceed with documented assumptions).
3. **Collect:** Invoke the `data-collection` skill.
4. **Clean:** Invoke the `data-cleaning` skill.
5. **Validate (Shared Step):** Run `shared/scripts/validate.py` against the cleaned data to check required columns, types, duplicates, and outliers.
   - *Validation Loop:* If validation fails, report, fix using `data-cleaning`, and re-run validation. Output quality depends on this loop.
6. **Aggregate / Synthesize:** Invoke the `data-aggregation` skill (only if requested/required by the goal).
7. **CHECKPOINT 2 — Confirm export layout:** Present the column order, user-friendly names, and single vs. multi-sheet Excel structure. Wait for approval.
8. **Export:** Invoke the `data-export` skill.
9. **Report back:** Summarize sources used, extraction methods, cleaning steps, aggregation logic, raw vs. cleaned record counts, files generated, skipped sources, limitations, and data-quality notes.
