# add all txt files to the current directory
import os

file = open('A.txt', 'w')

file.write("""! Description: It contains all list
! Expires: 1 hours
! Homepage: https://github.com/chirag127/adblock/
! Title: Chirag's All Annoyances list
""")

for dir in os.listdir('.'):

    if dir.endswith('.txt'):

        file.write( '\n'+'!#include ' + dir )

