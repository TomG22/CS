#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program prompts the user to provide 4 parameters to draw
# a nebulon spaceship from Star Wars using ASCII characters. The parameters are 
# the large, medium, and small layers on the bottom, and the front length.
# After all of the parameters listed are inputted by the user, the program prints the finished drawing.
#

l_bottom = int(input("Large Layers on bottom:\n")) 
m_bottom = int(input("Medium Layers on bottom:\n"))
s_bottom = int(input("Small Layers on bottom:\n"))
f_length = int(input("Front length:\n")) 

print(
'''
  /='''+"-"*f_length+'''\\                 /--------|
 /=='''+"/"*f_length+'''====\\            |=========|
|==-'''+"/"*f_length+'''======\\----================|
 \\=='''+"="*f_length+'''==-------------------------|
  \\='''+"-"*f_length+'''=///              \\=======/'''+
  l_bottom*("\n"+" "*(f_length-int(round(f_length-4)))+"\\"+"-"*f_length-4+"|")+\
     m_bottom*("\n"+" "*(f_length-int(round((f_length/2)-.25)))+":"+"+"*round((f_length/2-.25))+"|")+\
       s_bottom*("\n"+" "*(f_length-int(round((f_length/3)-.25)))+"\\"+"#"*round((f_length/3)-.25)+"|"))