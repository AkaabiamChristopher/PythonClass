import random

correct = 0
failed = 0
counter = 0


random.randrange(1, 1000)

for number in range(1, 1000):
	number = int(input("Enter number:"))

if number == 4:
	print("correct")
elif number != 4:
	print("failed")
