# Homework 1 Problem 4 mad.py
# Author name: Camran Mori-Khan
#
# Asks for user input on a number of different questions,
# Stores input as variables. Then, it uses the user input to create a story

# input function that asks the user for an adjective, expects a string
adj = input("Enter an adjective:")

# input function that asks the user for an noun, expects a string
noun = input("Enter a noun:")

# input function that asks the user for a plural noun, expects a string 
plural = input("Enter a plural noun:")

# input function that asks the user for a place, expects a string
place = input("Enter a place:")

# input function that asks the user for a body part, expects a string 
body = input("Enter a part of the body:")

# output result that applies what the user inputed for each question
# and creates a story. Each input is stored in a different variable
print()
print("There are many", adj, "ways to choose a", noun, "to read.")
print("You could ask recommendations from your friends and " + plural + ".")
print("If they are no help, head to your local library or", place, "and browse the shelves")
print("until something catches your", body + ".")  
