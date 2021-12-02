
import os

files = []

#  Add all files to a list
for dir in os.listdir('.'):

    if dir.endswith('.txt'):
        files.append(dir)


# remove NF.txt from the list
files.remove('Y.txt')




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

        # write the sorted list to the files

        write_to_file(file, content)

    print('Done')
