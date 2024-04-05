#!/usr/bin/python3

from add_0 import add as add_function

a = 1
b = 2
addition = add_function(a, b)
print("{a} + {b} = {addition}".format(a=a, b=b, addition=addition), end="\n")
