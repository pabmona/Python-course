name = 'Pablo Moreno'
age = 30 # not a lie
height = 72.8 # inches
weight = 176.4 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

# Conversion of variables
height_cm = round(height * 2.54, 2) # Inches to cm -> 1 inch = 2.54 cm
weight_kg = round(weight * 0.453592, 2) # Pounds to kg -> 1 pound = 0.453592 kg
# Function round has two arguments: number to round and numbers to show.

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilos heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#  this line is tricky, try to get it exactly right
total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")
