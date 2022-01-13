print("Mary had a little lamb.")
# Class for a string can be formatted as follows:
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# Operations to duplicate strings can be applied directly to print:
print("." * 10) # Create 10 copies of '.'

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. Try removing it to see what happens
#Basically, the blank space dissapears. Variables can be defined in print.
# But they are not kept as defined out of that environment.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# This line will give an error:
# print("Hola",end,"Hola")
