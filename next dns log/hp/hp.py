"""
This script processes the raw.txt file and converts it to a hosts file format in hp.txt.
"""

import os

# Use os.path.join for cross-platform compatibility
RAW_FILE = os.path.join("next dns log", "hp", "raw.txt")
OUTPUT_FILE = os.path.join("next dns log", "hp", "hp.txt")

with open(RAW_FILE, encoding="utf-8") as f:
    lines = f.readlines()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
    for line in lines:
        line = line.strip()
        if line:
            f_out.write(f"0.0.0.0 {line}\n")
