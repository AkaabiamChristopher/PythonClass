from unittest import TestCase
import prime_numbers

class TestPrimeFunction(TestCase):
	def test_that_get_prime_numbers_function_exists(self):
		primenumberprograms.get_prime_numbers(3)


	def test_that_get_prime_numbers_function(self):
		actual = prime_number.get_prime_numbers(19)
		expected = [2, 3, 5, 7, 11, 13, 17]
		self.assertEqual(actual, expected)