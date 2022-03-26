class BLFactory:

    @staticmethod
    def getBoard(parameters):
        from bl.board import Board
        return Board(parameters)

    @staticmethod
    def getSnake(snakes, board_utility_obj):
        from bl.snake import Snake
        return Snake(snakes, board_utility_obj)

    @staticmethod
    def getLadder(ladders, board_utility_obj):
        from bl.ladder import Ladder
        return Ladder(ladders, board_utility_obj)

    @staticmethod
    def getDice(config):
        from bl.dice import Dice
        return Dice(config)
    
    @staticmethod
    def getPlayer(player):
        from bl.player import Player
        return Player(player)
    
    @staticmethod
    def getGame(parameters, config, log):
        from bl.game import Game
        return Game(parameters, config, log)