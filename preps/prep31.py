def get_elements(dict, int):
	numbers = []
	for i,v in dict.items():
		if i[0].isupper() or i[len(i)-1].isupper() or v > int:
			numbers.append(v)
	return numbers
