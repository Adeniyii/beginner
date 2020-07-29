"""Introduction to for loops."""

# Create a bunch of lists
the_count = [1,2,3,4,5]
fruits = ['bananna', 'apple', 'watermelon', 'pineapple', 'pawpaw']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Create for loops to iterate through each list..
for  number in the_count:
    print(f"This is count number {number}.")

for fruit in fruits:
    print(f"A fruit of type {fruit}.")

for i in change:
    print(f"I got {i}.")

# Create an empty list.
elements = []

# Use a for loop to iterate through a range of numbers
for i in range(0,6):
    print(f"Adding {i} to the list.")

    # append each number in the range to the empty 'elements' list.
    elements.append(i)

for i in elements:
    print(f"Element was {i}.")
