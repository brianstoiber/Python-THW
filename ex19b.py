def people_that_piss_me_off(work_people, personal_people):
	print "I have %d people that piss me off at work." % work_people
	print "I have %d people that piss me off in my personal life." % personal_people
	print "Look at all the fucks I don't give. \n"
	
print "Method 1."
people_that_piss_me_off (5, 3)

print "Method 2."
work_people = 7
personal_people = 3

people_that_piss_me_off(work_people, personal_people)

print "Method 3."
print "Total people that piss me off."
people_that_piss_me_off(work_people + 0, personal_people + 0)

print "Method 4."
print "I added an extra person for good measure."
people_that_piss_me_off(work_people + 1, personal_people + 1)

print "How many people at work piss you off?"
work = raw_input()
print "How many people in your personal life piss you off?"
personal = raw_input()
print "You have a total of %s people at work \nand %s in your personal life that piss you off." % (work, personal)
