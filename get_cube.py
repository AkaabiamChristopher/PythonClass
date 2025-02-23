def get_cube(values):
	cube = []
	
	for i in values():
		cube.append(i**3)
	return cube
print(get_cube([1,2,3,4,5]))