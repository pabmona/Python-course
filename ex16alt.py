from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CRTL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#target.truncate() When we use 'w' mode, the file is automatically truncated.

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

formatter = "{}\n{}\n{}\n"

target.write(formatter.format(line1,line2,line3))

print("And finally, we close it.")
target.close()
