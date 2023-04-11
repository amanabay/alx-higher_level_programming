#!/usr/bin/python3
"""Class MyList inherited from class list"""


class MyList(list):
    """MyList sorts list"""

    def print_sorted(self):
        """Prints a list in sorted ascending order"""
        print(sorted(self))
