from unittest import TestCase
import get_numbers

class Testget_numbers(TestCase):
	def test_that_get_numbers_exist(self):
		get_numbers.get_numbers([2,7,9,17,19,2,8,10])

	def test_that_get_numbers_correct(self):
		actual = get_numbers.get_numbers([2,7,9,17,19,2,8,10])
		expected = 22
		self.assertEqual(actual,expected)