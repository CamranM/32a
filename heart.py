# Homework 1 Problem 6 heart.py
# Author name: Camran Mori-Khan
#
# Asks user for their age. Then, program calculates the user's maximum and
# target heart rate, and prints it 

# Input function asking the user for their age. Converts string to an integer
age = int(input("Enter your age:"))

# expression that calculates user's maximum heart rate in bpm
maximum = 220 - age

# expression that calculates user's lower bound of the target heart rate
# in bpm
target_one = maximum * 0.5

# expression that calculates user's upper bound of the target heart rate
# in bpm
target_two = maximum * 0.85

# output result that prints the user's maximum heart rate in bpm
print("Your maximum heart rate is", maximum, "bpm")

# output result taht prints the user's target heart rate in bpm
print("Your target heart rate is", target_one, "-", target_two, "bpm")
