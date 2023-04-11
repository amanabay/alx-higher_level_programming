#!/usr/bin/python3
"""Class checking function."""


def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of the specified class
    Args:
        obj (any): object to check
        a_class (type): class to check the object belongs to
    Returns:
        If obj is instance of a_class - True.
        If not - False.
    """
    if type(obj) == a_class:
        return True
    return False
