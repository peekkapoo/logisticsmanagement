#!/usr/bin/env python3
import argparse
import pandas as pd
import sys
import json

def synthesize(left_file, right_file, output_file, join_on, how):
    try:
        df_left = pd.read_csv(left_file)
        df_right = pd.read_csv(right_file)
    except Exception as e:
        print(f"Failed to read input files: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        # Perform join
        merged = pd.merge(df_left, df_right, on=join_on, how=how, suffixes=('_left', '_right'))
        
        merged.to_csv(output_file, index=False)
        
        print(json.dumps({
            "status": "success",
            "join_type": how,
            "join_keys": join_on,
            "left_rows": len(df_left),
            "right_rows": len(df_right),
            "merged_rows": len(merged)
        }, indent=2))
        
    except Exception as e:
        print(f"Merge failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge two datasets.")
    parser.add_argument("--left", required=True, help="Left CSV file")
    parser.add_argument("--right", required=True, help="Right CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    parser.add_argument("--join-on", nargs='+', required=True, help="Columns to join on")
    parser.add_argument("--how", choices=['left', 'right', 'outer', 'inner'], default='left', help="Join type")
    
    args = parser.parse_args()
    synthesize(args.left, args.right, args.output, args.join_on, args.how)
