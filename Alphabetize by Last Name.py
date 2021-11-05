

# sort a list of tuples by last name in ascending order and print the result to the screen
# input: list of tuples formatted as by newline
# output: sorted list of tuples

def main():
    # get the list of tuples
    list_of_tuples = get_list_of_tuples()
    # sort the list of tuples
    sorted_list_of_tuples = sort_list_of_tuples(list_of_tuples)
    # print the sorted list of tuples
    print_list_of_tuples(sorted_list_of_tuples)

    # key = lambda x: x[1]

    sorted_list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1])

    print_list_of_tuples(sorted_list_of_tuples)
    