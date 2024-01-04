#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n = number % -10
else:
    n = number % 10

if n > 5:
    phrase = "greater than 5"
elif n == 0:
    phrase = "0"
else:
    phrase = "less than 6 and not 0"
print(f"Last digit of {number} is {n} and is {phrase}")
