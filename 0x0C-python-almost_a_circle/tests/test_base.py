#!/usr/bin/python3
"""test_base class"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """class test_base"""

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id(self):
        b1 = Base(12)
        b2 = Base(12)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b1.id, b2.id)

    def test_three(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        self.assertNotEqual(b1.id + 1, b2.id)

if __name__ == "__main__":
    unittest.main()
