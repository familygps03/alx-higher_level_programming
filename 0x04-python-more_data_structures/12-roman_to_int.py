#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    roman_d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    for m in range(len(roman_string)):
        if roman_d.get(roman_string[m], 0) == 0:
            return (0)

        if (m != (len(roman_string) - 1) and
                roman_d[roman_string[m]] < roman_d[roman_string[m + 1]]):
            number += roman_d[roman_string[m]] * -1

        else:
            number += roman_d[roman_string[m]]
    return (number)
