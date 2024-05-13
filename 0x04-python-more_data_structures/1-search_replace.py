#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurences of an element by another in a new
    list.
    """
    replaced_list = [0 for numbers in range(len(my_list))]
    for numbers in range(len(my_list)):
        if my_list[numbers] == search:
            replaced_list[numbers] = replace
        else:
            replaced_list[numbers] = my_list[numbers]
    return replaced_list
