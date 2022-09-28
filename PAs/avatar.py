#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program draws a character based off the give inputs.
# Type in one of the options for the types of character to draw.
# If custom is chosen, provide the proper inputs for each question.
# Type exit to exit the program early.
#


def f_hat_style(style):
	if style == "left":
		print('''
          ~-~       
        /-~-~-\\
    ___/_______\\''')
	elif style == "right":
		print('''
       ~-~       
     /-~-~-\\     
    /_______\\___''')
	elif style == "both":
				print('''
       ~-~       
     /-~-~-\\     
 ___/_______\\___ ''')
	elif style == "front":
		print('''
       ~-~       
     /-~-~-\\     
    /_______\\''')


def f_hair(bool):
    if bool == "True":
        print(
'''   "|   V   |"    
   "|  ~~~  |"    
   " \\_____/ "''')
    elif bool == "False":
        print(
"""    |   V   |     
    |  ~~~  |     
     \\_____/""")

def f_eyes(style, hair_bool):
    if hair_bool == "True":
        print('   "|"""""""|"')
        print('   "| ' + style + "   " + style + ' |"')
    elif hair_bool == "False":
        print("    |'''''''|")
        print("    | " + style + "   " + style + " |")

def f_arms(style, torso_length):
    print(" 0" + style * 4 + "|---|" + style * 4 + "0")

def f_torso(length):
    i = 0
    while i < length:
        print("      |-X-|")
        i += 1
    print("      HHHHH")

def f_legs(length):
    i = 0
    while i < length:
        print(" " * (5 - i) + "///" + " " + "  " * i + "\\\\\\")
        i += 1

def f_shoes(style):
        print(style + "       " + style)

def Jeff():
    f_hat_style("both")
    f_eyes("0", "False")
    f_hair("False")
    print("      |-X-|")
    f_arms("=", 4)
    f_torso(4)
    f_legs(2)
    f_shoes("#HHH#")

def Jane():
    f_hat_style("right")
    f_eyes("*", "True")
    f_hair("True")
    f_arms("T", 2)
    f_torso(2)
    f_legs(3)
    f_shoes("<|||>")

def Chris():
    f_hat_style("front")
    f_eyes("U", "False")
    f_hair("False")
    print("      |-X-|")
    f_arms("W", 2)
    f_torso(2)
    f_legs(4)
    f_shoes("<>-<>")

def custom():
    print("Answer the following questions to create a custom avatar")
    hat = input("Hat style ?\n")
    eyes = input("Character for eyes ?\n")
    hair = input("Long hair (True/False) ?\n")
    arms = input("Arm style ?\n")
    torso = int(input("Torso length ?\n"))
    legs = int(input("Leg length (1-4) ?\n"))
    shoes = input("Shoe look ?\n")
    f_hat_style(hat)
    f_eyes(eyes, hair)
    f_hair(hair)
    f_arms(arms, torso)
    f_torso(torso)
    f_legs(legs)
    f_shoes(shoes)

def init_prompt():
    print("----- AVATAR -----")

    avatar_type = input("Select an Avatar or create your own:\n")
    while avatar_type != "custom" and avatar_type != "Jeff" and avatar_type != "Jane" and avatar_type != "Chris" and avatar_type != "exit":  
        avatar_type = input("Select an Avatar or create your own:\n")

    if avatar_type == "Jeff":
        Jeff()
    elif avatar_type == "Jane":
        Jane()
    elif avatar_type == "Chris":
        Chris()
    elif avatar_type == "custom":    
        custom()

init_prompt()
