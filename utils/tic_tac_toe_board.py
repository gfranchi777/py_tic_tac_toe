'''Module
'''
from pyutils.math_utils.grid.string_grid import StringGrid

class TicTacToeBoard(StringGrid):
    '''Class
    '''

    def __init__(self, length: int, width: int, engine_square_value: str, player_square_value: str) -> None:
        if self.is_valid_board_dimenstion(length, width):
            self._center_position = []
            self._corner_positions = []

            self._engine_square_value: int
            self._player_square_value: int

            super().__init__(length, width)
            self.initialize_board(engine_square_value, player_square_value)

    @property
    def engine_square_value(self) -> str:
        return self._engine_square_value

    @engine_square_value.setter
    def engine_square_value(self, engine_square_value: str) -> None:
        self._engine_square_value = engine_square_value

    @property
    def player_square_value(self) -> str:
        return self._player_square_value

    @player_square_value.setter
    def player_square_value(self, player_square_value: int) -> None:
        self._player_square_value = player_square_value

    @property
    def center_position(self) -> list[int]:
        return self._center_position

    @property
    def corner_positions(self) -> list[int]:
        return self._corner_positions

    def determine_center_position(self) -> None:
        self._center_position = [int(self.length / 2), int(self.width / 2)]

    def determine_corner_positions(self) -> None:
        # Top Left Corner
        self.corner_positions.insert(0, self.min_index)

        # Top Right Corner
        self.corner_positions.insert(1, [0, self.max_horizontal_boundary])

        # Bottom Left Corner
        self.corner_positions.insert(2, [self.max_horizontal_boundary, 0])

        # Bottom Right Corner
        self.corner_positions.insert(3, [self.max_horizontal_boundary, self.max_horizontal_boundary])

    def is_valid_grid_element(self, val: int) -> bool:
        is_valid_grid_element = False

        if val in range(1, 3):
            is_valid_grid_element = True
        else:
            print('[ERROR]: Value ' + str(val) + ' Is Not A Valid Grid Element.')
            print('         Valid Values For Grid Elements Are ' + str(self.player_square_value) + ' or ' +
                  str(self.engine_square_value))
            
        return is_valid_grid_element

    @staticmethod
    def is_valid_board_dimenstion(length: int, width: int) -> bool:
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

    def initialize_board(self, engine_square_value: int, player_square_value: int) -> None:
        super().initialize()

        self.engine_square_value = engine_square_value
        self.player_square_value = player_square_value

        self.determine_center_position()
        self.determine_corner_positions()

    def print_board_details(self) -> None:
        print('Playing Grid Size Is [' + str(self.length) + ',' + str(self.width) + '].')

        print('Center Position Index Is ' + str(self.center_position[0]) + '.')

        print('Corner Position Indices Are ')

        for row_index, row_val in enumerate(self.corner_positions):
            print('[' + str(self.corner_positions[row_index][0]) + ',' +
                        str(self.corner_positions[row_index][1]) + ']')

    def print_board(self) -> None:
        print('Current Board Status:', end='\n\n')
        for row in range(self.length):
            for col in range(self.width):
                print(str(self.grid[row][col]) + ' ', end='')
            print()
