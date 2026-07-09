#!/usr/bin/env python3
import argparse
import pandas as pd
import json
import sys
import os

# Add shared/scripts to path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'shared', 'scripts')))
try:
    import utils
except ImportError:
    print("Error: Could not import shared/scripts/utils.py. Ensure the bundle structure is intact.", file=sys.stderr)
    sys.exit(1)

def clean(input_file, output_file, drop_dupes, date_cols, num_cols, drop_na_cols, fill_na, rename_cols):
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Failed to read file: {e}", file=sys.stderr)
        sys.exit(1)
        
    initial_rows = len(df)

    # 1. Rename columns
    if rename_cols:
        try:
            rename_dict = json.loads(rename_cols)
            df = df.rename(columns=rename_dict)
        except Exception as e:
            print(f"Failed to parse rename dictionary: {e}", file=sys.stderr)

    # 2. Type coercion using shared utility logic (applied directly here for dataframes)
    if date_cols:
        for col in date_cols:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
                
    if num_cols:
        for col in num_cols:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace(r'[$,£€,%]', '', regex=True)
                df[col] = pd.to_numeric(df[col], errors='coerce')

    # 3. Handle missing values
    if drop_na_cols:
        df = df.dropna(subset=drop_na_cols)
        
    if fill_na:
        try:
            fill_dict = json.loads(fill_na)
            df = df.fillna(fill_dict)
        except Exception as e:
            print(f"Failed to parse fill_na dictionary: {e}", file=sys.stderr)

    # 4. Deduplicate
    if drop_dupes:
        df = df.drop_duplicates()

    try:
        df.to_csv(output_file, index=False)
        final_rows = len(df)
        print(json.dumps({
            "status": "success",
            "initial_rows": initial_rows,
            "final_rows": final_rows,
            "dropped_rows": initial_rows - final_rows,
            "columns": list(df.columns)
        }, indent=2))
    except Exception as e:
        print(f"Failed to write output: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean and standardize CSV data.")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    parser.add_argument("--drop-dupes", action="store_true", help="Drop duplicate rows")
    parser.add_argument("--date-cols", nargs='*', help="Columns to coerce to YYYY-MM-DD")
    parser.add_argument("--num-cols", nargs='*', help="Columns to coerce to numeric (strips currencies/commas/percents)")
    parser.add_argument("--drop-na-cols", nargs='*', help="Drop rows where these columns have NaN")
    parser.add_argument("--fill-na", help="JSON dict mapping columns to fill values (e.g., '{\"status\": \"unknown\"}')")
    parser.add_argument("--rename-cols", help="JSON dict for renaming cols (e.g., '{\"oldName\": \"new_name\"}')")
    
    args = parser.parse_args()
    clean(args.input, args.output, args.drop_dupes, args.date_cols, args.num_cols, args.drop_na_cols, args.fill_na, args.rename_cols)
