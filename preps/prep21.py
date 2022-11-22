def two_words(string_list):
	least = "z"
	greatest = "A"
	for word in string_list:
		if word > greatest:
			greatest = word
		if word < least:
			least = word
	return least + " " + greatest