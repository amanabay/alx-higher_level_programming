#!/usr/bin/python3
"""Function that adds a new attribute to an object if possible"""


def add_attribute(obj, att, val):
    """Adds a new attribute to an object if possible
    Args:
        obj (any): object to add an attribute to
        att (str): name of the attribute to add to obj
        val (any): value of att
    Raises:
        TypeError: if attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
