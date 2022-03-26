from constants.errors import Error


class Dice:
    def __init__(self, config):
        self.min_num = config['MIN']
        self.max_num = config['MAX']
    
    def roll(self):
        try:
            import random
            return random.randrange(self.min_num, self.max_num + 1)
        except Exception as error:
            print('Error while calling Roll: ', error)
            raise Exception(Error.ROLL_ERROR)