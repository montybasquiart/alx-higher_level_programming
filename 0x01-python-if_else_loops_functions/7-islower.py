#!/usr/bin/python3
def islower(c):
    """A Function that checks for lowercase character.
    """
# check if the ASCII letters is within the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')
