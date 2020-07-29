# import argv from sys.
from sys import argv

# unpack argv into variables.
script, filename = argv

# print an empty line.
print()

# print strings applying f-string formatting.
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do wan that, hit RETURN.")

# collect input
input("? ")

print("Opening the file...")

# open file into a variable -- this is an important step.
target = open(filename, 'w')

print("Truncating the file.")

# truncate the opened file -- this means clearing the file.
target.truncate()

print("Now i'm going to ask you for three lines..")

# collect input using the interactive prompt
line1 = input("Enter the first line:> ")
line2 = input("Enter the second line:> ")
line3 = input("Enter the third line:> ")

print("Now i'm going to write these to the file.")

# write to the opened truncated file using the write command
# and applying formatting methods for ease.
target.write(("\n{}\n{}\n{}\n").format(line1, line2, line3))

# close the written file when done -- this is important
target.close()

print("Now we read the file.")

# collect file name using the interactive prompt
# and open the file entered into a variable
newtext = open(input("Enter the filename:> "))

# read into the opened file and print out the contents.
print(newtext.read())

print()
print("And finally we close it.")

# close the file once done with it.
newtext.close()
