#!/usr/bin/env python3
import argparse
import pandas as pd
import sys
import json

def aggregate(input_file, output_file, group_by, agg_cols, method):
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Failed to read file: {e}", file=sys.stderr)
        sys.exit(1)

    if not group_by:
        print("Error: --group-by is required.", file=sys.stderr)
        sys.exit(1)

    if not agg_cols:
        print("Error: --agg-cols is required.", file=sys.stderr)
        sys.exit(1)

    try:
        # Build aggregation dictionary
        agg_dict = {col: method for col in agg_cols}
        
        # Perform group by
        grouped = df.groupby(group_by, dropna=False).agg(agg_dict).reset_index()
        
        # Rename aggregated columns to reflect the method
        rename_dict = {col: f"{col}_{method}" for col in agg_cols}
        grouped = grouped.rename(columns=rename_dict)
        
        grouped.to_csv(output_file, index=False)
        
        print(json.dumps({
            "status": "success",
            "group_by_columns": group_by,
            "metrics": list(rename_dict.values()),
            "output_rows": len(grouped)
        }, indent=2))
        
    except Exception as e:
        print(f"Aggregation failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Group and aggregate data.")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    parser.add_argument("--group-by", nargs='+', required=True, help="Columns to group by")
    parser.add_argument("--agg-cols", nargs='+', required=True, help="Columns to aggregate")
    parser.add_argument("--method", choices=['sum', 'mean', 'median', 'max', 'min', 'count'], default='sum', help="Aggregation method")
    
    args = parser.parse_args()
    aggregate(args.input, args.output, args.group_by, args.agg_cols, args.method)
