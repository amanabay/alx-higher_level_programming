#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Represents a square of a certain size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new square.

        Args:
            size (int): Size of square.
            position (int, int): Position of square.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """The position property."""
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value) or
                len(value) != 2):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Returns area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with octothorpe(#)."""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print("")
