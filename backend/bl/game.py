from bl.player import Player
from constants.errors import Error
from constants.game import PlayerStatus, Game as GameConstants
from factory.bl_factory import BLFactory


class Game:
    def __init__(self, parameters, config, log):
        self.log = log
        self.factory = BLFactory()
        self.board = self.factory.getBoard(parameters)
        self.dice = self.factory.getDice(config['DICE'])
        self.winner = None
        self.players = list()
        for player in parameters['Players']:
            self.players.append(self.factory.getPlayer(player))
        self.lucky_moves = 0
        self.unlucky_moves = 0
    
    def play(self):
        try:
            row_max = self.board.boardSize - 1
            col_max = self.board.boardSize - 1

            while not self.isActive():
                self.resetMoves()
                for player in self.players:
                    moves_list = list()
                    max_climb = 0
                    max_bite = 0
                    while player.moves != 0:
                        steps = self.dice.roll()
                        self.log.write('Player Current Location: {0}\nRolled Dice, Got: {1}\n'.format(player.location, steps))
                        moves_list.append(steps)

                        if player.status == PlayerStatus.INACTIVE and steps == 6:
                            player.location = [row_max, -1]
                            player.status = PlayerStatus.ACTIVE
                            
                        elif player.status == PlayerStatus.ACTIVE:
                            remaining_moves = (player.location[0]*self.board.boardSize) + \
                            (player.location[1] - 0 if player.location[0] % 2 == 0 else col_max - player.location[1])
                            if steps <= remaining_moves:
                                self.lucky_moves = self.lucky_moves + 1 if steps == remaining_moves else self.lucky_moves
                                player = self.board.move(player, steps)

                        self.log.write('Player Location After Move: {0}\n'.format(player.location))
                        if player.location:
                            player, max_climb, max_bite = self.checkForSnakesAndLadders(player, max_climb, max_bite)
                            if self.board.checkIfMissedSnake(player.location):
                                self.lucky_moves += 1

                        if player.location == [0,0]:
                            player.status = PlayerStatus.WIN
                            break

                        player.moves = player.moves - 1

                        if steps == 6:
                            player.moves += 1
                    self.log.write('Max Climb Distance in this turn is: {0}\nMax Slide Distance in this turn is: {1}\nMoves made by Player {2} in this turn are: {3}\n'.format(max_climb, max_bite, player.name, moves_list))

            self.log.write('Lucky Moves in this game: {0}\nUnlucky Moves in this game: {1}\nWinner of this game: {2}\n'.format(self.lucky_moves, self.unlucky_moves, self.winner))
            return self.winner + GameConstants.WINNER_STRING
        except Exception as error:
            print('Error while calling Play: ', error)
            raise Exception(Error.GAME_ERROR)
    
    def checkForSnakesAndLadders(self, player: Player, max_climb: int, max_bite: int):
        try:
            # TODO: Check case if Snake bite location and Ladder Climb location same?
            if self.board.snakes.checkIfSnake(player.location):
                player.location, distance = self.board.snakes.bite(player.location)
                max_bite = max(distance, max_bite)
                self.unlucky_moves += 1
                self.log.write('Player Bitten By Snake, Reaches: {0}\n'.format(player.location))

            # TODO: Check case if Ladder Climb then Bitten by Snake possible?
            if self.board.ladders.checkIfLadder(player.location):
                player.location, distance = self.board.ladders.climb(player.location)
                max_climb = max(distance, max_climb)
                self.lucky_moves += 1
                self.log.write('Player Climbs The Ladder, Reaches: {0}\n'.format(player.location))
            return player, max_climb, max_bite
        except Exception as error:
            print('Error while checking Snakes and Ladders: ', error)
            raise Exception(Error.SNAKES_AND_LADDERS_ERROR)

    def isActive(self):
        for player in self.players:
            if player.status == PlayerStatus.WIN:
                self.winner = player.name
                return True
        return False

    def resetMoves(self):
        for player in self.players:
            player.moves = 1