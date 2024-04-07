#!/usr/bin/python3

if __name__ == "__main__":
    # This program imports functions and does some basic Maths
    from tests import calculator_1 as cal
    a = 10
    b = 5

    # This program does Addition
    add_it = cal.add(a, b)
    print("{a} + {b} = {add_it}".format(a=a, b=b, add_it=add_it), end="\n")

    # This program does Subtraction
    sub_it = cal.sub(a, b)
    print("{a} - {b} = {sub_it}".format(a=a, b=b, sub_it=sub_it), end="\n")

    # This program does Multiplication
    mul_it = cal.mul(a, b)
    print("{a} * {b} = {mul_it}".format(a=a, b=b, mul_it=mul_it), end="\n")

    # This program does Division
    div_it = cal.div(a, b)
    print("{a} / {b} = {div_it}".format(a=a, b=b, div_it=div_it), end="\n")
