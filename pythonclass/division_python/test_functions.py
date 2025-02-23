import unittest
import functions



class TestGetNumber(unittest.TestCase):

	def test_that_getnumber_returns_correct_value(self):
		
		number = [1,2,3,4,5]

		actual = functions.get_number(number)

		expected = 60     
		self.assertEqual(actual, expected)

class TestMergeAndSort(unittest.TestCase):

	def test_that_merge_and_sort_returns_correct_value(self):
		
		number1 = [1,2,3,4,9]
		number2 = [5,6,7,8,12]

		actual = functions.merge_and_sort(number1,number2)

		expected = [1,2,3,4,5,6,7,8,9,12]     
		self.assertEqual(actual,expected)

class TestGetVowels(unittest.TestCase):

	def test_that_getvowels_returns_correct_value(self):
		strings = "python is sweet"

		actual = functions.getvowels(strings)

		expected = 4    
		self.assertEqual(actual,expected)

class TestGetAnagram(unittest.TestCase):

	def test_that_getanagram_returns_correct_value(self):
		first = "silent"
		second = "listen"

		actual = functions.getanagram(first, second)

		expected = "True"    
		self.assertEqual(actual,expected)

class TestGetEvenNumbers(unittest.TestCase):

	def test_that_getevennumbers_returns_correct_value(self):
		numbers = [1,2,3,4,5,6]

		actual = functions.getevennumber(numbers)

		expected = 12    
		self.assertEqual(actual,expected)

class TestGetPrime(unittest.TestCase):

	def test_that_getprime_returns_correct_value(self):
		number = 7

		actual = functions.getprime(number)

		expected = True   
		self.assertEqual(actual,expected)

class TestGetPalindrome(unittest.TestCase):

	def test_that_getpalindrome_returns_correct_value(self):
		string = "madam"

		actual = functions.getpalindrome(string)

		expected = True   
		self.assertEqual(actual,expected)
