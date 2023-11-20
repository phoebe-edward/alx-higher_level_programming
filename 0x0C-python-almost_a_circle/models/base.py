#!/usr/bin/python3
import json
"""class Base"""


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """from list of dictionaries to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
