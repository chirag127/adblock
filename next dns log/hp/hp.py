import os

# Use os.path.join for cross-platform compatibility
raw_file = os.path.join("next dns log", "hp", "raw.txt")
output_file = os.path.join("next dns log", "hp", "hp.txt")

with open(raw_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        with open(output_file, "a") as f1:
            f1.write(f"0.0.0.0 {line}")
            f1.write("\n")
