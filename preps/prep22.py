def most_common_vehicle(file_name):
	file = open(file_name, "r")
	
	max_num = 0
	num_list = []
	for line in file:
		line = int(line.strip("\n"))
		num_list.append(int(line))
		if line > max_num:
			max_num = line
		elif line == max_num:
			print("There's a tie!")
			exit()
	
	if max_num == num_list[0]:
		print("Toyota most common")
	elif max_num == num_list[1]:
		print("Ford most common")
	elif max_num == num_list[2]:
		print("Chevy most common")
