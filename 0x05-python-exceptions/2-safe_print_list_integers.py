#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list and only integers.
    """
    printed_int = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            printed_int += 1
        except (ValueError, TypeError):
            pass
    print()
    return printed_int
