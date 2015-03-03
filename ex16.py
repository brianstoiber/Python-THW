# Imports argv library
from sys import argv

# script defines the script name and filename defines another argument
script, filename = argv

# Prints the following 3 lines and inserts filename after erase
print "We're going to erase %r" % filename
print "If you don't want that, press CTRL-C (^C)."
print "If you do want that, press RETURN."

# Asks for input of CTRL-C or RETURN
raw_input("?")

# Prints, assigns filename to target and opens it
print "Opening the file..."
target = open(filename, 'w')

# Prints, truncates file
print "Truncating the file. Goodbye!"
target.truncate()

# Prints
print "Now I'm going to ask you for three lines."

# Prints "line 1: " and asks for the raw_input of what you want those lines to be
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Prints
print "I'm going to write these to the file."

# From line 27-29, takes raw_input and writes to each line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Opens target
target = open(filename)

# Prints
print target.read()

# Prints, closes target
print "And finally, we close it."
target.close()