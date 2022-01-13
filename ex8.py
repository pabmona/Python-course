formatter = "{} {} {} {}"

# You can use all kinds of variables as part of the string blanks:
print(formatter.format(1, 2, 3, 4)) # Numbers - Integers
print(formatter.format("one", "two", "three", "four")) # Strings
print(formatter.format(1., 2.00, 3.0, 4.0)) # Numbers - Floats - Though the same format for all
print(formatter.format(True, False, False, True)) # Booleans
print(formatter.format(formatter,formatter,formatter,formatter)) # Even more formats...
print(formatter.format( # You can break your lines!!
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
