from  sys import argv
from os.path import exists # imports "exists" command

# script defines script name, from_file and to_file are other variables
script, from_file, to_file = argv

# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# Prints, prints filesize
# len(indata) rerurns an int
print "The input file is %d bytes long" % len(indata)

# Prints, prints True or False depending if file already exists
# waits for input from user to continue or abort
print "Does the output file exist? %r" % exists(to_file)
print "Ready hit RETURN to continue, CTRL_C to about."
raw_input()

# Opens to_file in write mode as out_file
# Writes indata to out_file
out_file = open(to_file, 'w')
out_file.write(indata)

# Prints
print "Alright, all done."

# Closes files
out_file.close()
in_file.close()