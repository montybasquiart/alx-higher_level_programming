#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """A function that prints all integers of a list.
    """
    my_list = [1, 2, 3, 4, 5]

    for i in my_list:
        print("{i}".format(i=i), end="\n")
