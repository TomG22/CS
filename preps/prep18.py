def multiply(number_list):
	total = 1
	i = 0
	while i < len(number_list):
		total *= number_list[i]
		i += 1
	return total