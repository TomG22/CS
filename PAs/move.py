#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program prompts the user to answer a set of questions in madlib format.
# After all the inputs are received, the entire completed madlib is printed.
#

f = input("A female name:\n")
street = input("A street name:\n")
m = input("A male name:\n")
obj = input("An object:\n")
vehicle = input("A vehicle:\n")
adj = input("An adjective:\n")

print("----------\n"+f+" decided to move from her apartment on 5th\n\
to a condo on "+street+". She called her friend "+m+"\n\
for help. However, they could not fit "+obj+" into\n\
the moving truck, so they had to rent a "+adj+" "+vehicle+"\n\
in order to move it!")