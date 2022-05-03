# _____________________________________Player selection___________________________________________
# Method for player selection
def player_selection(player):
    while player != 1 and player != 2:                                                                          # Looping until the input is valid
        try:
            player = int(input("Enter the number of player to play first. Press '1' or '2': "))                 # Asking for users input on the player number they choose
            if player != 1 and player != 2:                                                                     # Checking if the input is valid
                raise ValueError                                                                                # If not, we raise ValueError exception
        except ValueError:                                                                                      # Handling the exception
            print("\nWrong input!!!!! \nPlease try again\n")                                                    # Printing the error message
    return player                                                                                               # Returning the player number


# ___________________________________Correct Coordinates__________________________________________
# Method for ???
def correct_coordinates(curr_player, curr_board):
    cord_x = cord_y = -1                                                                                        # Initializing the x and y coordinates to -1
    print("\n##########   Currently playing -> player ", curr_player, "   ###########")                         # Printing the corresponding message

    while cord_x < 0 or cord_y < 0:                                                                             # Looping until we get valid coordinates
        try:
            cord_x, cord_y = input("Enter the row and column coordinates separated with space: ").split()       # Getting the user input
            cord_x = int(cord_x)                                                                                # Converting the x coordinates to integer
            cord_y = int(cord_y)                                                                                # Converting the y coordinates to integer
            if curr_board[cord_x - 1][cord_y - 1] != 0:                                                         # Checking whether the spot is already occupied
                print("\nPlace already taken!!!!\n Please try again\n")                                         # If true, we print the error message
            else:                                                                                               # Else
                curr_board[cord_x - 1][cord_y - 1] = curr_player                                                # We populate that cell
                break                                                                                           # Continuing the game
        except (ValueError, TypeError, IndexError):                                                             # Error handling for the input
            print("\ninvalid coordinates!!!! \nPlease try again\n")                                             # Printing the error message

        cord_x = cord_y = -1                                                                                    # Setting the x and y coordinates to -1


# ____________________________________Printing the board__________________________________________
# Method for printing the board
def print_board(curr_board):
    print()                                                                                                     # Printing an empty line
    print(curr_board[0])                                                                                        # Printing the first row
    print(curr_board[1])                                                                                        # Printing the second row
    print(curr_board[2])                                                                                        # Printing the third row


# ______________________________________Check win/Tie_____________________________________________
def check_win_tie(curr_player, curr_board):
    for i in range(0, 3):                                                                                       # Checking for winner
        if (curr_board[i][0] == curr_board[i][1] == curr_board[i][2] != 0) or \
                (curr_board[0][i] == curr_board[1][i] == curr_board[2][i] != 0) or \
                (curr_board[0][0] == curr_board[1][1] == curr_board[2][2]) or \
                (curr_board[2][0] == curr_board[1][1] == curr_board[0][2] != 0):                                # Checking if there are 3 of the same in every possible way
            print("\nWe have a Winner\nCongratulation player", curr_player, "!!!!!!!!!!!!\n")                   # Printing the winner message
            return True                                                                                         # Returning true as we have a winner

    for i in range(0, 3):
        if curr_board[i][0] == 0 or curr_board[i][1] == 0 or curr_board[i][2] == 0:                             # Checking if there are any empty tiles left
            return False                                                                                        # If true, the game continues
    else:                                                                                                       # Else, there are no moves left
        print("\nGame ended with a Tie\n")                                                                      # Printing the Tie message
        return True                                                                                             # Returning true as the game has ended


# ________________________________________Play time_______________________________________________
# Method for playing one game
def game_on(curr_player, curr_board):
    game_finished = False                                                                                       # Created the game_finished flag

    while not game_finished:                                                                                   # Looping until the game has ended
        correct_coordinates(curr_player, curr_board)                                                           # Getting correct coordinates from the current player2
        print_board(curr_board)                                                                                # Printing the board
        game_finished = check_win_tie(curr_player, curr_board)                                                 # Checking if there is a winner
        curr_player = change_player(curr_player)                                                               # Changing the current player


# ______________________________________Change Player_____________________________________________
# Method for changing between the players
def change_player(curr_player):
    if curr_player == 1:                                                                                        # Checking player 1 was playing
        curr_player = 2                                                                                         # Changing the current player to player 2
    else:                                                                                                       # Else if player 2 was playing
        curr_player = 1                                                                                         # Changing the current player to player 1
    return curr_player                                                                                          # Returning the new current player


# ____________________________________Play again - Quit___________________________________________
# Method for determining if the players want to play another round
def play_quit(answer):
    while answer != "play" and answer != "quit":                                                                # Looping until the input is valid
        answer = input("To play again enter 'play', to quit enter 'quit': ")                                    # Getting the user input
        if answer != "play" and answer != "quit":                                                               # Checking if the input is valid
            print("Wrong input! Try again")                                                                     # Printing the error "Wrong Input Message"
    return answer                                                                                               # Returning the valid answer


# __________________________________________Main__________________________________________________
# Main method
if __name__ == "__main__":
    board = [[0, 0, 0],                                                                                         # Creating the board
             [0, 0, 0],
             [0, 0, 0]]

    choice = ''                                                                                                 # Creating a variable for the user choice
    while choice != "quit":                                                                                     # Looping until the user wants to quit
        choice = first = ''                                                                                     # Resetting the values of the first player and user choice

        current_player = player_selection(first)                                                                # Getting the player number who plays first
        game_on(current_player, board)                                                                          # Starting the game
        choice = play_quit(choice)                                                                              # Getting the player choice
    print("Thank you for playing")                                                                              # Printing the exit message
