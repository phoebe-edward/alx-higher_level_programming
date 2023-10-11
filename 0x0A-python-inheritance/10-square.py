#!/usr/bin/python3
"""module for the class of Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
