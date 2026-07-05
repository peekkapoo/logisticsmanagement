import os
import PyPDF2
import re
from collections import defaultdict

pdf_dir = r"d:\LogManagement\01_tai-lieu-tham-khao\bai-bao"
output_file = r"d:\LogManagement\03_phan-tich\tieu-chi\extracted_insights.md"

criteria_keywords = {
    "Price": ["price", "cost", "budget", "pricing", "expense"],
    "CPU": ["cpu", "processor", "performance", "processing power"],
    "RAM": ["ram", "memory"],
    "Storage": ["storage", "hard drive", "ssd", "hdd", "disk"],
    "Display": ["display", "screen", "resolution", "monitor"],
    "GPU": ["gpu", "graphics", "vga", "video card"],
    "Battery": ["battery", "power consumption", "charge"],
    "Keyboard": ["keyboard", "touchpad", "input"],
    "Ports": ["ports", "connectivity", "interface", "usb", "hdmi"],
    "Design": ["design", "material", "build quality", "aesthetics", "appearance"],
    "Portability": ["portability", "weight", "size", "dimensions", "lightweight"],
    "Brand": ["brand", "reputation", "manufacturer", "loyalty"],
    "Warranty": ["warranty", "after-sales", "support", "service", "guarantee"],
    "Durability": ["durability", "reliability", "lifespan", "robustness", "sturdy"]
}

# Context keywords to ensure the sentence is somewhat relevant to decision making or evaluation
context_keywords = ["important", "significant", "affect", "decision", "weight", "criteria", "factor", "review", "consider", "prefer", "impact", "evaluate", "select"]

results = defaultdict(lambda: defaultdict(list))

for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        try:
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + " "
                
                # Simple sentence split
                sentences = re.split(r'(?<=[.!?])\s+', text)
                
                for sentence in sentences:
                    sentence_lower = sentence.lower()
                    
                    # Check if it has a context keyword to filter noise
                    if any(c_kw in sentence_lower for c_kw in context_keywords):
                        for crit, kws in criteria_keywords.items():
                            if any(kw in sentence_lower for kw in kws):
                                # Clean up sentence formatting (newlines etc)
                                clean_sentence = " ".join(sentence.split())
                                if len(clean_sentence) > 30 and len(clean_sentence) < 500: # reasonable length
                                    results[crit][filename].append(clean_sentence)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

with open(output_file, "w", encoding="utf-8") as out:
    out.write("# Báo cáo Trích xuất Dữ liệu từ 17 PDF\n\n")
    for crit, files in results.items():
        out.write(f"## Tiêu chí: {crit}\n")
        for file, sentences in files.items():
            out.write(f"### Nguồn: {file}\n")
            # Only take top 3 unique sentences per file to avoid bloat
            unique_sentences = list(set(sentences))[:3]
            for s in unique_sentences:
                out.write(f"- {s}\n")
            out.write("\n")
        out.write("---\n")

print("Extraction complete. Results saved to", output_file)
