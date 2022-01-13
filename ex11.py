print("How old are you?", end=' ') # It seems that end=' ' is to replace
# the last character by default of a line (line break).
age = input() # You can introduce string, integer, floats...
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
