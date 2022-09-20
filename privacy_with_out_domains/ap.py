# import os
# import requests


# url = "https://filters.adtidy.org/extension/ublock/filters/118_optimized.txt"

# print("Downloading", url)

# r = requests.get(url)


# print("Downloaded", len(r.text), "bytes")

# rules = r.text.splitlines()

# # urls = """https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies.txt
# # https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/css_extended.txt
# # https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_elemhide.txt
# # https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_extensions.txt
# # https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_url.txt
# # https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/specific.txt
# # https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/whitelist.txt"""
# # file_name = "ap.txt"

# urls = """https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_allowlist.txt
# https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_general.txt
# https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_specific.txt
# https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_thirdparty.txt"""

# file_name = "easyprivacy.txt"


# file_path = os.path.join(os.path.dirname(__file__), file_name)

# all_urls = urls.split("\n")

# print("Downloading", len(all_urls), "files")

# all_rules = []
# for url in urls.splitlines():

#     r = requests.get(url)

#     all_rules.extend(r.text.splitlines())


# all_rules = set(all_rules)

# rules = set(rules)

# # get the intersection of the two sets
# intersection = rules.intersection(all_rules)

# intersection = list(intersection)

# # remove rules which starts with || and end with ^
# for i in intersection:
#     if i.startswith ("||"):
#         intersection.remove(i)

# new_intersection = []
# for i in intersection:
#     if not i.startswith("||") and not i.endswith("^"):
# # write the intersection to a file privacy_with_out_domains\ap.txt

# # write the intersection with join with newline
# rules_to_write = "\n".join(intersection)
# with open(file_path, "w") as f:
#     f.write(rules_to_write)

# print("Done")
