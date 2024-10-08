#!/usr/bin/python3
def safe_print_integer_err(value):
    """A function that prints an integer
    """
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
