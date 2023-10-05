#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""class Testmax_integer"""


class Testmax_integer(unittest.TestCase):
    """class to test max_integer function"""
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([4.5, 3.2, 9.7]), 9.7)
        self.assertEqual(max_integer([-4, -20, -31]), -4)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, ['a', 'b', 4])
        self.assertRaises(TypeError, max_integer, 3)
