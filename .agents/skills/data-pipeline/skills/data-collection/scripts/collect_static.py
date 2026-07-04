#!/usr/bin/env python3
import argparse
import httpx
from bs4 import BeautifulSoup
import json
import sys
from datetime import datetime

def collect(url, css_selector, output_file):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) DataPipeline/1.0"}
    try:
        response = httpx.get(url, headers=headers, follow_redirects=True, timeout=15.0)
        response.raise_for_status()
    except Exception as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'lxml')
    elements = soup.select(css_selector)
    
    results = [{"extracted_text": el.get_text(strip=True), "html": str(el)} for el in elements]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    log = {
        "source_url": url,
        "accessed_at": datetime.utcnow().isoformat(),
        "extraction_method": "static_css_selector",
        "record_count": len(results)
    }
    print(json.dumps(log))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract data from static HTML using CSS selectors.")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--selector", required=True, help="CSS selector to extract")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    args = parser.parse_args()
    collect(args.url, args.selector, args.output)
