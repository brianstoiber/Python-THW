# Defining variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those that know %s and those who %s." % (binary, do_not)

# Print variable x and variable y
print x
print y

# Print "I said: x" and "I also said: y"
print "I said: %r." % x
print "I also said: '%s'." % y

# Defining variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Printing "Isn't that joke so funny?!"  and False
print joke_evaluation % hilarious

# Defining variables
w = "This is the left side of..."
e = "a string with a right side."

# Printing "This is the left side of..." and "a string with a right side."
print w + e