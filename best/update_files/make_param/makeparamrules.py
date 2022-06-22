from urllib.parse import urlparse
from urllib.parse import parse_qs
file_path = "best\\update_files\\make_param\\url.txt"

file = open(file_path, "r")


for url in file:
    url = url.strip()
    domain = urlparse(url).netloc
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)
    for key, value in query.items():
        with open("P.txt", "a") as f:
            f.write(f"\n||{domain}^$removeparam={key}")

with open(file_path, "w") as f:
    f.write("")
