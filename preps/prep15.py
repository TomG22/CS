def get_height_category(gender, height):	
	if gender == "male":
		if height <= 70:
			return "below average"
		else:
			return "above average"
	elif gender == "female":
		if height <= 64:
			return "below average"
		else:
			return "above average"
	else:
		return "unknown average"