import csv
import glob
import urllib.request
import os

csv_files = glob.glob(r"d:\LogManagement\01_tai-lieu-tham-khao\*.csv")
dois = []

for file in csv_files:
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            doi = row.get('DOI', '').strip()
            if doi:
                dois.append(doi)

dois = list(set(dois))
bibtex_entries = []

for doi in dois:
    url = f"https://doi.org/{doi}"
    req = urllib.request.Request(url, headers={'Accept': 'application/x-bibtex'})
    try:
        with urllib.request.urlopen(req) as response:
            bibtex = response.read().decode('utf-8')
            bibtex_entries.append(bibtex)
            print(f"Fetched BibTeX for {doi}")
    except Exception as e:
        print(f"Failed to fetch {doi}: {e}")

bib_path = r"d:\LogManagement\04_bao-cao-latex\references.bib"
os.makedirs(os.path.dirname(bib_path), exist_ok=True)
with open(bib_path, 'w', encoding='utf-8') as f:
    for entry in bibtex_entries:
        f.write(entry + "\n\n")

print(f"Successfully wrote {len(bibtex_entries)} entries to references.bib")
