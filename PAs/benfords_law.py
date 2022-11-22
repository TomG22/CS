#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program creates a graphical representation of the occurences 
# of the first digit in the inputted sample file.
# If the user sets the mode to text, a textual representation will be printed.
# If the user sets the mode to gui, a graphical representation will run.
#

from graphics import graphics

def draw_print(counts, string):
	'''Prints the graphical representation of the count dictionary
	Parameters: counts can be a dictionary
	string can be a string'''
	for i,v in counts.items():
		if i != "numbers_list_length":
			print(str(i) + " | " + int(v*100/counts["numbers_list_length"]) * "#")
	print("\n" + string)

def draw_gui(counts, string):
	'''Draws the graphical representation of the count dictionary using graphics.py
	Parameters: counts can be a dictionary
	string can be a string'''
	gui = graphics(700, 700, "Benford's Law")
	while True:
		gui.rectangle(0, 0, 700, 700, "cyan")
		gui.rectangle(50, 50, 600, 600, "black")
		gui.rectangle((700-590)/2, (700-590)/2, 590, 590, "cyan")
		gui.text(160, 10, "Benford's Law Analysis Results", "black", 20)
		gui.text(50, 660, string, "black", 18)

		i = 0
		for i,v in counts.items():
			if i != "numbers_list_length":
				gui.rectangle(85, i*65, int(counts[i]*100/counts["numbers_list_length"])*1500,
				600/(len(counts)-1)-20)
				gui.text(60, i*65 + 10, i)
				i += 1
		gui.update_frame(60)

def check(counts):
	'''Checks if the given dictionary follows Benford's Law 
	If it does, the function returns True, otherwise it returns False
	Parameters: counts can be a dictionary'''
	benfords_dict = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}
	for i,v in benfords_dict.items():
		if not (v - 5) <= int(counts[i]*100/counts["numbers_list_length"]) <= (v + 10):
			return False
	return True

def count(file_name):
	'''Counts the number of occurences of the first digit in a sample file and 
	returns this data as a dictionary.
	Parameters: file_name can be a string
	'''
	sample_lines = open(file_name, "r")
	numbers_list = []
	counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	for line in sample_lines:
		line = line.strip("\n")
		line = line.split(",")
		for element in line:
			if element[0].isnumeric() and element[0] != "0" and element[len(element)-1].isnumeric():
				numbers_list.append(float(element))
				counts[int(element[0])] += 1
		counts["numbers_list_length"] = len(numbers_list)
	string = ""
	if check(counts):
		string = "Follows Benford's Law"
	else:
		string = "Does not follow Benford's Law"
	return counts, string

def main():
	file_name = input("Data file name:\n")
	mode = input("Mode:\n")
	while mode != "text" and mode != "gui":
		mode = input("Mode:\n")
	print()
	counts, string = count(file_name)
	if mode == "text":
		draw_print(counts, string)
	elif mode == "gui":
		draw_gui(counts, string)

main()