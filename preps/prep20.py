def grade_info(grade_list):
	minimum = 100
	maximum = 0
	total = 0 
	for grade in grade_list:
		if grade < minimum:
			minimum = grade
		if grade > maximum:
			maximum = grade
		total += grade
	return maximum, minimum, total/len(grade_list)