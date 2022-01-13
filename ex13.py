# Here, we are importing modules or libraries. In this case, we are importing
# the arguments that we introduce when we execute this file:
# python3.9 ex13.py arg1 arg2 arg3. All variables after python3.9 are arguments.
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

# Unpacking of argv variable into four single variables.
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
