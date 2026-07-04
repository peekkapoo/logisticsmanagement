# Examples: Data Export

**Compiling three CSVs into a finalized Excel workbook:**
`python scripts/export_data.py --output "Q3_Financial_Report.xlsx" --sheets '[{"file": "summary.csv", "sheet": "Summary"}, {"file": "clean_records.csv", "sheet": "Cleaned Data"}, {"file": "sources.csv", "sheet": "Source Log"}]'`
