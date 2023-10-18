#!/usr/bin/python3
""""use json to return back a str to python object"""


import json


def from_json_string(my_str):
    """convert back to object"""
    return json.loads(my_str)
