#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurrences of an element by another in a new
    list.
    """
    return [numbers if not numbers == search else replace for numbers in my_list]