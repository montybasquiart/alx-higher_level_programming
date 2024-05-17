#!/usr/bin/python3
def uniq_add(my_list=[]):
    """A function that adds all unique integers in a list (only once for each integer).
    """
    unique_int = set(my_list)
    add_result = sum(unique_int)
    return add_result