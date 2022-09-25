#
# Author: Group 2
# Class: CSC 110
# Description: This program is for two players to compete in rock paper scissors.
# Player one's input is compared against player two's and the output prints whoever wins.
#

player_one = input("Player one: ")
player_two = input("Player two: ")

#Checks if there's a tie
if player_one == player_two:
	print("It's a tie!")
#Checks all of the other combinations of inputs
elif player_one == "rock" and player_two == "paper":
	print("Player two wins!")
elif player_two  == "rock" and player_one == "paper":
	print("Player one wins!")
elif player_one  == "rock" and player_two == "scissors":
	print("Player one wins!")
elif player_two  == "rock" and player_one == "scissors":
	print("Player two wins!")
elif player_one  == "paper" and player_two == "scissors":
	print("Player two wins!")
elif player_two  == "paper" and player_one == "scissors":
	print("Player one wins!")
