#!/usr/bin/python3
"""Subclass of class int."""


class MyInt(int):
    """Has == and != operators inverted"""

    def __eq__(self, value):
        """ == operator with !="""
        return self.real != value

    def __ne__(self, value):
        """!= operator with =="""
        return self.real == value
