import random;
import os;
# a function to clear the board
def clear():
    os.system('cls')
#function to create the display board. Update the board to look better later
def display_board(board):
    clear()
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('-----------')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('-----------')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])


# function to assign the marker to the players
def player_input():

    '''
    OUTPUT = (PLAYER 1 MARKER, PLAYER 2 MARKER)
    :return:
    '''


    marker=''
    #ask player1 to choose x or o
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    #assign player2 the opposite marker
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')




#write a function to get the position and placing the marker in the position
def place_marker(board, marker, position):
    board[position] = marker

#function to check if the mark has won
def win_check(board, mark ):
    # check all the ROWS to see if they all share the same marker
    # check all the COLUMNS to see if they all share the same marker
    #check the diagonals at last
    return(
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[1] == board[5] == board[9] == mark)
    )

# function that uses random module to decide which player goes first
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

# function that returns a boolean indicating a white space is available or not
def space_check(board, position):
    return board[position] == ''

# function to check whether the board is full or not
def full_board_check(board):
    for i in (1,10):
        if space_check(board,i):
            return False
    return True #this means the board is full

# function that asks for a player's next position , checks whether it is a free position, then returns the position for later use
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board , position):
        position = int(input('Choose a position: (1 to 9)'))
    return position

# function that asks if they wanna play again and return true if yes
def replay():
    choice = input('Play again? Enter yes or no')
    return choice =='yes'





# real implementation


# while loop to keep running the game
print('Welcome to Tic Tac Toe! Enjoy the Game')
while True:

    # play the game
    # set everything up (board, first player, choose markers x,0 )
    the_board = ['']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Ready to play? enter y or n?')
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            #show the board to choose the position
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player1_marker,position)
            # check if they  won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!!')
                game_on = False
            else:
                if full_board_check(the_board):           # or check if there's a tie
                    display_board(the_board)
                    print('TIE GAME!!!!!')
                    break
                else:
                    turn = 'Player 2'                  # no tie or no win ? Then next Player's turn?
        else:    #player 2 position
            # show the board to choose the position
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # check if they  won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!!')
                game_on = False
            else:
                if full_board_check(the_board):         # or check if there's a tie
                    display_board(the_board)
                    print('TIE GAME!!!!!')
                    break
                else:
                    turn = 'Player 1'             # no tie or no win ? Then next Player's turn?


    if not replay():
        break
# break out of the loop on replay()













