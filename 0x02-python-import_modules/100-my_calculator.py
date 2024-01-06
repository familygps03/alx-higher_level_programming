#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arg_count = len(sys.argv) - 1
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == "+":
          result = add(a, b)
    elif operator == "-":
          result = sub(a, b)
    elif operator == "*":
          result = mul(a, b)
    elif operator == "/":
         if b == 0:
              exit(1)
         result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    result = {'+': add, '-': sub, '*': mul, '/': div}[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
