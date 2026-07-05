import os
import re

input_dir = r"d:\LogManagement\02_du-lieu-tho\parsed_papers"
output_file = r"d:\LogManagement\scratch\criteria_extraction.md"

keywords = [
    "price", "cost", "cpu", "processor", "ram", "memory", "storage", "hdd", "ssd", 
    "gpu", "graphics", "display", "screen", "keyboard", "port", "design", "appearance", 
    "weight", "size", "portability", "battery", "durability", "brand", "after-sales", "warranty",
    "ahp", "topsis", "criteria", "weight", "important", "rank"
]
pattern = re.compile(r'\b(' + '|'.join(keywords) + r')\b', re.IGNORECASE)

with open(output_file, 'w', encoding='utf-8') as out:
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(input_dir, filename)
            out.write(f"# {filename}\n")
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
                # Split into paragraphs or sentences. We'll split by newline for simplicity.
                lines = text.split('\n')
                for line in lines:
                    line = line.strip()
                    if not line: continue
                    if len(line.split()) < 5: continue # Skip very short lines
                    if pattern.search(line):
                        out.write(f"- {line}\n")
            out.write("\n")
