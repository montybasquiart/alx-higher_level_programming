#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """A function that deletes the item at a specific position in a list.
    """
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return(my_list)
    else:
        new_list.extend(my_list[:idx])
        new_list.extend(my_list[idx + 1:])
        del my_list[idx]
        return (new_list)
