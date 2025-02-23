from unittest import TestCase
import squarenumber

class TestFunctionsquarenumber(TestCase):
	def test_that_square_function_exist(self):
		functionsquarenumber.get_square(5)

	def test_that_square_function_returns_correct_value(self):
		actual = functionsquare.get_square(5)
		expected = 25
		self.assertEqual(actual, expected)