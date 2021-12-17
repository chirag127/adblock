import glob

read_files = glob.glob("*.txt")

for f in read_files:
    print(f)
