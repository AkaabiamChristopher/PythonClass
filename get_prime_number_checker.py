def get_prime_number(value: int) -> list:
    array = []
    for i in range(2, value):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            array.append(i)
    
    print(array)
    return array

number = 19
get_prime_number(number)




