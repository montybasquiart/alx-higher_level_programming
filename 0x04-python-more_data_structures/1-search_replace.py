#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurences of an element by another in a new
    list.
    """
    new_list = []
    for numbers in my_list:
        if numbers == search:
            new_list.append(replace)
        else:
            new_list.append(numbers)
    return new_list
