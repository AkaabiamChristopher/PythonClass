from unittest import TestCase
import squarenumber

class TestFunctionsquarenumber(TestCase):
	def test_that_square_function_exist(self):
		squarenumber.get_squarenumber(5,4)

	def test_that_square_function_returns_correct_value(self):
		actual = squarenumber.get_squarenumber(5,5)
		expected = 1
		self.assertEqual(actual, expected)