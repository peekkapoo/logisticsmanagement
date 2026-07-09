import os
import sys
import glob
from pathlib import Path
from academic_parser import extract_academic_pdf

def main():
    project_root = r"d:\LogManagement"
    pdf_dir = os.path.join(project_root, "01_tai-lieu-tham-khao", "bai-bao")
    
    pdf_files = glob.glob(os.path.join(pdf_dir, "*.pdf"))
    
    if not pdf_files:
        print("No PDF files found.")
        return

    print(f"Found {len(pdf_files)} PDF files to parse.")
    
    success_count = 0
    fail_count = 0
    
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] Processing: {os.path.basename(pdf_path)}")
        try:
            success, msg, output_path = extract_academic_pdf(pdf_path, project_root)
            if success:
                print(f"  -> SUCCESS: {msg}")
                if output_path:
                    print(f"  -> Output: {output_path}")
                success_count += 1
            else:
                print(f"  -> FAILED: {msg}")
                fail_count += 1
        except Exception as e:
            print(f"  -> ERROR processing {pdf_path}: {e}")
            fail_count += 1
            
    print(f"\nBatch processing complete! Success: {success_count}, Failed: {fail_count}")

if __name__ == "__main__":
    main()
