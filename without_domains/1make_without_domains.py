from typing import List
import requests

def get_rules(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        raise Exception("Something went wrong while getting the rules")

def remove_domains(rules_list: List[str]) -> List[str]:
    new_rules_list = []
    for rule in rules_list:
        if (
            rule.startswith("||")
            and (rule.endswith("^") or rule.endswith("^$third-party"))
            or rule.startswith("!")
        ):
            pass
        else:
            new_rules_list.append(rule)
    return new_rules_list

def remove_domains(rules_list: List[str]) -> List[str]:
    new_rules_list = []
    for rule in rules_list:
        if (
            rule.startswith("||")
            and (rule.endswith("^") or rule.endswith("^$third-party"))
            or rule.startswith("!")
        ):
            pass
        else:
            new_rules_list.append(rule)
    return new_rules_list

def remove_duplicates(rules_list):
    return list(set(rules_list))

def sort_list(rules_list):
    rules_list.sort()
    return rules_list

def save_rules(name, rules_list):
    with open(f"without_domains/{name}.txt", "w", encoding="utf8") as f:
        f.write("\n".join(rules_list))

def main():
    adguard_registry = (
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/"
    )
    urls = {
        "AdGuard tracking": adguard_registry + "filter_3_Spyware/filter.txt",
        "AdGuard social": adguard_registry + "filter_4_Social/filter.txt",
        "AdGuard annoyances": adguard_registry + "filter_14_Annoyances/filter.txt",
        "easyprivacy": "https://filters.adtidy.org/extension/ublock"
        + "/filters/118_optimized.txt",
    }

    for name, url in urls.items():
        rules_list = get_rules(url)
        rules_list = remove_domains(rules_list)
        rules_list = remove_duplicates(rules_list)
        rules_list = sort_list(rules_list)
        save_rules(name, rules_list)

if __name__ == "__main__":
    main()
