#!/usr/bin/python3
def weight_average(my_list=[]):
    """A function that returns the weighted average of all integers tuple.
    """
    if not my_list:
        return 0
    sum = 0
    total_weights = 0
    for score, weight in my_list:
        sum += score * weight
        total_weights += weight

    return sum / total_weights
