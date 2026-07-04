#!/usr/bin/env python3
import argparse
import pandas as pd
import sys
import json
from datetime import datetime

def extract(url, output_prefix):
    try:
        tables = pd.read_html(url)
    except Exception as e:
        print(f"Failed to extract tables: {e}", file=sys.stderr)
        sys.exit(1)

    total_rows = 0
    for i, df in enumerate(tables):
        out_file = f"{output_prefix}_table_{i}.csv"
        df.to_csv(out_file, index=False)
        total_rows += len(df)
        print(f"Saved table {i} to {out_file} ({len(df)} rows)")

    log = {
        "source_url": url,
        "accessed_at": datetime.utcnow().isoformat(),
        "extraction_method": "html_tables",
        "record_count": total_rows
    }
    print(json.dumps(log))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract all HTML <table> elements from a URL to CSVs.")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--output-prefix", required=True, help="Prefix for output CSV files")
    args = parser.parse_args()
    extract(args.url, args.output_prefix)
