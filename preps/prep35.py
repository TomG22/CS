def get_common_movies(sets):
	return_set = set()
	for _set in sets:
		for item in _set:
			found_item = None
			for _set in sets:
				if item in _set and found_item != False:
					found_item = item
				else:
					found_item = False
			if found_item:
				return_set.add(found_item)
	return return_set