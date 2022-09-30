def print_words_starting_with(sentence, letter):	
	sentence_index = 0
	while sentence_index < len(sentence):
		character = sentence[sentence_index]
		if character == letter:
			word_index = sentence_index
			while word_index < len(sentence) and sentence[word_index] != ' ':
				print(sentence[word_index], end = '')
				word_index += 1			
			print("")
		sentence_index += 1