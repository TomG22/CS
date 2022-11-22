def every_other(strings):
	lst = strings.split()
	new_strings = ""
	i = 0
	for string in lst:
		if i % 2 == 0:
			new_strings += string + " "
		i += 1
	return new_strings
	