#!/usr/bin/python3
for char_code in range(0, 100):
    print("{:02d}".format(char_code), end='\n' if char_code == 99 else ", ")
