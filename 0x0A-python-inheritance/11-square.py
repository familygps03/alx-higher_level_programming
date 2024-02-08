#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle (9)"""

from typing import Union
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class inheriting from Rectangle."""

    def __init__(self, size: int):
        """Initializes a Square instance.

        Args:
            size (int): The size of one side of the square.
        """
        super().__init__(size, size)

    def __str__(self) -> str:
        """Returns a string representation of the square.

        Returns:
            str: A string indicating the square's size.
        """
        return f"[Square] {self.width}/{self.height}"
