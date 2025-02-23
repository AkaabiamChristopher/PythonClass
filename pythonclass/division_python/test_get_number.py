
class TestGetSum(TestCase):
	def test_that_get_sum_function_exist(self):
		addition_of_list.get_sum([1,2,3,4])

	def test_that_get_sum_function_correct(self):
		actual = addition_of_list.get_sum([1,2,3])
		expected = 12
		self.assertEqual(actual, expected)



	def test_that_get_sum_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, addition_of_list.get_sum, "Moses")



class TestGetMergeFunction(TestCase):
	def test_that_get_merge_function_exist(self):
		addition_of_list.get_combination([1,2,3], [7, 9, 8])



	def test_that_get_merge_function_return_value(self):
		actual  = addition_of_list.get_combination([1,2,4,90], [-8,3, 5, 6])
		expected = [-8,1, 2, 3, 4, 5, 6,90]
		self.assertEqual(actual, expected)