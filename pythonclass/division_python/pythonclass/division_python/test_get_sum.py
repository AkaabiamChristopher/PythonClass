import unittest
import getsum
class TestGetSum(unittest.TestCase):
	def test_that_get_sum_exist(self):
		getsum.get_sum([1,2,3,4])

	def test_that_get_sum_function_correct(self):
		actual = getsum.get_sum([1,2,3,4,5,6])
		expected = 105
		self.assertEqual(actual,expected)



	def test_that_get_sum_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError,getsum.get_sum, "chris")



