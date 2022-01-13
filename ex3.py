# This writes a line
print("I will now count my chickens:")

# Counts hens as the sum of 25 and 30/6 = 5, equals 30. Uses float due to division /
print("Hens", 25 + 30 / 6)
# Counts roosters as 100 - 25 * 3 % 4. % is the modulus. That means that (25 * 3)
# is 75, and modulus of 4 is 3. So 100 - 3 is 97. Integer number
# If one of the numbers is a float, the result is a float as well
print("Roosters", 100.0 - 25 * 3 % 4)

# This writes a line
print("Now I will count the eggs:")

# Modulus and division go first. So 4%2 is 0 (no residue) and 1/4 = 0.25, float again
# After that, sums and substractions.
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

# The answer to this is a boolean, False or True in string.
print(3 + 2 < 5 - 7)

# You can put it next to a line. To make it a float it can have a single point
# and nothing behind, not even a single zero.
print("What is 3 + 2?", 3. + 2)
print("What is 5 - 7?", 5. - 7)

print("Oh, that's why it's False.")

print("How about some more.")

# You can put it next to a line
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
