#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """Rectangle representation

    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_symbol (char): Symbol for string representation.
    """

    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes new Rectangle
        Args:
            width (int): Width of new rectangle
            height (int): Height of new rectangle
        """
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """Print rectangle using any symbol"""

        if self.__width == 0 or self.__height == 0:
            return ""

        pr = []
        for i in range(self.__height):
            for j in range(self.__width):
                pr.append(str(self.print_symbol))
            if i != self.__height - 1:
                pr.append("\n")

        return ("".join(pr))

    def __repr__(self):
        """String representation of the Rectangle"""

        pr = "Rectangle(" + str(self.__width)
        pr += ", " + str(self.__height) + ")"
        return pr

    def __del__(self):
        """Prints message for every deletion of Rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles accroding to area

        Args:
            rect_1 (Rectangle): Rectangle instance of first rectangle
            rect_2 (Rectangle): Rectangle instance of second rectangle
        Raises:
            TypeError: If either of the objects are not Rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new Rectangle with width = height = size aka square

        Args:
            size (int): Width and height of new Rectangle
        """
        return (cls(size, size))
