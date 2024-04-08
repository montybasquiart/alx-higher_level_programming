#!/usr/bin/python3

if __name__ == "__main__":
    """A program that prints the result of addition of all arguments.
    """
    import sys

    # Check if there are arguments passed to the script
    if len(sys.argv) == 1:
        print(0)
    else:
        arguments = sys.argv[1:]

        result = sum(int(arg) for arg in arguments)
        print(result)
