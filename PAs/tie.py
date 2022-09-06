#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program prompts the user to a width parameter to draw
# a tie fighter spaceship from Star Wars using ASCII characters.
# After the width is inputted by the user, the program prints the finished drawing.
#

width = int(input('Enter TIE width:\n'))
print('             ')
print('|[' + ' ' + '         ' + ' ' + ']|')
print('|[' + ' ' * width + ' /=---=\\ ' + ' ' * width + ']|')
print('|[' + '/' * width + '|== X ==|' + '\\' * width + ']|')
print('|[' + ' ' * width + ' \\=---=/ ' + ' ' * width + ']|')
print('|[' + ' ' * width + '            ' + ' ' * width + ']|')
