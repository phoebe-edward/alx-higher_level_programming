#!/usr/bin/python3
"""test_rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class test_rectangle(unittest.TestCase):
    """class test_rectangle"""

    def test_error(self):
        self.assertRaises(TypeError, Rectangle, 'srt1', 'str2')
        self.assertRaises(TypeError, Rectangle, [1, 2], [3, 4])
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(ValueError, Rectangle, -2, -3)
        self.assertRaises(ValueError, Rectangle, 0, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3, -4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 'x', 'y')
        self.assertRaises(TypeError, Rectangle, 1, 2, [1, 2], [3, 4])
        r1 = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            print(r1.__y)
            print(r1.__x)
            print(r1.__width)
            print(r1.__height)

    def test_inheritance(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_id(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 3)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(Rectangle(1, 2, 0, 0, 12).id, 12)

    def test_values(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_area(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 2 * 3)

    @staticmethod
    def capture_stdout(rect, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display(self):
        r1 = Rectangle(2, 3)
        capture = test_rectangle.capture_stdout(r1, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())