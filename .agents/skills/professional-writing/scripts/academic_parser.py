import os
import sys
import hashlib
from pathlib import Path

# Force stdout to utf-8 to handle unicode characters in filenames (e.g. Šostar)
sys.stdout.reconfigure(encoding='utf-8')

# Limit threads to prevent out of memory RAM spikes
os.environ["OMP_NUM_THREADS"] = "4"
os.environ["OPENBLAS_NUM_THREADS"] = "4"
os.environ["MKL_NUM_THREADS"] = "4"
os.environ["VECLIB_MAXIMUM_THREADS"] = "4"
os.environ["NUMEXPR_NUM_THREADS"] = "4"

# Relocate AI models to D drive (prevent filling up C drive)
models_dir = Path("d:/LogManagement") / ".agents" / "skills" / "professional-writing" / "models"
os.makedirs(models_dir, exist_ok=True)
os.environ["HF_HOME"] = str(models_dir)
os.environ["TORCH_HOME"] = str(models_dir)

def get_file_hash(file_path):
    """Calculate MD5 hash of the PDF file to use as a safe cache filename."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def parse_with_mineru(pdf_path, output_md_path):
    """Tier 1: Use MinerU (Magic-PDF) for perfect 2-column & math extraction"""
    try:
        import subprocess
        import tempfile
        import shutil
        import logging
        
        # MinerU has issues with Unicode paths on Windows (throws "Inconsistent number of pages: X!=-1").
        # We copy the file to a safe ASCII temporary path, parse it, and then move the result back.
        safe_temp_dir = tempfile.mkdtemp(prefix="mineru_")
        safe_pdf_path = os.path.join(safe_temp_dir, "input.pdf")
        shutil.copy2(pdf_path, safe_pdf_path)
        
        try:
            cmd = f'magic-pdf -p "{safe_pdf_path}" -o "{safe_temp_dir}" -m txt'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"[MinerU CLI Error]\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}")
                return False, f"MinerU CLI failed: {result.stderr[-200:]}"
            
            # Find the markdown file using glob
            import glob
            md_files = glob.glob(os.path.join(safe_temp_dir, "**", "*.md"), recursive=True)
            if md_files:
                # Get the first markdown file
                shutil.copy2(md_files[0], output_md_path)
                return True, "Parsed with MinerU (Tier 1)"
            
            print(f"[MinerU CLI Warn] No MD file found. STDOUT: {result.stdout}\nSTDERR: {result.stderr}")
            return False, "MinerU finished but no Markdown file was found."
        finally:
            shutil.rmtree(safe_temp_dir, ignore_errors=True)
            
    except Exception as e:
        print(f"[MinerU Error] {e}")
        return False, str(e)

def parse_with_docling(pdf_path, output_md_path):
    """Tier 2: Use Docling to parse (Preserves structure, tables, formulas)"""
    import tempfile
    import shutil
    safe_temp_dir = tempfile.mkdtemp(prefix="docling_")
    safe_pdf_path = os.path.join(safe_temp_dir, "input.pdf")
    shutil.copy2(pdf_path, safe_pdf_path)
    try:
        from docling.document_converter import DocumentConverter
        converter = DocumentConverter()
        result = converter.convert(safe_pdf_path)
        markdown_text = result.document.export_to_markdown()
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        return True, "Parsed with Docling (Tier 2)"
    except Exception as e:
        print(f"[Docling Error] {e}")
        return False, str(e)
    finally:
        shutil.rmtree(safe_temp_dir, ignore_errors=True)

def parse_with_pymupdf4llm(pdf_path, output_md_path):
    """Tier 3: Use pymupdf4llm to extract Markdown with layout (Fallback 2)"""
    try:
        import pymupdf4llm
        md_text = pymupdf4llm.to_markdown(pdf_path)
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(md_text)
        return True, "Parsed with pymupdf4llm (Tier 3)"
    except Exception as e:
        print(f"[pymupdf4llm Error] {e}")
        return False, str(e)



def extract_academic_pdf(pdf_path, project_root="d:/LogManagement"):
    """
    Main function to handle extracting text from PDF to Markdown.
    Includes a caching mechanism to avoid re-parsing.
    """
    pdf_path = Path(pdf_path).resolve()
    if not pdf_path.exists():
        return False, f"File not found: {pdf_path}", None

    # Initialize cache directory
    cache_dir = Path(project_root) / "02_du-lieu-tho" / "parsed_papers"
    os.makedirs(cache_dir, exist_ok=True)

    # Set cache filename based on MD5 to prevent name collision with different contents
    file_md5 = get_file_hash(pdf_path)
    base_name = pdf_path.stem
    safe_name = "".join([c if c.isalnum() or c in ('-', '_') else '_' for c in base_name])
    cache_file = cache_dir / f"{safe_name}_{file_md5[:8]}.md"

    # Return result if already parsed previously
    if cache_file.exists():
        return True, "Loaded from Cache", str(cache_file)

    print(f"Starting to parse PDF: {pdf_path.name}")
    
    # Tier 1 (MinerU - Disabled due to CPU deadlock / empty text issues)
    # success, msg = parse_with_mineru(pdf_path, cache_file)
    # if success:
    #     return True, msg, str(cache_file)

    # Tier 2 (Docling)
    success, msg = parse_with_docling(pdf_path, cache_file)
    if success:
        return True, msg, str(cache_file)

    # Tier 3
    success, msg = parse_with_pymupdf4llm(pdf_path, cache_file)
    if success:
        return True, msg, str(cache_file)

    return False, "All parsing tiers failed.", None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python academic_parser.py <path_to_pdf>")
        sys.exit(1)
    
    pdf_to_parse = sys.argv[1]
    success, message, cache_path = extract_academic_pdf(pdf_to_parse)
    if success:
        print(f"SUCCESS: {message}")
        print(f"Output File: {cache_path}")
    else:
        print(f"FAILED: {message}")
        sys.exit(1)
