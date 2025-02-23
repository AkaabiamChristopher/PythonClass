def get_even_odd(input:list):
	odd = 0
	even = 0
	holder = []
	for count in input:
		if count % 2 == 0:
			even += 1
		else:
			odd += 1
	holder.append(odd)
	holder.append(even)
	return holder
print(get_even_odd([1,2,3,6,8,10,1]))