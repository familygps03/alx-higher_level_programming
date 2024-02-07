#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: This method must be implemented by subclasses.
        """
        raise Exception("area() is not implemented")
