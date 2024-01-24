#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class that represents the properties of a square based on 3-square.py.

    Attributes:
        size (int): The size of the square (1 side).
    """
    def __init__(self, size=0):
        """
        Creates new instances of a square.

        Args:
            size (int): The size of the square (1 side).
        """
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter for size.

        Args:
            value (int): The size of a square (1 side).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        """Rich comparison operator to check if square area is less than another."""
        return self.__size < other.__size

    def __le__(self, other):
        """Rich comparison operator to check if square area is less than or equal to another."""
        return self.__size <= other.__size

    def __eq__(self, other):
        """Rich comparison operator to check if square area is equal to another."""
        return self.__size == other.__size

    def __ne__(self, other):
        """Rich comparison operator to check if square area is not equal to another."""
        return self.__size != other.__size

    def __gt__(self, other):
        """Rich comparison operator to check if square area is greater than another."""
        return self.__size > other.__size

    def __ge__(self, other):
        """Rich comparison operator to check if square area is greater than or equal to another."""
        return self.__size >= other.__size
