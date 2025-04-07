print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() #This line completely missing
print("How much do you weigh?", end=' ') #End parenthesis missing
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

import sys
script, filename = sys.argv

txt = open(filename) #Bad spelling of variable

print("Here's your file {filename}:")
print(txt.read()) #Bad spelling of variable

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) #Dot instead of underscore.


print('Let\'s practice everything.') #Wrong type of quotes or \' to print a quote as text
print('''You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.''')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") #Missing end quote
print(poem)
print("--------------") #Missing starting quote


five = 10 - 2 + 3 - 6 #Missing 6 at the end
print(f"This should be five: {five}") #Missing parenthesis

def secret_formula(started): #missing the colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 #Missing operator
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # A third variable missing.

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #Mispelled start_point
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 # Mispelled variable
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") #Missing parentheses

if people > cats: # > instead of <
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: #Missing colon
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: #Missing colon
    print("People are less than or equal to dogs.") #Missing quote


if people == dogs: # == with two equals, not one.
    print("People are dogs.")
