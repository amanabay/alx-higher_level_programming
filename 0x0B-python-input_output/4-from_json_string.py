#!/usr/bin/python3
"""Function definition for JSON-to-object"""
import json


def from_json_string(my_str):
    """ Returns an object (Python data structure) of a JSON string"""
    return json.loads(my_str)
