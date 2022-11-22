def get_supply_count():
	supplies_file = open("supplies.txt", "r")
	total = 0
	for line in supplies_file:
		num = int(line.split()[1].strip("\n"))
		total += num
	total_file = open("total.txt", "w")
	total_file.write(str(total))
	