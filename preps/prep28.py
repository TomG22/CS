def count_calories(calories_dict):
	total = 0
	for food, calories in calories_dict.items():
		total += calories
	return total