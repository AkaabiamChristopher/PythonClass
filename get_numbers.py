def get_numbers(number:list)-> int:
	total = 0
	for numbers in number:
		if numbers % 2 == 0:
			total += numbers
	return total

print(get_numbers([2,7,9,17,19,2,8,10]))


 