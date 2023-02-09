import requests

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
    response = requests.get(url)
    if response.status_code == 200:
        rules_list = response.text.splitlines()

        new_rules_list = []
        for rule in rules_list:

            # check if the rule is a domain
            if (
                rule.startswith("||")
                and (rule.endswith("^") or rule.endswith("^$third-party"))
                or rule.startswith("!")
            ):

                pass

            else:

                new_rules_list.append(rule)

        # remove duplicates
        new_rules_list = list(set(new_rules_list))


        # sort the list
        new_rules_list.sort()


        with open(f"without_domains/{name}.txt", "w", encoding="utf8") as f:
            f.write("\n".join(new_rules_list))
