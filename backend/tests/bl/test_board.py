from unittest import TestCase, mock

import pytest

from bl.board import Board
from bl.player import Player
from constants.game import PlayerStatus

class TestBoardBL(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mock = mock

    def testGetBoardValue1(self):
        test_row = 4
        test_col = -1
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        output = board.getBoardValue(test_row, test_col)
        expected_output = None
        assert expected_output == output

    def testGetBoardValue2(self):
        test_row = '4'
        test_col = '-1'
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        with pytest.raises(Exception):
            output = board.getBoardValue(test_row, test_col)

    def testGetBoardValue3(self):
        test_row = 2
        test_col = 4
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        output = board.getBoardValue(test_row, test_col)
        expected_output = 11
        assert expected_output == output

    def testMove1(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [1, 2]
        mock_steps = 6
        player_output = board.move(mock_player, mock_steps)
        expected_output = [0, 1]
        assert expected_output == player_output.location

    def testMove2(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [0, 4]
        mock_steps = 3
        player_output = board.move(mock_player, mock_steps)
        expected_output = [0, 1]
        assert expected_output == player_output.location

    def testMove3(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_steps = 3
        with pytest.raises(Exception):
            player_output = board.move(mock_player, mock_steps)

    def testMoveLeft1(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [0, 2]
        mock_steps = 2
        player_output = board.moveLeft(mock_player, mock_steps)
        expected_output = [0, 0]
        assert expected_output == player_output.location

    def testMoveLeft2(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [2, 4]
        mock_steps = 5
        player_output = board.moveLeft(mock_player, mock_steps)
        expected_output = [1, 0]
        assert expected_output == player_output.location

    def testMoveLeft3(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [2]
        mock_steps = 5
        with pytest.raises(Exception):
            player_output = board.moveLeft(mock_player, mock_steps)

    def testMoveRight1(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [1, 2]
        mock_steps = 6
        player_output = board.moveRight(mock_player, mock_steps)
        expected_output = [0, 1]
        assert expected_output == player_output.location

    def testMoveRight2(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [3, 0]
        mock_steps = 6
        player_output = board.moveRight(mock_player, mock_steps)
        expected_output = [2, 3]
        assert expected_output == player_output.location

    def testMoveRight3(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [4, 0]
        mock_steps = 2
        player_output = board.moveRight(mock_player, mock_steps)
        expected_output = [4, 2]
        assert expected_output == player_output.location
    
    def testMoveRight4(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [4]
        mock_steps = 2
        with pytest.raises(Exception):
            player_output = board.moveRight(mock_player, mock_steps)

    def testMoveUp1(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [4,0]
        player_output = board.moveUp(mock_player)
        expected_output = [3, 0]
        assert expected_output == player_output.location

    def testMoveUp2(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        mock_player = Player('Anushka')
        mock_player.location = [0,0]
        with pytest.raises(Exception):
            player_output = board.moveUp(mock_player)

    def testInitializeBoard1(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        board_output = board.initializeBoard()
        expected_output = [[25, 24, 23, 22, 21], [16, 17, 18, 19, 20], [15, 14, 13, 12, 11], [6, 7, 8, 9, 10], [5, 4, 3, 2, 1]]
        assert expected_output == board_output
    
    def testInitializeBoard2(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 10, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        board_output = board.initializeBoard()
        expected_output = [[100, 99, 98, 97, 96, 95, 94, 93, 92, 91], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [80, 79, 78, 77, 76, 75, 74, 73, 72, 71], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [60, 59, 58, 57, 56, 55, 54, 53, 52, 51], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [40, 39, 38, 37, 36, 35, 34, 33, 32, 31], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        assert expected_output == board_output

    def testInitializeBoard3(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 20, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        board_output = board.initializeBoard()
        expected_output = [[400, 399, 398, 397, 396, 395, 394, 393, 392, 391, 390, 389, 388, 387, 386, 385, 384, 383, 382, 381], [361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380], [360, 359, 358, 357, 356, 355, 354, 353, 352, 351, 350, 349, 348, 347, 346, 345, 344, 343, 342, 341], [321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340], [320, 319, 318, 317, 316, 315, 314, 313, 312, 311, 310, 309, 308, 307, 306, 305, 304, 303, 302, 301], [281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300], [280, 279, 278, 277, 276, 275, 274, 273, 272, 271, 270, 269, 268, 267, 266, 265, 264, 263, 262, 261], [241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260], [240, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224, 223, 222, 221], [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220], [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181], [161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180], [160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141], [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140], [120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100], [80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
        assert expected_output == board_output
    
    def testInitializeBoard4(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 10, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        board_output = board.initializeBoard()
        expected_output = 10
        assert expected_output == len(board_output)

    def testInitializeBoard5(self):
        test_parameters = {"Players": ["Anushka"], "BoardSize": 20, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        board_output = board.initializeBoard()
        expected_output = 20
        assert expected_output == len(board_output[0])
        
    def testCheckIfMissedSnake1(self):
        test_location = [0, 1]
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        output = board.checkIfMissedSnake(test_location)
        expected_output = True
        assert expected_output == output

    def testCheckIfMissedSnake2(self):
        test_location = [4, -1]
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        output = board.checkIfMissedSnake(test_location)
        expected_output = False
        assert expected_output == output
    
    def testCheckIfMissedSnake3(self):
        test_location = [1, 2]
        test_parameters = {"Players": ["Anushka"], "BoardSize": 5, "Snakes": [[22, 18], [14, 6]], "Ladders": [[8, 12], [13, 17]]}
        board = Board(test_parameters)
        output = board.checkIfMissedSnake(test_location)
        expected_output = False
        assert expected_output == output