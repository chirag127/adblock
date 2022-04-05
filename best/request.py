import requests

with open("Custom/url.txt", "r") as file:
    urls = file.read()
for url in urls.split("\n"):
    if url != "":
        content = requests.get(url)

        if content != "":
            with open("Custom/results.txt", "a") as file:
                file.write(content.text)
