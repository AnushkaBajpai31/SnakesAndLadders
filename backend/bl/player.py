from constants.game import PlayerStatus


class Player:
    def __init__(self, player) -> None:
        self.name = player
        self.location = None
        self.moves = 1
        self.status = PlayerStatus.INACTIVE