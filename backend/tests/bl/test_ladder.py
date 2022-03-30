from unittest import TestCase, mock

import pytest

from bl.ladder import Ladder

class TestLadderBL(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mock = mock

    def testInitializeLadder1(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_ladder_list = [[8, 12], [13, 17]]
        expected_output = {(3, 2): (2, 3), (2, 2): (1, 1)}
        ladder = Ladder(test_ladder_list, board_utility)
        output = ladder.initializeLadders(test_ladder_list)
        assert output == expected_output
    
    def testInitializeLadder2(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_ladder_list = [[18, 12], [13, 17]]
        with pytest.raises(Exception):
            ladder = Ladder(test_ladder_list, board_utility)
    
    def testInitializeLadder3(self):
        board_utility = mock.Mock(getBoardDict=lambda: None)
        test_ladder_list = [[8, 12], [13, 17]]
        with pytest.raises(Exception):
            ladder = Ladder(test_ladder_list, board_utility)

    def testCheckIfLadder1(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_ladder_list = [[8, 12], [13, 17]]
        ladder = Ladder(test_ladder_list, board_utility)
        test_location = [4, -1]
        expected_output = False
        output = ladder.checkIfLadder(test_location)
        assert expected_output == output

    def testCheckIfLadder2(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_ladder_list = [[8, 12], [13, 17]]
        ladder = Ladder(test_ladder_list, board_utility)
        test_location = [3, 2]
        expected_output = True
        output = ladder.checkIfLadder(test_location)
        assert expected_output == output

    def testCheckIfLadder3(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict)
        test_ladder_list = [[8, 12], [13, 17]]
        ladder = Ladder(test_ladder_list, board_utility)
        test_location = 0
        with pytest.raises(Exception):
            output = ladder.checkIfLadder(test_location)

    def testClimb1(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict, 
        getDistanceDict=lambda: mocked_distance_dict)
        test_ladder_list = [[8, 12], [13, 17]]
        ladder = Ladder(test_ladder_list, board_utility)

        mocked_distance_dict = {(0, 0): 25, (0, 1): 24, (0, 2): 23, (0, 3): 22, (0, 4): 21, (1, 4): 20, (1, 3): 19, (1, 2): 18, (1, 1): 17, (1, 0): 16, (2, 0): 15, (2, 1): 14, (2, 2): 13, (2, 3): 12, (2, 4): 11, (3, 4): 10, (3, 3): 9, (3, 2): 8, (3, 1): 7, (3, 0): 6, (4, 0): 5, (4, 1): 4, (4, 2): 3, (4, 3): 2, (4, 4): 1}
        test_location = [2, 2]
        expected_output = [1, 1], 4
        output = ladder.climb(test_location)
        assert output == expected_output

    def testClimb2(self):
        mocked_board_dict = {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3,0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}
        board_utility = mock.Mock(getBoardDict=lambda: mocked_board_dict, 
        getDistanceDict=lambda: mocked_distance_dict)
        test_ladder_list = [[8, 12], [13, 17]]
        ladder = Ladder(test_ladder_list, board_utility)

        mocked_distance_dict = {(0, 0): 25, (0, 1): 24, (0, 2): 23, (0, 3): 22, (0, 4): 21, (1, 4): 20, (1, 3): 19, (1, 2): 18, (1, 1): 17, (1, 0): 16, (2, 0): 15, (2, 1): 14, (2, 2): 13, (2, 3): 12, (2, 4): 11, (3, 4): 10, (3, 3): 9, (3, 2): 8, (3, 1): 7, (3, 0): 6, (4, 0): 5, (4, 1): 4, (4, 2): 3, (4, 3): 2, (4, 4): 1}
        test_location = [0, 0]
        with pytest.raises(Exception):
            output = ladder.climb(test_location)