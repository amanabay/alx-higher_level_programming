#!/usr/bin/python3
"""Class and inherited class object check function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class
    Args:
        obj (any): object to check
        a_class (type): class to check the object belongs to
    Returns:
        If obj is an instance or inherited instance of a_class - True
        If not - False
    """
    if isinstance(obj, a_class):
        return True
    return False
