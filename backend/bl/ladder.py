from constants.errors import Error


class Ladder:
    def __init__(self, ladders, board_utility):
        self.board_utility = board_utility
        self.ladders_dict = self.initializeLadders(ladders)

    def initializeLadders(self, ladders_list: list):
        try:
            board_dict = self.board_utility.getBoardDict()
            ladders_dict = dict()
            for ladder in ladders_list:
                if ladder[0] < ladder[1] and ladder[0] in board_dict and ladder[1] in board_dict:
                    ladders_dict.update({tuple(board_dict[ladder[0]]): tuple(board_dict[ladder[1]])})
                else:
                    raise Exception(Error.LADDER_VALUE_ERROR)
            return ladders_dict
        except Exception as error:
            print('Error while initializing Ladders: ', error)
            raise Exception(Error.LADDER_INIT_ERROR)
    
    def checkIfLadder(self, location: list):
        try:
            return tuple(location) in self.ladders_dict
        except Exception as error:
            print('Error while checking Ladder: ', error)
            raise Exception(Error.LADDER_CHECK_ERROR)

    def climb(self, location: list):
        try:
            distance_dict = self.board_utility.getDistanceDict()
            climbed_location = self.ladders_dict[tuple(location)]
            distance = distance_dict[climbed_location] - distance_dict[tuple(location)]
            return list(climbed_location), distance
        except Exception as error:
            print('Error while climbing Ladders: ', error)
            raise Exception(Error.LADDER_CLIMB_ERROR)