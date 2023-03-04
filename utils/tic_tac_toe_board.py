from utils.grid import Grid


class TicTacToeBoard(Grid):
    # Variables
    engine_square_value: int
    player_square_value: int

    corner_positions = []
    center_position = []

    def __init__(self, length: int, width: int, engine_square_value: int, player_square_value: int):
        if self.isValidBoardDimension(length, width):
            super().__init__(length, width)
            self.initializeBoard(engine_square_value, player_square_value)

    def getEngineSquareValue(self):
        return self.engine_square_value

    def getPlayerSquareValue(self):
        return self.player_square_value

    def getCenterPosition(self):
        return self.center_position[0]

    def getCornerPositions(self):
        return self.corner_positions

    def determineCenterPosition(self):
        self.center_position.insert(0, [int(self.getLength() / 2), int(self.getWidth() / 2)])

    def determineCornerPositions(self):
        # Top Left Corner
        self.corner_positions.insert(0, self.getMinIndex())

        # Top Right Corner
        self.corner_positions.insert(1, [0, self.getMaxHorizontalBoundary()])

        # Bottom Left Corner
        self.corner_positions.insert(2, [self.getMaxHorizontalBoundary(), 0])

        # Bottom Right Corner
        self.corner_positions.insert(3, [self.getMaxHorizontalBoundary(), self.getMaxHorizontalBoundary()])

    def isValidGridElement(self, val: int):
        is_valid_grid_element = False

        if val in range(1, 3):
            is_valid_grid_element = True
        else:
            print('[ERROR]: Value ' + str(val) + ' Is Not A Valid Grid Element.')
            print('         Valid Values For Grid Elements Are ' + str(self.getPlayerSquareValue()) + ' or ' +
                  str(self.getEngineSquareValue()))

        return is_valid_grid_element

    @staticmethod
    def isValidBoardDimension(length: int, width: int):
        is_valid_board_dimension = False

        if length == width:
            if length >= 3:
                if length % 2 != 0:
                    is_valid_board_dimension = True
                else:
                    print('[ERROR]: Grid Size Must Be An Odd Number.')
                    print('         Grid Size Entered: [' + str(length) + ',' + str(width) + '].')
            else:
                print('[ERROR]: Grid Size Must Be Greater Than Or Equal To 3.')
                print('         Grid Size Entered: [' + str(length) + ',' + str(width) + '].')
        else:
            print('[ERROR] Grid Must Be A Square.')
        return is_valid_board_dimension

    def initializeBoard(self, engine_square_value: int, player_square_value: int):
        self.engine_square_value = engine_square_value
        self.player_square_value = player_square_value

        self.determineCenterPosition()
        self.determineCornerPositions()

    def printBoardDetails(self):
        print('Playing Grid Size Is [' + str(self.getLength()) + ',' + str(self.getWidth()) + '].')

        print('Center Position Index Is ' + str(self.getCenterPosition()[0]) + '.')

        corner_positions_string = ""

        print('Corner Position Indices Are ' + corner_positions_string)

        for row in range(len(self.getCornerPositions())):
            print('[' + str(self.corner_positions[row][0]) + ',' + str(self.corner_positions[row][1]) + ']')

    def printBoard(self):
        print('Current Board Status:', end='\n\n')
        for row in range(self.getLength()):
            for col in range(self.getWidth()):
                print(str(self.grid[row][col]) + ' ', end='')
            print()
