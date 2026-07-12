# Reference: Output Schema Template

When constructing a final Excel workbook, map your intermediate CSV files to sheets in this exact order (from most synthesized to most raw):

1. **`summary`**: High-level analytical findings, charts (if supported), or top-line metrics.
2. **`aggregated_data`**: The results of `data-aggregation`.
3. **`cleaned_data`**: The standardized, deduplicated record set.
4. **`raw_data`**: The untouched extraction (crucial for auditability).
5. **`data_dictionary`**: Definitions of all column headers and metric calculations.
6. **`source_log`**: The compilation of `source_log` JSON outputs generated during `data-collection`.
7. **`validation_report`**: The output of the final run of `shared/scripts/validate.py`.
