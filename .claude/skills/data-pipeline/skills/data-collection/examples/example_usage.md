# Examples: Data Collection

**Extracting all tables from a Wikipedia page:**
`python scripts/extract_tables.py --url "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies" --output-prefix "sp500"`

**Fetching a REST API endpoint:**
`python scripts/collect_api.py --url "https://api.github.com/repos/microsoft/vscode/issues" --output "issues.json"`

**Extracting specific elements from static HTML:**
`python scripts/collect_static.py --url "https://news.ycombinator.com/" --selector ".titleline > a" --output "hn_titles.json"`
