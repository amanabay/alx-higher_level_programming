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

    def to_json(self, attrs=None):
        """Returns the json representation of an instance
        Args:
            attrs (list): a given attributes
        Returns:
            (dict): a dictionary
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): key value pairs to replace with
        """
        for k, v in json.items():
            self.__dict__[k] = v
