#!/usr/bin/python3
"""Defines the MagicClass"""

import math

class MagicClass:
    """
    A class representing the properties of MagicClass.

    Attributes:
        radius (int or float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of MagicClass.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        else:
            self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
