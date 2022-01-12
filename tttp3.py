#!/usr/bin/env python3

import os
import random


def display_board(board):

    os.system('cls||clear')

    print('  |   |  ')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('__|___|__')
    print('  |   |  ')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('__|___|__')
    print('  |   |  ')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('  |   |  ')


def player_input():

    choice = False

    while choice == False:
        marker = input('Player 1: Choose marker (X or O): ')

        if marker not in ['X','x','O','o']:
            print('Please choose X or O (nor zero)')
        else:
            marker = marker.upper()
            choice = True

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):

    check_cond = set()
    win_cond = [set([1,2,3]), set([4,5,6]), set([7,8,9]),
                set([1,4,7]), set([2,5,8]), set([3,6,9]),
                set([1,5,9]), set([3,5,7])]

    for index, value in enumerate(board):
        if value == mark:
            check_cond.add(index)

    for i in win_cond:
        if i.issubset(check_cond):
            return True

    return False


def choose_first():

    if random.randint(1,100) <= 50:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):

    # if board[position] not in ['X','O']:
    #     return True
    # else:
    #     return False

    return board[position] not in ['X','O']


def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):

    choice = ''
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input('Please select next position (1-9): ')

        if choice.isdigit() == False:
            print('Please select a number (1-9)!')
        else:
            if int(choice) not in range(1,10):
                print('Stay within 1 to 9')
            else:
                if not space_check(board, int(choice)):
                    print('Position taken, try again')
                else:
                    within_range = True

    return int(choice)


def replay():

    replay = ''

    while replay not in ['Y','y','N','n']:

        replay = input('Would you like to play again? (Y or N): ')

        if replay not in ['Y','y','N','n']:
            print('Please type "Y" or "N" only.')

    if replay.upper() == 'Y':
        return True
    elif replay.lower() == 'N':
        return False


def play_game():

    state = False

    while state == False:

        play_game = input('Are you ready to play? Enter Yes or No: ')

        if play_game[0].upper() not in ['Y','N']:
            print('Please enter Yes or No: ')
        else:
            state = True
            play_game = play_game[0].upper()

    # if play_game == 'Y':
    #     return True
    # else:
    #     return False
    return play_game == 'Y'



print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    os.system('cls||clear')
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    game_on = play_game()

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        print('Thank you for playing!')
        break
