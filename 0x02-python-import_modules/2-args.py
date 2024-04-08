#!/usr/bin/python3

# A program that prints the number of and list of its args
if __name__ == "__main__":
    """Print the nummber of and list of arguments.
    """
    import sys

    # Exlude the script name from the arguments
    args = sys.argv[1:]

    num_of_args = len(args)

    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
        print(f"1: {args[0]}")
    else:
        print(f"{num_of_args} arguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
