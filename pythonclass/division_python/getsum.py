
def get_sum (number:list) -> int:
	if type(number) is list:
		sumed = 0
		mutiplication = 0
		for count in number:
			sumed += count
		mutiplication  = sumed * len(number)
		mutiplication = mutiplication - sumed
		return mutiplication
	raise TypeError("Not a list object")

print(get_sum([1,2,3,4,5]))



