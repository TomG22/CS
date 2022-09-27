#
# Author: Tom Giallanza
# Class: CSC 110
# This is a program which plots data points based off of data inputs from the user.
# This can be used to represent the value of a stock for example.
# Provide the correct input format for the program to print your graph!
#


#Checks if inputs are valid, if not, repeats the question
mode = input("Enter stock plotter mode:\n")

while mode != "horizontal" and mode != "vertical":
  mode = input("Enter stock plotter mode:\n")

string = input("Enter stock plot input string:\n")

while len(string) % 2 != 0:
  string = input("Enter stock plot input string:\n")

def vertical_plots():
  i = 1
  width = 19
  last_num = 0

  print("#" * width)
  #Iterates through each row and prints an astrisk wherever the relative data point is located
  while i < len(string):
    sign = 1
    character = int(string[i])
    previous = string[i-1]
    if previous == "d":
      sign = -1
    space = (8 + character * sign) + last_num
    print("#" + " " * space + "*" + " " * (16 - space) + "#")
    last_num += character * sign
    i += 2
  print("#" * width)

def horizontal_plots():
  row_index = 0
  string_length = len(string)
  width = string_length // 2
  height = 17
  print("##" + "#" * width + "##")
  #Iterates through each column in each row and determines if an asterisk belongs there
  while row_index < height:
    print("# ", end = "")
    char_index = 1
    row_place = 8
    while char_index < string_length:
      character = int(string[char_index])
      previous = string[char_index-1]
      if previous == "u":
        row_place = row_place - character
      elif previous == "d":
        row_place = row_place + character
      if row_place == row_index:
        print("*", end = "")
      else:
        print(" ",  end = "")
      char_index += 2
    print(" #")
    row_index += 1
  print("##" + "#" * width + "##")

#Initially calls the correct plot mode
if mode == "vertical":
  vertical_plots()
elif mode == "horizontal":
  horizontal_plots() 
