#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Represents a square of a certain size."""

    def __init__(self, size=0):
        """Initialize new square.

        Args:
            size (int): Size of square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
