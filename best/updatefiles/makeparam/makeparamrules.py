
from urllib.parse import urlparse
from urllib.parse import parse_qs

file = open("best/updatefiles/url.txt", "r")


for url in file:
    url = url.strip()
    domain = urlparse(url).netloc
    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)
    for key, value in query.items():
        with open("P.txt", "a") as f:
            f.write(f"||{domain}^$removeparam={key}\n")

with open("best/updatefiles/makeparam/url.txt", "w") as f:
    f.write("")