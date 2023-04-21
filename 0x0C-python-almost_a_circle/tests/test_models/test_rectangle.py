#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        r2 = Rectangle(5, 5, 10, 10, 1)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 10)
        self.assertEqual(r2.id, 1)

    def test_width(self):
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

        with self.assertRaises(TypeError):
            r.width = "hello"
        with self.assertRaises(ValueError):
            r.width = -10

    def test_height(self):
        r = Rectangle(10, 20)
        r.height = 30
        self.assertEqual(r.height, 30)

        with self.assertRaises(TypeError):
            r.height = "hello"
        with self.assertRaises(ValueError):
            r.height = -10

    def test_x(self):
        r = Rectangle(10, 20)
        r.x = 30
        self.assertEqual(r.x, 30)

        with self.assertRaises(TypeError):
            r.x = "hello"
        with self.assertRaises(ValueError):
            r.x = -10

    def test_y(self):
        r = Rectangle(10, 20)
        r.y = 30
        self.assertEqual(r.y, 30)

        with self.assertRaises(TypeError):
            r.y = "hello"
        with self.assertRaises(ValueError):
            r.y = -10

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

        r.width = 5
        r.height = 5
        self.assertEqual(r.area(), 25)

    def test_update(self):
        r = Rectangle(10, 20)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

        r.update(id=10, x=20, y=30)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 30)

        r.update(5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 30)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 12)
        r_dict = r.to_dictionary()
        self.assertDictEqual(r_dict, {'id': 12, 'width': 10,
                                      'height': 2, 'x': 1, 'y': 9})

        r2 = Rectangle(1, 1)
        r2.update(**r_dict)
        self.assertEqual(str(r), str(r2))
        self.assertNotEqual(r, r2)


if __name__ == "__main__":
    unittest.main()
