import unittest

from occurrance import occurrance

class test_occurrence(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(occurrance("hello", "h"), ("h", 1))

    def test_multiple_occurrences(self)  :
        self.assertEqual(occurrance("banana", "a"), ("a", 3))

    def test_no_occurrence(self):
        self.assertEqual(occurrance("hello", "z"), ("z", 0))

    def test_case_sensitivity(self):
        self.assertEqual(occurrance("Hello", "h"), ("h", 0))
        self.assertEqual(occurrance("Hello", "H"), ("H", 1))
