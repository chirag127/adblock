"""
make files for each site with all the rules from all the lists
"""
# pylint: disable=duplicate-code
import requests

# pylint: disable=line-too-long
URLS = [
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_11_Mobile/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
]
# pylint: enable=line-too-long

DOMAINS = [
    "youtube.com",
    "google.com",
    "quora.com",
    "reddit.com",
    "twitter.com",
    "facebook.com",
    "instagram.com",
    "tiktok.com",
    "twitch.tv",
]


for domain in DOMAINS:
    file_name_domain = (
        f"extract_sites_specific/all_rules_for_popular_sites_"
        f"{domain.replace('.', '_')}.txt"
    )

    for url in URLS:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                rules_list = response.text.splitlines()
                for rule in rules_list:

                    if domain in rule and not rule.startswith("!"):
                        with open(file_name_domain, "a", encoding="utf8") as file:
                            file.write(rule + "\n")
            else:
                print(f"Error in {url}: Status code {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
