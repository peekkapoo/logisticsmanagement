#!/usr/bin/env python3
import argparse
import pandas as pd
import json
import sys
import os

def export_to_excel(input_configs, output_file):
    try:
        from openpyxl.utils import get_column_letter
    except ImportError:
        print("openpyxl is required for Excel export. Run: pip install openpyxl", file=sys.stderr)
        sys.exit(1)

    try:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for config in input_configs:
                csv_path = config.get('file')
                sheet_name = config.get('sheet', 'Sheet')
                
                if not os.path.exists(csv_path):
                    print(f"Warning: {csv_path} not found. Skipping sheet '{sheet_name}'.", file=sys.stderr)
                    continue
                    
                df = pd.read_csv(csv_path)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                # Formatting: Freeze panes and auto-width
                worksheet = writer.sheets[sheet_name]
                worksheet.freeze_panes = 'A2'
                
                for idx, col in enumerate(df.columns):
                    series = df[col]
                    max_len = max((
                        series.astype(str).map(len).max(),
                        len(str(series.name))
                    )) + 2
                    # Cap width to avoid giant columns
                    worksheet.column_dimensions[get_column_letter(idx + 1)].width = min(max_len, 50)

        print(json.dumps({"status": "success", "file": output_file, "sheets_written": [c.get('sheet') for c in input_configs]}))

    except Exception as e:
        print(f"Failed to write Excel file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export multiple CSVs into a formatted, multi-sheet Excel workbook.")
    parser.add_argument("--output", required=True, help="Output .xlsx file path")
    parser.add_argument("--sheets", required=True, help="JSON array mapping CSVs to sheet names. Example: '[{\"file\":\"raw.csv\", \"sheet\":\"raw_data\"}]'")
    
    args = parser.parse_args()
    
    try:
        configs = json.loads(args.sheets)
    except json.JSONDecodeError:
        print("Error: --sheets must be a valid JSON array.", file=sys.stderr)
        sys.exit(1)
        
    export_to_excel(configs, args.output)
