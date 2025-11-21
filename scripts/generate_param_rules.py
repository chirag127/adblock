"""
This script generates rule parameters from a list of URLs.
"""
import pathlib
from urllib.parse import urlparse, parse_qs

# Configuration
ROOT_DIR = pathlib.Path('.')
SCRIPT_DIR = pathlib.Path('scripts')
URL_FILE = SCRIPT_DIR / 'url.txt'
TARGET_FILE = ROOT_DIR / 'chirag_annoyance_filters/AntiUrlTrackingParameter.txt'

def main():
    """
    Main function to process URLs and generate rules.
    """
    if not URL_FILE.exists():
        # Check old location just in case
        old_url_file = pathlib.Path('python files/make_param/url.txt')
        if old_url_file.exists():
            print("Found url.txt in old location.")
        else:
            print(f"No input file found at {URL_FILE}. Please create it to use this tool.")
            return

    with open(URL_FILE, "r", encoding='utf-8') as file:
        urls = file.readlines()

    if not urls:
        print("No URLs to process.")
        return

    count = 0
    # Append to the target file
    with open(TARGET_FILE, "a", encoding='utf-8') as f:
        for url in urls:
            url = url.strip()
            if not url:
                continue

            try:
                parsed_url = urlparse(url)
                domain = parsed_url.netloc
                query = parse_qs(parsed_url.query)

                for key, _ in query.items():
                    # AdGuard syntax for removing param
                    rule = f"||{domain}^$removeparam={key}"
                    f.write(f"\n{rule}")
                    count += 1
            except Exception as e: # pylint: disable=broad-exception-caught
                print(f"Error processing URL {url}: {e}")

    # Clear the url file
    with open(URL_FILE, "w", encoding='utf-8') as f:
        f.write("")

    print(f"Appended {count} rules to {TARGET_FILE}.")

if __name__ == "__main__":
    main()
