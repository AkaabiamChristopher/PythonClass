import math

number_of_sides = int(input("Enter numberofsides: "))
number_of_length = int(input("Enter numberoflength of one of the sides: "))

area = (number_of_sides*number_of_length**2) / (4*math.tan(math.pi/number_of_sides))
print(area)