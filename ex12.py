# This is another way of using input. You can put the input message as the
# first argument of the function
age = input('How old are you? ')
height = input("How tall are you? ")
weight = input("How much do you weight? ")
x = int(input("Número complementario? "))

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print(f"Tu número de la suerte es el {x % 7 + 3}")
