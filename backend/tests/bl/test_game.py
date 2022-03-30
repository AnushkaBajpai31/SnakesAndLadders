from unittest import TestCase, mock

import pytest

from bl.game import Game
from bl.player import Player
from constants.game import PlayerStatus, Game as GameConstants

class TestGameBL(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mock = mock

    def testPlay1(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': 1, 'MAX': 6}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        expected_winner = 'Anushka'
        game.winner = expected_winner
        output = game.play()
        expected_output = expected_winner + GameConstants.WINNER_STRING
        assert expected_output == output

    def testPlay2(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': '1', 'MAX': '6'}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        with pytest.raises(Exception):
            output = game.play()

    def testIsActive1(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': 1, 'MAX': 6}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        output = game.isActive()
        expected_output = False
        assert expected_output == output

    def testIsActive2(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': 1, 'MAX': 6}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        for player in game.players:
            player.status = PlayerStatus.WIN
        output = game.isActive()
        expected_output = True
        assert expected_output == output

    def testResetMoves1(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': 1, 'MAX': 6}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        game.resetMoves()
        expected_output = 1
        assert expected_output == game.players[0].moves
        
    def testCheckForSnakesAndLadders1(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': 1, 'MAX': 6}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        mock_player = Player('Anushka')
        mock_player.location = [0, 3]
        mock_player.status = PlayerStatus.ACTIVE
        mock_climb = 0
        mock_bite = 0
        output = game.checkForSnakesAndLadders(mock_player, mock_climb, mock_bite)
        expected_player_location = [1, 2] 
        expected_climb = 0
        expected_bite = 4
        assert output[0].location == expected_player_location
        assert output[1] == expected_climb
        assert output[2] == expected_bite
    
    def testCheckForSnakesAndLadders2(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': 1, 'MAX': 6}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        mock_player = Player('Anushka')
        mock_player.location = [0, 4]
        mock_player.status = PlayerStatus.ACTIVE
        mock_climb = 0
        mock_bite = 0
        output = game.checkForSnakesAndLadders(mock_player, mock_climb, mock_bite)
        expected_player_location = [0, 4] 
        expected_climb = 0
        expected_bite = 0
        assert output[0].location == expected_player_location
        assert output[1] == expected_climb
        assert output[2] == expected_bite

    def testCheckForSnakesAndLadders3(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': 1, 'MAX': 6}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        mock_player = Player('Anushka')
        mock_player.location = 0
        mock_player.status = PlayerStatus.ACTIVE
        mock_climb = 0
        mock_bite = 0
        with pytest.raises(Exception):
            output = game.checkForSnakesAndLadders(mock_player, mock_climb, mock_bite)

    def testCheckForSnakesAndLadders4(self):
        test_parameters = {'Players': ['Anushka'], 'BoardSize': 5, 'Snakes': [[22, 18], [14, 6]], 'Ladders': [[8, 12], [13, 17]]}
        test_config = {'DICE': {'MIN': 1, 'MAX': 6}, 'LOG_FOLDER_PATH': 'D:\\snake_n_ladder\\backend\\logs'}
        log = mock.Mock(write=lambda a: None)
        game = Game(test_parameters, test_config, log)
        mock_player = Player('Anushka')
        mock_player.location = [3, 2]
        mock_player.status = PlayerStatus.ACTIVE
        mock_climb = 0
        mock_bite = 0
        output = game.checkForSnakesAndLadders(mock_player, mock_climb, mock_bite)
        expected_player_location = [2, 3] 
        expected_climb = 4
        expected_bite = 0
        assert output[0].location == expected_player_location
        assert output[1] == expected_climb
        assert output[2] == expected_bite
        