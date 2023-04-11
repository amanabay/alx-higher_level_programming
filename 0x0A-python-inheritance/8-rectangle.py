#!/usr/bin/python3
"""Class Rectangle inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Intializes a new Rectangle
        Args:
            width (int): width of new Rectangle
            height (int): height of new Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """print() and str() representation of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return
