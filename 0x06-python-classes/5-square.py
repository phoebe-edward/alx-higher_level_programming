#!/usr/bin/python3
"""Define Square class."""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """initialize square:
        Args:
        size(int): the size of the square"""
        self.__size = size

    def area(self):
        """calculate area"""
        return (self.__size)**2

    @property
    def size(self):
        """get value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size
        based on restrictions"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print square with #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
