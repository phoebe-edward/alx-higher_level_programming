#!/usr/bin/python3
"""test Square class"""
import unittest
from models.square import Square
from models.base import Base


class test_square(unittest.TestCase):
    """class test_square"""

    def test_initialization(self):
        s1 = Square(5)
        self.assertEqual("[Square] ({}) 0/0 - 5".format(s1.id), str(s1))
        self.assertEqual(s1.area(), 25)
        s11 = Square(5, 3)
        self.assertEqual("[Square] ({}) 3/0 - 5".format(s11.id), str(s11))
        s2 = Square(5, 3, 4)
        self.assertEqual("[Square] ({}) 3/4 - 5".format(s2.id), str(s2))
        s3 = Square(5, 3, 4, 12)
        self.assertEqual("[Square] (12) 3/4 - 5", str(s3))
        s3.update(s3.id, 7, 7)
        self.assertEqual("[Square] (12) 7/4 - 7", str(s3))
        self.assertRaises(TypeError, Square)
        

    def test_square_size(self):
        s4 = Square(5)
        self.assertEqual(5, s4.size)
        s4.size = 7
        self.assertEqual("[Square] ({}) 0/0 - 7".format(s4.id), str(s4))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s4.size = "8"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s4.size = -4

    def test_inheritance(self):
        self.assertIsInstance(Square(5), Base)

    def test_to_dictionary(self):
        r4 = Square(1, 3, 4, 12)
        dic4 = r4.to_dictionary()
        self.assertIsInstance(dic4, dict)
        self.assertDictEqual(
            {'x': 3, 'y': 4, 'id': 12, 'size': 1}, dic4)
        self.assertEqual(dic4["x"], 3)
        self.assertEqual(dic4["y"], 4)
        self.assertEqual(dic4["size"], 1)
        self.assertEqual(dic4["id"], 12)
        r5 = Square(6)
        dic5 = r5.to_dictionary()
        self.assertEqual(dic5["x"], 0)
        self.assertEqual(dic5["y"], 0)
        self.assertEqual(dic5["size"], 6)
        self.assertEqual(dic5["id"], r5.id)

    def test_update(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(12, 4, 5, 6)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.size, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)
        self.assertEqual("[Square] (12) 5/6 - 4", str(r1))
        r1.update()
        self.assertEqual("[Square] (12) 5/6 - 4", str(r1))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(12, -4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(12, "string size")
        r1.update(None, 4, 5, 2)
        ref = "[Square] ({}) 5/2 - 4".format(r1.id)
        self.assertEqual(ref, str(r1))
        r1.update(12, 3)
        self.assertEqual("[Square] (12) 5/2 - 3", str(r1))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(12, "string width", "string height")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(12, 4, "string x", "string y")
        r2 = Square(10, 10, 10, 10)
        r2.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(r2))
        r2.update(size=2)
        self.assertEqual("[Square] (1) 10/10 - 2", str(r2))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(size=-3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(x="string x")
        r2.update(size=4, id=12, y=2, x=1)
        self.assertEqual("[Square] (12) 1/2 - 4", str(r2))
        r2.update(id=None)
        ref = "[Square] ({}) 1/2 - 4".format(r2.id)
        self.assertEqual(ref, str(r2))
        r3 = Square(10, 10, 10, 10)
        r3.update(12, 3, y=4, x=6)
        self.assertEqual("[Square] (12) 10/10 - 3", str(r3))


if __name__ == "__main__":
    unittest.main()
