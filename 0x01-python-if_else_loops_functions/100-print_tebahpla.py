#!/usr/bin/python3
for char_code in range(122, 96, -1):
    if char_code % 2 == 0:
        c = chr(char_code)
    else:
        c = chr(char_code - 32)
    print("{:s}".format(c), end='')
