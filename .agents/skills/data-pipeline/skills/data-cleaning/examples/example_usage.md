# Examples: Data Cleaning

**Full cleaning pass:**
Rename columns to snake case, strip symbols from prices, enforce ISO dates, drop rows missing an ID, and drop duplicates.

`python scripts/clean_data.py --input raw.csv --output clean.csv --rename-cols '{"Product Name": "product_name", "List Price": "price"}' --num-cols price --date-cols sale_date --drop-na-cols id --drop-dupes`
