import requests
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resourceabuse.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt

urls = """
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_English/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt"""

urls_list = urls.split()

domain = "a"

for url in urls_list:
    response = requests.get(url)
    if response.status_code == 200:
        rules_list = response.text.splitlines()
        for rule in rules_list:
            if domain in rule and not rule.startswith("!"):
                with open("add.txt", "a") as f:
                    f.write(rule + "\n")
    else:
        print("Error")


