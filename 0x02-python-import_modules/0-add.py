#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    add_it = add(a, b)
    print("{a} + {b} = {add_it}".format(a=a, b=b, add_it=add_it), end="\n")
