import os
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
from pypdf import PdfReader, PdfWriter

files_to_fix = [
    r"d:\LogManagement\01_tai-lieu-tham-khao\bai-bao\Jiménez-Parra et al. - 2014 - Key drivers in the behavior of potential consumers of remanufactured products a study on laptops in Spain.pdf",
    r"d:\LogManagement\01_tai-lieu-tham-khao\bai-bao\Kang et al. - 2022 - A study on the influence of online reviews of new products on consumers’ purchase decisions an empirical study on JD.com.pdf",
    r"d:\LogManagement\01_tai-lieu-tham-khao\bai-bao\Sönmez Çakır and Pekkaya - 2020 - Determination of interaction between criteria and the criteria priorities in laptop selection problem.pdf",
    r"d:\LogManagement\01_tai-lieu-tham-khao\bai-bao\Šostar and Ristanović - 2023 - Assessment of influencing factors on consumer behavior using the AHP model.pdf"
]

for file in files_to_fix:
    try:
        print(f"Fixing {file}")
        reader = PdfReader(file)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        
        tmp_path = file + ".fixed.pdf"
        with open(tmp_path, "wb") as output:
            writer.write(output)
            
        os.replace(tmp_path, file)
        print(f"Success fixing {file}")
    except Exception as e:
        print(f"Failed to fix {file}: {e}")
