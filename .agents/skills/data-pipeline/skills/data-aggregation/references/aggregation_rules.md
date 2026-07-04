# Reference: Aggregation Rules

1. **Suffixes on Metrics:** Always suffix aggregated columns with the operation used (e.g., `sales_sum`, `price_mean`). `aggregate_data.py` does this automatically.
2. **Merging vs Appending:** 
   - Use `synthesize_data.py` (merging) when adding *new columns* (attributes) to existing records using a common ID.
   - Use standard OS commands (like `cat file1.csv file2.csv` or a quick pandas script) to append *new rows* to an existing schema.
3. **Handling Contradictions in Merges:** If an `outer` or `inner` join results in conflicting values for the same conceptual metric (e.g., `revenue_left` and `revenue_right`), do not silently drop one. Retain both and let the analyst see the discrepancy.
