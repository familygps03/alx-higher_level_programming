#!/usr/bin/python3
"""Defines a class Rectangle based on 8-base_geometry.py."""

from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A class to represent a rectangle."""

    def __init__(self, width: int, height: int):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.width = width
        self.height = height

    def area(self) -> int:
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def __str__(self) -> str:
        """Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.width}/{self.height}"
