def swap(dict, set):
	similar_dict = {}
	swap_dict = {}
	for i,v in dict.items():
		if i in set:
			 swap_dict[v] = i
		else:
			similar_dict[i] = v
	dict.clear()
	for i,v in similar_dict.items():
		dict[i] = v
	for i,v in swap_dict.items():
		dict[i] = v

dict_data = {'a':'b', 'c':'d', 'e':'f'}
set_data = {'c', 'e'}
swap(dict_data, set_data)