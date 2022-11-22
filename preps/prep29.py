def differences(set1, set2):
	differences = 0
	for element1 in set1:
		match = False
		for element2 in set2:
			if element2 == element1 and match == False:
				match = True
		if match == False:
			differences += 1

	for element2 in set2:
		match = False
		for element1 in set1:
			if element2 == element1 and match == False:
				match = True
		if match == False:
			differences += 1

	return differences
