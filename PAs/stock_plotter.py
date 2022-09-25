#mode = input("Enter mode (horizontal or vertical):\n")
#string = input("Enter a stock input string:\n")

#Test parameters
mode = "horizontal"
string = "u0d1d2u0u1"
width = 0
height = 0
last_num = None
last_letter = None

def vertical_plots():
  i = 0
  width = 19
  last_num = 0
  print("#" * width)
  while i < len(string):
    sign = 1
    character = string[i]
    if character == "d":
      sign = -1
    elif character != "u":
      character = int(character)# not sure if where to put sign here VV
      print("#" + " " * (((width // 2 ) + character * sign)) + "*" + " " * (((width // 2) - 2 - character) * sign) + "#")
      last_num = character + last_num
    i += 1
  print("#" * width)

def horizontal_plots():
  i = 0
  width = len(string)
  height = 19
  last_num = 0

  print("#" * width)
  while i < height:
    sign = 1
    character = string[i]
    if character == "d":
      sign = -1
    elif character != "u":
      if character
      character = int(character)
      print("#" + " " * ((width // 2) - character * sign) + "*" + " " * ((width // 2) - character * sign) + "#")
      last_num = character + last_num
    i += 1
  print("#" * width)

if mode == "vertical":
  vertical_plots()
elif mode == "horizontal":
  horizontal_plots() 
