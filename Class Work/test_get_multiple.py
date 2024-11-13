from unittest import TestCase
import functionmultiplication


class TestMultiplicationFunction(TestCase):
	def test_multiplication_function_return_correct_value(self):
		actual= functionmultiplication.get_multiply(3, 4)
		expected = 12
		self.assertEqual(actual, expected)


	def test_that_cube_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, functionmultiplication.get_multiply, "moses","Tawio")


	def test_multiplication_function_return_correct_value(self):
		actual= functionmultiplication.get_multiply(2.3, 2.4)
		expected = 5.52
		self.assertEqual(actual, expected)


	