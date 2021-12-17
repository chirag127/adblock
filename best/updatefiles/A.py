# add all txt files to the current directory

import os

files = []

#  Add all files to a list
for dir in os.listdir("."):

    if dir.endswith(".txt"):
        files.append(dir)


# remove NF.txt from the list
files.remove("A.txt")


file = open("A.txt", "w")

file.write(
    """! Description: It contains all list
! Expires: 1 hours
! Homepage: https://github.com/chirag127/adblock/
! Title: Chirag's All Annoyances list
"""
)

for dir in files:

    if dir.endswith(".txt"):

        file.write("!#include " + dir + "\n")
