import re

bib_path = r"d:\LogManagement\04_bao-cao-latex\references.bib"
with open(bib_path, encoding='utf-8') as f:
    content = f.read()

entries = re.findall(r'@\w+\{([^,]+),.*?author\s*=\s*\{([^}]+)\}', content, re.DOTALL | re.IGNORECASE)

pdfs = {
    'Al Hazza': 'Al Hazza et al. - 2022 - An integrated approach for supplier evaluation and selection using the delphi method and analytic hierarchy process (AHP) a new framework.pdf',
    'Altubaishe': 'Altubaishe and Desai - 2023 - Multicriteria decision making in supply chain management using FMEA and hybrid AHP-PROMETHEE algorithms.pdf',
    'Jiménez-Parra': 'Jiménez-Parra et al. - 2014 - Key drivers in the behavior of potential consumers of remanufactured products a study on laptops in Spain.pdf',
    'Kang': 'Kang et al. - 2022 - A study on the influence of online reviews of new products on consumers’ purchase decisions an empirical study on JD.com.pdf',
    'Liao': 'Liao and Chuang - 2022 - Determinants of innovative green electronics an experimental study of eco-friendly laptop computers.pdf',
    'Liu': 'Liu et al. - 2020 - A review of fuzzy AHP methods for decision-making with subjective judgements.pdf',
    'Maghsoudi': 'Maghsoudi et al. - 2026 - A hybrid framework for notebook market analysis integrating social media sentiment mining with expert knowledge for feature prioritization.pdf',
    'Rau': 'Rau and Fang - 2018 - Optimal time for consumers to purchase electronic products with consideration of consumer value and eco-efficiency.pdf',
    'Sönmez': 'Sönmez Çakır and Pekkaya - 2020 - Determination of interaction between criteria and the criteria priorities in laptop selection problem.pdf',
    'Tighnavard': 'Tighnavard Balasbaneh et al. - 2025 - A systematic review of implementing multi-criteria decision-making (MCDM) approaches for the circular economy and cost assessment.pdf',
    'Villalba': 'Villalba et al. - 2024 - A review of multi-criteria decision-making methods for building assessment, selection, and retrofit.pdf',
    'Weng Siew Lam': 'Weng Siew Lam et al. - 2023 - Evaluation and selection of mobile phones using integrated AHP-TOPSIS model.pdf',
    'Yannis': 'Yannis et al. - 2020 - State-of-the-art review on multi-criteria decision-making in the transport sector.pdf',
    'Zakeri': 'Zakeri et al. - 2023 - A decision analysis model for material selection using simple ranking process.pdf',
    'Zyoud': 'Zyoud and Fuchs-Hanusch - 2017 - A bibliometric-based survey on AHP and TOPSIS techniques.pdf',
    'Šostar': 'Šostar and Ristanović - 2023 - Assessment of influencing factors on consumer behavior using the AHP model.pdf'
}

matches = {}
for p in pdfs:
    # try to find a match in entries
    for e in entries:
        if p.lower() in e[1].lower():
            matches[p] = e[0]
            break

print(matches)
