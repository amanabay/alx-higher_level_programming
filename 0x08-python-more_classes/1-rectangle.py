#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """Rectangle representation"""

    def __init__(self, width=0, height=0):
        """Initializes new Rectangle
        Args:
            width (int): Width of new rectangle
            height (int): Height of new rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """The width @property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """The height @property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
