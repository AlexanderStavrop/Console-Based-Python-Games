# _____________________________________Player selection___________________________________________
def player_selection(player):
    while player != 1 and player != 2:
        try:
            player = int(input("Enter the number of player to play first. Press '1' or '2': "))
            if player != 1 and player != 2:
                raise ValueError
        except ValueError:
            print("\nWrong input!!!!! \nPlease try again\n")

    return player

# ___________________________________Correct Coordinates__________________________________________
def correct_coordinates(curr_player, trliz):
    cord_x = cord_y = -1
    print("\n##########   Currently playing -> player ", curr_player, "   ###########")

    while cord_x < 0 or cord_y < 0:  # Getting the correct coordinates
        try:
            cord_x, cord_y = input("Enter the row and column coordinates separated with space: ").split()
            cord_x = int(cord_x)
            cord_y = int(cord_y)
            if trliz[cord_x - 1][cord_y - 1] != 0:
                print("\nPlace already taken!!!!\n Please try again\n")
            else:
                trliz[cord_x - 1][cord_y - 1] = curr_player
                break
        except (ValueError, TypeError, IndexError):
            print("\ninvalid coordinates!!!! \nPlease try again\n")

        cord_x = cord_y = -1

# ____________________________________Printing the board__________________________________________
def print_triliza(trliz):
    print()
    print(trliz[0])
    print(trliz[1])
    print(trliz[2])

# ______________________________________Check win/Tie_____________________________________________
def check_win_tie(curr_player, trliz):
    for i in range(0, 3):  # Checking for winner
        if (trliz[i][0] == trliz[i][1] == trliz[i][2] != 0) or \
                (trliz[0][i] == trliz[1][i] == trliz[2][i] != 0) or \
                (trliz[0][0] == trliz[1][1] == trliz[2][2] or trliz[2][0] == trliz[1][1] == trliz[0][2] != 0):
            print("\nWe have a Winner\nCongratulation player", curr_player, "!!!!!!!!!!!!\n")
            return True

    for i in range(0, 3):  # Checking for tie
        if trliz[i][0] == 0 or trliz[i][1] == 0 or trliz[i][2] == 0:
            break
    else:
        print("\nGame ended with a Tie\n")
        return True
    return False

# ________________________________________Play time_______________________________________________
def game_on(curr_player, trliz):
    game_finished = False

    while not game_finished:

        correct_coordinates(curr_player, trliz)
        print_triliza(trliz)
        game_finished = check_win_tie(curr_player, trliz)
        curr_player = change_player(curr_player)

# ______________________________________Change Player_____________________________________________
def change_player(curr_player):
    if curr_player == 1:
        curr_player = 2
    else:
        curr_player = 1
    return curr_player

# ____________________________________Play again - Quit___________________________________________
def play_quit(answer):
    while answer != "play" and answer != "quit":
        answer = input("To play again enter 'play', to quit enter 'quit': ")
        if answer != "play" and answer != "quit":
            print("Wrong input! Try again")
    return answer

# __________________________________________Main__________________________________________________
if __name__ == "__main__":
    triliza = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    choice = ''

    while choice != "quit":
        choice = first = ''

        current_player = player_selection(first)
        game_on(current_player, triliza)
        choice = play_quit(choice)
    print("Thank you for playing")
