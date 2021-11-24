
import os

# define the function to LIST ALL THE FILES IN THE current DIRECTORY AND SUBDIRECTORIES


def list_all_files():
    # get the current directory
    current_dir = os.getcwd()
    # get the list of all files in the current directory
    files = os.listdir(current_dir)
    # get the list of all files in the current directory and subdirectories
    files_all = [os.path.join(current_dir, file) for file in files]
    # get the list of all files in the current directory and subdirectories
    files_all = [file for file in files_all if os.path.isfile(file)]

    print(files_all.sort())
    

list_all_files()


