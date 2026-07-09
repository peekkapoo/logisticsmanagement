#!/usr/bin/env python3
import argparse
import pandas as pd
import json
import sys

def validate_data(input_file, required_cols=None, unique_cols=None, non_null_cols=None):
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(json.dumps({"valid": False, "error": f"Failed to read file: {e}"}))
        sys.exit(1)

    report = {"valid": True, "rows": len(df), "columns": list(df.columns), "issues": []}

    if required_cols:
        missing = [c for c in required_cols if c not in df.columns]
        if missing:
            report["valid"] = False
            report["issues"].append(f"Missing required columns: {missing}")

    if unique_cols:
        for col in unique_cols:
            if col in df.columns:
                dupes = df[col].duplicated().sum()
                if dupes > 0:
                    report["valid"] = False
                    report["issues"].append(f"Column '{col}' has {dupes} duplicate values.")

    if non_null_cols:
        for col in non_null_cols:
            if col in df.columns:
                nulls = df[col].isnull().sum()
                if nulls > 0:
                    report["valid"] = False
                    report["issues"].append(f"Column '{col}' has {nulls} null values.")

    print(json.dumps(report, indent=2))
    sys.exit(0 if report["valid"] else 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate schema and data quality of a CSV.")
    parser.add_argument("--input", required=True, help="Input CSV file to validate")
    parser.add_argument("--required-cols", nargs='*', help="Columns that must exist")
    parser.add_argument("--unique-cols", nargs='*', help="Columns that must contain unique values")
    parser.add_argument("--non-null-cols", nargs='*', help="Columns that must not contain nulls")
    
    args = parser.parse_args()
    validate_data(args.input, args.required_cols, args.unique_cols, args.non_null_cols)
