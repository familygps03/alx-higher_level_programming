#!/usr/bin/python3
"""Defines a class Square based on 9-rectangle.py."""

from typing import Union
from 9-rectangle import Rectangle

class Square(Rectangle):
    """A Square class inheriting from Rectangle."""

    def __init__(self, size: int):
        """Initializes a Square instance.

        Args:
            size (int): The size of one side of the square.
        """
        super().__init__(size, size)

    def area(self) -> int:
        """Calculates the area of a square.

        Returns:
            int: The area of the square.
        """
        return self.width ** 2
