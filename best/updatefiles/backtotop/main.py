from typing import ContextManager
import requests
import os

url = "https://filters.adtidy.org/extension/ublock/filters/122_optimized.txt"


Content = requests.get(url).text

for line in Content.splitlines():

    f = open("GEN\B.txt", "a")

    if line.startswith("##"):
        if "back" in line and "top" in line:
            f.write(line + "\n")
        if "scroll" in line and "top" in line:
            f.write(line + "\n")
    f.close()
