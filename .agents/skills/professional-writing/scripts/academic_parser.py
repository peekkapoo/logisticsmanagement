import os
import sys
import hashlib
from pathlib import Path

def get_file_hash(file_path):
    """Tính mã băm MD5 của file PDF để làm tên file cache an toàn."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def parse_with_docling(pdf_path, output_md_path):
    """Tier 1: Sử dụng Docling để parse (Giữ nguyên cấu trúc, bảng biểu, công thức)"""
    try:
        from docling.document_converter import DocumentConverter
        converter = DocumentConverter()
        result = converter.convert(pdf_path)
        markdown_text = result.document.export_to_markdown()
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        return True, "Parsed with Docling (Tier 1)"
    except Exception as e:
        print(f"[Docling Error] {e}")
        return False, str(e)

def parse_with_pdfplumber(pdf_path, output_md_path):
    """Tier 2: Sử dụng pdfplumber để lấy text thô (Fallback 1)"""
    try:
        import pdfplumber
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True, "Parsed with pdfplumber (Tier 2)"
    except Exception as e:
        print(f"[pdfplumber Error] {e}")
        return False, str(e)

def parse_with_pypdf(pdf_path, output_md_path):
    """Tier 3: Sử dụng pypdf để lấy text siêu thô (Fallback 2)"""
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n\n"
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True, "Parsed with pypdf (Tier 3)"
    except Exception as e:
        print(f"[pypdf Error] {e}")
        return False, str(e)

def extract_academic_pdf(pdf_path, project_root="d:/LogManagement"):
    """
    Hàm chính xử lý việc trích xuất văn bản từ PDF thành Markdown.
    Có cơ chế lưu cache để tránh parse lại.
    """
    pdf_path = Path(pdf_path).resolve()
    if not pdf_path.exists():
        return False, f"File not found: {pdf_path}", None

    # Khởi tạo thư mục cache
    cache_dir = Path(project_root) / "02_du-lieu-tho" / "parsed_papers"
    os.makedirs(cache_dir, exist_ok=True)

    # Đặt tên file cache dựa trên MD5 để tránh trùng tên nhưng nội dung khác nhau
    file_md5 = get_file_hash(pdf_path)
    base_name = pdf_path.stem
    safe_name = "".join([c if c.isalnum() or c in ('-', '_') else '_' for c in base_name])
    cache_file = cache_dir / f"{safe_name}_{file_md5[:8]}.md"

    # Trả về kết quả nếu đã được parse trước đó
    if cache_file.exists():
        return True, "Loaded from Cache", str(cache_file)

    print(f"Bắt đầu parse PDF: {pdf_path.name}")
    
    # Tier 1
    success, msg = parse_with_docling(pdf_path, cache_file)
    if success:
        return True, msg, str(cache_file)

    # Tier 2
    success, msg = parse_with_pdfplumber(pdf_path, cache_file)
    if success:
        return True, msg, str(cache_file)

    # Tier 3
    success, msg = parse_with_pypdf(pdf_path, cache_file)
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
