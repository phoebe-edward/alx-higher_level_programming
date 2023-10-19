#!/usr/bin/python3
"""from object to dict JSON"""


import json


def class_to_json(obj):
    """obj to dict"""
    return obj.__dict__
