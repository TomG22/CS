#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program prompts the user to answer a set of questions in madlib format.
# After all the inputs are received, the entire completed madlib is printed.
#

m = input("A male name:\n")
f = input("A female name:\n")
pet = input("A pet name:\n")
place = input("A place:\n")
adj = input("An adjective:\n")
anim = input("An animal:\n")
verb = input("A verb ending in ing:\n")
adverb = input("An adverb:\n")

print("----------\n"+m+" and "+f+" were best friends.\n\
One day "+m+" and "+f+" decided to go on a\n\
vacation to "+place+". However, they didn't know\n\
what to do with their "+adj+" pet "+anim+" named "+pet+".\n\
"+pet+" had been causing problems, due to constant "+verb+".\n\
"+m+" found a sitter for their pet, and "+adverb+" went on the trip.")
