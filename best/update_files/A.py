# add all txt files to the current directory

import os

files = [dir for dir in os.listdir(".") if dir.endswith(".txt")]

# remove NF.txt from the list
files.remove("A.txt")


file = open("A.txt", "w")


file.write(
    """! Description: It contains all list
! Expires: 1 hours
! Homepage: https://github.com/chirag127/adblock/
! Title: Chirag's Annoyance list
"""
)

for dir in files:

    if dir.endswith(".txt"):

        file.write(f"!#include {dir}" + "\n")
