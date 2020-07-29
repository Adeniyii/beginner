# Importing argv
from sys import argv
# Unpacking argv into variables
script_name, input_file = argv

# collect file name
def print_all(f):
    # read and print file
    print(f.read())

# collect file name
def rewind(f):
    # move the indicator in the file to a specified byte
    f.seek(0)

# collect line count and filename
def print_a_line(line_count, f):
    # print line count and current line
    print(line_count, f.readline())

# open input file argument into variable
current_file = open(input_file)

print()
print("First let's print the entire file.\n")

# print complete file
print_all(current_file)
print()

print("Now lets rewind, like a tape.")
print()

# take indicator to the first line
rewind(current_file)
print("Now we print each line.")
print()

# create a current_line variable.
current_line = 1

# print the current line number and the current line content.
print_a_line(current_line, current_file)

# increment the current line.
current_line += 1

# print the current line number and the current line content.
print_a_line(current_line, current_file)

# increment the current line.
current_line += 1

# print the current line number and the current line content.
print_a_line(current_line, current_file)
