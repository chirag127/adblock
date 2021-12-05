import requests


urls = """https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt
https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt
https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt
https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt
https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resourceabuse.txt
https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt
https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt
https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_English/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt
https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt"""

urls_list = urls.split()

domain = "daum"


for url in urls_list:
    response = requests.get(url)
    if response.status_code == 200:
        rules_list = response.text.split('\n')
        for rule in rules_list:
            # write rule to sitespecific/domain.txt if it contains domain
            if domain in rule:
                f = open(f"best/sitespecific/{domain}.txt", "a")
                f.write(rule + '\n' + "filterlist = " + url + '\n' )

print("Done!")