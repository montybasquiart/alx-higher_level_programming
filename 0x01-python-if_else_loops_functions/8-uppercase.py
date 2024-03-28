#!/usr/bin/python3
def uppercase(str):
    """A Function that prints a string in UPPERCASE.
    """
    for char in str:
        if ord(char) >= 97 and ord(char) < 123:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(char) - letter), end="")
    print()
