#!/usr/bin/env python3
import argparse
import pandas as pd
import sys
import os

def parse_file(input_file, output_csv):
    ext = os.path.splitext(input_file)[1].lower()
    try:
        if ext == '.csv':
            df = pd.read_csv(input_file)
        elif ext in ['.xls', '.xlsx']:
            df = pd.read_excel(input_file)
        elif ext == '.json':
            df = pd.read_json(input_file)
        else:
            print(f"Unsupported file type: {ext}", file=sys.stderr)
            sys.exit(1)
        
        df.to_csv(output_csv, index=False)
        print(f"Successfully converted {input_file} to {output_csv} ({len(df)} rows)")
    except Exception as e:
        print(f"Failed to parse file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse local Excel/JSON/CSV into standardized CSV format.")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output CSV file path")
    args = parser.parse_args()
    parse_file(args.input, args.output)
