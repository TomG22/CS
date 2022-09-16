mode = input("Enter mode (horizontal or vertical):\n")
string = input("Enter a stock input string:\n")


i = 0  
sign = 1
width = 0
height = 0

while i < len(string):
  if string[i] != "u" and string[i] != "d":

  height = i+height

while i < len(string):
  character = string[i]
  if character == "u":
    sign = 1
  elif character == "d":
    sign = -1
  else:
    character = character*sign

  if mode == "vertical":
    print("#"+" "*i+" "*(width-i)+"#")
  elif mode == "horizontal":
    print("#"+" "*i+" "*(width-i)+"#")

  i += 1
