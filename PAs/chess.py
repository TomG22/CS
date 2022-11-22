###
### Author: Tom Giallanza
### Description: Draws a 1 dimentional chess board for the user to interact with.
### Enter in the index for each piece the piece you want to move and the direction afterwards.
###

from graphics import graphics

# You should use these globals in the functions in this file!
W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'

def is_valid_move(board, position, player):
    '''Description: Checks if the piece that the player is trying to move is their color.
    Parameters: board can be a list
    position can be an integer
    player can be a string'''
    if board[position][0] == player[0]:
        return True
    else:
        return False

def move_knight(board, position, direction):
    '''Description: Moves the selected knight 2 spaces in the left or right direction while
    updating the board list.
    Parameters: board can be a list
    position can be an integer
    direction can be an integer'''
    if 0 <= position + direction*2 <= len(board) - 1:
        board[position + direction*2] = board[position]
        board[position] = EMPTY
        position = position+2*direction

def move_king(board, position, direction):
    '''Description: Moves the selected king 1 space to the left or right direction until
    it hits another piece or the edge of the board while updating the board list.
    Parameters: board can be a list
    position can be an integer
    direction can be an integer'''
    found_piece = False
    while 0 <= position + direction <= len(board) - 1 and found_piece == False:
        if board[position+ direction] != EMPTY:
            found_piece = True
        board[position+1*direction] = board[position]
        board[position] = EMPTY
        position = position+1*direction


def print_board(board):
    '''Description: Prints the current chess board using the board list
    Parameters: board can be a list'''
    print(
        "+-----------------------------------------------------+\n"
        "| " + board[0] + " | " + board[1] + " | " + board[2] + " | "+ board[3] +
        " | " + board[4] + " | " + board[5] + " | " + board[6] + " | " + board[7] + " | " + board[8] + " |\n"
        "+-----------------------------------------------------+")

def draw_board(board, gui):
    '''Description: Draws the current chess board in a graphics window using the board list
    Parameters: board can be a list
    gui can be a graphics window object from the graphics module'''
    gui.clear()
    gui.text(210, 50, "1 Dimensional Chess", "green", 25)
    i = 5
    for piece in board:
        gui.rectangle(i-2, 98, 79, 79, "black")
        gui.rectangle(i, 100, 75, 75, "darkred")
        if piece[0] == "W":
            gui.text(i + 5, 125, piece, "white")
        else:
            gui.text(i + 5, 125, piece, "black")
        i += 77
    gui.update_frame(30)

def is_game_over(board):
    '''Description: Checks if a player has won the game by seeing if the opposite
    color possesses a king.
    Parameters: board can be a list'''
    winner = None
    for piece in board: 
        if piece == W_KING:
            winner = False
    if winner != False:
        winner = BLACK
    if winner != BLACK:
        winner = None
        for piece in board:
            if piece == B_KING:
                winner = False
        if winner != False:
            winner = WHITE
    if winner and winner != False:
        print_board(board)
        print(winner + " wins!")
        return True
    else: 
        return False

def move(board, position, direction):
    '''Description: Sees if the piece being moved is a knight or a king and calls
    the designated move function for each piece.
    Parameters: board can be a list
    position can be an integer
    direction can be a string'''
    if direction == "r":
        direction = 1
    else:
        direction = -1
    if board[position][2] == "n":
        move_knight(board, position, direction)
    if board[position][2] == "i":
        move_king(board, position, direction)

def main():
   
    # DO NOT CHANGE THE CODE IN THE MAIN FUNCTION

    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]
    
    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE
    
    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:
        
        print_board(board)

        # Draw the board
        draw_board(board, gui)  
      
        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            # Draw the board again
            draw_board(board, gui)
            is_game_won = is_game_over(board)

main()
