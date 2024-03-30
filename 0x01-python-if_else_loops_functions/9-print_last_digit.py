#!/usr/bin/python3
def print_last_digit(number):
    """A function that prints the last digit of a number.
    """
    last_digit = abs(number) % 10
    # prints the last digit.
    print(last_digit, end="")
    # returns the last digit as the function's output.
    return last_digit
