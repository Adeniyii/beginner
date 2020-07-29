# print an empty line
print()

# store curly braces to be formatted into a variable
# the braces must be within a string
formatter = "{} {} {} {}"

# print the formatted variable
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(
formatter.format("Roses are blue",
                "Tangerines are grey",
                "God is mighty",
                "And I am Smart as fuuuck.")
)
# empty line
print()

# storing curly braces within a string sentence
sentence = "{} are blue,\nTangerines are {},\nGod {} mighty\nDayo is {}."

# The statement above and below print the same thing
# curly braces work fine as long as they are within " ".

tense = "{}" " are blue,\nTangerines are ""{}"",\nGod ""{}"" mighty\nDayo is ""{}."

# printing out the formatted string sentence.
print(sentence.format("skipping ropes", "For orangutans", "is always", "sexy"))
print()
print(tense.format("Martians", "Earthlings", "Venus", "Mecurial"))
print()

# Again storing curly braces in between a string.
gombe = "kakobe{}chicken"

# Printing out the formatted string.
print(gombe.format("-"))
