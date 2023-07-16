from tic_tac_toe.engine.game_engine import GameEngine
from tic_tac_toe.utils.tic_tac_toe_board import TicTacToeBoard

GRID_SIZE = 3
ENGINE_SQUARE_VALUE = 1
PLAYER_SQUARE_VALUE = 2

board = TicTacToeBoard(GRID_SIZE, GRID_SIZE, ENGINE_SQUARE_VALUE, PLAYER_SQUARE_VALUE)

game_engine = GameEngine()

# Test Center Move
print('Test Center Move:')
for i in range(2):
    if game_engine.isCenterAvailable(board):
        print('Center Position ' + str(board.getCenterPosition()) +
              ' Is Available. Engine Has Taken Center Position.')
        board.setValueAtIndex(board.getCenterPosition(), board.getEngineSquareValue())
    else:
        print('Center Position Is Not Available.')

print()

# Test Corner Move
print('Test Corner Move:')
for i in range(5):
    available_corner = game_engine.getAvailableCorner(board)
    if available_corner[0]:
        board.setValueAtIndex(available_corner[1], board.getEngineSquareValue())
        print('Corner ' + str(available_corner[1]) + ' Is Available. Engine Has Taken Corner.')
    else:
        print('No Available Corners.')
print()

print('Testing Engine\'s Ability To Make First Move:')
board.resetGridValues()
game_engine.makeMove(board)
board.printBoard()
print()

print('Testing Engine\'s Ability To Win Via Row:')
board.resetGridValues()
for col in range(board.getMaxIndex()[1]):
    board.setValueAtIndex([0, col], engine_square_value)
    print('Engine Move Set To [0,' + str(col) + '].')
game_engine.makeMove(board)
board.printBoard()
print()

print('Testing Engine\'s Ability To Win Via Column:')
board.resetGridValues()
for row in range(board.getMaxIndex()[0]):
    board.setValueAtIndex([row, 0], engine_square_value)
    print('Engine Move Set To [' + str(row) + ',0].')
game_engine.makeMove(board)
board.printBoard()
print()

print('Testing Engine\'s Ability To Block Via Row:')
board.resetGridValues()
for col in range(board.getMaxIndex()[1]):
    board.setValueAtIndex([0, col], player_square_value)
    print('Engine Move Set To [0,' + str(col) + '].')
game_engine.makeMove(board)
board.printBoard()
print()

print('Testing Engine\'s Ability To Block Via Column:')
board.resetGridValues()
for row in range(board.getMaxIndex()[0]):
    board.setValueAtIndex([row, 0], player_square_value)
    print('Engine Move Set To [' + str(row) + ',0].')
game_engine.makeMove(board)
board.printBoard()
print()

print('Testing Engine\'s Ability To Win Via Diagonal:')
board.resetGridValues()
row = 0
col = 0
for i in range(board.getMaxIndex()[0]):
    board.setValueAtIndex([row, col], engine_square_value)
    row += 1
    col += 1
game_engine.makeMove(board)
board.printBoard()
print()

print('Testing Engine\'s Ability To Block Via Diagonal:')
board.resetGridValues()
row = 0
col = 0
for i in range(board.getMaxIndex()[0]):
    board.setValueAtIndex([row, col], player_square_value)
    row += 1
    col += 1
game_engine.makeMove(board)
board.printBoard()