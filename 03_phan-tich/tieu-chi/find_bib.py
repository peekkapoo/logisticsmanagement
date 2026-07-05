import pybtex.database

bib_path = r"d:\LogManagement\04_bao-cao-latex\references.bib"
bib_data = pybtex.database.parse_file(bib_path)

pdf_files = [
    "Al Hazza", "Altubaishe", "Jiménez-Parra", "Kang", "Liao", "Liu", "Maghsoudi", "Rau", "Sönmez", "Tighnavard", "Villalba", "Weng Siew Lam", "Yannis", "Zakeri", "Zyoud", "Šostar"
]

found_entries = []
for entry_id, entry in bib_data.entries.items():
    authors = ""
    if "author" in entry.persons:
        authors = " ".join([str(p) for p in entry.persons["author"]])
    
    for pdf in pdf_files:
        if pdf.lower() in authors.lower() or pdf.lower() in entry_id.lower():
            if entry_id not in found_entries:
                found_entries.append(entry_id)
                print(f"Found: {entry_id} -> {authors}")

print(found_entries)
