# this is like your scripts with argv
# defines print_two as a function and tell it we want to use args
def print_two(*args):
	arg1, arg2 = args # unpacks the function
	print "arg1: %r, arg2: %r" % (arg1, arg2) # prints the function
	
# does the same as print_two 
def print_two_again(arg1, arg2): # doesn't unpack the function, it just uses the arguments
	print "arg1: %r, arg2: %r" % (arg1, arg2) # prints the function
	
# this just takes one argument
def print_one(arg1): 
	print "arg1: %r" % arg1
	
# this one takes no argument
def print_none():
	print "I got nothin'."
	
print_two("Zed","Shaw") # this is similar to using the % () at the end of a string to fill in %r or %s
print_two_again("Zed","Shaw")
print_one("First")
print_none()