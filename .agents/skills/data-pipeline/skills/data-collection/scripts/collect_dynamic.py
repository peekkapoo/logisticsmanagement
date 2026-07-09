#!/usr/bin/env python3
import argparse
import json
import sys
from datetime import datetime

def collect(url, css_selector, output_file, wait_for):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright not installed. Run: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) DataPipeline/1.0")
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            if wait_for:
                page.wait_for_selector(wait_for, timeout=10000)
            
            elements = page.query_selector_all(css_selector)
            for el in elements:
                results.append({"extracted_text": el.inner_text(), "html": el.inner_html()})
        except Exception as e:
            print(f"Playwright execution failed: {e}", file=sys.stderr)
            browser.close()
            sys.exit(1)
        browser.close()

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    log = {
        "source_url": url,
        "accessed_at": datetime.utcnow().isoformat(),
        "extraction_method": "dynamic_playwright",
        "record_count": len(results)
    }
    print(json.dumps(log))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract data from JS-rendered pages using Playwright.")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--selector", required=True, help="CSS selector to extract")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    parser.add_argument("--wait-for", help="Optional CSS selector to wait for before extracting")
    args = parser.parse_args()
    collect(args.url, args.selector, args.output, args.wait_for)
