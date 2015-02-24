name = 'Brian Stoiber'
age = 31 # as of 02-16-2015
height = 74 # inches
weight = 170 # lbs
eyes = 'brown'
teeth = 'white'
hair = 'brown'
inches = height
centimeters = height * 2.54
lbs = weight
kgs = lbs * 0.453

print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "He's %r centimetres tall." %centimeters
print "He weights %d pounds." %weight
print "He weights %r kilograms." %kgs
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the tea." %teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)