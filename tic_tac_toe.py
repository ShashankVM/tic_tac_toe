from graphics import Canvas
import time
from math import floor
CANVAS_HEIGHT = 400
CANVAS_WIDTH = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    BOARD_LENGTH=300
    draw_board(canvas, BOARD_LENGTH)
    # print initial text
    initial_text = canvas.create_text(
    0, 
    330, 
    text = f"Welcome to Tic Tac Toe!",
    font = 'Arial', 
    font_size = 25, 
    color ='teal'
    )
    time.sleep(1)
    # create game matrix
    game_matrix = [["" for x in range(3)] for y in range(3)]
    player_num = 1
    player_1_turn = True
    game_over = False
    number_of_turns_played = 0
    while not game_over:
          
        if number_of_turns_played >= 5:
                result = check_win(game_matrix, matrix_x, matrix_y, piece)
                if result is not None:
                    draw_arrow(canvas, result) 
                    time.sleep(0.5) 
                    print_message(canvas, initial_text, f"Congratulations Player {player_num}!")               
                    game_over = True
                    break

        if number_of_turns_played == 9:
                game_over == True
                print_message(canvas, initial_text, f"Game Over!")
                break

        piece, player_num = ['X', 1] if player_1_turn == True else ['O', 2]
        print_message(canvas, initial_text, f"Player {player_num} turn")
   
        click = canvas.get_last_click() 
        if click is not None:
            click_x_pos, click_y_pos = click
            if ((click_x_pos <= 300) and (click_y_pos <= 300)):
                matrix_x, matrix_y = get_matrix_pos(click_x_pos, click_y_pos)
                if game_matrix[matrix_x][matrix_y] == "":
                    put_piece(canvas, matrix_x, matrix_y, piece)
                    game_matrix[matrix_x][matrix_y] = piece
                    # alternate player turn
                    player_1_turn = not(player_1_turn)
                    number_of_turns_played += 1
                    time.sleep(0.5)

def draw_arrow(canvas, result):
    """
    Function to draw an arrow over the winning line
    Inputs: canvas, result tuple
    Effects: Draws a line over the winning line
    """
    if result[1] == "column":
        line_height = result[0]*100 + 50
        horizontal_line = canvas.create_line(0, line_height, 300, line_height, 'yellow')
    elif result[1] == "row":
        line_x = result[0]*100 + 50
        vertical_line = canvas.create_line(line_x, 0, line_x, 300, 'yellow')
    elif result[1] == "diagonal":
        if result[0] == "main":
            main_diagonal_line = canvas.create_line(0, 0, 300, 300, 'yellow')
        else:
            off_diagonal_line = canvas.create_line(0, 300, 300, 0, 'yellow')        

def print_message(canvas, text, new_text):
    """
    Function to print new message
    Inputs: canvas, text
    Effects: Modifies the printed text on the screen
    """
    canvas.change_text(
    text, 
    new_text
    )
         

def get_matrix_pos(x_pos, y_pos):
    """
    Function to convert mouse click position into matrix index
    Inputs: mouse click x and y co-ordinates
    Returns: Tuple of matrix x and y index
    """
    
    matrix_x, matrix_y = map(lambda x: floor(x/100), [x_pos, y_pos])
    return (matrix_x, matrix_y)
  


def check_win(game_matrix, x_pos, y_pos, piece):
    """
    Funtion to check if any player has won the game.
    Inputs: Game matrix, x and y co-ordinates of last piece, piece type
    Returns:
    Winning line co-ordinates if any player has won
    (0,0) Otherwise
    """
    winning_piece = (piece * 3)
    # check if row in x_pos is a winning row
    def check_row():
        rowwise_concatenation = ''.join(elem for elem in game_matrix[x_pos])
        return (x_pos, 'row') if  rowwise_concatenation == winning_piece else None

    # check if column in y_pos is a winning column
    def check_column():
        columnwise_contatenation = ''
        for x_idx in range(3):
            columnwise_contatenation += game_matrix[x_idx][y_pos]
        return (y_pos, 'column') if columnwise_contatenation == winning_piece else None

    # check if main diagonal is a winning diagonal
    def check_main_diagonal():
        main_diagonal_concatenation = ''
        for i in range(0,3):
             main_diagonal_concatenation += game_matrix[i][i]
        return ('main', 'diagonal') if main_diagonal_concatenation == winning_piece else None
    
    # check if off diagonal is a winning diagonal
    def check_off_diagonal():
        off_diagonal_concatenation = game_matrix[2][0] + game_matrix[1][1] + game_matrix[0][2]
        return ('off', 'diagonal') if off_diagonal_concatenation == winning_piece else None

    if check_row() is not None:
        return check_row()
    elif check_column() is not None:
        return check_column()
    elif (x_pos == y_pos) and (check_main_diagonal() is not None):
        return check_main_diagonal()
    elif ((abs(x_pos - y_pos) == 2) or (x_pos, y_pos) == (1, 1)) and (check_off_diagonal() is not None):
        return check_off_diagonal() 
    else:
        return None




def put_piece(canvas, x_pos, y_pos, piece):
    """
    Function to place the piece in the middle of the square
    Inputs: canvas, x-co-ordinate, y-co-ordinate, piece type
    Effects: Places piece on the screen
    """
    x_pos, y_pos = map(lambda x: (x*100) + 30, [x_pos, y_pos])
    canvas.create_text(
    x_pos, 
    y_pos, 
    text = f"{piece}",
    font = 'Arial', 
    font_size = 60, 
    color = 'magenta' if piece == 'X' else 'green'
    )


def draw_board(canvas, BOARD_LENGTH):
    """
    Function to draw Tic Tac Toe board
    It is a 3x3 board
    Inputs: canvas, BOARD_LENGTH
    Effects: Draws a Tic Tac Toe board of BOARD_LENGTH
    """
    
    # calculate one third length
    one_third_length = BOARD_LENGTH/3

    # draw 2 vertical lines
    for i in range(1,3):
        vertical_first_line = canvas.create_line(i*one_third_length, 0, i*one_third_length, BOARD_LENGTH, 'white')
   
    # draw 3 horizontal lines
    for i in range(1,4):
        horizontal_line = canvas.create_line(0, i*one_third_length, BOARD_LENGTH, i*one_third_length, 'white') 


if __name__ == '__main__':
    main()
