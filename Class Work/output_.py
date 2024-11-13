int(input("Enter input number from 1 to 5: "))
for num in range(1,5,+ -1):
	for number in range(1,num + 1,-1):
		print(number,end = " ")
	print()