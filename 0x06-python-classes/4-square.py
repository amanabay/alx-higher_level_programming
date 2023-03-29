#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Represents a square of a certain size."""

    def __init__(self, size=0):
        """Initialize new square.

        Args:
            size (int): Size of square.
        """

        self.size = size

    @property
    def size(self):
        """The size property."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns area of square."""
        return (self.__size * self.__size)
