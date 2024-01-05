#!/usr/bin/python3
for char_code in range(10):
    for j in range(10):
        if (char_code < j):
            print("{}{}".format(char_code, j), end="")
            if (char_code != 8):
                print(", ", end="")
            else:
                print(end="\n")
