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

    @staticmethod
    def from_json_string(json_string):
        """from json string to the original type (list of dictionaries)"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a square or rectangle with attributes given in dictionary"""
        if dictionary is not None and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """from file to list of class instances"""
        filename = cls.__name__ + ".json"
        with open(filename, "r", encoding="utf-8") as file:
            str_out = file.read()
        list_out = cls.from_json_string(str_out)
        if list_out is None or len(list_out) == 0:
            return []
        else:
            list_obj = []
            for dic in list_out:
                list_obj.append(cls.create(**dic))
            return list_obj
