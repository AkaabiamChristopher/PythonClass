import math

latitude_1 = float(input("Enter the latitude of coordinate 1: "))
longitude_1 =  float(input("Enter the longitude of coordinate 1: "))
latitude_2 =  float(input("Enter the latitude of coordinate 2: "))
longitude_2 =  float(input("Enter the longitide of coordinate 2: "))
radius = 6371.01

distance = radius * math.acos(math.sin(latitude_1) * math.sin(latitude_2) + math.cos(latitude_1) * math.cos(latitude_2) * math.cos(longitude_1 - longitude_2))
print(distance)