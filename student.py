def score_grade(**args):
	students_list = []
	count = 0
	while count < 10:
		for i in range(1,11):
			print(f"<---Enter name of student{i}--->")
			student = (input())
			students_list.append(student)
			count += 1
	languages = ["Python", "JavaS", "DataScience", "DesignThinking"]
	
	
	for i in range(0, 9):
		for j in range(0, 4): 
			print(f"Enter {students_list[i]} score in {languages[j]}")
		scores = (input())
		scores = scores.split(",")
		students_list[i].append(scores)	
		print(f"Enter {students_list[i]} score in {languages[j]}")
		
	print(students_list)



score_grade()