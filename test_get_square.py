from unittest import TestCase
import get_square

class TestGetSquare(TestCase):
	def test_that_get_square_numbers_function_exists(self):
		number = 4
		get_square.get_square


	def test_that_get_square_function_return_correct_value(self):
		actual = get_square.get_square(self)
		actual = (4)
		expected = [1,5,12,15,8]
		self.assertEqual(actual,expected)