# Chirag Personal Filter lists

[![syntax](https://img.shields.io/badge/syntax-AdGuard-%23c61300.svg)](https://kb.adguard.com/en/general/how-to-create-your-own-ad-filters)

A personal filter list of mine with additional filters for AdGuard to block third-party, tracking, annoyances, anti-adblock, resource-abuse and all other unwarranted resources.

Contains filters specific to AdGuard and some filters that have not yet been added to other filter lists.

## Requirements

The requirements to use these lists in chromium based desktop browser is that AdGuard AdBlocker extension should be already installed on a chromium based desktop browser.

You can install the extension from [here](https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg).

## Maintenance

To maintain and update the lists, use the scripts in the `scripts/` directory.

### Updating and Sorting Filters

Run `scripts/maintain.py` to sort all filter files, remove duplicates, and regenerate the aggregate `A.txt` list.

```bash
python3 scripts/maintain.py
```

### Generating Parameter Removal Rules

To generate parameter removal rules from a list of URLs:
1. Add URLs to `scripts/url.txt`.
2. Run `scripts/generate_param_rules.py`.
3. The rules will be appended to `chirag_annoyance_filters/AntiUrlTrackingParameter.txt`.

```bash
python3 scripts/generate_param_rules.py
```

## Lists

### Chirag's Lists






##### This list indented to be used with no comment list and Fanboy's anti-comment list














> People using DNS blocking don't need to use the complete AdGuard Tracking Protection List as approx 80% rules of the AdGuard Tracking Protection List are domains which are already blocked by AdGuard DNS or other DNS blocking services. The same concept can not be applied to AdGuard Base as AdGuard extension also blocks the frame and placeholders of the domains and URLs blocked by it and if the user wants to block the frame and place blocks the placeholder of the ads, then the user needs to use the complete AdGuard Base filtering list.

## Disclaimer

As this is a **personal** filter list of mine, there maybe some filters that you disagree with and if you do, feel free to click on the **fork** button and make your own list.
