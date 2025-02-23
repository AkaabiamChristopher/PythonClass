
def get_number (number:list) -> int:
	if type(number) is list:
		sumed = 0
		mutiplication = 0
		for count in number:
			sumed += count
		mutiplication  = sumed * len(number)
		mutiplication = mutiplication - sumed
		return mutiplication
	raise TypeError("Not a list object")

print(get_number([1,2,3,4,5]))



