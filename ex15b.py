# Asks for the filename you want to open
print "Type the filename you are looking for."
filename = raw_input("> ")

# Passes filename as txt
txt = open(filename)

# Prints Line 8 and then prints file
print "Here's your file %r:" % filename
print txt.read()

# Closes the file
txt.close()