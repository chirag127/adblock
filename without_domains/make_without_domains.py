"""This script removes domains from the rules and saves them in the
without_domains folder.
"""

from typing import Dict, List

import requests
import os
import sys
import glob


def get_rules(url):
    """
    Get the rules from the url.
    :param url: The url of the rules.
    :return: A list of rules.
    """
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.text.splitlines()


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


def makeAllListForWithoutDomains() -> None:

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

    adguard_registry: str = (
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/"
    )
    urls: Dict[str, str] = {
        "AdGuard tracking": adguard_registry + "filter_3_Spyware/filter.txt",
        "AdGuard social": adguard_registry + "filter_4_Social/filter.txt",
        "AdGuard annoyances": adguard_registry + "filter_14_Annoyances/filter.txt",
        "easyprivacy": "https://filters.adtidy.org/extension/ublock"
        + "/filters/118_optimized.txt",
        "bpc-paywall-filter": "https://gitlab.com/magnolia1234/"
        + "bypass-paywalls-clean-filters/-/raw/main/bpc-paywall-filter.txt",
    }

    for name, url in urls.items():
        rules_list: List[str] = get_rules(url)
        rules_list: List[str] = remove_domains(rules_list)
        rules_list: List[str] = remove_duplicates(rules_list)
        rules_list: List[str] = sort_list(rules_list)
        save_rules(name, rules_list)


if __name__ == "__main__":

    if not os.path.exists("without_domains"):
        os.makedirs("without_domains")


    try:
        makeAllListForWithoutDomains()
        main()
    except Exception as e:
        print(e)
        sys.exit(1)
    else:
        sys.exit(0)
