import os
try:
    import PyPDF2
except ImportError:
    os.system('pip install PyPDF2')
    import PyPDF2

def get_first_page_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            if len(reader.pages) > 0:
                text = reader.pages[0].extract_text()
                return text[:500].replace('\n', ' ')
            return "No pages"
    except Exception as e:
        return str(e)

paper_dir = r"d:\LogManagement\paper_search"
with open(r"d:\LogManagement\scratch\pdf_titles.txt", "w", encoding="utf-8") as out_f:
    for fname in os.listdir(paper_dir):
        if fname.endswith(".pdf") and not fname.startswith("What") and not fname.startswith("Which"):
            path = os.path.join(paper_dir, fname)
            text = get_first_page_text(path)
            out_f.write(f"--- {fname} ---\n")
            out_f.write(text.strip()[:200] + "\n")
