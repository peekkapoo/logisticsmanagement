---
name: data-collection
description: Extracts structured data from APIs, static/dynamic web pages, and local files. Outputs raw datasets and a source log. Do not use for cleaning, aggregation, or export.
---
# Skill: Data Collection

You are responsible for safely and reliably extracting data from permitted sources.

## Core Directives
1. **Source Hierarchy:** Always prefer official APIs > structured files (CSV/JSON/XML) > HTML tables (`scripts/extract_tables.py`) > CSS selectors (`scripts/collect_static.py`) > JS-rendering (`scripts/collect_dynamic.py`).
2. **Reproducibility:** Log every source. Your output must include the raw dataset AND a `source_log` containing `source_url`, `source_name`, `accessed_at`, `extraction_method`, and `record_count`.
3. **No Walls:** Stop and ask the user if you encounter a CAPTCHA, login, or paywall. Do not bypass.

## Capabilities
All tools are executable CLI scripts. Run them with `--help` to view their arguments.

- **`scripts/collect_api.py`**: Fetch and paginate JSON/XML from REST APIs.
- **`scripts/collect_static.py`**: Fast, lightweight HTML extraction via `httpx` and `BeautifulSoup`.
- **`scripts/collect_dynamic.py`**: Headless browser extraction via `Playwright` (use ONLY if JS is required).
- **`scripts/extract_tables.py`**: Automatically find and extract `<table>` elements from URLs to CSV.
- **`scripts/collect_files.py`**: Parse local PDF, CSV, or XLSX files into raw flat formats.
- **`scripts/discover_sources.py`**: Help find RSS feeds, sitemaps, or API endpoints on a target domain.

## References
Read these before deciding how to approach a new target:
- `references/source_decision_guide.md`: How to pick the right script for the target.
- `references/extraction_strategy_guide.md`: Best practices for selectors and pagination.
