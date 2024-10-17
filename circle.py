# Homework 1 Problem 8 circle.py
# Author name: Camran Mori-Khan
#
# Asks user for radius. Then, calculates the diameter, circumference, and area
# of a circle with the givin radius 

# variable that holds pi's value
pi = 3.14159

# input function that asks user for a radius. Converts the string to a floating
# point number
radius = float(input("Enter radius:"))

# expression that calculates diamter given user input radius  
diameter = radius * 2

# expression that calculates circumference given user input radius
circ = 2 * pi * radius

# expression that calculates area of a circle given user input radius
area = (radius**2) * pi

#output result that prints the calculated diameter
print("Diameter", diameter)

# output result that prints the calculated circumference
print("Circumference", circ)

# output result that prints the calcualted area of the circle 
print("Area", area)
