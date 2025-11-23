import os
import requests
import re

def main():
    url = "https://gitflic.ru/project/magnolia1234/bypass-paywalls-clean-filters/blob/raw?file=bpc-paywall-filter.txt"
    output_dir = "domain"
    output_file = os.path.join(output_dir, "bpc-paywall-filter-domains.txt")

    print(f"Downloading filter list from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
    except Exception as e:
        print(f"Error downloading file: {e}")
        return

    domains = set()
    # Regex to capture domain from adblock syntax like ||example.com^ or ||example.com$
    # It looks for ||, then captures characters until ^, $, or end of line.
    # It ensures there is no path (/) after the domain.
    pattern = re.compile(r"^\|\|([a-zA-Z0-9.-]+)(?:[\^\$]|$)")

    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("!"):
            continue

        match = pattern.match(line)
        if match:
            domain = match.group(1)
            domains.add(domain)

    sorted_domains = sorted(list(domains))

    print(f"Extracted {len(sorted_domains)} domains.")

    os.makedirs(output_dir, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        for domain in sorted_domains:
            f.write(domain + "\n")

    print(f"Saved domains to {output_file}")

if __name__ == "__main__":
    main()
