#!/usr/bin/python3
"""Defines a class Rectangle based on 7-base_geometry.py."""

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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
