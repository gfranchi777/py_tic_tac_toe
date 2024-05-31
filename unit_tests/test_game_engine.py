'''Module
'''
from tic_tac_toe.engine.game_engine import GameEngine
from tic_tac_toe.utils.tic_tac_toe_board import TicTacToeBoard

GRID_SIZE = 3
ENGINE_SQUARE_VALUE = 'X'
PLAYER_SQUARE_VALUE = 'O'

board = TicTacToeBoard(GRID_SIZE, GRID_SIZE, ENGINE_SQUARE_VALUE, PLAYER_SQUARE_VALUE)

game_engine = GameEngine()

# Test Center Move
print('Test Center Move:')
for i in range(2):
    if game_engine.is_center_available(board):
        print('Center Position ' + str(board.center_position) +
              ' Is Available. Engine Has Taken Center Position.')
        board.set_value_at(board.center_position, board.engine_square_value)
    else:
        print('Center Position Is Not Available.')

print()

# Test Corner Move
print('Test Corner Move:')
for i in range(5):
    available_corner = game_engine.get_available_corner(board)
    if available_corner[0]:
        board.set_value_at(available_corner[1], board.engine_square_value)
        print('Corner ' + str(available_corner[1]) + ' Is Available. Engine Has Taken Corner.')
    else:
        print('No Available Corners.')
print()

print('Testing Engine\'s Ability To Make First Move:')
board.initialize()
game_engine.make_move(board)
board.print_board()
print()

print('Testing Engine\'s Ability To Win Via Row:')
board.initialize()
for col in range(board.max_index[1]):
    board.set_value_at([0, col], board.engine_square_value)
    print('Engine Move Set To [0,' + str(col) + '].')
game_engine.make_move(board)
board.print_board()
print()

print('Testing Engine\'s Ability To Win Via Column:')
board.initialize()
for row in range(board.max_index[0]):
    board.set_value_at([row, 0], board.engine_square_value)
    print('Engine Move Set To [' + str(row) + ',0].')
game_engine.make_move(board)
board.print_board()
print()

print('Testing Engine\'s Ability To Block Via Row:')
board.initialize()
for col in range(board.max_index[1]):
    board.set_value_at([0, col], board.player_square_value)
    print('Engine Move Set To [0,' + str(col) + '].')
game_engine.make_move(board)
board.print_board()
print()

print('Testing Engine\'s Ability To Block Via Column:')
board.initialize()
for row in range(board.max_index[0]):
    board.set_value_at([row, 0], board.player_square_value)
    print('Engine Move Set To [' + str(row) + ',0].')
game_engine.make_move(board)
board.print_board()
print()

print('Testing Engine\'s Ability To Win Via Diagonal:')
board.initialize()
row = 0
col = 0
for i in range(board.max_index[0]):
    board.set_value_at([row, col], board.engine_square_value)
    row += 1
    col += 1
game_engine.make_move(board)
board.print_board()
print()

print('Testing Engine\'s Ability To Block Via Diagonal:')
board.initialize()
row = 0
col = 0
for i in range(board.max_index[0]):
    board.set_value_at([row, col], board.player_square_value)
    row += 1
    col += 1
game_engine.make_move(board)
board.print_board()
