import random
import eel

eel.init("web")
eel.start("index.html")

def create_board(rows, cols, num_mines, move1):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines = set()
    
    while len(mines) < num_mines:
        row = random.randint(0, rows - 1) 
        col = random.randint(0, cols - 1) 
        if row == move1[0] and col == move1[1]:
            continue
        mines.add((row, col))
        board[row][col] = "X"
    
    return board

def print_board(board):
    rows = len(board)
    cols = len(board[0])
    
    print('   ' + ' '.join(str(i) for i in range(cols)))
    print('  +' + '-' * (2 * cols - 1) + '+')
    
    for i in range(rows):
        print(f'{i} | ' + ' '.join(board[i]) + ' |')
    
    print('  +' + '-' * (2 * cols - 1) + '+')

def show_mines(move, board):
    if board[move[0]][move[1]] == 'X':
        print("You lose!")
    else:
        print("No mine here")

def mines_nearby(move):
    return 0
# if mine then return -1 & end the game (should go in play_game?)
# if no mines nearby then 0 (display all 0s in adjacency)
# for coords around the 0s display the number of mines nearby on them

def play_game():
    rows = int(input('Enter the number of rows: '))
    if rows < 0:
        raise Exception("Invalid number of rows, try again")
    cols = int(input('Enter the number of columns: '))
    if cols < 0:
        raise Exception("Invalid number of columns, try again")
    num_mines = int(input('Enter the number of mines: '))
    if num_mines > rows*cols:
        raise Exception("Invalid number of mines, try again")
    move1 = tuple(int (x) for x in input('Enter the row and column of your first move (r,c): ').split(","))
    if move1[0] > rows or move1[0] < 0 or move1[1] > cols or move1[1] < 0:
        raise Exception("Invalid move, try again")

    board = create_board(rows, cols, num_mines, move1)
    print_board(board)

    print("board generated!")

    show_mines(move1, board)

play_game()