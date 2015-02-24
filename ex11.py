print "How old are you", # Prints the string
age = raw_input() # Waits for input
print "How tall are you", # Prints the string
height = raw_input() # Waits for input
print "How much do you weight", # Prints the string
weight = raw_input() # Waits for input

# Prints the string. %r prints exactly what is entered. %s prints the string
# %() is used to is used to insert the 3 variables into the string
print "So you're %r old, %s tall and %r heavy." %(
	age, height, weight)