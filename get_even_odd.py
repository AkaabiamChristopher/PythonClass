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
print(get_even_odd([5,3,7,9,2,8]))