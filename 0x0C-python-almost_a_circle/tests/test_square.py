#!/usr/bin/python3
"""test Square class"""
import unittest
from models.square import Square


class test_square(unittest.TestCase):
    """class test_square"""

    def test_initialization(self):
        s1 = Square(5)
        self.assertEqual("[Square] ({}) 0/0 - 5".format(s1.id), str(s1))
        self.assertEqual(s1.area(), 25)
        s2 = Square(5, 3, 4)
        self.assertEqual("[Square] ({}) 3/4 - 5".format(s2.id), str(s2))
        s3 = Square(5, 3, 4, 12)
        self.assertEqual("[Square] (12) 3/4 - 5", str(s3))
        s3.update(s3.id, 7, 7)
        self.assertEqual("[Square] (12) 3/4 - 7", str(s3))

    def test_square_size(self):
        s4 = Square(5)
        self.assertEqual(5, s4.size)
        s4.size = 7
        self.assertEqual("[Square] ({}) 0/0 - 7".format(s4.id), str(s4))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s4.size = "8"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s4.size = -4
