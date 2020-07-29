"""A game of tic-tac-toe"""
import random

# print message to user.
print("\nWelcome to a game of Tic-Tac-Toe!")

# create default prompt.
prompt = "> "
# create default winner variable.
winner = None
# create default game-on variable.
game_on = True

# create variable to record player 1 score
p1_score = 0
# create variable to record player 2 score
p2_score = 0
# create variable to record ties
ties = 0
# create dictionary to hold player scores and ties.
score_card = {"player1":p1_score, "player2": p2_score}

# Create 'display board' function.
def display_board():
    # print board on screen using index positioning.
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# define 'choose chsracter' function.
def choose_character():
    # set global variables.
    global player1, player2, current_player
    # print message to user.
    print("\nChoose your character.\n")
    # collect user input.
    player1 = input("player1" + prompt)
    player2 = input("player2" + prompt)
    players = [player1, player2]
    # create current player value.
    current_player = random.choice(players)
    print(f"\n{current_player} plays first.")


# define 'make move' function.
def make_move():
    # create infinite loop.
    while True:
        # print message to user.
        print(f"\nMake your move {current_player}")
        # collect position input from user.
        position = input(prompt)
        # convert position input to integer and convert to cardinal number.
        position = int(position) - 1

        # set conditional if-statement.
        if board[position] == "-" and position in range(9):
            # set board position index to player character.
            board[position] = current_player
            # break out of infinite loop.
            break
        else:
            # print message to user.
            print("Invalid entry.")
            # call display board function.
            display_board()


# define 'switch player' function.
def switch_player():
    # set global variables.
    global current_player, player1, player2

    # set conditional if-statement.
    if current_player == player1:
        # switch from player1 to player2.
        current_player = player2
    else:
        # switch from player2 to player1.
        current_player = player1


# define start function.
def start():

    global board
    # create board using list.
    board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
    ]

    # call 'choose character' function.
    choose_character()
    # call 'display board' function.
    display_board()

    # set conditional while loop.
    while game_on:
        # call defined functions in a select sequence.
        make_move()
        display_board()
        check_win()
        switch_player()


# define a 'check win' function.
def check_win():
    # call defined functions in a select sequence.
    check_rows()
    check_columns()
    check_diagonals()
    check_tie()


# define 'check rows' function.
def check_rows():
    # set global variable.
    global winner

    # assign equality statements to row variables.
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    # set conditional if-statements.
    if row1:
        # assign value to winner variable.
        winner = board[0]
        # print who won message to user.
        print(f"\n{winner} won the game!\n")
        # call 'try_again' function.
        try_again()
    # set conditional if-statements.
    elif row2:
        # assign value to winner variable.
        winner = board[3]
        # print who won message to user.
        print(f"\n{winner} won the game!\n")
        # call 'try_again' function.
        try_again()
    # set conditional if-statements.
    elif row3:
        # assign value to winner variable.
        winner = board[6]
        # print who won message to user.
        print(f"\n{winner} won the game!\n")
        # call 'try_again' function.
        try_again()
    else:
        return


# define 'check column' function.
def check_columns():
    # set global variables.
    global winner
    # assign equality statements to col variables.
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    # set conditional if-statements.
    if col1:
        # set value for winner.
        winner = board[0]
        print(f"\n{winner} won the game!\n")
        # call 'try_again' function.
        try_again()
    elif col2:
        # set value for winner.
        winner = board[1]
        print(f"\n{winner} won the game!\n")
        # call 'try_again' function.
        try_again()
    elif col3:
        # set value for winner.
        winner = board[2]
        print(f"\n{winner} won the game!\n")
        # call 'try_again' function.
        try_again()
    else:
        return


# define 'check diagonals' function.
def check_diagonals():
    # set global variables.
    global winner

    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"
    # set conditional if-statements.
    if dia1:
        # set value for winner.
        winner = board[0]
        print(f"\n{winner} won the game!\n")
        # call 'try_again' function.
        try_again()
    elif dia2:
        # set value for winner.
        winner = board[2]
        print(f"\n{winner} won the game!\n")
        # call 'try_again' function.
        try_again()
    else:
        return


# define 'check tie' function.
def check_tie():
    # set global variable.
    global winner
    # set conditional if-statements.
    if "-" not in board:
        print("\nGame ended as a tie.\n")
        # set value for winner.
        winner = None
        # call 'try_again' function.
        try_again()
    else:
        return


# define a 'try_again' function.
def try_again():
    # set global variables.
    global player1, player2, p1_score, p2_score, ties
    # set conditional if-statements.
    if winner == player1:
        # increment player1 score.
        p1_score +=1
    # set conditional if-statements.
    elif winner == player2:
        # increment player2 score.
        p2_score +=1
    # set conditional if-statements.
    elif winner == None:
        # increment ties.
        ties +=1

    print(f"\nplayer 1: {p1_score} wins, {ties} ties.")
    print(f"\nplayer 2: {p2_score} wins, {ties} ties.")
    # ask user for a rematch.
    print("\nWould you like a rematch?")
    # collect user input.
    go_again = input(prompt)
    # run code if user answered yes.
    if go_again == "yes" or go_again == "y":
        # call start function.
        start()
    # run code if user answered no.
    elif go_again == "no" or go_again == "n":
        print("\nGame Over.\n")
        # call exit function.
        exit(0)




# call start function.
start()
