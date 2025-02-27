import unittest

from ce import ce


class TestInsertCe(unittest.TestCase):
    def test_even_length_word(self):
        self.assertEqual(ce("helloo"), "helceloo")

    def test_odd_length_word(self):
        self.assertEqual(ce("joy"), "joyce")

    def test_another_even_length_word(self):
        self.assertEqual(ce("python"), "pytcehon")
 
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            ce("")

