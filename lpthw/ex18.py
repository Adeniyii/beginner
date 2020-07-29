# Defining a function that takes unlimited args using *args.
def print2(*args):
    # Unpacking the *args into variables.
    arg1, arg2 = args
    # Printing out strings using f-strings.
    print(f"arg1: {arg1}, arg2: {arg2}")

# defining a function that takes two arguments.
def print2_again(arg1, arg2):
    # Printing out strings using f-strings.
    print(f"This is arg1: {arg1}, and this arg2: {arg2}")

# Defining a function that takes one argument.
def print1(arg1):
    # print out a string using f-strings.
    print(f"This one takes one argument: {arg1}")

# defining a function that takes no arguments.
def print0():
    print("This one takes no argument.")

print()
# calling the function and passing the unpacked arguments.
print2("The weeknd", "Orgasm")
print()
# calling the function and passing the two arguments.
print2_again("Kendrick", "Cerebral")
print()
# calling the function and passing the single argument.
print1("Snoh Aalegra")
print()
# calling the function.
print0()
