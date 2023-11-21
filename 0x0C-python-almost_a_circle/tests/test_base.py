#!/usr/bin/python3
"""test_base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertRaises(TypeError, Base.to_json_string)
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        r1 = Rectangle(1, 2)
        dic1 = r1.to_dictionary()
        str1 = Rectangle.to_json_string([dic1])
        self.assertIsInstance(str1, str)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertRaises(TypeError, Base.from_json_string)
        r1 = Rectangle(1, 2, 0, 0, 12)
        dic1 = r1.to_dictionary()
        str1 = Rectangle.to_json_string([dic1])
        dic11 = Rectangle.from_json_string(str1)
        self.assertIsInstance(dic11, list)
        self.assertDictEqual(dic11[0], {"id": 12, "width": 1, "height": 2, "x": 0, "y": 0})

    def test_create_rectangle(self):
        r1 = Rectangle.create(**{"id": 98})
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 98)
        r1 = Rectangle.create(**{"id": 98, "x": 5})
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.x, 5)
        r1 = Rectangle.create(**{"id": 98, "x": 5, "width": 2})
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.width, 2)
        r1 = Rectangle.create(**{"id": 98, "x": 5, "width": 2, "y": 3})
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.y, 3)
        r1 = Rectangle.create(**{"id": 98, "x": 5, "width": 2, "y": 3, "height": 6})
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.height, 6)

    def test_create_square(self):
        r1 = Square.create(**{"id": 98})
        self.assertIsInstance(r1, Square)
        self.assertEqual(r1.id, 98)
        r1 = Square.create(**{"id": 98, "x": 5})
        self.assertIsInstance(r1, Square)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.x, 5)
        r1 = Square.create(**{"id": 98, "x": 5, "size": 2})
        self.assertIsInstance(r1, Square)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.size, 2)
        r1 = Square.create(**{"id": 98, "x": 5, "size": 2, "y": 3})
        self.assertIsInstance(r1, Square)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.y, 3)

    def test_save_to_file(self):
        self.assertRaises(TypeError, Base.save_to_file)
        Rectangle.save_to_file([])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(len(list_objs), 0)
        Rectangle.save_to_file(None)
        list_objs = Rectangle.load_from_file()
        self.assertEqual(len(list_objs), 0)
        r1 = Rectangle(1, 2)
        Rectangle.save_to_file([r1])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(len(list_objs), 1)
        self.assertIsInstance(list_objs, list)
        Square.save_to_file([])
        list_objs = Square.load_from_file()
        self.assertEqual(len(list_objs), 0)
        Square.save_to_file(None)
        list_objs = Square.load_from_file()
        self.assertEqual(len(list_objs), 0)
        r1 = Square(5)
        Square.save_to_file([r1])
        list_objs = Square.load_from_file()
        self.assertEqual(len(list_objs), 1)
        self.assertIsInstance(list_objs, list)


if __name__ == "__main__":
    unittest.main()
