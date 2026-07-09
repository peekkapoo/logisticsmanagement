---
name: data-cleaning
description: Standardizes column names, dates, numbers, and currencies; handles missing values; deduplicates and coerces types. Outputs cleaned structured data. Do not use to collect new data or compute aggregates.
---
# Skill: Data Cleaning

You are responsible for transforming raw collected data into standardized, high-quality, analysis-ready formats. 

## Core Directives
1. **Never alter source meaning:** Coerce types and normalize formats, but do not change the fundamental meaning of the data. 
2. **Never fabricate data:** Missing data must remain explicitly missing (e.g., empty or NaN) or be dropped. Never invent data points.
3. **Log transformations:** Track row counts before and after dropping duplicates or invalid rows.

## Capabilities
All tools are executable CLI scripts. Run them with `--help` to view arguments.
- **`scripts/clean_data.py`**: A comprehensive CLI for column renaming, date/numeric normalization, filling/dropping missing values, and deduplication. It wraps `shared/scripts/utils.py`.

## References
Read these before deciding your cleaning strategy:
- `references/data_cleaning_rules.md`: Rules for standardizing timestamps, currencies, encoding, and missing values.
