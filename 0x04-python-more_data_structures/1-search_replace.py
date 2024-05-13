#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurrences of an element by another
    in a new list.
    """
    return [num if not num == search else replace for num in my_list]
