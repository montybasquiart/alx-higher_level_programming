#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# This program will assign a random signed number to the variable number
# each time it is executed.
# Extract the last digit of the random number
# Ensure the last digit retains its sign for negative numbers
if number < 0:
    last_digit = -(abs(number) % 10)
else:
    last_digit = number % 10

# Check conditions and print messages
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is "
          f"greater than 5", end="\n")
if last_digitd < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is "
          f"less than 6 and not 0", end="\n")
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0", end="\n")
