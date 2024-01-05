#!/usr/bin/python3
for char_code in range(0, 90):
    if char_code % 10 != char_code / 10 and char_code % 10 > char_code / 10:
       print("{:02d}{}".format(char_code, ", " if char_code < 89 else '\n'), end='')
