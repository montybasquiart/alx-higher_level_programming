#!/usr/bin/python3
def best_score(a_dictionary):
    """ A function that returns a key with the biggest integer value.
    """

    if not a_dictionary:
        return None
    
    max_value = max(a_dictionary.values())
    
    for key in a_dictionary:
        if a_dictionary[key] == max_value:
            return key
