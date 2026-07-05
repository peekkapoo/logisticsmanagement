import glob
import shutil
import os

src_dir = r"D:\Research\paper_dataset\MDCM - Laptop Selection"
dst_dir = r"d:\LogManagement\01_tai-lieu-tham-khao\bai-bao"

pdfs = glob.glob(os.path.join(src_dir, "*.pdf"))
count = 0
for pdf in pdfs:
    shutil.copy2(pdf, dst_dir)
    count += 1

print(f"Successfully copied {count} PDFs.")
