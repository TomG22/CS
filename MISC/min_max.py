def min_max(a, b, c):
	max = 0
	min = 0
	if a > b and a > c:
		max = a
	elif b > a and b > c:
		max = b
	elif c > b and c > a:
		max = c
	if a < b and a < c:
		min = a
	elif b < a and b < c:
		min = b
	elif c < a and c < b:
		min = c
	return min, max
minimum, maximum = min_max(40,70,10)
print(minimum, maximum)