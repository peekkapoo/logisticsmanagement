# Reference: Source Decision Guide

When identifying how to extract data from a target, evaluate in this order:

1. **Check for an API:** Use `scripts/discover_sources.py` or inspect network traffic. If JSON/XML is returned directly, use `scripts/collect_api.py`. It is the most robust method.
2. **Check for HTML Tables:** If the data is visibly in a table grid on the page, try `scripts/extract_tables.py` first. It uses Pandas to perfectly map HTML `<table>` structures to CSVs.
3. **Static HTML Scrape:** If data is in divs, spans, or lists, use `scripts/collect_static.py`. It is fast and respects server load.
4. **Dynamic JS Scrape:** ONLY if the page requires JavaScript to render the data (e.g., Infinite Scroll, React/Vue SPAs that don't hydrate from server), fall back to `scripts/collect_dynamic.py`.

**Rule of Thumb:** Never use Playwright if `requests` / `httpx` can do the job.
