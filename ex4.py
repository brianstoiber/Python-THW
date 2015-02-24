# Defining what each variable equals to, int or another variable
cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

# Prints There are 100 cars available"
print "There are", cars, "cars available"

# Prints "There are only 30 drivers available"
print "There are only", drivers, "drivers available."

# Prints "There will be 70 to carpool today"
print "There will be", cars_not_driven, "to carpool today."

# Prints "We have 90 to carpool today"
print "We have", passengers, "to carpool today."

# Prints "Wee need to put about 3 in each car" 
print "We need to put about", average_passengers_per_car, "in each car."