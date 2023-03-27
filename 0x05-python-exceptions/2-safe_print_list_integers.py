#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ Prints the first x elements of a list and only integers
    Args:
        my_list (list): List
        x (int): Number of integer elements from my_list to print
    Returns:
        The number of elements printed.
    """

    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num)
