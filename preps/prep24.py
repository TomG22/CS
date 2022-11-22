def count_vowels(string, A, B):
	i = A
	vowel_count = 0
	while i <= B:
		if string[i] == "a" or string[i] == "e" or string[i] == "i"\
		or string[i] == "o" or string[i] == "u":
			vowel_count += 1
		i += 1
	return vowel_count
	