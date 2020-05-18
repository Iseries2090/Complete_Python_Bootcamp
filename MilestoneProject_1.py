"""
Create a 2 player game for humans of Tic Tac Toe
"""
import random
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print("\n")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("\n")

#Test the display board function
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():
    '''
    Output = (Player 1 marker, Player 2 marker)
    
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player1: Choose X or O: ").upper()
    if marker == "X":
        return ('X', 'O')
    else:
        return ('O', 'X')
    pass

#Test player_input function
#player1_marker,player2_marker = player_input()

def place_marker(board, marker, position):
    board[position] = marker

#Testing the place_marker function
#place_marker(test_board,'$',8)
#display_board(test_board)

def win_check(board, mark):
    
    #Win Tic TAC Toe?
    return(
    #All rows and check to see if they all share the same marker?
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    #all columns, check to see if marker matches
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    #2 diagonals, check to see marker matches
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

#Test win_check function
#display_board(test_board)
#win_check(test_board,'X')

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ''

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full is we return true
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9) '))
        
    return position

def replay():
    
    choice = input("Play again?  Enter Yes or No: ")
    
    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    the_board = ['']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? y/n?')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    #pass

    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = 'Player 2'    
        
        
        
        else:
            #Player 2 Turn
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player2_marker,position)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = 'Player 1'    
                        


    if not replay():
        break