from unittest import TestCase
import get_double_digit

class TestGetDoubleDigit(TestCase):
	def test_that_double_exist(self):
		get_double_digit.get_double_digit([1,2,3])

	def test_get_double_digit_correct(self):
		actual = get_double_digit.get_double_digit([1,2,3])
		expected = [2,4,6]
		self.assertEqual(actual,expected)


class TestGetDoubleDigit(TestCase):
	def test_that_words_greater_than_five_exist(self):
		get_double_digit.get_double_digit("Orange","Apple","Ice","Lime ")

	def test_get_double_digit_correct(self):
		actual = get_double_digit.get_double_digit([1,2,3])
		expected = [2,4,6]
		self.assertEqual(actual,expected)