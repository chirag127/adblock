# write code to sort the lines in the files in the file_list
# and overwrite the original files with the sorted lines


# list all files in the current directory and directories within it
files = ['i.txt']

# define function to get the content of the file


def get_content(file):
    with open(file, 'r') as f:
        content = f.read()
    return content


# define the function to convert the content to the list of strings


def convert_to_list(content):
    return content.split('\n')

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
        content = get_content(file)

        # reverse the strings
        content = content[::-1]

        content = convert_to_list(content)

        # remove empty lines from the list of strings
        content = remove_empty_lines(content)

        # sort the list of strings
        content = sort_list(content)

        content = join_list(content)

        # reverse the strings
        content = content[::-1]

        # write the sorted list to the files
        write_to_file(file, content)
