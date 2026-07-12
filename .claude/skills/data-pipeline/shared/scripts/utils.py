#!/usr/bin/env python3
import argparse
import pandas as pd
import json
import sys

def process_data(input_file, output_file, drop_duplicates=False, date_cols=None, numeric_cols=None):
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading {input_file}: {e}", file=sys.stderr)
        sys.exit(1)

    initial_rows = len(df)

    if drop_duplicates:
        df = df.drop_duplicates()

    if date_cols:
        for col in date_cols:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')

    if numeric_cols:
        for col in numeric_cols:
            if col in df.columns:
                # Remove common currency symbols and commas before converting
                df[col] = df[col].astype(str).str.replace(r'[$,£€,]', '', regex=True)
                df[col] = pd.to_numeric(df[col], errors='coerce')

    try:
        df.to_csv(output_file, index=False)
        final_rows = len(df)
        print(json.dumps({"status": "success", "initial_rows": initial_rows, "final_rows": final_rows}))
    except Exception as e:
        print(f"Error writing {output_file}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shared utility for basic data normalization.")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    parser.add_argument("--drop-duplicates", action="store_true", help="Drop duplicate rows")
    parser.add_argument("--date-cols", nargs='*', help="Columns to coerce to YYYY-MM-DD")
    parser.add_argument("--numeric-cols", nargs='*', help="Columns to coerce to numeric (strips currencies/commas)")
    
    args = parser.parse_args()
    process_data(args.input, args.output, args.drop_duplicates, args.date_cols, args.numeric_cols)
