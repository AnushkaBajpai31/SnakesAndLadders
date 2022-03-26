from constants.errors import Error
from factory.bl_factory import BLFactory
from factory.util_factory import UtilFactory
from utility.board import BoardUtility


class Board:
    def __init__(self, parameters):
        # TODO: VALIDATE PARAMETERS
        self.boardSize = parameters['BoardSize']
        self.refDict = dict()
        self.board = self.initializeBoard()
        self.boardUtility = UtilFactory().getBoardUtility(self.refDict)
        self.snakes = BLFactory().getSnake(parameters['Snakes'], self.boardUtility)
        self.ladders = BLFactory().getLadder(parameters['Ladders'], self.boardUtility)

    def getBoardValue(self, row, col):
        try:
            return self.board[row][col]
        except Exception as error:
            print('Error while getting Board Value: ', error)
            raise Exception(Error.BOARD_VALUE_ERROR)

    def move(self, player, steps):
        try:
            if player.location[0] % 2 == 0:
                player = self.moveLeft(player, steps)
            elif player.location[0] % 2 != 0:
                player = self.moveRight(player, steps)
            return player
        except Exception as error:
            print('Error while calling Move: ', error)
            raise Exception(Error.MOVE_ERROR)

    def moveLeft(self, player, steps):
        try:
            curr_col = player.location[1]
            stepper = curr_col - steps

            if stepper >= 0:
                player.location[1] = stepper
            else:
                player.location[1] = 0
                remaining_steps = 0 - stepper
                player = self.moveUp(player)
                remaining_steps = remaining_steps - 1
                if remaining_steps != 0:
                    player = self.move(player, remaining_steps)

            return player
        except Exception as error:
            print('Error while calling Move Left: ', error)
            raise Exception(Error.MOVE_ERROR)

    def moveRight(self, player, steps):
        try:
            col_max = self.boardSize - 1
            curr_col = player.location[1]
            stepper = curr_col + steps

            if stepper <= col_max:
                player.location[1] = stepper
            else:
                player.location[1] = col_max
                remaining_steps = stepper - col_max
                player = self.moveUp(player)
                remaining_steps = remaining_steps - 1
                if remaining_steps != 0:
                    player = self.move(player, remaining_steps)

            return player
        except Exception as error:
            print('Error while calling Move Right: ', error)
            raise Exception(Error.MOVE_ERROR)

    def moveUp(self, player):
        try:
            curr_row = player.location[0]
            if curr_row - 1 > -1:
                player.location[0] = curr_row - 1
                return player
            else:
                raise Exception(Error.BOARD_ROW_EXCEEDED)
        except Exception as error:
            print('Error while calling Move Up: ', error)
            raise Exception(error)

    def initializeBoard(self):
        try:
            board_dict = dict()
            board = [[0 for i in range(self.boardSize)] for j in range(self.boardSize)]
            num = self.boardSize*self.boardSize
            for i in range(self.boardSize):
                if i % 2 == 0:
                    j = 0
                    while j < self.boardSize:
                        board[i][j] = num
                        board_dict.update({num: [i,j]})
                        num = num - 1
                        j = j + 1
                else:
                    j = self.boardSize - 1
                    while j > -1:
                        board[i][j] = num
                        board_dict.update({num: [i,j]})
                        num = num - 1
                        j = j - 1
            self.refDict.update({'boardDict': board_dict})
            return board
        except Exception as error:
            print('Error while initializing Board: ', error)
            raise Exception(Error.BOARD_ERROR)

    def checkIfMissedSnake(self, location):
        num = self.getBoardValue(location[0], location[1])
        return self.snakes.checkIfMissedSnake(num)