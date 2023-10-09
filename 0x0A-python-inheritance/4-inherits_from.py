#!/usr/bin/python3
"""enherits from?"""


def inherits_from(obj, a_class):
    """is subclass?"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
