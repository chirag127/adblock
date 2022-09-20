import os
import requests

url = "https://filters.adtidy.org/extension/ublock/filters/118_optimized.txt"
print("Downloading", url)
r = requests.get(url)
print("Downloaded", len(r.text), "bytes")
rules = r.text.splitlines()
file_name = "easyprivacy.txt"
file_path = os.path.join(os.path.dirname(__file__), file_name)
# remove rules that starts with || and end with ^ or starts with || and end with ^$third-party
for i in range(len(rules)):
    if rules[i].startswith("||") and (
        rules[i].endswith("^") or rules[i].endswith("^$third-party")
    ):
        rules[i] = ""
# remove empty lines
rules = [x for x in rules if x]
print("Writing", len(rules), "rules to", file_path)
with open(file_path, "w", encoding="utf-8") as f:
    for rule in rules:
        f.write(rule + "\n")

