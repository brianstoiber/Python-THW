# Imports argv module
from sys import argv

# Gets the file name
script, filename = argv

# Opens the file give
txt = open(filename)

# Prints Line 11 and then prints the contents of file name
print "Here's your file %r:" % filename
print txt.read()

# Asks the user to enter the file name again and assigns that to file_again
print "Type the file name again:"
file_again = raw_input("> ") # Begins line with the > and waits for input

# opens file again 
txt_again = open(file_again)

# Prints file again
print txt_again.read()