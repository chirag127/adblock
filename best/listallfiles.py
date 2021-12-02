# list all files in a directory

import os

for dir in os.listdir('.'):
    if os.path.isfile(dir):
        print(dir)