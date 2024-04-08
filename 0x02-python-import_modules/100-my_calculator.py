#!/usr/bin/python3

if __name__ == "__main__":
    """A program that imports functions and handles basic operations.
    """
    import sys
    from calculator_1  import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    basic_operators = sys.argv[2]
    b = int(sys.argv[3])

    if basic_operators not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if basic_operators == "+":
        result = add(a, b)
    elif basic_operators == "-":
        result = sub(a, b)
    elif basic_operators == "*":
        result = mul(a, b)
    elif basic_operators == "/":
        result = div(a, b)

    print(f"{a} {basic_operators} {b} = {result}")
