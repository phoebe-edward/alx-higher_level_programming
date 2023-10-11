#!/usr/bin/python3
"""empty class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
