import requests

file = open("Custom/url.txt", "r")
urls = file.read()
file.close()

for url in urls.split("\n"):
    if url != "":
        content = requests.get(url)

        if content != "":
            file = open("Custom/results.txt", "a")
            file.write(content.text)
            file.close()
