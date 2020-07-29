# Import the argv module
from sys import argv

# unpack the argv contents into variables.
script, filename = argv

# store a default prompt indicator
prompt = '> '

# open your file and store inside  a variable (file object)
txt = open(filename)
print()

# print a string using f string formatting
print(f"Here's your file {filename}: ")

# call the file object, call the read function on it and print it.
print(txt.read())
print()

# collect the filename using an interactive prompt this time
print("Enter your file name again: ", end = ' ')
filename_again = input(prompt)

print()

# open the text file into a file object (variable)
txt_again = open(filename_again)

# read into the text object variable and print it
print(txt_again.read())
print()

# close the text files
txt.close()
txt_again.close()
