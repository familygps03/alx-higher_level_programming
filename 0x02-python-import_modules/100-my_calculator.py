#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arg_count = len(sys.argv) - 1

    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = map(int, sys.argv[1:4])

    if operator not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '/' and b == 0:
        print("Error: Division by zero is not allowed.")
        sys.exit(1)

    result = {'+': add, '-': sub, '*': mul, '/': div}[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
