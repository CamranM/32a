# Homework 1 Problem 7 paint.py
# Author name: Camran Mori-Khan
#
# Asks user for length, width, and height of the room they are painting. Then,
# program calculates amount of cans the user needs 


print("Paint coverage estimator")

# Asks user for length of their room. Converts string into an integer using a
# nested function
length = int(input("Length of room in inches:"))

# Asks user for width of their room. Converts string into an integer using a
# nested function
width = int(input("Width of room in inches:"))

# Asks user for height of their room. Converts string into an integer 
height = int(input("Average height of room in inches:"))

# Expression that calculates the total area in square inches
area = (2 * (height * width)) + (2 * (height * width))

# Converts square inches to square feet 
# Divdes the total area in inches by 144, since there are 12 inches in a foot
# And, because the area is in square inches, it is divided by 144 square inches 
in_to_ft = area / 144

# Expression divdes total area in square feet by amount of paint per can
float_cans = in_to_ft / 100

# converts amount of cans, which right now is a floating number, to an integer
integer_cans = int(float_cans)

# Since the user needs a rounded up amount of cans to paint their entire room
# This expression rounds up the amount of cans 
num_cans = integer_cans + 1

# output result of amount of cans the user needs to paint their room
print("You'll want", num_cans, "cans.")
