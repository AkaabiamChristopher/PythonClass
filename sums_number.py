def sum_number(numbers):
	sums = 0
	for number in numbers:
		if number % 2 == 0:
		 sums += number
	return sums

numb =[2,2,3,3,4,4,5]
print(sum_number(numb))


