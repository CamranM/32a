# Homework 1 Problem 10 converter.py
# Author name: Camran Mori-Khan
#
# asks user for a single character string. Then, prints out the integer and
# binary correspondance of that string character 

# input function asks user for single character string
char = input("Enter a character:")

# the ord function, which converts the user's input of a string into an integer
num = ord(char)

# the binary function, which converts the string's integer representation into
# a binary number, which the cpu understands 
binary = bin(num)

# output result that prints the integer and binary representation of the
# string character that the user inputed 
print(char, "corresponds to the integer", num, "which is", binary, "in binary.")
