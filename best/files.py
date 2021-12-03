
import os

# define the function to LIST ALL THE FILES IN THE current DIRECTORY AND SUBDIRECTORIES



import os

files = []

#  Add all files to a list
for dir in os.listdir('.'):

    if dir.endswith('.txt'):
        files.append(dir)
        print(dir)


#  print number of items in the list
print(len(files))
