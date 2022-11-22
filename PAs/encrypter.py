#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program scrambles a given file's lines using a randomizing algorithm.
#

import random

def random_swap(sample_list, index_list):
	'''Randomizes the two given lists by swapping randomly chosen indeces
	Parameters: sample_list can be a list
	index_list can be a list'''
	rand_num1 = random.randint(0, len(sample_list)-1)
	rand_num2 = random.randint(0, len(sample_list)-1)
	last_rand_sample = sample_list[rand_num1]
	last_rand_index = index_list[rand_num1]
	sample_list[rand_num1] = sample_list[rand_num2].strip("\n") + "\n"
	sample_list[rand_num2] = last_rand_sample.strip("\n") + "\n"
	index_list[rand_num1] = str(index_list[rand_num2]).strip("\n") + "\n"
	index_list[rand_num2] = str(last_rand_index).strip("\n") + "\n"

def encrypter(file_name):
	"""Randomizes a given file's text lines, encrypting the file
	file_name can be a string"""
	sample_lines = open(file_name, "r").readlines()
	encrypted = open("encrypted.txt", "w")
	index = open("index.txt", "w")

	i = 1
	indices = []
	while i <= len(sample_lines):
		indices.append(i)
		i += 1

	i = 0
	while i < len(sample_lines)*5:
		random_swap(sample_lines, indices)
		i += 1

	index.write(''.join(indices))
	encrypted.write(''.join(sample_lines))

def main():
	random.seed(125)
	encrypted = input("Enter a name of a text file to encrypt:\n")
	encrypter(encrypted)

main()
