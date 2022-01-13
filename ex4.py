# Variables are not declared. Directly = to the corresponding value
cars = 100
# Even floats
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


# We can stack as many arguments as we need in print fcn.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
# We can separate lines without any kind of separator command or character.
print("We need to put about", average_passengers_per_car,
      "in each car")
