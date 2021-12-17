# open all url in file custom/url.txt
import webbrowser

File = open("custom/url.txt", "r")

urls = File.read().splitlines()

for url in urls:
    webbrowser.open(url)
