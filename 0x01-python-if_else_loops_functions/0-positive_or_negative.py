#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# This program will asign a random signed number to the variable number
# each time it is executed.
if number > 0:
    print(f"{number} is positive", end="\n")
if number == 0:
    print(f"{number} is zero", end="\n")
if number < 0:
    print(f"{number} is negative", end="\n")
