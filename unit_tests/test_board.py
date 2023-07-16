""""Module
"""
from tic_tac_toe.utils.tic_tac_toe_board import TicTacToeBoard

GRID_SIZE = 3
ENGINE_SQUARE_VALUE = 1
PLAYER_SQUARE_VALUE = 2

def main() -> None:
    """Main
    """
    board = TicTacToeBoard(GRID_SIZE, GRID_SIZE, ENGINE_SQUARE_VALUE, PLAYER_SQUARE_VALUE)

    board.print_board_details()
    print()
    board.print_board()

    print()

    print('Element Retrieval Test - Success')
    print('Playing Grid Element ' + str(board.max_index) + ' Is ' +
            str(board.get_value_at(board.max_index)))
    print()

    print('Element Retrieval Test - Failure')
    board.get_value_at([GRID_SIZE, GRID_SIZE])
    print()

    print('Element Modification Test - Success')
    board.set_value_at(board.max_index, 1)
    print('Playing Grid Element ' + str(board.max_index) + ' Is ' +
            str(board.get_value_at(board.max_index)))
    board.print_board()
    print()

    print('Element Modification Test - Failure')
    board.set_value_at([GRID_SIZE, GRID_SIZE], 3)

if __name__ == '__main__':
    main()
