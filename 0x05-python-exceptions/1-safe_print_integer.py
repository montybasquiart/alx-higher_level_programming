#!/usr/bin/python3
def safe_print_integer(value):
    """A function that prints an integer with "{:d}".format().
    """
    try:
        print("{:d}".format(value))
        return True
    except IndexError:
        return False
