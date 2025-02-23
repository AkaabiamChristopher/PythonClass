def get_even_number(number):
    return number % 2 == 0

def get_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def subtraction(a, b):
    return abs(a - b)

def division(a, b):
    if b == 0:
        return 0
    return a / b

def factor_of_number(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count

def get_square_of_number(number):
    return number ** 0.5 % 1 == 0

def get_palindrome_of_number(nummber):
    original_nummber = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number // == 10
    return original_number == reversed_number

def factorial_of_number(number):
    if number = 0:
        return 1
    return number * factorial_of_number(number - 1)

def square_of_number(number):
    return number * number
