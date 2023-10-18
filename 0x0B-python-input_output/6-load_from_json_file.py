#!/usr/bin/python3
""""use json to load an object from a file"""


import json


def load_from_json_file(filename):
    """load obj from a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
