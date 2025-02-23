def get_number(numbers):
	
	summed = 0
	for i in range(len(numbers)):
		summed += (sum(numbers) - numbers[i])
	return summed

	
def merge_and_sort(number1,number2):
	
	numbers = number1 + number2
	
	numbers.sort()
	return numbers	

def getvowels(strings):
	strings = strings.lower()
	totalvowels = 0
	for alphabet in strings:
		if alphabet in 'aeiou':
			totalvowels += 1
	return totalvowels

def getanagram(first,second):
	first.lower()
	second.lower()
	numberofsamealphabet = 0
	if len(first) != len(second):
		return "false"
			
	else:
		for letter in first:
			for alpha in second:
				if letter == alpha:
					numberofsamealphabet += 1
	if numberofsamealphabet == len(first):
		return "True"

def getevennumber(numbers):
	totaleven = 0
	for number in numbers:
		if number % 2 == 0:
			totaleven += number
	return totaleven
			
def getprime(number):
	primecounter = 0
	if number <= 1:
		return False
	for i in range(2,number):
		if number % i == 0:
			primecounter += 1
	if primecounter == 0:
		return True
	else: return False
		
def getpalindrome(string):
	string = string.lower().replace(" ", "")  
	pal = string[::-1]
	if pal == string:
		return True
	else:
		returnFalse