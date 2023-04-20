#!/usr/bin/python3
"""Class definition for Base"""

import json


class Base:
    """Base class for all other classes

    Private Class Attributes:
        __nb_object (int): number of instantiated objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer with id

        Args:
            id (int): identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries

            Args:
                list_dictionaries (list): list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries is []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        fname = cls.__name__ + ".json"

        with open(fname, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                for obj in list_objs:
                    list_dictionaries = obj.to_dictionary()
                jfile.write(Base.to_json_string(list_dictionaries))


