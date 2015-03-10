# defines cheese_and_crackers with the arguments ""heese_count" and "boxes_of_crackers"
# each time cheese_and_crackers is run, the 4 prints below will be printed
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count #cheese_count is the first argument
	print "You have %d boxes of crackers" % boxes_of_crackers # boxes_of_crackers is the second argument
	print "Man that's enough for a party!"
	print "Get a blanket. \n" # forces a new line

# prints, prints cheese_and_crackers and inserts 20 and 30 in for the two variables
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# prints, prints cheese_and_crackers and inserts 10 and 50 in for the variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# defines cheese_and_crackers variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints, uses 10 + 20 (30) and 5 + 6 (11) as variables
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# prints uses amount_of_cheese + 100 and amount_of_crackers + 1000 as variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)