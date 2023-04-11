#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if paramenter is an integer.
        Args:
            name (str): Name of the parameter
            value (int): Parameter to validate
        Raises:
            TypeError: If value not an integer
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
