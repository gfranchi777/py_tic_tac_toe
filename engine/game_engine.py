from utils.tic_tac_toe_board import TicTacToeBoard
import random


class GameEngine:
    #
    # Variables
    #

    game_ended: bool
    is_first_move: bool

    #
    # Functions
    #

    def __init__(self):
        self.game_ended = False
        self.is_first_move = True

    def isGameEnded(self):
        return self.game_ended

    def isFirstMove(self, board: TicTacToeBoard):
        for row in range(board.getLength()):
            if not self.is_first_move:
                for col in range(board.getLength()):
                    if board.getValueAtIndex([row, col]) != board.getInitialElementValue():
                        self.is_first_move = False
                        break

        return self.is_first_move

    @staticmethod
    def isCenterAvailable(board: TicTacToeBoard):
        is_center_available = False

        if board.getValueAtIndex(board.getCenterPosition()) == board.getInitialElementValue():
            is_center_available = True

        return is_center_available

    @staticmethod
    def getAvailableCorner(board: TicTacToeBoard):
        is_corner_available = False
        available_corner = []

        for i in range(4):
            if board.getValueAtIndex(board.getCornerPositions()[i]) == board.getInitialElementValue():
                is_corner_available = True
                available_corner = board.getCornerPositions()[i]
                break

        return [is_corner_available, available_corner]

    def makeFirstMove(self, board: TicTacToeBoard):
        if (random.randint(1, 2) % 2) == 0:
            board.setValueAtIndex(board.getCenterPosition(), board.getEngineSquareValue())
        else:
            board.setValueAtIndex(board.getCornerPositions()[random.randint(0, 3)],
                                  board.getEngineSquareValue())

        self.is_first_move = False

    def makeMove(self, board: TicTacToeBoard):
        if self.is_first_move:
            self.makeFirstMove(board)
        else:
            move_made = self.checkForWinOrBlock(board)
            if move_made[0] != "":
                if move_made[0] == "WINNING":
                    print('Engine Determined Winning Move Possible At Index (' +
                          str(move_made[1][0]) + ',' + str(move_made[1][1]) + ').')
                    board.setValueAtIndex(move_made[1], board.getEngineSquareValue())
                elif move_made[0] == "BLOCKING":
                    print('Engine Determined It Must Block A Possible Player Win At Index (' +
                          str(move_made[1][0]) + ',' + str(move_made[1][1]) + ').')
                    board.setValueAtIndex(move_made[1], board.getEngineSquareValue())
            else:
                pass

    @staticmethod
    def checkForWinOrBlock(board: TicTacToeBoard):
        move_made = False
        move_type = ""
        move_coordinates = []
        engine_move_count: int
        player_move_count: int

        # Check Rows
        for row in range(board.getLength()):
            engine_move_count = 0
            player_move_count = 0
            for col in range(board.getLength()):
                if board.getValueAtIndex([row, col]) == board.getEngineSquareValue():
                    engine_move_count += 1
                elif board.getValueAtIndex([row, col]) == board.getPlayerSquareValue():
                    player_move_count += 1
                else:
                    move_coordinates.clear()
                    move_coordinates.insert(0, row)
                    move_coordinates.insert(1, col)

            if board.getValueAtIndex(move_coordinates) == board.getInitialElementValue():
                if engine_move_count == (board.getMaxHorizontalBoundary()):
                    move_made = True
                    move_type = "WINNING"
                    break
                elif player_move_count == (board.getMaxHorizontalBoundary()):
                    move_made = True
                    move_type = "BLOCKING"
                    break

        # Check Cols
        if not move_made:
            for col in range(board.getLength()):
                engine_move_count = 0
                player_move_count = 0
                for row in range(board.getLength()):
                    if board.getValueAtIndex([row, col]) == board.getEngineSquareValue():
                        engine_move_count += 1
                    elif board.getValueAtIndex([row, col]) == board.getPlayerSquareValue():
                        player_move_count += 1
                    else:
                        move_coordinates.clear()
                        move_coordinates.insert(0, row)
                        move_coordinates.insert(1, col)

                if board.getValueAtIndex(move_coordinates) == board.getInitialElementValue():
                    if engine_move_count == (board.getMaxHorizontalBoundary()):
                        move_made = True
                        move_type = "WINNING"
                        break
                    elif player_move_count == (board.getMaxHorizontalBoundary()):
                        move_made = True
                        move_type = "BLOCKING"
                        break

            # Check Diagonals
            if not move_made:
                engine_move_count = 0
                player_move_count = 0
                row = 0
                col = 0
                for i in range(board.getLength()):
                    if board.getValueAtIndex([row, col]) == board.getEngineSquareValue():

                        engine_move_count += 1
                    elif board.getValueAtIndex([row, col]) == board.getPlayerSquareValue():
                        player_move_count += 1
                    else:
                        move_coordinates.clear()
                        move_coordinates.insert(0, row)
                        move_coordinates.insert(1, col)

                    row += 1
                    col += 1

                if board.getValueAtIndex(move_coordinates) == board.getInitialElementValue():
                    if engine_move_count == (board.getMaxHorizontalBoundary()):
                        move_made = True
                        move_type = "WINNING"
                    elif player_move_count == (board.getMaxHorizontalBoundary()):
                        move_made = True
                        move_type = "BLOCKING"

            if not move_made:
                engine_move_count = 0
                player_move_count = 0
                row = 0
                col = 0
                for i in range(board.getLength()):
                    if board.getValueAtIndex([row, col]) == board.getEngineSquareValue():
                        engine_move_count += 1
                    elif board.getValueAtIndex([row, col]) == board.getPlayerSquareValue():
                        player_move_count += 1
                    else:
                        move_coordinates.clear()
                        move_coordinates.insert(0, row)
                        move_coordinates.insert(1, col)

                    row += 1
                    col -= 1

                if board.getValueAtIndex(move_coordinates) == board.getInitialElementValue():
                    if engine_move_count == (board.getMaxHorizontalBoundary()):
                        move_type = "WINNING"
                    elif player_move_count == (board.getMaxHorizontalBoundary()):
                        move_type = "BLOCKING"

        return [move_type, move_coordinates]
