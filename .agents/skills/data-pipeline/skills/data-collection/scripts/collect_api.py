#!/usr/bin/env python3
import argparse
import requests
import json
import sys
from datetime import datetime

def collect(url, output_file, headers=None):
    parsed_headers = {}
    if headers:
        try:
            parsed_headers = json.loads(headers)
        except json.JSONDecodeError:
            print("Invalid JSON for headers", file=sys.stderr)
            sys.exit(1)

    try:
        response = requests.get(url, headers=parsed_headers, timeout=15)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"API Request failed: {e}", file=sys.stderr)
        sys.exit(1)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    record_count = len(data) if isinstance(data, list) else 1
    log = {
        "source_url": url,
        "accessed_at": datetime.utcnow().isoformat(),
        "extraction_method": "rest_api",
        "record_count": record_count
    }
    print(json.dumps(log))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch JSON from REST APIs.")
    parser.add_argument("--url", required=True, help="API Endpoint URL")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    parser.add_argument("--headers", help="JSON string of request headers (e.g., '{\"Authorization\": \"Bearer xyz\"}')")
    args = parser.parse_args()
    collect(args.url, args.output, args.headers)
