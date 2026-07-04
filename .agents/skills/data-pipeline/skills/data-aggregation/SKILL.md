---
name: data-aggregation
description: Appends, merges, and groups data to compute totals, means, growth rates, and pivots. Flags contradictions. Outputs synthesized datasets. Do not use for raw collection or file export.
---
# Skill: Data Aggregation

You are responsible for combining and summarizing cleaned data. 

## Core Directives
1. **Preserve lineage:** Whenever appending or merging sources, keep a `source_name` column.
2. **Highlight contradictions:** If combining sources yields conflicting numbers for the same entity, compute both and flag the uncertainty (do not just arbitrarily overwrite).
3. **Metric definitions:** Clearly name your calculated columns (e.g., `total_revenue_usd`, `yoy_growth_pct`).

## Capabilities
All tools are executable CLI scripts. Run them with `--help` to view arguments.
- **`scripts/aggregate_data.py`**: Perform GroupBy operations (sum, mean, median, count, max, min) on specific columns.
- **`scripts/synthesize_data.py`**: Perform DataFrame joins (inner, left, outer) to combine multiple datasets.

## References
Read these before deciding your aggregation strategy:
- `references/aggregation_rules.md`: Rules for defining metrics, handling source comparisons, and ensuring calculation fidelity.
