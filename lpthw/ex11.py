print()

# Applying the end = '' functionality to prompts
print("How old are you.", end = ' ')
age = input("kelegbemegbe?")
print("How tall are you.", end = ' ')
height = input()
print("How much do you weigh.", end = ' ')
weight = input()

# The end = '' functionality skips variables unless it has a prompt stored in it.
print("What is your total?", end = ' ')
total = age + height + weight
total1 = input()

print()

# Using f string formatting methods
print(f"so you're {age} years old, weigh {weight}, and are {height} inches tall. total is {total} ")
print()
