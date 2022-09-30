def count_characters(string, letter_1, letter_2):
	i = 0
	letter_1_count = 0
	letter_2_count = 0
	while i < len(string):
		if string[i] == letter_1:
			letter_1_count += 1
		if string[i] == letter_2:
			letter_2_count += 1
		i += 1
	print("'" + letter_1 + "' and '" + letter_2 + "' appeared " + str(letter_1_count + letter_2_count) + " times in the string '" + string +"'")