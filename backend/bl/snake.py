from constants.errors import Error


class Snake:
    def __init__(self, snakes, board_utility):
        self.board_utility = board_utility
        self.snakes_dict = self.initializeSnakes(snakes)
        self.snakes_faces = set([snake[0] for snake in snakes])

    def initializeSnakes(self, snakes_list: list):
        try:
            board_dict = self.board_utility.getBoardDict()
            snakes_dict = dict()
            for snake in snakes_list:
                if snake[0] > snake[1] and snake[0] in board_dict and snake[1] in board_dict:
                    snakes_dict.update({tuple(board_dict[snake[0]]): tuple(board_dict[snake[1]])})
                else:
                    raise Exception(Error.SNAKE_VALUE_ERROR)
            return snakes_dict
        except Exception as error:
            print('Error while initializing Snakes: ', error)
            raise Exception(Error.SNAKE_INIT_ERROR)
    
    def checkIfSnake(self, location: list):
        try:
            return tuple(location) in self.snakes_dict
        except Exception as error:
            print('Error while checking Snake: ', error)
            raise Exception(Error.SNAKE_CHECK_ERROR)

    def bite(self, location: list):
        try:
            distance_dict = self.board_utility.getDistanceDict()
            bite_location = self.snakes_dict[tuple(location)]
            distance = distance_dict[tuple(location)] - distance_dict[bite_location]
            return list(bite_location), distance
        except Exception as error:
            print('Error while Snake biting: ', error)
            raise Exception(Error.SNAKE_BITE_ERROR)

    def checkIfMissedSnake(self, num: int):
        if num - 1 in self.snakes_faces or num + 1 in self.snakes_faces or num - 2 in self.snakes_faces or num + 2 in self.snakes_faces:
            return True
        return False