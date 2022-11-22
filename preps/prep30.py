def copy_and_increment(lst):
	new_list = []
	i = 0
	while i < len(lst):
		new_list.append(lst[i]+1)
		i += 1
	return new_list