from unittest import TestCase
import get_sum_numbers

class Test_get_sum_numbers(TestCase):
	def test_that_get_sum_numbers_exist(self):
		get_sum_numbers.get_sum_numbers([2,7,9,17,19,2,8,10])

	def test_that_get_sum_numbers_correct(self):
		actual = get_sum_numbers.get_sum_numbers([2,7,9,17,19,2,8,10])
		expected = 22
		self.assertEqual(actual, expected)