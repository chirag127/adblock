"""This script removes domains from the rules and saves them in the
without_domains folder.
"""

import glob
import os
import sys
from typing import Dict, List
import requests


def get_rules(url):
    """
    Get the rules from the url.
    :param url: The url of the rules.
    :return: A list of rules.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text.splitlines()

        print(f"Error fetching {url}: Status code {response.status_code}")
        return []
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []


def remove_domains(rules_list: List[str]) -> List[str]:
    """
    Remove domains from the rules.
    :param rules_list: A list of rules.
    :return: A list of rules without domains.
    """

    # or rule.endswith("^$third-party")

    new_rules_list = []
    for rule in rules_list:
        if (rule.startswith("||") and (rule.endswith("^"))) or rule.startswith("!"):
            pass
        else:
            new_rules_list.append(rule)
    return new_rules_list


def remove_duplicates(rules_list: list) -> list:
    """
    Remove duplicates from the rules.
    :param rules_list: A list of rules.
    :return: A list of rules without duplicates.
    """
    return list(set(rules_list))


def sort_list(rules_list: list) -> list:
    """
    Sort the rules.
    :param rules_list: A list of rules.
    :return: A sorted list of rules.
    """

    rules_list.sort()
    return rules_list


def save_rules(name: str, rules_list: list) -> None:
    """
    Save the rules in a file.
    :param name: The name of the file.
    :param rules_list: A list of rules.
    :return: None
    """

    with open(f"without_domains/{name}.txt", "w", encoding="utf8") as file:
        file.write("\n".join(rules_list))


def make_all_list_for_without_domains() -> None:
    """
    Combines all generated lists into one file.
    """

    # /workspaces/adblock/without_domains
    all_files = glob.glob("without_domains/*.txt")

    # remove the all.txt file and .py file
    all_files = [x for x in all_files if not x.endswith("all.txt")]
    all_files = [x for x in all_files if not x.endswith(".py")]

    with open("without_domains/all.txt", "w", encoding="utf8") as file:

        file.write("! Description: It contains all list without domains\n")
        file.write("! Expires: 1 hours\n")
        file.write("! Homepage: https://github.com/chirag127/adblock/\n")
        file.write("! Title: Chirag's without domains list\n")

        for file_name in all_files:
            with open(file_name, "r", encoding="utf8") as f:
                file.write(f.read())
                file.write("\n")

def main() -> None:
    """
    Main function.

    :return: None
    """

    # AdGuard Filters Registry URLs
    # Source: https://adguard.com/kb/general/ad-filtering/adguard-filters/
    adguard_registry: str = (
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/"
    )

    urls: Dict[str, str] = {
        # AdGuard Base filter - removes ads from English websites
        "AdGuard Base": adguard_registry + "filter_2_Base/filter.txt",

        # Tracking Protection filter - blocks online counters and web analytics
        "AdGuard Tracking Protection": adguard_registry + "filter_3_Spyware/filter.txt",

        # Social media filter - removes social media buttons and integrations
        "AdGuard Social Media": adguard_registry + "filter_4_Social/filter.txt",

        # Annoyances filter - blocks irritating elements on web pages
        "AdGuard Annoyances": adguard_registry + "filter_14_Annoyances/filter.txt",

        # Cookie Notices filter - blocks cookie notices
        "AdGuard Cookie Notices": adguard_registry + "filter_18_Annoyances_Cookies/filter.txt",

        # Popups filter - blocks all kinds of popups
        "AdGuard Popups": adguard_registry + "filter_19_Annoyances_Popups/filter.txt",

        # Mobile App Banners filter - blocks mobile app promotion banners
        "AdGuard Mobile App Banners": (
            adguard_registry + "filter_20_Annoyances_MobileApp/filter.txt"
        ),

        # Other Annoyances filter - blocks other annoyances
        "AdGuard Other Annoyances": adguard_registry + "filter_21_Annoyances_Other/filter.txt",

        # Widgets filter - blocks third-party widgets
        "AdGuard Widgets": adguard_registry + "filter_22_Annoyances_Widgets/filter.txt",

        # URL Tracking filter - removes tracking parameters from URLs
        "AdGuard URL Tracking": adguard_registry + "filter_17_TrackParam/filter.txt",

        # Mobile ads filter - blocks ads on mobile devices
        "AdGuard Mobile Ads": adguard_registry + "filter_11_Mobile/filter.txt",

        # EasyPrivacy (optimized for uBlock)
        "EasyPrivacy": "https://filters.adtidy.org/extension/ublock/filters/118_optimized.txt",

        # Bypass Paywalls Clean filter - filters for news sites
        # Source: https://gitflic.ru/project/magnolia1234/bypass-paywalls-clean-filters
        # pylint: disable=line-too-long
        "Bypass Paywalls Clean": "https://gitflic.ru/project/magnolia1234/bypass-paywalls-clean-filters/blob/raw?file=bpc-paywall-filter.txt",
    }

    for name, url in urls.items():
        print(f"Processing {name}...")
        rules_list = get_rules(url)
        if rules_list:
            rules_list = remove_domains(rules_list)
            rules_list = remove_duplicates(rules_list)
            rules_list = sort_list(rules_list)
            save_rules(name, rules_list)
            print(f"Saved {len(rules_list)} rules for {name}")
        else:
            print(f"No rules found for {name}")


if __name__ == "__main__":

    if not os.path.exists("without_domains"):
        os.makedirs("without_domains")


    try:
        main()  # Generate individual files first
        make_all_list_for_without_domains()  # Then combine them into all.txt
    except Exception as e: # pylint: disable=broad-exception-caught
        print(e)
        sys.exit(1)
    else:
        sys.exit(0)
