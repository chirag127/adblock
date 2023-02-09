import requests

urls = """https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_11_Mobile/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt"""
# https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt
# https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt
#
# https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt
# https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt
# https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt
# https://secure.fanboy.co.nz/fanboy-annoyance.txt
urls_list = urls.splitlines()


domains = """youtube.com
google.com
quora.com
reddit.com
twitter.com"""


# domain = "quora.com"

for domain in domains.splitlines():
    name_of_file = domain.replace(".", "_") + ".txt"

    for url in urls_list:
        response = requests.get(url)
        if response.status_code == 200:
            rules_list = response.text.splitlines()
            for rule in rules_list:

                if domain in rule and not rule.startswith("!"):
                    with open(f"UBOS/{name_of_file}", "a", encoding="utf8") as f:
                        f.write(rule + "\n")



        else:
            print(f"Error in {url}")
