#!/usr/bin/python3
"""Module of the class MyInt"""


class MyInt(int):
    """class MyInt"""

    def __eq__(self, other):
        return self.real != other.real

    def __ne__(self, other):
        return self.real == other.real
