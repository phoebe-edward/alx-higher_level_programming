#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            for a in attrs:
                if type(a) != str:
                    return self.__dict__
        else:
            return self.__dict__
        my_dict = {}
        for a in attrs:
            if hasattr(self, a):
                my_dict[a] = getattr(self, a)
        return my_dict

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
        return self.__dict__
