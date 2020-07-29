# import argv and exists modules.
from sys import argv
from os.path import exists
# unpack argv into variables.
script, from_file, to_file = argv
print()
# print string applying f-string formatting.
print(f"Copying from{from_file} to {to_file}.")
# open a file and call the read function on it. store in a variable.
input = (open(from_file)).read()
print()
# apply f-string formatting.
print(f"The input file is{len(input)} bytes long.")
print()
# apply f-string formatting.
print(f"Does the output file exist? {exists(to_file)}.")
# open a second file with the 'w' functionality
# and call the write function on it, then store it in a variable.
output = (open(to_file, 'w')).write(input)
print()
print("All done!")
