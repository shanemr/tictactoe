import re


board = {'1': '1', '2': '2 ', '3': '3',
         '4': '4', '5': '5 ', '6': '6 ',
         '7': '7', '8': '8 ', '9': '9 '}


def display_board(the_board):
    print(board['1'] + " | " + board['2'] + "| " + board['3'])
    print("--+--+--")
    print(board['4'] + " | " + board['5'] + "| " + board['6'])
    print("--+--+--")
    print(board['7'] + " | " + board['8'] + "| " + board['9'])


def check_winner():
    if board['1'] == board['2'] == board['3'] != ' ':
        print("Player " + board['2'] + " is the winner")
        reset_game()
    elif board['4'] == board['5'] == board['6'] != ' ':
        print("Player " + board['5'] + " is the winner")
        reset_game()
    elif board['7'] == board['8'] == board['9'] != ' ':
        print("Player " + board['8'] + " is the winner")
        reset_game()
    elif board['1'] == board['3'] == board['7'] != ' ':
        print("Player " + board['3'] + " is the winner")
        reset_game()
    elif board['2'] == board['4'] == board['8'] != ' ':
        print("Player " + board['4'] + " is the winner")
        reset_game()
    elif board['3'] == board['6'] == board['9'] != ' ':
        print("Player " + board['6'] + " is the winner")
        reset_game()
    elif board['1'] == board['5'] == board['9'] != ' ':
        print("Player " + board['5'] + " is the winner")
        reset_game()
    elif board['3'] == board['5'] == board['7'] != ' ':
        print("Player " + board['5'] + " is the winner")
        reset_game()


def reset_game():
    play_again = ''
    print("Would you like to play again? y for yes, or n for no")

    play_again = input()

    if play_again == 'y':
        board.update({}.fromkeys(board, ' '))
        play_game()
    else:
        exit()


def play_game():

    selection = " "
    current = "X"
    count = 0

    for i in range(10):
        display_board(board)
        print("Player " + current + " it's your turn\n")

        selection = input()

        while not re.search("[0-9]", board[selection]):
            print("Selection already taken. Please choose again")
            selection = input()

        board[selection] = current

        if current == 'X':
            current = 'O '
        else:
            current = 'X '

        check_winner()


play_game()
