import unittest
import test_sums_number


class Test_sums_number(unittest.TestCase):

	def test_that_sums_number_exist(self):	
		numbers = [1,2,3,4,5,6]
		sum_number.sums_number(numbers)

	
	def test_that_sums_number_returns_correct_value(self):
		numbers = [1,2,3,4,5,6]
		actual = sums_number.sum_number(numbers)
		expected = 12
		self.assertEqual(actual, expected)



