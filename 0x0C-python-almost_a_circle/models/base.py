#!/usr/bin/python3
"""class Base"""
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json string of list of objs to a json file"""
        if list_objs is None or len(list_objs) == 0:
            string_req = Base.to_json_string([])
        else:
            list_dictionaries = []
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
            string_req = Base.to_json_string(list_dictionaries)
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(string_req)
