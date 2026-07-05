import os
import glob
import re
import shutil

root_dir = r"d:\LogManagement"
bai_bao_dir = os.path.join(root_dir, "01_tai-lieu-tham-khao", "bai-bao")

# 1. Delete old PDFs
old_pdfs = glob.glob(os.path.join(bai_bao_dir, "*.pdf"))
for pdf in old_pdfs:
    os.remove(pdf)

# 2. Move new PDFs
new_pdfs = glob.glob(os.path.join(root_dir, "*.pdf"))
for pdf in new_pdfs:
    shutil.move(pdf, bai_bao_dir)

# 3. BibTeX Merging
zotero_bib_path = os.path.join(root_dir, "Exported Items.bib")
main_bib_path = os.path.join(root_dir, "04_bao-cao-latex", "references.bib")

with open(zotero_bib_path, 'r', encoding='utf-8') as f:
    zotero_bib = f.read()

# Extract DOIs from Zotero
zotero_dois = set()
for match in re.finditer(r'doi\s*=\s*\{([^}]+)\}', zotero_bib, re.IGNORECASE):
    # normalize doi (sometimes they include https://doi.org/)
    doi = match.group(1).strip().lower()
    if doi.startswith('10.'):
        zotero_dois.add(doi)
    elif '10.' in doi:
        zotero_dois.add(doi[doi.find('10.'):])

with open(main_bib_path, 'r', encoding='utf-8') as f:
    main_bib = f.read()

# Split main bib into entries
entries = re.split(r'\n(?=@)', main_bib)
kept_entries = []

removed_count = 0
for entry in entries:
    if not entry.strip(): continue
    # Extract DOI from this entry
    doi_match = re.search(r'DOI\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
    if doi_match:
        doi = doi_match.group(1).strip().lower()
        if doi.startswith('10.'):
            pass
        elif '10.' in doi:
            doi = doi[doi.find('10.'):]
            
        if doi in zotero_dois:
            print(f"Removing duplicate entry from references.bib (DOI: {doi})")
            removed_count += 1
            continue # Skip this entry
    
    # Also try to check by title just in case DOI parsing failed or DOI was slightly different
    title_match = re.search(r'title\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
    if title_match:
        title = title_match.group(1).strip().lower()
        title_alphanum = re.sub(r'[^a-z0-9]', '', title)
        
        is_duplicate = False
        for z_match in re.finditer(r'title\s*=\s*\{([^}]+)\}', zotero_bib, re.IGNORECASE):
            z_title = z_match.group(1).strip().lower()
            z_title_alphanum = re.sub(r'[^a-z0-9]', '', z_title)
            if title_alphanum and title_alphanum == z_title_alphanum:
                is_duplicate = True
                break
                
        if is_duplicate:
            print(f"Removing duplicate entry from references.bib (Title match: {title})")
            removed_count += 1
            continue
            
    kept_entries.append(entry)

# Write merged bibtex
with open(main_bib_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(kept_entries))
    f.write("\n\n% --- ZOTERO EXPORTED ITEMS ---\n\n")
    f.write(zotero_bib)

print(f"Removed {removed_count} duplicates.")
print("Bibtex successfully merged!")
