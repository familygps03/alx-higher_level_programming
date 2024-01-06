#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
       result = add(a, b)
       for j in range(4, 6):
           result = add(result, j)
       return result
    else:
        return sub(a, b)
