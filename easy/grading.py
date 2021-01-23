def gradingStudents(grades):
	new_grades=[]
	for i in grades:
		if(i>38):
			curr=i
			while(1):
				if(curr%5==0):
					if(curr-i<3):
						new_grades.append(curr)
						break
					else:
						new_grades.append(i)
						break
						
				curr+=1
		else:
			new_grades.append(i)
	print(new_grades)
gradingStudents([44,52,49,23,98])
