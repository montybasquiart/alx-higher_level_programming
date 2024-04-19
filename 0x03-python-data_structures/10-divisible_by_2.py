#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """A function that finds all multiples of 2 in a list.
    """
    multiple_numbers = []
    for numbers in my_list:
        multiple_numbers.append(numbers % 2 == 0)
    return multiple_numbers
