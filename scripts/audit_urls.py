import os
import re
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

# Configuration
TIMEOUT = 15
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}
IGNORE_DIRS = {".git", ".github", ".vscode", "__pycache__", "node_modules", "venv", ".ruff_cache", "site-packages"}
IGNORE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pyc", ".exe", ".dll", ".bin", ".zip", ".gz", ".pdf", ".svg"}

def extract_urls_and_domains(text):
    """Extracts URLs and domains from text using regex."""
    urls = set()

    # Standard URLs
    # Matches http:// or https:// followed by non-whitespace/non-quote chars
    url_pattern = re.compile(r'https?://[a-zA-Z0-9.-]+(?:/[^\s<>"\'()\[\]]*)?')
    urls.update(url_pattern.findall(text))

    # Adblock syntax domains
    # ||example.com^ or ||example.com$
    adblock_pattern = re.compile(r'\|\|([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:[\^\$]|$)')
    for match in adblock_pattern.findall(text):
        urls.add(f"http://{match}")

    # domain=example.com
    domain_param_pattern = re.compile(r'domain=([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
    for match in domain_param_pattern.findall(text):
        urls.add(f"http://{match}")

    return urls

def check_url(url):
    """Checks if a URL is reachable. Returns (url, is_broken, status_code/error)."""
    try:
        # Some sites block HEAD, so we try HEAD first then GET
        response = requests.head(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)

        # If HEAD fails with 405 (Method Not Allowed) or 404/403, try GET to be sure
        # actually 404 on HEAD usually means 404 on GET, but 405/403/400 might be server quirks
        if response.status_code >= 400:
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT, stream=True)

        if response.status_code >= 400:
            # 403 Forbidden is often bot protection. We SKIP deleting these to be safe.
            if response.status_code == 403:
                return url, False, 403
            return url, True, response.status_code

        return url, False, response.status_code

    except requests.RequestException as e:
        # DNS errors, connection refused, timeouts -> Broken
        return url, True, str(e)
    except Exception as e:
        return url, True, str(e)

def process_file(filepath, dry_run=True):
    """Reads a file, checks URLs, and removes lines with broken URLs."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0

    urls_in_file = set()
    for line in lines:
        urls_in_file.update(extract_urls_and_domains(line))

    if not urls_in_file:
        return 0

    print(f"Scanning {filepath} ({len(urls_in_file)} URLs)...")

    broken_urls = set()
    # Check URLs concurrently
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in urls_in_file}
        for future in as_completed(future_to_url):
            url, is_broken, status = future.result()
            if is_broken:
                print(f"  [BROKEN] {url} -> {status}")
                broken_urls.add(url)

    if not broken_urls:
        return 0

    new_lines = []
    removed_count = 0

    for line in lines:
        line_urls = extract_urls_and_domains(line)
        should_remove = False

        # If any URL in the line is broken, we flag the line for removal
        for url in line_urls:
            if url in broken_urls:
                should_remove = True
                break

        if should_remove:
            removed_count += 1
            if dry_run:
                print(f"  [DRY RUN] Would remove: {line.strip()}")
        else:
            new_lines.append(line)

    if not dry_run and removed_count > 0:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"  [REMOVED] {removed_count} lines from {filepath}")
        except Exception as e:
            print(f"Error writing {filepath}: {e}")

    return removed_count

def main():
    parser = argparse.ArgumentParser(description="Audit and remove obsolete URLs.")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be removed without doing it.")
    parser.add_argument("--path", default=".", help="Root directory to scan.")
    args = parser.parse_args()

    total_removed = 0

    print(f"Starting audit in '{args.path}' (Dry run: {args.dry_run})")

    for root, dirs, files in os.walk(args.path):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if any(file.endswith(ext) for ext in IGNORE_EXTS):
                continue

            filepath = os.path.join(root, file)
            # Skip the script itself
            if os.path.abspath(filepath) == os.path.abspath(__file__):
                continue

            total_removed += process_file(filepath, dry_run=args.dry_run)

    print(f"\nTotal lines {'would be ' if args.dry_run else ''}removed: {total_removed}")

if __name__ == "__main__":
    main()
