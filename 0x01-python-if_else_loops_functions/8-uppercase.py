#!/usr/bin/python3
def uppercase(str):
    """A function that prints strings in UPPERCASE."""
    for i in str:
        value = ord(i)
        if value > 96 and value < 123:
            value -= 32
        print("{:c}".format(value), end="")
    print("")
