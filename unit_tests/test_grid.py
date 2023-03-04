from ..grid import Grid

grid_size = 3
engine_square_value = 1
player_square_value = 2
board = TicTacToeBoard(grid_size, grid_size, engine_square_value, player_square_value)

board.printBoardDetails()
print()
board.printGrid()
print()
board.printBoard()
print()

print('Element Retrieval Test - Success')
print('Playing Grid Element ' + str(board.getMaxIndex()) + ' Is ' +
      str(board.getValueAtIndex(board.getMaxIndex())))
print()

print('Element Retrieval Test - Failure')
board.getValueAtIndex([grid_size, grid_size])
print()

print('Element Modification Test - Success')
board.setValueAtIndex(board.getMaxIndex(), 1)
print('Playing Grid Element ' + str(board.getMaxIndex()) + ' Is ' +
      str(board.getValueAtIndex(board.getMaxIndex())))
board.printBoard()
print()

print('Element Modification Test - Failure')
board.setValueAtIndex([grid_size, grid_size], 3)