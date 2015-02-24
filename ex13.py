# Imports the argument variable module
from sys import argv

# Assigns variables to argv
script, first, second, third = argv

# Assigns raw_input to name and age
name = raw_input("What is your name? ")
age = raw_input("What is your age? ")

# Prints Line 13 asking for "name" and "age"
# Prints Lines 14 - 17 with the variables assigned in Line 5
print "So you are %r and you are %r years old" %(name, age)
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third 