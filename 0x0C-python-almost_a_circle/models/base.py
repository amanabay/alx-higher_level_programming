#!/usr/bin/python3
"""Class definition for Base"""


class Base:
    """Base class for all other classes

    Private Class Attributes:
        __nb_object (int): number of instantiated objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer with id

        Args:
            id (int): identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
