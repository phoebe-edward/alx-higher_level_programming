#!/usr/bin/python3
"""function to add attribute if possible"""


def add_attribute(obj, name, value):

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
