#!/usr/bin/env python

import unittest
import task3


class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        f = task3.factorial(5)
        self.assertEqual(f, 120)


if __name__ == '__main__':
    unittest.main()
