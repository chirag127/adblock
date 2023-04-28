"""This script removes domains from the rules and saves them in the
without_domains folder.
"""

from typing import Dict, List

import requests


def get_rules(url):
    """
    Get the rules from the url.
    :param url: The url of the rules.
    :return: A list of rules.
    """
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        raise Exception("Something went wrong while getting the rules")


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
    with open(f"without_domains/{name}.txt", "w", encoding="utf8") as f:
        f.write("\n".join(rules_list))


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
    main()
