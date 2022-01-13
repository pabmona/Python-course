from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Trying to do the code in a single line
indata = open(to_file, 'w').write(open(from_file).read())
