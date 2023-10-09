#!/usr/bin/python3
"""is kind of class"""


def is_kind_of_class(obj, a_class):
    """return True if is from this class or any other superclass"""
    return isinstance(obj, a_class)
