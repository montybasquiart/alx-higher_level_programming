#!/usr/bin/python3

if __name__ == "__main__":
    # This program imports functions and does some basic Maths
    import calculator_1 as cal
    a = 10
    b = 5

    # This program does Addition
    addition = cal.add(a, b)
    print("{a} + {b} = {addition}".format(a=a, b=b, addition=addition), end="\n")

    # This program does Subtraction
    subtract = cal.sub(a, b)
    print("{a} - {b} = {subtract}".format(a=a, b=b, subtract=subtract), end="\n")

    # This program does Multiplication
    multiply = cal.mul(a, b)
    print("{a} * {b} = {multiply}".format(a=a, b=b, multiply=multiply), end="\n")

    # This program does Division
    divide = cal.div(a, b)
    print("{a} / {b} = {divide}".format(a=a, b=b, divide=divide), end="\n")
