#!/usr/bin/python3
"""Function definition for JSON file-read"""
import json


def load_from_json_file(filename):
    """Creates Object from a JSON file"""
    with open(filename) as fp:
        return json.load(fp)
