#!/usr/bin/python3
"""Class definition for Square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Rectangle class

        Args:
            size (int): size of square
            x (int): x coordinate of square
            y (int): y coordinate of square
            id (int): unique identifier of Rectangle

        """
        super.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """The size property."""
        return self.height

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """ Update the parameters of a Rectangle

            Args:
                *args (int):
                    at index 0 is the id
                    at index 1 is the size
                    at index 2 is the x attribute
                    at index 3 is the y attribute
                **kwargs (dict): key/value pairs of new attributes
        """

        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
