# Homework 1 Problem 9 divide.py
# Author name: Camran Mori-Khan
#
# Asks user for two numbers. Prints out the whole number of the two numbers
# divded, and the remainder of the two numbers divided 

# input function asking user for a number. Converts that to an integer
num1 = int(input("Enter a number:"))

# input function asking user for a second number. Converts that to an integer
num2 = int(input("Enter a number to divide that by:"))

# expression for the whole number when the two numbers are divided
floor = num1 // num2

# expression for the remainder when the two numbers are divided
remainder = num1 % num2

# output result that prints both the whole number and remainder of when
# two numbers are divded 
print(num1, "divided by", num2, "is", floor, "with", remainder, "remaining")
