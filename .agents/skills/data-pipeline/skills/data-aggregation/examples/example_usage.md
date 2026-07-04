# Examples: Data Aggregation

**Group by country and year, summing revenue:**
`python scripts/aggregate_data.py --input clean_sales.csv --output yearly_sales.csv --group-by country year --agg-cols revenue --method sum`

**Left join user metadata onto transaction logs:**
`python scripts/synthesize_data.py --left transactions.csv --right users.csv --output enriched.csv --join-on user_id --how left`
