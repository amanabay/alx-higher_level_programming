#!/usr/bin/python3
"""Class Student"""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """Initializer
        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation of the Student"""
        return self.__dict__
