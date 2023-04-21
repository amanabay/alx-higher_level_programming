#!/usr/bin/python3
"""Class definition for Base"""

import json
import csv


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
        """ Saves JSON string representation to JSON file

            Args:
                list_objs (list): is a list of instances who inherits of Base
        """

        fname = cls.__name__ + ".json"

        with open(fname, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                for obj in list_objs:
                    list_dictionaries = obj.to_dictionary()
                jfile.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string

            Args:
                json_string (list): string representing a list of dictionaries
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set from
            a dictionary of attributes

            Args:
                **dictionary (dict): dictionary of attributes to initialize
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(2, 3)
            else:
                new = cls(3)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a file ofJSON
           strings"""
        fname = str(cls.__name__) + ".json"

        try:
            with open(fname, "r") as jfile:
                list_dictionaries = Base.from_json_string(jfile.read())
                for d in list_dictionaries:
                    return cls.create(**d)
        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves csv string representation to JSON file

            Args:
                list_objs (list): is a list of instances who inherits of Base
        """
        fname = cls.__name__ + ".csv"
        with open(fname, "w", newline="") as cfile:
            if list_objs is None or list_objs == []:
                cfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(cfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated from a CSV file
        """
        fname = cls.__name__ + ".csv"
        try:
            with open(fname, "r", newline="") as cfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dictionaries = csv.DictReader(cfile,
                                                   fieldnames=fieldnames)
                for d in list_dictionaries:
                    list_dictionaries = dict([k, int(v)] for k, v in d.items())
                    return cls.create(**d)
        except IOError:
            return []
