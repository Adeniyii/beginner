"""Introduction to while loops"""

# define a function to house the loop.
def loop(inc):

    # Create and assign a variable.
    i = 0
    # Create an empty list.
    numbers = []
    # Create the while loop with a condition.
    while i in range(6):
        # print the first value of i.
        print(f"At the top, i is {i}.")
        # Append the first value of i to he numbers list.
        numbers.append(i)
        # Increment i by 1.
        i += inc
        # print the numbers list.
        print(f"Numbers now is {numbers}")
        # Print the new value of i after incrementing.
        print(f"At the bottom, i is {i}")
    # Print the final elements of the numbers list using a for loop.
    for num in numbers:
        print(num)

loop(2)
