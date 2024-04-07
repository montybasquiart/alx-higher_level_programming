#!/usr/bin/python3

if __name__ == "__main__":
    from tests import add_0
    a = 1
    b = 2
    add_it = add_0.add(a, b)
    print("{a} + {b} = {add_it}".format(a=a, b=b, add_it=add_it), end="\n")
