#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for the square class"""

    def test_init(self):
        s = Square(10)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s = Square(20, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_size(self):
        s = Square(10)
        self.assertEqual(s.size, 10)
        s.size = 20
        self.assertEqual(s.size, 20)
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)

    def test_update(self):
        s = Square(10)
        s.update(2)
        self.assertEqual(s.id, 2)
        s.update(3, 30, 4, 5)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.size, 30)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

        s.update(id=4)
        self.assertEqual(s.id, 4)
        s.update(size=40, y=5, x=4, id=5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 40)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_to_dictionary(self):
        s = Square(10, 2, 3, 4)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 4, "size": 10, "x": 2, "y": 3})

    def test_str(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 10")


if __name__ == "__main__":
    unittest.main()
