#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program draws a nature scene that can be interacted with by the user.
# Press 'z' to zoom in and out
# Press 'r' to reset the scene
# Press 'c' to toggle coordinates with axis
#

from graphics import graphics
import random

def random_color():
	'''
	Returns a random hex color code when called
	'''
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return win.get_color_string(r, g, b)

def calc_pos(position, direction, parallax_dampen):
	'''
	Description: Returns the mathematical calculation for how far the objects' positions
	relative to the both the parallax and global_scale or zoom level
	Parameters: position can be an integer
	direction can be a string ("y" or "x")
	parallax_dampen can be an integer
	'''
	if direction == "x":
		return position*global_scale + parallax_x/parallax_dampen + global_offset_x
	else:
		return position*global_scale + parallax_y/parallax_dampen + global_offset_y

def draw_mountains():
	'''
	Description:
	Draws the mountains in the background which use the random, globally assigned color variables 
	'''
	global parallax_x, parallax_y, global_scale, color_1, color_2, color_3
	win.triangle(
		calc_pos(360, "x", 2.5), calc_pos(100, "y", 2.5), 
		calc_pos(200, "x", 2.5), calc_pos(500, "y", 2.5),
		calc_pos(500, "x", 2.5), calc_pos(500, "y", 2.5),
		color_1)
	win.triangle(
		calc_pos(200, "x", 2.5), calc_pos(200, "y", 2.5),
		calc_pos(-50, "x", 2.5), calc_pos(500, "y", 2.5),
		calc_pos(450, "x", 2.5), calc_pos(500, "y", 2.5),
		color_2)
	win.triangle(
		calc_pos(550, "x", 2.5), calc_pos(200, "y", 2.5), 
		calc_pos(300, "x", 2.5), calc_pos(500, "y", 2.5),
		calc_pos(850, "x", 2.5), calc_pos(500, "y", 2.5),
		color_3)

def draw_birds(frame_time):
	'''
	Description: Draws 5 birds which are offset from each other a specified amount
	and then moves them relative to a global time tracking variable
	Parameters: frame_time can be an integer
	'''
	bird_index = 0
	speed = 6
	offset = frame_time * speed

	while bird_index < 5:
		bird_width = bird_index * 80 - 400 + offset
		bird_height = bird_index * 30 + 40
		win.line(
			calc_pos(bird_width + 1, "x", 1.5), calc_pos(bird_height, "y", 1.5), 
			calc_pos(bird_width - 30, "x", 1.5), calc_pos(bird_height - 10, "y", 1.5), 
			"black", 5 * global_scale)
		win.line(
			calc_pos(bird_width - 1, "x", 1.5), calc_pos(bird_height, "y", 1.5), 
			calc_pos(bird_width + 30, "x", 1.5), calc_pos(bird_height - 10, "y", 1.5),
			"black", 5 * global_scale)
		bird_index += 1

def draw_landscape():	
	'''
	Description: Draws all of the shapes which make the landscape: sun, grass, mountains, etc...
	'''
	win.rectangle(0, 0, 720, 720, 'lightblue')
		
	win.ellipse(calc_pos(600, "x", 4), calc_pos(100, "y", 4), 
		100 * global_scale, 100 * global_scale, 'yellow')
	
	draw_mountains()

	win.rectangle(0, calc_pos(470, "y", 1), 
		width * global_scale, 200 * global_scale, "lightgreen")
	
	i = -30
	while i <= 800:
		win.line(
			calc_pos(i, "x", 1), calc_pos(500, "y", 1), 
			calc_pos(i, "x", 1), calc_pos(450, "y", 1), 
			"lightgreen", 3 * global_scale)
		i += 8

	win.rectangle(calc_pos(480, "x", 1.5), calc_pos(480, "y", 1.5), 
		40 * global_scale, 80 * global_scale, "brown")	
	win.ellipse(calc_pos(500, "x", 1.5) , calc_pos(425, "y", 1.5),
	 80 * global_scale, 150 * global_scale, "green")

def draw_coordinates():
	'''
	Description: Draws a crosshair along with the cursor position on the screen
	when the crosshair variable is True
	'''
	global crosshair, width, height
	if crosshair == True:
		win.text(0, 620, "Mouse (X, Y): " + str(win.mouse_x) + ", " + str(win.mouse_y))
		win.line(win.mouse_x, 0, win.mouse_x, height, "white", 3)
		win.line(0, win.mouse_y, width, win.mouse_y, "white", 3)

def on_key_action(self, key):
	'''
	Description: If a key is pressed that is registered by the graphics module,
	it will return the character of the key that was pressed.
	Parameters: self is referring to the graphics class in the module
	key is the string that is returned
	'''
	if key == "r":		
		global color_1, color_2, color_3, frame_time, global_scale
		frame_time = 0
		global_scale = 1
		color_1 = random_color()
		color_2 = random_color()
		color_3 = random_color()

	elif key == "f":
		if win.primary.state() != "zoomed":
			win.primary.state("zoomed")
		else:
			win.primary.state("normal")

	elif key == "c":
		global crosshair
		if crosshair == True:
			crosshair = False
		else:
			crosshair = True

	elif key == "z":
		if global_scale == 1:
			global_scale = 1 + .5
		elif global_scale == 1.5:
			global_scale = 2
		elif global_scale == 2:
			global_scale = 1

def main():
	global win, width, height, frame_rate, cycle_time
	width, height = 720, 720
	win = graphics(width, height, 'Landscape')
	win.primary.state("zoomed")
	frame_rate = 60
	cycle_time = 5
	
	global color_1, color_2, color_3
	color_1 = random_color()
	color_2 = random_color()
	color_3 = random_color()

	global parallax_x, parallax_y

	global global_scale, global_offset_x, global_offset_y
	global_scale = 1

	global frame_time
	frame_time = 0

	global crosshair
	crosshair = False

	while True:
		win.clear()
		win.set_keyboard_action(on_key_action)
		parallax_x = (win.mouse_x - width/2)/40
		parallax_y = (win.mouse_y - height/2)/40
		global_offset_x = ((global_scale * width) - width)/width * - (win.mouse_x)
		global_offset_y = ((global_scale * height) - height)/height * - (win.mouse_y)
		draw_landscape()
		draw_coordinates()
		draw_birds(frame_time)
		
		if frame_time + 1 > frame_rate * cycle_time:
			frame_time = 0
		win.update_frame(frame_rate)
		frame_time = frame_time + 1

main()