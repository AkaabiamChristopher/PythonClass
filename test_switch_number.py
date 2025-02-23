import unittest
import switch_number



class Testswitchnumber(unittest.TestCase):

	def test_that_switch_number_returns_correct_value(self):
		
		number = [1,2,3,4,5]

		actual = switch_number.switch_number(number)

		expected = True     
		self.assertEqual(actual, expected)


	