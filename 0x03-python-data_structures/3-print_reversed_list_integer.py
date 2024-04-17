#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list, in a reverse order.

    Args:
    my_list: The list of int to print. Defaults to []
    """
    for number in reversed(my_list):
        print("{:d}".format(number)
