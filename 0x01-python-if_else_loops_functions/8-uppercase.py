#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        ascii_code = ord(char)
        if 97 <= ascii_code <= 122:
            ascii_code -= 32
        print(chr(ascii_code), end='')
    print()
