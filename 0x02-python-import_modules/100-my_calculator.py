#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = map(int, sys.argv[1:4])

    operations = {'+': add, '-': sub, '*': mul, '/': div}

    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = operations[operator](a, b)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))

