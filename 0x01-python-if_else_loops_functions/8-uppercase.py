def uppercase(s):
    """A Function that prints a string in UPPERCASE.
    """


# Check if the character is a lowercase letter
for i in range(len(str)):
    if ord(str[i]) >= 97 and ord(str[i]) < 123:
        letter = 32
    else:
        letter = 0
        print("{:c}".format(ord(str[i] - letter), end="")
print()
