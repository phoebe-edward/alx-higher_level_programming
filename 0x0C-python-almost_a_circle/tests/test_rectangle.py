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
        self.assertRaises(TypeError, Rectangle, 'srt1', 2)
        self.assertRaises(TypeError, Rectangle, 1, 'str2')
        self.assertRaises(TypeError, Rectangle, [1, 2], [3, 4])
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(ValueError, Rectangle, -2, 3)
        self.assertRaises(ValueError, Rectangle, 1, -3)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3, 4)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 'x', 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 'y')
        self.assertRaises(TypeError, Rectangle, 1, 2, [1, 2], [3, 4])
        r1 = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            print(r1.__y)
            print(r1.__x)
            print(r1.__width)
            print(r1.__height)
        r2 = Rectangle(1, 2)
        self.assertEqual("[Rectangle] ({}) 0/0 - 1/2".format(r2.id), str(r2))
        r2 = Rectangle(1, 2, 3)
        self.assertEqual("[Rectangle] ({}) 3/0 - 1/2".format(r2.id), str(r2))
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual("[Rectangle] ({}) 3/4 - 1/2".format(r2.id), str(r2))
        r2 = Rectangle(1, 2, 3, 4, 12)
        self.assertEqual("[Rectangle] (12) 3/4 - 1/2", str(r2))

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
        r11 = Rectangle(2, 3, 1)
        capture = test_rectangle.capture_stdout(r11, "display")
        self.assertEqual(" ##\n ##\n ##\n", capture.getvalue())
        r2 = Rectangle(2, 3, 1, 2)
        capture = test_rectangle.capture_stdout(r2, "display")
        self.assertEqual("\n\n ##\n ##\n ##\n", capture.getvalue())

    def test_str(self):
        r1 = Rectangle(2, 3, 1, 0, 5)
        self.assertEqual("[Rectangle] (5) 1/0 - 2/3", r1.__str__())
        capture = test_rectangle.capture_stdout(r1, "print")
        self.assertEqual("[Rectangle] (5) 1/0 - 2/3\n", capture.getvalue())
        r2 = Rectangle(4, 5)
        capture = test_rectangle.capture_stdout(r2, "print")
        self.assertEqual("[Rectangle] ({}) 0/0 - 4/5\n".format(r2.id),
                         capture.getvalue())

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(12, 4, 5, 6, 7)
        self.assertEqual(r1.width, 4)
        self.assertEqual("[Rectangle] (12) 6/7 - 4/5", str(r1))
        r1.update()
        self.assertEqual("[Rectangle] (12) 6/7 - 4/5", str(r1))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(12, -4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(12, "string width")
        r1.update(None, 4, 5, 2)
        ref = "[Rectangle] ({}) 2/7 - 4/5".format(r1.id)
        self.assertEqual(ref, str(r1))
        r1.update(12, 3)
        self.assertEqual("[Rectangle] (12) 2/7 - 3/5", str(r1))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(12, "string width", "string height")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(12, 4, "string height", "string x")
        r2 = Rectangle(10, 10, 10, 10, 10)
        r2.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r2))
        r2.update(width=2)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r2))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(width=-3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.update(height="string height")
        r2.update(height=4, width=3, id=12, y=2, x=1)
        self.assertEqual("[Rectangle] (12) 1/2 - 3/4", str(r2))
        r2.update(id=None)
        ref = "[Rectangle] ({}) 1/2 - 3/4".format(r2.id)
        self.assertEqual(ref, str(r2))
        r3 = Rectangle(10, 10, 10, 10, 10)
        r3.update(12, 3, height=4, x=6)
        self.assertEqual("[Rectangle] (12) 10/10 - 3/10", str(r3))

    def test_to_dictionary(self):
        r4 = Rectangle(1, 2, 3, 4, 12)
        dic4 = r4.to_dictionary()
        self.assertIsInstance(dic4, dict)
        self.assertDictEqual(
            {'x': 3, 'y': 4, 'id': 12, 'height': 2, 'width': 1}, dic4)
        self.assertEqual(dic4["x"], 3)
        self.assertEqual(dic4["y"], 4)
        self.assertEqual(dic4["width"], 1)
        self.assertEqual(dic4["height"], 2)
        self.assertEqual(dic4["id"], 12)
        r5 = Rectangle(6, 7)
        dic5 = r5.to_dictionary()
        self.assertEqual(dic5["x"], 0)
        self.assertEqual(dic5["y"], 0)
        self.assertEqual(dic5["width"], 6)
        self.assertEqual(dic5["height"], 7)
        self.assertEqual(dic5["id"], r5.id)


if __name__ == "__main__":
    unittest.main()
