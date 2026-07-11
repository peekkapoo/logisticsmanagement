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
    """Tier 1: Use MinerU Precise API for perfect 2-column & math extraction"""
    import os
    import time
    import requests
    import zipfile
    import io
    
    token = os.environ.get("MINERU_API_KEY")
    if not token:
        print("[MinerU API Error] MINERU_API_KEY environment variable is not set.")
        return False, "MINERU_API_KEY is not set"

    try:
        # Step 1: Request presigned upload URL via v4 batch API
        agent_url = "https://mineru.net/api/v4/file-urls/batch"
        file_name = os.path.basename(pdf_path)
        upload_req_data = {
            "files": [{"name": file_name}],
            "model_version": "vlm",
            "enable_table": True,
            "enable_formula": True
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        res_upload = requests.post(agent_url, headers=headers, json=upload_req_data).json()
        if res_upload.get("code") != 0:
            return False, f"Failed to get upload URL: {res_upload.get('msg')}"
        
        file_url = res_upload["data"]["file_urls"][0]
        batch_id = res_upload["data"]["batch_id"]
        
        # Step 2: PUT file to OSS (no Content-Type to prevent Signature mismatch)
        print(f"[MinerU] Uploading {file_name} to OSS...")
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
            put_res = requests.put(file_url, data=pdf_bytes)
            if put_res.status_code != 200:
                return False, f"Upload to OSS failed: {put_res.status_code}"
                
        # Step 3: Poll for results (v4 API automatically starts task on upload)
        query_url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
        print("[MinerU] Polling for results...")
        
        # Wait up to 15 mins (180 * 5s)
        for _ in range(180):
            time.sleep(5)
            resp = requests.get(query_url, headers={"Authorization": f"Bearer {token}", "Accept": "*/*"})
            try:
                status_res = resp.json()
            except Exception as e:
                return False, f"MinerU API returned non-JSON: {resp.status_code} {resp.text}"
                
            if status_res.get("code") == 0 and "data" in status_res:
                result_list = status_res["data"].get("extract_result", [])
                if not result_list:
                    continue # Not started or no results yet
                
                result = result_list[0]
                state = result.get("state")
                
                if state == "done":
                    zip_url = result.get("full_zip_url")
                    print("[MinerU] Downloading and extracting result...")
                    zip_resp = requests.get(zip_url)
                    with zipfile.ZipFile(io.BytesIO(zip_resp.content)) as z:
                        md_files = [f for f in z.namelist() if f.endswith(".md")]
                        if md_files:
                            md_content = z.read(md_files[0]).decode('utf-8')
                            with open(output_md_path, 'w', encoding='utf-8') as md_f:
                                md_f.write(md_content)
                            return True, "Parsed with MinerU Precise API (Tier 1)"
                    return False, "MinerU succeeded but no Markdown file found in ZIP."
                
                elif state == "failed":
                    return False, f"MinerU API parsing failed: {result.get('err_msg')} (Full result: {result})"
            else:
                return False, f"MinerU API status check failed: {status_res}"
            
        return False, "MinerU API timeout after 15 minutes."

    except Exception as e:
        print(f"[MinerU API Error] {e}")
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
    
    # Tier 1 (MinerU Precise API)
    success, msg = parse_with_mineru(pdf_path, cache_file)
    if success:
        return True, msg, str(cache_file)
    
    print(f"[Fallback] MinerU failed: {msg}")

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
