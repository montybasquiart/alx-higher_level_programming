#!/usr/bin/python3
def print_numbers():
    """A function that prints all numbres from 0 to 98.
    """


# Print numbers from "0" to "98" in decimal and hexadecimal
for number in range(0, 99):
    print("{:d} = 0x{:x}".format(number, number))

# Call the function to print numbers from 0 to 98 in decimal and hexadecimal
print_numbers()
