# write code to a list of urls in the files in the and sort them alphabetically and overwrite the original files
#  with the sorted list

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
    return files_all

    




# list all files in the current directory and directories within it
files = ['AD.txt', 'AL.txt', 'D.txt', 'E.txt', 'F.txt', 'FE.txt', 'N.txt', 'O.txt', 'P.txt', 'S.txt', 'T.txt', 'WL.txt' , 'UBOS/AD.txt' , 'UBOS/AAll.txt']


# define the function to convert the contents of the files to a list of strings
# content of the files is the list of strings separated by newlines
def convert_to_list(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
    return content

# remove empty lines from the list of strings
def remove_empty_lines(list):
    return [line for line in list if line.strip()]
    
# define the function to sort the list of strings
def sort_list(list):
    return sorted(list)

def join_list(list):
    return '\n'.join(list)


# define the function to write the sorted list to the files
def write_to_file(filename, list):
    with open(filename, 'w') as file:
        file.writelines(list)


if __name__ == '__main__':

    # loop through the list of files
    for file in files:

        # convert the contents of the files to a list of strings
        content = convert_to_list(file)

        # remove empty lines from the list of strings
        content = remove_empty_lines(content)

        # sort the list of strings
        content = sort_list(content)

        content = join_list(content)

        # write the sorted list to the files

        write_to_file(file, content)

    print('Done')


