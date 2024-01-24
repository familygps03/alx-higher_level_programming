#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    A class that specifies properties of a square (based on 0-square.py).

    Attributes:
        size (int): The size of the square (1 side).
    """
    def __init__(self, size):
        """
        Creates new instances of a square (1 side).

        Args:
            size (int): The size of the square.
        """
        self.__size = size
