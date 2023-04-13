#!/usr/bin/python3
"""Class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
