#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    addition = add(a, b)
    print("{a} + {b} = {addition}".format(a=a, b=b, addition=addition), end="\n")
