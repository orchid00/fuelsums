# Author: Paula Andrea Martinez
# Date: 2020-11-26
# Description: introduction to python


# how to check my python version 
import sys
sys.version

# small calculations
2 + 2 

# Calculate Fuel
# Return mass divided by three, rounded down and 
# substract two


# Test cases
# mass 12 returns 2
int(12 / 3 ) - 2
# mass 14 returns 2
int(14 / 3 ) - 2 
# mass 1969 returns 654
int(1969 / 3 ) - 2
# mass 100756 returns 33583
int(100756 / 3 ) - 2 


# Calculate Fuel function
# mass divided by three, round down, substract 2

def calculateFuel(inputNum):
    out = int(inputNum / 3 ) - 2
    print(out)
    return out

# test the function
calculateFuel(12)
calculateFuel(14)
calculateFuel(1969)
calculateFuel(100756)

# Data structures list

myList = [1, 2, 4, 5, 6, 33]
# print the values of my list
# print(myList)
# text list
days = ['monday', 'tuesday', 'wednesday']
# print(days)

# indexing in python starts from 0
# indexing will finish one less of the total items
# indexing can go forward open
# or backwards with negative indexes

# Create a list of masses
masses = [12, 14, 1969, 100756]
print(masses)

# fuelAmounts list to save results



# for loops for iteration
# for mass in masses:
#   print(mass)


# now how to read a File into a list
# read into a list, by default it will read at str
with open(file = 'data/input.txt') as file:
  masses = [line.rstrip('\n') for line in file]

print(masses)

# then we have our fuelAmounts empty list
fuelAmmounts = []

# Use the for loop to go over the masses and calculate fuel
# convert to int the value of mass
for mass in masses:
  fuelAmmounts.append(calculateFuel(int(mass)))


print(fuelAmmounts)

# sum up the fuelAmounts list values
print(sum(fuelAmmounts))










