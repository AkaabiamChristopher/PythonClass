import unittest
from arrangement import arrangement

class testarrangeuppercasefirst(unittest.TestCase):
    def test_mixed_case(self):
        self.assertEqual(arrangement("sEmIColOn"), "EICOsmoln")

    def test_all_uppercase(self):
        self.assertEqual(arrangement("HELLO"), "HELLO")

    def test_all_lowercase(self):
        self.assertEqual(arrangement("hello"), "hello")

    def test_alternating_case(self):
        self.assertEqual(arrangement("hElLo"), "ELhlo")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            arrangement("")

    def test_single_uppercase_character(self):
        self.assertEqual(arrangement("A"), "A")

    def test_single_lowercase_character(self):
        self.assertEqual(arrangement("a"), "a")

