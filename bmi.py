# Homework 1 Problem 5 bmi.py
# Author name: Camran Mori-Khan
#
# Asks the user for their height and weight. Using a bmi formula, it finds
# the user's bmi and prints it

# input function asks the user for their height in inches. Converts it to a
# floating point number
height = float(input("Enter height in inches:"))

# input function asks the user for their weight in punds. Converts it to a
# floating point number
weight = float(input("Enter weight in pounds:"))

# applies user height and weight into an expression that finds user's bmi
bmi = (weight/(height**2)) * 703

# output result that prints the user's bmi. converts bmi to str to cocatenate
print("BMI: " + str(bmi))
