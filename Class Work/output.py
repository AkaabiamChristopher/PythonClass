number= int(input("Enter  number: "))
for number in range(1,number+1):
	for num in range(1,number,1):
		print(num,end=" ")
	print(number)