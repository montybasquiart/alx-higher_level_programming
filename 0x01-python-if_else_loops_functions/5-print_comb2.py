#!/usr/bin/python3
def print_numbers():
    """A Function that prints numbers from 0 to 99.
    """


# This program prints numbers from 0 to 99
# Separated by "," followed by a space
# Numbers are printed in ascending order with two digits
for number in range(100):
    print("{:02d}".format(number), end=", " if number < 99 else "\n")

# Call the function to print numbers from 0 to 99
print_numbers()
