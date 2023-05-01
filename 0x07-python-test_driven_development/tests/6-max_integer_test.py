#!/usr/bin/python3

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_item_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 2, 2, 3]), 3)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.0, 2.5, 3.7]), 3.7)


if __name__ == '__main__':
    unittest.main()
