import os
total = 0
for root, dirs, files in os.walk("C:/Users/giall/Desktop/Programming/Python/CS/"):
	for file in files:
		print(file)
		if str(file)[-2:] == "py":
			print(open(file, "r").readlines())
