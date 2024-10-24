number = int(input('Enter anumber between o and 1000:'))
num1 = number//100
num2 = (number//10)//10
num3 = number&10

sum = num1  + num2 + num3
print('The sum of digit is', sum)