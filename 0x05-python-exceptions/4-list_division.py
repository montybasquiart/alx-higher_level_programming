#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """A function that divides element by element 2 lists.
    """
    result = []
    for index in range(list_length):
        try:
            dividend = my_list_1[index]
            divisor = my_list_2[index]
            result.append(dividend / divisor)
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
    return result
