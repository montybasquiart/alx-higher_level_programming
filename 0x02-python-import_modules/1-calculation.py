#!/usr/bin/python3

if __name__ == "__main__":
    # This program imports functions and does some Maths
    # This program does Addition
    import calculator_1 as cal
    a = 10
    b = 5

    addition = cal.add(a, b)
    print("{a} + {b} = {addition}".format(a=a, b=b, addition=addition), end="\n")

    # This program does Subtraction
