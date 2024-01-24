#!/usr/bin/python3
import math

class MagicClass:
    """
    A class that calculates the area and circumference of a circle.
    """

    def __init__(self, radius=0):
        """Initialize the MagicClass with a specified radius."""
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")

        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
