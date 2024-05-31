'''Module
'''
from tic_tac_toe.utils.tic_tac_toe_board import TicTacToeBoard
import random


class GameEngine:
    '''Class
    '''
    def __init__(self):
        self._game_ended = False
        self._is_first_move = True

    @property
    def game_ended(self) -> bool:
        return self._game_ended
    
    @game_ended.setter
    def game_ended(self, game_ended: bool) -> None:
        self._game_ended = game_ended
    
    def is_first_move(self, board: TicTacToeBoard) -> bool:
        for row in range(board.length):
            if not self._is_first_move:
                for col in range(board.length):
                    if board.get_value_at([row, col]) != board.type.value["initial_value"]:
                        self._is_first_move = False
                        break

        return self._is_first_move

    @staticmethod
    def is_center_available(board: TicTacToeBoard):
        is_center_available = False

        if board.get_value_at(board.center_position) == board.type.value["initial_value"]:
            is_center_available = True

        return is_center_available

    @staticmethod
    def get_available_corner(board: TicTacToeBoard):
        is_corner_available = False
        available_corner = []

        for i in range(4):
            if board.get_value_at(board.corner_positions[i]) == board.type.value["initial_value"]:
                is_corner_available = True
                available_corner = board.corner_positions[i]
                break

        return [is_corner_available, available_corner]

    def make_first_move(self, board: TicTacToeBoard):
        if (random.randint(1, 2) % 2) == 0:
            board.set_value_at(board.center_position, board.engine_square_value)
        else:
            board.set_value_at(board.corner_positions[random.randint(0, 3)],
                                  board.engine_square_value)

        self._is_first_move = False

    def make_move(self, board: TicTacToeBoard):
        if self.is_first_move(board):
            self.make_first_move(board)
        else:
            move_made = self.check_for_win_or_block(board)
            if move_made[0] != "":
                if move_made[0] == "WINNING":
                    print('Engine Determined Winning Move Possible At Index (' +
                          str(move_made[1][0]) + ',' + str(move_made[1][1]) + ').')
                    board.set_value_at(move_made[1], board.engine_square_value)
                elif move_made[0] == "BLOCKING":
                    print('Engine Determined It Must Block A Possible Player Win At Index (' +
                          str(move_made[1][0]) + ',' + str(move_made[1][1]) + ').')
                    board.set_value_at(move_made[1], board.engine_square_value)
            else:
                pass

    @staticmethod
    def check_for_win_or_block(board: TicTacToeBoard):
        move_made = False
        move_type = ""
        move_coordinates = []
        engine_move_count: int
        player_move_count: int

        # Check Rows
        for row in range(board.length):
            engine_move_count = 0
            player_move_count = 0
            for col in range(board.length):
                if board.get_value_at([row, col]) == board.engine_square_value:
                    engine_move_count += 1
                elif board.get_value_at([row, col]) == board.player_square_value:
                    player_move_count += 1
                else:
                    move_coordinates.clear()
                    move_coordinates.insert(0, row)
                    move_coordinates.insert(1, col)

            if board.get_value_at(move_coordinates) == board.type.value["initial_value"]:
                if engine_move_count == (board.max_horizontal_boundary):
                    move_made = True
                    move_type = "WINNING"
                    break
                elif player_move_count == (board.max_horizontal_boundary):
                    move_made = True
                    move_type = "BLOCKING"
                    break

        # Check Cols
        if not move_made:
            for col in range(board.length):
                engine_move_count = 0
                player_move_count = 0
                for row in range(board.length):
                    if board.get_value_at([row, col]) == board.engine_square_value:
                        engine_move_count += 1
                    elif board.get_value_at([row, col]) == board.player_square_value:
                        player_move_count += 1
                    else:
                        move_coordinates.clear()
                        move_coordinates.insert(0, row)
                        move_coordinates.insert(1, col)

                if board.get_value_at(move_coordinates) == board.type.value["initial_value"]:
                    if engine_move_count == (board.max_horizontal_boundary):
                        move_made = True
                        move_type = "WINNING"
                        break
                    elif player_move_count == (board.max_horizontal_boundary):
                        move_made = True
                        move_type = "BLOCKING"
                        break

            # Check Diagonals
            if not move_made:
                engine_move_count = 0
                player_move_count = 0
                row = 0
                col = 0
                for i in range(board.length):
                    if board.get_value_at([row, col]) == board.engine_square_value:

                        engine_move_count += 1
                    elif board.get_value_at([row, col]) == board.player_square_value:
                        player_move_count += 1
                    else:
                        move_coordinates.clear()
                        move_coordinates.insert(0, row)
                        move_coordinates.insert(1, col)

                    row += 1
                    col += 1

                if board.get_value_at(move_coordinates) == board.type.value["initial_value"]:
                    if engine_move_count == (board.max_horizontal_boundary):
                        move_made = True
                        move_type = "WINNING"
                    elif player_move_count == (board.max_horizontal_boundary):
                        move_made = True
                        move_type = "BLOCKING"

            if not move_made:
                engine_move_count = 0
                player_move_count = 0
                row = 0
                col = 0
                for i in range(board.length):
                    if board.get_value_at([row, col]) == board.engine_square_value:
                        engine_move_count += 1
                    elif board.get_value_at([row, col]) == board.player_square_value:
                        player_move_count += 1
                    else:
                        move_coordinates.clear()
                        move_coordinates.insert(0, row)
                        move_coordinates.insert(1, col)

                    row += 1
                    col -= 1

                if board.get_value_at(move_coordinates) == board.type.value["initial_value"]:
                    if engine_move_count == (board.max_horizontal_boundary):
                        move_type = "WINNING"
                    elif player_move_count == (board.max_horizontal_boundary):
                        move_type = "BLOCKING"

        return [move_type, move_coordinates]
