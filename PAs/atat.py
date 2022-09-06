#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program prompts the user to provide 3 parameters to draw
# an ATAT figure from Star Wars using ASCII characters. The parameters are the neck length, the body height, and the leg height.
# After all of the parameters listed are inputted by the user, the program prints the finished drawing.
#

n_length = int(input("Neck Length:\n")) 
b_height = int(input("Body Height:\n"))
l_height = int(input("Leg Height:\n"))

print(
'''
     _..-Y  |  |  Y-._
 .--"   ||  |  |  |   "-.
 |______________________|'''+    
 "\n |______________________|"*b_height+" "*n_length+"    _____"+
 '\n L______________________[--'+"-"*n_length+'''--------).
I____________________ [__L]'''+"_"*n_length+'''[----(_}--P
L________________________j~ '''+" "*n_length+''''+++++++//
\\________________________]
  [___________________]
     I--I"~~"""~~"I--I'''+\
    "\n     |\\n|         |\\n|"*l_height
    +'''\n     ([])         ([])
    /||||\\       /||||\\
   |=}--{=|     |=}--{=|
  .-4----4-.   .-4----4-.''')


print("     |\\n|         |\\n|\n"*l_height-1)
print("test2")
print("test")