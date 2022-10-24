#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program draws a character based off the give inputs.
# Type in one of the options for the types of character to draw.
# If custom is chosen, provide the proper inputs for each question.
# Type exit to exit the program early.
#

'''Each of the below functions prints out their particular module of the character'''

def f_hat_style(style):
    '''
    This function takes in a string to determine which hat style to print
    Parameters: style can be a string
    '''
    if style == "left":
        print('''~-~       
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
    '''
    This function takes in a boolean to determine which type of hairstyle to print
    Parameters: bool can be a string
    '''
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
    '''
    This function takes in a string parameter for the style of the eye
    along with a boolean to determine which hair style should be printed
    Parameters: style can be a string, hair_bool can be a string
    '''
    if hair_bool == "True":
        print('   "|"""""""|"')
        print('   "| ' + style + "   " + style + ' |"')
    elif hair_bool == "False":
        print("    |'''''''|")
        print("    | " + style + "   " + style + " |")

def f_arms(style):
    '''
    This function prints the arms of the character.
    The first parameter takes in a string used to style the arm
    Parameters: style can be a string
    '''
    print(" 0" + style * 4 + "|---|" + style * 4 + "0")

def f_torso(length):
    '''
    Prints the torso of the character, taking into account the 
    numeric parameter to set the length of the torso
    Parameters: length can be an integer 
    '''
    i = 0
    while i < length:
        print("      |-X-|")
        i += 1
    print("      HHHHH")

def f_legs(length):
    '''
    Prints the legs of the character, basing the length off of the given parameter
    Parameters: length can be an integer
    '''
    i = 0
    while i < length:
        print(" " * (5 - i) + "///" + " " + "  " * i + "\\\\\\")
        i += 1

def f_shoes(style):
    '''
    Prints the shoes of the character based off the style off of the parameter given
    Parameters: style can be a string
    '''
    print(style + "       " + style)

def Jeff():
    '''
    Prints out Jeff character preset using the modular based parts of the functions above
    Parameters: None
    '''
    f_hat_style("both")
    f_eyes("0", "False")
    f_hair("False")
    print("      |-X-|")
    f_arms("=")
    f_torso(4)
    f_legs(2)
    f_shoes("#HHH#")

def Jane():
    '''
    Prints out Jane character preset using the modular based parts of the functions above
    Parameters: None
    '''
    f_hat_style("right")
    f_eyes("*", "True")
    f_hair("True")
    f_arms("T")
    f_torso(2)
    f_legs(3)
    f_shoes("<|||>")

def Chris():
    '''
    Prints out Chris character preset using the modular based parts of the functions above
    Parameters: None
    '''
    f_hat_style("front")
    f_eyes("U", "False")
    f_hair("False")
    print("      |-X-|")
    f_arms("W")
    f_torso(2)
    f_legs(4)
    f_shoes("<>-<>")

def custom():
    '''Asks the user for custom settings using the modular based parts of the functions above
    to apply these settings.
    Parameters: None
    '''
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
    f_arms(arms)
    f_torso(torso)
    f_legs(legs)
    f_shoes(shoes)

def main(): 
    print("----- AVATAR -----")
    avatar_type = input("Select an Avatar or create your own:\n")
    while avatar_type != "custom" and avatar_type != "Jeff" and avatar_type != "Jane" and avatar_type != "Chris" and\
    avatar_type != "exit":
        avatar_type = input("Select an Avatar or create your own:\n")

    if avatar_type == "Jeff":
        Jeff()
    elif avatar_type == "Jane":
        Jane()
    elif avatar_type == "Chris":
        Chris()
    elif avatar_type == "custom":
        custom()

main()