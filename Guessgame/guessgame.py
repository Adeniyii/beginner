"""A numbers guessing game"""
# import randrange module.
from random import randrange
import string
from sys import exit

# assign default prompt.
prompt = '> '


# define function that starts the program.
def start():
    # set global variables
    global guessed_correct, guess_count
    # create variable to count guesses.
    guess_count = 0
    # assign default boolean
    guessed_correct = False
    # create a conditional while loop
    while guessed_correct == False:

        print("\nWelcome to a modified numbers guessing game!")
        # call 'choose difficulty' function.
        choose_difficulty()
        # call 'guess num' function.
        guess_num()
        # call 'try again' function.
        try_again()


# define choose difficulty function.
def choose_difficulty():
    # create an infinite loop.
    while True:
        print("\nChoose a difficulty between easy, medium, and hard.")
        # collect user input into variable.
        choice = input(prompt)

        # set conditional if statements to run code block.
        if choice.lower() == "easy":
            print(f"You chose {choice} mode.")
            # call 'easy' function.
            easy()
            break

        elif choice.lower() == "medium":
            print(f"You chose {choice} mode.")
            # call 'medium' function.
            medium()
            break

        elif choice.lower() == "hard":
            print(f"You chose {choice} mode.")
            # call 'hard' function.
            hard()
            break

        else:
            print("Invalid entry.")


# define 'easy' difficulty
def easy():
    # set global variables.
    global attempts, guess_range, secret_num

    # create variable to store allowed no of attempts.
    attempts = 6
    # create variable to store allowed guess range.
    guess_range = range(1,11)
    # create variable to store randomly selected number as guess.
    secret_num = randrange(1,11)
    # show user attempts allowed.
    print(f"You have {attempts} attempts.")


# define 'medium' difficulty
def medium():
    # set global variables.
    global attempts, guess_range, secret_num

    # create variable to store allowed no of attempts.
    attempts = 4
    # create variable to store allowed guess range.
    guess_range = range(1,21)
    # create variable to store randomly selected number as guess.
    secret_num = randrange(1,21)
    # show user attempts allowed.
    print(f"You have {attempts} attempts.")


# define hard difficulty
def hard():
    # set global variables.
    global attempts, guess_range, secret_num

    # create variable to store allowed no of attempts.
    attempts = 3
    # create variable to store allowed guess range.
    guess_range = range(1,51)
    # create variable to store randomly selected number as guess.
    secret_num = randrange(1,51)
    # show user attempts allowed.
    print(f"You have {attempts} attempts.")


# define function to guess the secret number.
def guess_num():
    # set global variables.
    global guess_count, attempts, guessed_correct, guess_range

    # create conditional while loop.
    while guess_count < attempts and not guessed_correct:

        try:

            print(f"\nGuess a number between {guess_range[0]} and {guess_range[-1]}.")
            # collect user input into 'guess' variable
            guess = int(input(prompt))

            # create conditional if-statements
            if guess == secret_num:
                print("You guessed right. Well done!")
                guessed_correct = True

            elif guess != secret_num and guess in guess_range:
                # increment 'guess_count'.
                guess_count += 1
                # assign if-block inside elif statement.
                if (attempts - guess_count) == 0:
                    print("\nWrong guess. Game over!")
                    break

                print("\nYou guessed wrong. Try again!")
                print(f"{attempts - guess_count} attempts left")

            elif guess not in guess_range:
                print("You guessed out of your scope. Try again!")

        except ValueError:
            print("Invalid entry. Try again!")


# define function the rerun the program after it ends.
def try_again():
    # create infinite while loop.
    while True:
        print("\nWould you like to play again?")
        # collect user input into 'go_again' variable.
        go_again = input(prompt)
        # create conditional if-statement.
        if go_again == "yes" or go_again == "y":
            # call start function
            start()

        elif go_again == "no" or go_again == "n":
            print("\nGame over.\n")
            # call exit function with no error message.
            exit(0)

        else:

            print("Invalid entry.")


# call start function
start()
