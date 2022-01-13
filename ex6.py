types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# A string inside a string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}") # A string inside a string
# We can use '' to make them appear in print fcn
print(f"I also said: '{y}'") # A string inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# New form to introduce variables in a string. More on this later.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)
