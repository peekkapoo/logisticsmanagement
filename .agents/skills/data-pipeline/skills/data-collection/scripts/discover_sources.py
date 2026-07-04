#!/usr/bin/env python3
import argparse
import httpx
from urllib.parse import urljoin, urlparse
import sys

def discover(url):
    print(f"Probing {url} for common data endpoints...")
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    
    targets = {
        "Robots.txt": urljoin(base, "/robots.txt"),
        "Sitemap": urljoin(base, "/sitemap.xml"),
        "RSS/Atom Feed": urljoin(base, "/feed/"),
        "API Index": urljoin(base, "/api/")
    }

    for name, target in targets.items():
        try:
            r = httpx.head(target, timeout=5)
            if r.status_code == 200:
                print(f"[FOUND] {name}: {target}")
            else:
                print(f"[MISSING] {name}: {target} (Status: {r.status_code})")
        except Exception:
            print(f"[ERROR] {name}: Connection failed to {target}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Discover sitemaps, RSS, and robots.txt on a domain.")
    parser.add_argument("--url", required=True, help="Base URL to probe")
    args = parser.parse_args()
    discover(args.url)
