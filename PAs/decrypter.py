#
# Author: Tom Giallanza
# Class: CSC 110
# Description: The program decrypts a given file after it's 
# been encrypted with the encrypter.py script.
#

def decrypter(encrypted_name, index_name):
	'''Decrypts the given encrypted file by using the index file's 
	indices to match the correct lines.
	Parameters: encrypted_name can be a list
	index_name can be a list'''
	encrypted_lines = open(encrypted_name, "r").readlines()
	index_lines = open(index_name, "r").readlines()
	decrypted = open("decrypted.txt", "w")
	decrypted_lines = []

	for index in index_lines:
	decrypted_lines.append(None)

	i = 0
	for line in encrypted_lines:
		decrypted_lines[int(index_lines[i])-1] = line
		i += 1

	decrypted.write(''.join(decrypted_lines))

def main():
	encrypted = input("Enter the name of an encrypted text file:\n")
	index = input("Enter the name of the encryption index file:\n")
	decrypter(encrypted, index)

main()