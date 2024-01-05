#!/usr/bin/python3
def uppercase(str):
    for char_code in str:
        c = ord(char_code)
        if ord(char_code) >= 97 and ord(char_code) <= 122:
            c -= 32
        print("{:c}".format(c), end='')
    print()
