#!/usr/bin/python3
def roman_to_int(roman_string):
    """A function that converts a Roman numeral to an integer.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    num = 0
    previous_char = 0

    for char in roman_string:
        current_value = roman_dict[char]
        if current_value > previous_char:
            num += current_value - 2 * previous_char
        else:
            num += current_value
        previous_char = current_value
    return num
