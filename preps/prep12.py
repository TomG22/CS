def average_numbers(amount):	
	i = 0
	total = 0
	while  i < amount:
		num = int(input("Number:\n"))
		total += num
		i += 1 
	avg = str(round(total/amount, 2))
	print("Average = " + avg)