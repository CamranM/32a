# Homework 1 Challenge Problem hybrid.py
# Author name: Camran Mori-Khan
#
# Program asks the user input for information about a hyrbid car including
# cost, how many miles they expect to drive a year, gas cost, mpg,
# and estimated resale value. Then, it prints out the gas cost, depreciation,
# and total cost of owning the hybrid car. 

# input function asks for the cost of the car
# converts it to a floating point number using a nested function.
car_cost = float(input("Cost of car:"))

# input function asks for the miles of the car
# converts it to a floating point number using a nested function.
mpy = float(input("Miles driven per year:"))

# input function asks for the cost of gas
# converts it to a floating point number
gas_cost = float(input("Cost of gas:"))

# input function asks for the miles per gallon for the car 
# converts it to a floating point number using a nested function.
mpg = float(input("Fuel efficiency (mpg):"))

# input function asks for the reslae value of the car in 5 years
# converts it to a floating point number using a nested function.
est_resale = float(input("Estimated resale value after 5 years:"))

# expression calculates five year gas cost by first finding the amount of
# gallons that the car uses a year. Then, it mutliplies it by the cost per
# gallon, and multiplies by 5 to find the five year cost 
five_gas_cost = mpy / mpg * gas_cost * 5

# this expression calculates the depreciation, which is the loss in value
# of the car in 5 years
depreciation = car_cost - est_resale

# this expression calculates the total cost of owning the car for 5 years 
# by adding the gas cost and depreciation 
total_cost = five_gas_cost + depreciation 

# output result that prints the five year gas cost
print("Five year gas cost:", five_gas_cost)

#output result that prints the five year depreciation 
print("Five year car cost:", depreciation)

#output result that prints out the total cost of owning the car over 5 years
print("Five year total cost:", total_cost)
