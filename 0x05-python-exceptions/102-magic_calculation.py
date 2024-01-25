#!/usr/bin/python3

def magic_calculation(a, b):
    """function that does exactly the same as the given Python bytecode.

    Args:
        a: integer
        b: integer
    """
    product = 0

    for number in range(1, 3):
        try:
            if number > a:
                raise Exception("Too far")
            else:
                product += (a ** b) / number
        except Exception:
            product = b + a
            break
    return product
