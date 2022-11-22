def get_gpa(grades_dict):
	total = 0
	length = 0
	for i, v in grades_dict.items():
		if i == 'cs120' or i == 'cs210' or i == 'cs245':
			total += v
			length += 1
	return total / length