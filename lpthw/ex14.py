# import argv from sys
from sys import argv

# unpack argv into variables
script, user_name, alias = argv

# set a default prompt
prompt = '>: '

# pring strings applying f-strings for ease
print(f"Hi {user_name}, i'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you prefer being called {user_name} or {alias}?", end = ' ')
preferred_name = input(prompt)
print(f"Do you like me {preferred_name}?", end = ' ')
likes = input(prompt)
print()
print(f"Where do you live {preferred_name}?", end = ' ')
lives = input(prompt)
print()
print(f"What kind of computer do you have {preferred_name}", end = ' ')
computer = input(prompt)
print()

# print multiple line strings using triple quote strings.
print(f"""
Alright \"{preferred_name}\", you said \"{likes}\" about liking me,
You live at \"{lives}\", not sure where that is,
And you own a \"{computer}\" computer, nice.
""")
