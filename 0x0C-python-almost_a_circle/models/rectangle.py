#!/usr/bin//python3
"""Class definition for Rectangle class"""
from base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x (int): x coordinate of Rectangle
            y (int): y coordinate of Rectangle
            id (int): unique identifier of Rectangle

        Raises:
            TypeError: if either width, height, x or y is not int
            ValueError: if either width, height, x or y is < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """The x property."""
        return self._x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y property."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of Rectangle"""
        return (self.width * self.height)

    def display(self):
        if self.height == 0 or self.width == 0:
            print("")
            return

        for i in range(self.width):
            for j in range(self.height):
                print("#", end="")
            print("")

r1 = Rectangle(4, 6)
r1.display()

print("---")

r1 = Rectangle(2, 2)
r1.display()
