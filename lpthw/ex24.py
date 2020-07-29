print("Let's print everything.")
print('you\'d need to know \'bout escapes with \\ that do: ')
print("newlines \\n and tabs \\t.")
print()

poem = """
\t The lovely world with logic so firmly planted
cannot discern \n the needs of love nor comprehend
passion from intuition, and requires an explanation
\n\t where there is none.
"""
print("............")
print(poem)
print("............")
print()
five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(kumbaya):
    heinz_beans = kumbaya * 500
    ketchup = heinz_beans/1000
    plates = ketchup/100
    return heinz_beans, ketchup, plates

startpoint = 1000
beans, ketchup, plates = secret_formula(startpoint)
print("With a starting point of: {}".format(startpoint))
print(f"We'd have beans: {beans}, ketchup: {ketchup}, and plates: {plates}")
print()

startpoint = startpoint/10
print("We can also do that this way: ")
# This is an easy way to apply a list to a format string.
formula = secret_formula(startpoint)
print("We should have beans: {}, ketchup: {}, and plates: {}.".format(*formula))
