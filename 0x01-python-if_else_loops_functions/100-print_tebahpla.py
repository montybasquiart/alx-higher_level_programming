#!/usr/bin/python3

# A program that prints the ASCII alphabets in reverse order,
# alternating lowercase and uppercase(z in lowercase Y in uppercase).

i = 0
for char in range(ord("z"), ord("a") - 1, - 1):
    print("{}".format(chr(char - i)), end="")
    i = 32 if i == 0 else 0
