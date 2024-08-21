#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for index in range(1, 4):
        if index > a:
            raise Exception("Too far")
        result += (a ** b) / index
    result += a + b
    return result