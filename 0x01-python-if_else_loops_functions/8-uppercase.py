#!/usr/bin/python3
def uppercase(str):
    """A Function that prints a string in UPPERCASE.
    """
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) < 123:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(str[char]) - letter), end="")
    print()
