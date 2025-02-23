my_dict = {"name":"Alice","age":25,"city":"New York"}
print(my_dict)

print(my_dict["name"])

if"city" in my_dict:
	print("city is in the dicttionary")

del my_dict["city"]
print(my_dict)

print(my_dict.get("name"))
print(my_dict.get("salary","Not Availabe"))

for key in my_dict:
	print(key)

for value in my_dict.value():
	print(value)