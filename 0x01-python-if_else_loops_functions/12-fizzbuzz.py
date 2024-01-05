#!/usr/bin/python3
def fizzbuzz():
    for char_code in range(1, 101):
        if char_code % 3 == 0 and char_code % 5 == 0:
            print("FizzBuzz ", end='')
        elif char_code % 3 == 0:
            print("Fizz ", end='')
        elif char_code % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{:d} ".format(char_code), end='')
