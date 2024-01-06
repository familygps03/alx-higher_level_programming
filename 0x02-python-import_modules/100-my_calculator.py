#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    arg_count = len(sys.argv) - 1

    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    i = int(sys.argv[1])
    j = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        result = add(i, j)
    elif operator == "-":
        result = sub(i, j)
    elif operator == "*":
        result = mul(i, j)
    elif operator == "/":
        if j == 0:
            exit(1)
        result = div(i, j)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(i, operator, j, result))
