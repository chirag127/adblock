# add all txt files to the current directory
import os

f = open('A.txt', 'w')

# list all txt files in the current directory
def listTxtFiles():
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            print(file)
            f.write(file + '\n')
                
    listTxtFiles()
    f.close()

    
