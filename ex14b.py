# Imports argv module
from sys import argv

# Defines the argv script passing name and age in
script, user_name, user_age = argv
prompt = '> ' # Defining the > as the prompt to begin each line with

# Prints the question filling in the given user name
print "Hi %s, I'm the %s script." % (user_name, script)
print "I's like to ask you a few questions."

# Asks the users age again and assigns that to age
print "Tell me again how old you are. %s years old can't be right." % (user_age)
age = raw_input(prompt)

# Asks the question and assigns yes or now to likes
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

# Asks the question and assigns the location to lives
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

# Asks the question ans assigns the computer type to computer
print "What kind of computer do you have?"
computer = raw_input(prompt)

# Prints the final paragraph reviewing the given answers
# Line 35 defines what each %r is in line 31 - 34
print """
Aright, so claim you are %r but I don't believe you.
You said %r you do like me.
You live in %r. Not sure where that is.
And you have a %r computer. That's nice.
""" % (age, likes, lives, computer)