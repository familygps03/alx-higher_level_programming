#!/usr/bin/python3
import math

class MagicClass:
    """
    Class that creates a circle area
    """


    def __init__(self, radius=0):
        """initialize"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """function defining area"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """function defininf circumference"""
        return ((2 * math.pi) * self.__radius)
