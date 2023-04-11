#!/usr/bin/python3
"""Inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class
    Args:
        obj (any): object to check
        a_class (type): class to check the object belongs to
    Returns:
        If obj is an inherited instance of a_class - True
        If not - False
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
