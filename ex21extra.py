def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a,b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = int(input("Edad: "))
height = int(input("Altura: "))
weight = int(input("Peso: "))
iq = int(input("IQ: "))

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
