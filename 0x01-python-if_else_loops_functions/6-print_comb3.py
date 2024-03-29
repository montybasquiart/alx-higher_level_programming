#!/usr/bin/python3
def print_combinations():
    """A function that prints all possible diff combinations of two digits.
    """


# A program that prints all possible different combinations of two digits
# Numbers must be separated by "," followed by a space
# 01 and 10 are considered the same combinations of the two digits 0 and 1

for tens in range(10):
    for units in range(tens + 1, 10):
        print("{:02d}".format(tens * 10 + units), end="")
        # This line of code was fixed in my dream
        if tens != 8 and units != 10:
            print(", ", end="")
print("")
