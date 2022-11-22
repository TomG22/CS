#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program produces an infographic that analyzes the words in a given text file
# using the graphics.py module. This is done using dictionaries which organize the file data into 
# categories. The result is the graphic displayed in bar graph format aided by text.
#

from graphics import graphics

def draw_bar1(gui, cap_dict, len_dict):
	'''This function draws the word length bar graph using the cap_dict and len_dict dictionaries.
	Parameters: gui can be a graphics object
	cap_dict can be a dictionary
	len_dict can be a dictionary
	'''
	gui.rectangle(120, 250, 200, (500/len(cap_dict['count_dict']))*len_dict['small'], "dodgerblue")
	gui.text(130, 250, "small words", "white",  15)
	gui.rectangle(120, 250 + (500/len(cap_dict['count_dict']))*len_dict['small'], 200,
		(500/len(cap_dict['count_dict']))*len_dict['medium'], "green")
	gui.text(130, 250 + (500/len(cap_dict['count_dict']))*len_dict['small'],
	"medium words", "white",  15)
	gui.rectangle(120, 250 + (500/len(cap_dict['count_dict']))*len_dict['small'] +
		(500/len(cap_dict['count_dict']))*len_dict['medium'], 200,
		(500/len(cap_dict['count_dict']))*len_dict['large'], "dodgerblue")
	gui.text(130, 250 + (500/len(cap_dict['count_dict']))*len_dict['small'] + 
		(500/len(cap_dict['count_dict']))*len_dict['medium'], "large words", "white",  15)

def draw_bar2(gui, cap_dict):
	'''This function draws the capitalization bar graph using the cap_dict dictionary.
	Parameters:
	gui can be a graphics object
	cap_dict can be a dictionary
	'''
	gui.text(370, 200, "Cap/Non-Cap", "white", 25)
	gui.rectangle(370, 250, 200, (500/len(cap_dict['count_dict']))*cap_dict['cap'], "dodgerblue")	
	gui.text(380, 250, "Capitalized", "white",  15)
	gui.rectangle(370, 250 + (500/len(cap_dict['count_dict']))*cap_dict['cap'], 200,
		(500/len(cap_dict['count_dict']))*cap_dict['no_cap'], "green")
	gui.text(380, 250 + (500/len(cap_dict['count_dict']))*cap_dict['cap'], 
		"Non Capitalized", "white",  15)

def draw_bar3(gui, cap_dict, punc_dict):
	'''This function draws the punctuation bar graph using the cap_dict and punc_dict dictionaries.
	Paramters: gui can be a graphics object
	cap_dict can be a dictionary
	punc_dict can be a dictionary
	'''
	gui.text(620, 200, "Punctuation", "white", 25)
	gui.rectangle(620, 250, 200, (500/len(cap_dict['count_dict']))*punc_dict['punc'], "dodgerblue")
	gui.text(630, 250, "Punctuated", "white",  15)
	gui.rectangle(620, 250 + (500/len(cap_dict['count_dict']))*punc_dict['punc'], 200,
		(500/len(cap_dict['count_dict']))*punc_dict['non_punc'], "green")
	gui.text(630, 250 + (500/len(cap_dict['count_dict']))*punc_dict['punc'], 
		"Non Punctuated", "white",  15)

def draw_graphic(file_name, len_dict, cap_dict, punc_dict):
	'''This function draws all of the infographic using the graphics module. It converts the data 
	inside of the dictionaries into bar graphs along with descriptive text. To save space, cap_dict 
	has a key named "count_dict" which contains the count dictionary in the get_dict function.
	Parameters: file_name can be a string
	len_dict can be a dictionary
	cap_dict can be a dictionary
	punc_dict can be a dictionary'''
	gui = graphics(950, 800, "infographic")
	gui.rectangle(0,0, 950, 800, "grey30")
	gui.text(50, 40, file_name, "cyan", 28)
	gui.text(50, 100, "Total Unique Words: " + str(len(cap_dict['count_dict'])), "white", 20)
	gui.text(50, 150, "Most used words (s/m/l): ", "white",  15)
	gui.text(280, 150, len_dict['most_small'] + 
		" (" + str(cap_dict['count_dict'][len_dict['most_small']]) + "x)" + " " + 
		len_dict['most_medium'] +
		" (" + str(cap_dict['count_dict'][len_dict['most_medium']]) + "x)" + " " +
		len_dict['most_large'] + 
		" (" + str(cap_dict['count_dict'][len_dict['most_large']]) + "x)", "cyan", 15)
	gui.text(120, 200, "Word lengths", "white", 25)	
	
	draw_bar1(gui, cap_dict, len_dict)
	draw_bar2(gui, cap_dict)
	draw_bar3(gui, cap_dict, punc_dict)

	gui.draw()

def iterate_dict(count_dict, punc_dict, len_dict, cap_dict):
	'''This function iterates through the count_dict dictionary and assigned particular 
	values to the other designated dictionaries for their particular categories, effectively sorting
	the categorized data for each bar graph.
	Parameters:	count_dict can be a dictionary
	punc_dict can be a dictionary
	len_dict can be a dictionary
	cap_dict can be a dictionary
	'''
	for i,v in count_dict.items():
		if 0 <= len(i) <= 4:
			len_dict['small'] += 1
			if len_dict['most_small'] == None:
				len_dict['most_small'] = i
			elif v > count_dict[len_dict['most_small']]:
				len_dict['most_small'] = i
		elif 5 <= len(i) <= 7:
			len_dict['medium'] += 1
			if len_dict['most_medium'] == None:
				len_dict['most_medium'] = i
			elif v > count_dict[len_dict['most_medium']]:
				len_dict['most_medium'] = i
		elif len(i) >= 8:
			len_dict['large'] += 1
			if len_dict['most_large'] == None:
				len_dict['most_large'] = i
			elif v > count_dict[len_dict['most_large']]:
				len_dict['most_large'] = i
		if i[0].isupper():
			cap_dict['cap'] += 1
		else:
			cap_dict['no_cap'] += 1
		if i[len(i)-1] == "!" or i[len(i)-1] == "." or i[len(i)-1] == "," or i[len(i)-1] == "?":
			punc_dict['punc'] += 1
		else:
			punc_dict['non_punc'] += 1
	return len_dict, cap_dict, punc_dict

def get_dict(file_name):
	'''This function opens the given file using the file_name parameter. It iterates through the
	lines of the file and counts up the occurences of words into a dictionary called "count_dict".
	Then, this dictionary is iterated through to create the other dictionaries which classify the
	words by specfic attributes (len_dict being word length; punc_dict being word punctuation;
	and cap_dict being word capitalization). These dictionaries are then returned.
	Parameters:
	file_name can be a string
	'''
	lines = open(file_name, "r").readlines()
	lines = " ".join(lines).split(" ")
	count_dict = {}
	i = 0
	while i < len(lines):
		lines[i] = lines[i].strip("\n")
		if lines[i] == "":
			lines.pop(i)
		count_dict[lines[i]] = 0
		i += 1
	max_num = 0 
	for line in lines:
		count_dict[line] += 1
	punc_dict = {'punc': 0, 'non_punc': 0}
	len_dict = {'small': 0, 'medium': 0, 'large': 0, 'most_small': None, 
				'most_medium': None, 'most_large': None}
	cap_dict = {'cap': 0, 'no_cap': 0, 'count_dict': count_dict}
	
	return iterate_dict(count_dict, punc_dict, len_dict, cap_dict) 

def main():
	file_name = input("Infographic file:\n")
	len_dict, cap_dict, punc_dict = get_dict(file_name)
	draw_graphic(file_name, len_dict, cap_dict, punc_dict)

main()