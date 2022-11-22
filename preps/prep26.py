def longest_word(strings):
	lst = strings.split()
	max_length = 0
	max_string = ""
	for string in lst:
		if len(string) > max_length:
			max_length = len(string)
			max_string = string
	return max_string
	