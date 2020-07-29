# import the exit module.
from sys import exit
# set a default ptompt string.
prompt = '> '


# define the gold room function.
def gold_room():
    # print his line first once the function is called.
    print("This is a room full of gold, how much do you take?")

    # collect user input as integer into 'choice' variable.
    choice = int(input(prompt))

    # set a conditional statement to run code block.
    if choice > 50:
        # collect user input into 'how_much' variable
        dead("You greedy bastard.")
    # set a conditional statement to run code block.
    elif choice < 50:
        # run this code block if condition id met.
        print("Nice, you're not greedy. You win!")
        # call the exit function with no error '(0)'.
        exit(0)
    else:
        # call the 'dead' function.
        dead("You die of foolishness.")


# define the bear_room function.
def bear_room():
    # run indented code block.
    print("There is a bear here.")
    print("The bear has a lot of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear.")
    # set boolean value into a variable.
    bear_moved = False

    # call an infinite while loop.
    while True:

        # collect user input.
        choice = input(prompt)

        # set conditional statement to run code block.
        if choice == "take honey":
            # run 'dead' function if condition is true.
            dead("The bear gave you a sharp igbaju.")
        # set conditional statement to run code block.
        elif choice == "taunt bear" and not bear_moved:
            # run code block if condition is met.
            print("The bear has moved from the door.")
            print("You can go through it now.")
            # set formerly assigned boolean variable to true.
            bear_moved = True
        # set conditional statement to run code block.
        elif choice == "taunt bear" and bear_moved:
            # run 'dead' function if condition is true.
            dead("The bear gets annoyed and chows your legs.")
        # set conditional statement to run code block.
        elif choice == "open door" and bear_moved:
            # run 'gold room' function if condition is true.
            gold_room()
        # set conditional statement to run code block.
        else:
            # run code block if condition is met.
            print("I've got no idea what this means.")


# define 'ojuju room' function.
def ojuju_room():
    # run indented code block.
    print("Here you see the great evil ojuju.")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    # collect user input in 'choice' variable.
    choice = input(prompt)

    # set conditional statement to run code block.
    if "flee" in choice:
        # run 'start' function if condition is true.
        start()
    # set conditional statement to run code block.
    elif "head in" in choice:
        # run 'dead' function if condition is true.
        dead("Coconut head.")
    # set conditional statement to run code block.
    else:
        # run 'ojuju_room' function if condition is true.
        ojuju_room()


# define dead function.
def dead(why):
    # run code block.
    print(why, "Good job!")
    # call 'exit' function
    exit(0)


# define start function.
def start():
    # run code block.
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    # collect user input.
    choice = input(prompt)

    # set conditional statement to run code block.
    if choice == "right":
        # run 'bear_room' function if condition is true.
        bear_room()
    # set conditional statement to run code block.
    elif choice == "left":
        # run 'ojuju_room' function if condition is true.
        ojuju_room()
    # set conditional statement to run code block.
    else:
        # run 'dead' function if condition is true.
        dead("You stumble around the room until you die.")

# call the start function.
start()
