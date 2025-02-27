import unittest
from swap_strings import *


class test_swap_strings(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(swap_strings('abc', 'xyz'), 'xyc abz')

    def test_case_2(self):
        self.assertEqual(swap_strings('hello', 'world'), 'wollo herld')

    def test_case_3(self):
        self.assertEqual(swap_strings('swap', 'test'), 'teap swst')

    def test_case_4(self):
        self.assertEqual(swap_strings('1234', '5678'), '5634 1278')
