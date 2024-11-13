failed = 0
passes = 0
count = 1
for result in range(15):

	result = int(input("Enter number "))

	if result < 45:
	     failed += 1	
if result >= 45:
	passes = passes + 1 	
			
print("Passed: ", passes)
print("Failed: ", failed)

count += 1