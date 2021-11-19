#  list of items to put them in alphabetical order by last name is in the file input.txt

from os import read

# list of the files to be read
file_list = ['input.txt']


if __name__ == '__main__':

    for file in file_list:

        # read the file and put it in a list
        with open(file, 'r') as f:
            rules = f.read().splitlines()

        # split the rules into first and last name separated by commas or - or  -- or . or ## or . ## or ### [ or ] and put them in a list
        rules_list = []
        for rule in rules:
            rules_list.append(rule.split(','))
            


        # sort the list of the urls by last name
        rules.sort(key=lambda x: x.split(' ')[-1])


        # write the sorted list to the output file
        with open(file, 'w') as f:
            for rule in rules:
                f.write(rule + '\n')

        print('File {} sorted'.format(file))




    
