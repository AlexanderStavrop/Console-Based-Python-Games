import random

choice = ''

# _____________________________________________Word Choice_____________________________________________
def word_choice():
    found_word = False
    tmp_word = ''
    num = 0

    words = open("words.txt")
    while num < 5 and not found_word:
        num = random.randint(1, 25)
        if num < 5:
            pass
        else:
            words.seek(0)
            for i in words:
                tmp_word = words.readline()
                if len(tmp_word) == num + 1:
                    found_word = True
                    break
            else:
                num = 0

    words.close()
    return tmp_word

# _____________________________________________Print Bord______________________________________________
def print_board(ltrs,incorrct):
    print()
    print_list(ltrs)
    print("\nIncorrect letters:", end=' ')
    print_list(incorrct)

# _____________________________________________Print List______________________________________________
def print_list(lst):
    for i in lst:
        print(i, end=' ')

# ___________________________________________Check If Valid____________________________________________
def check_if_valid(vld, entered):
    while not vld:
        tmp_letter = input("\nGuess a letter: ").upper()
        for i in entered:
            if i == tmp_letter:
                vld = False
                print("You have already picked that letter. Try again")
                break
        else:
            vld = True
    return tmp_letter, vld

# __________________________________________Check If Correct___________________________________________
def check_if_correct(word, entered, ltr):
    found = False
    counter = 0
    for i in word:
        if i == entered:
            ltr[counter] = entered
            found = True
        counter = counter + 1
    return found

# _________________________________________Check If Finished____________________________________________
def check_if_finished(ltrs):
    for i in ltrs:
        if i == "_":
            break
    else:
        return True
    return False

# _______________________________________________Hangman_______________________________________________
def hangman(word):
    game_finished = False
    letters = ["_"] * (len(word) - 1)
    incorrect_letters = ['_'] * 6
    incorrect_counter = 0
    entered_letters = []

    print("Welcome to Hangman!")

    while not game_finished and incorrect_counter < 6:
        found_letter = valid = False

        print_board(letters, incorrect_letters)
        input_letter, valid = check_if_valid(valid, entered_letters)
        entered_letters.append(input_letter)
        found_letter = check_if_correct(word, input_letter, letters)
        game_finished = check_if_finished(letters)

        if not found_letter:
            incorrect_letters[incorrect_counter] = input_letter
            incorrect_counter = incorrect_counter + 1

    print_board(letters, incorrect_letters)
    print()
    if incorrect_counter == 6:
        print("You lost :( !!!!!\n")
    elif game_finished:
        print("Congratulations you solved the word")

# ______________________________________________play Quit______________________________________________
def play_quit():
    answer = ''
    while answer != "play" and answer != "quit":
        answer = input("\nIf you wish to play again enter 'play', if you wish to quit enter 'quit': ")
        if answer != "play" and answer != "quit":
            print("\nWrong input!!!!!!\nPlease try again")
    return answer


if __name__ == "__main__":
    while choice != "quit":
        hidden_word = word_choice().upper()
        hangman(hidden_word)
        choice = play_quit()
