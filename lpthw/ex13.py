from sys import argv
# argv is called an argument variable
# argv is used to hold all the arguments entered when you run your python script

script, first, second, third, fourth, fifth = argv
# the above code is called unpacking an argument variable into other variables.

print()
print("The script is called:", script)
print("The first variable is called:", first)
print("The second variable is called:", second)
print("The third variable is called:", third)
print("The fourth variable is called:", fourth)
print("The fifth variable is called:", fifth)
print("The extra variable is called:",input("Enter an extra variable: "))
print()
print(argv)

#script = argv
#print("The scripts name is:", script)
