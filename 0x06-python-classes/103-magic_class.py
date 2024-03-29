#!/usr/bin/python3

"""MagicClass definition to bytecode"""

import math


class MagicClass:
    """Circle."""

    def __init__(self, radius=0):
        """MagicClass.
        Arg:
            radius (float or int): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns circumference of the circle."""
        return (2 * math.pi * self.__radius)
