print "Type the filename you are looking for."
filename = raw_input("> ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()