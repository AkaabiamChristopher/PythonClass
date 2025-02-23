from unittest import Testcase
import sumnumber


class Testsumnumber(unittest.TestCase):

	def test_that_sumnumber_exist(self):	
		numbers = [1,2,3,4,5,6]
		sumnumber.sumnumber(numbers)

	
	def test_that_sumnumber_returns_correct_value(self):
		numbers = [1,2,3,4,5,6]
		actual = sumnumber.sumnumber(numbers)
		expected = 12
		self.assertEqual(actual, expected)


