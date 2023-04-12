#!/usr/bin/python3
"""Function definition for JSON to file-write"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as fp:
        json.dump(my_obj, fp)
