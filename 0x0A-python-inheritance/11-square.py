#!/usr/bin/python3
"""Defines a class Square based on Rectangle."""

from typing import Union
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square as a subclass of Rectangle."""

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

    def area(self) -> Union[int, float]:
        """Computes the area of the square.

        Returns:
            Union[int, float]: The area of the square.
        """
        return self.width * self.height
