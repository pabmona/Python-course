from sys import argv

script, filename = argv

# It's important to identify the open file with a variable
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

# To close the opened file. Like a class.
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


txt_again.close()
