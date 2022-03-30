from unittest import TestCase, mock

import pytest

from bl.snake import Snake

class TestSnakeBL(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mock = mock

    def testInitializeSnake1(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_snake_list = [[22, 18], [14, 6]]
        expected_output = {(0, 3): (1, 2), (2, 1): (3, 0)}
        snake = Snake(test_snake_list, board_utility)
        output = snake.initializeSnakes(test_snake_list)
        assert output == expected_output

    def testInitializeSnake2(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_snake_list = [[2, 18], [14, 6]]
        with pytest.raises(Exception):
            snake = Snake(test_snake_list, board_utility)
    
    def testInitializeSnake3(self):
        board_utility = mock.Mock(getBoardDict=lambda: None)
        test_snake_list = [[22, 18], [14, 6]]
        with pytest.raises(Exception):
            snake = Snake(test_snake_list, board_utility)

    def testCheckIfSnake1(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_snake_list = [[22, 18], [14, 6]]
        snake = Snake(test_snake_list, board_utility)
        test_location = [4, -1]
        expected_output = False
        output = snake.checkIfSnake(test_location)
        assert expected_output == output

    def testCheckIfSnake2(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_snake_list = [[22, 18], [14, 6]]
        snake = Snake(test_snake_list, board_utility)
        test_location = [0, 3]
        expected_output = True
        output = snake.checkIfSnake(test_location)
        assert expected_output == output

    def testCheckIfSnake3(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_snake_list = [[22, 18], [14, 6]]
        snake = Snake(test_snake_list, board_utility)
        test_location = 0
        with pytest.raises(Exception):
            output = snake.checkIfSnake(test_location)

    def testBite1(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        mocked_distance_dict = {(0, 0): 25, (0, 1): 24, (0, 2): 23, (0, 3): 22, (0, 4): 21, (1, 4): 20, (1, 3): 19, (1, 2): 18, (1, 1): 17, (1, 0): 16, (2, 0): 15, (2, 1): 14, (2, 2): 13, (2, 3): 12, (2, 4): 11, (3, 4): 10, (3, 3): 9, (3, 2): 8, (3, 1): 7, (3, 0): 6, (4, 0): 5, (4, 1): 4, (4, 2): 3, (4, 3): 2, (4, 4): 1}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict, 
        getDistanceDict=lambda: mocked_distance_dict)
        test_snake_list = [[22, 18], [14, 6]]
        snake = Snake(test_snake_list, board_utility)
        test_location = [0, 3]
        expected_output = [1, 2], 4
        output = snake.bite(test_location)
        assert output == expected_output

    def testBite2(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        mocked_distance_dict = {(0, 0): 25, (0, 1): 24, (0, 2): 23, (0, 3): 22, (0, 4): 21, (1, 4): 20, (1, 3): 19, (1, 2): 18, (1, 1): 17, (1, 0): 16, (2, 0): 15, (2, 1): 14, (2, 2): 13, (2, 3): 12, (2, 4): 11, (3, 4): 10, (3, 3): 9, (3, 2): 8, (3, 1): 7, (3, 0): 6, (4, 0): 5, (4, 1): 4, (4, 2): 3, (4, 3): 2, (4, 4): 1}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict, 
        getDistanceDict=lambda: mocked_distance_dict)
        test_snake_list = [[22, 18], [14, 6]]
        snake = Snake(test_snake_list, board_utility)
        test_location = [1, 4]
        with pytest.raises(Exception):
            output = snake.bite(test_location)

    def testCheckIfMissedSnake1(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_snake_list = [[22, 18], [14, 6]]
        snake = Snake(test_snake_list, board_utility)
        output = snake.checkIfMissedSnake(21)
        expected_output = True
        assert expected_output == output
    
    def testCheckIfMissedSnake2(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_snake_list = [[22, 18], [14, 6]]
        snake = Snake(test_snake_list, board_utility)
        output = snake.checkIfMissedSnake(10)
        expected_output = False
        assert expected_output == output