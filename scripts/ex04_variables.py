# Let's move beyond just the print function.

# We can store values in "variables".

number_of_cars = 10
seats_per_car = 4
total_carpool_capacity = number_of_cars * seats_per_car
number_of_passengers = 28
number_of_drivers = number_of_cars # because each car needs exactly 1 driver.
open_seats = total_carpool_capacity - (number_of_passengers + number_of_drivers)
carpool_name = "porta-party"

print("There are", open_seats, "open seats in the", carpool_name)

# Variable names are very important. Longer, more descriptive names are better!
# You will thank yourself later for using nice, descriptive variable names.

# Variable names can contain upper and lower case letters, numbers, and
# underscores, although they cannot begin with a number.

# The convention is to use only lower case letters, numbers, and underscores in
# variable names.