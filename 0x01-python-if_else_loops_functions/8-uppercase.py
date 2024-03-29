#!/usr/bin/python3
def uppercase(str):
    """A Function that prints a string in UPPERCASE."""
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
            result += upper_char
        else:
            result += char
    print("{}".format(result))



    #for char in str:
     #   if ord(char) >= 97 and ord(char) <= 122:
      #      char = chr(ord(char) - 32)
       # print("{}".format(char), end="")
    #print()
