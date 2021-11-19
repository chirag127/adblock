
# write code to sort the lines in the files in the file_list 
# and overwrite the original files with the sorted lines


# write code to a list of urls in the files in the and sort them alphabetically and overwrite the original files
#  with the sorted list


# list all files in the current directory and directories within it
files = ['AD.txt', 'AL.txt', 'D.txt', 'E.txt', 'F.txt', 'FE.txt', 'N.txt', 'O.txt', 'P.txt', 'S.txt', 'T.txt', 'WL.txt' , 'UBOS/AD.txt', 'UBOS/AL.txt', 'UBOS/D.txt', 'UBOS/E.txt', 'UBOS/F.txt', 'UBOS/FE.txt', 'UBOS/N.txt', 'UBOS/O.txt', 'UBOS/P.txt', 'UBOS/S.txt', 'UBOS/T.txt', 'UBOS/WL.txt']



# define the function to convert the contents of the files to a list of strings
# content of the files is the list of strings separated by newlines
def convert_to_list(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
    return content

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

        # convert the file contents to a list of strings
        file_list = convert_to_list(file)

        # sort the list of strings
        sorted_list = sort_list(file_list)

        # write the sorted list to the file
        write_to_file(file, sorted_list)

    print('Done')


