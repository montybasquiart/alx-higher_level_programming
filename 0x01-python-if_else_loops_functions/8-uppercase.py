#!/usr/bin/python3
def uppercase(str):
    """A function that prints in UPPERCASE."""
    for char in str:
        value = ord(char)
        if value > 96 and value < 123:
            value -= 32
        print("{:c}".format(value), end="")
    print("")
