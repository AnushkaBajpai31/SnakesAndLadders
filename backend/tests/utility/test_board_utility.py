from unittest import TestCase, mock

from utility.board import BoardUtility

class TestBoardUtility(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mock = mock

    def testGetBoardDict(self):
        mocked_ref_dict = {'boardDict': {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3, 0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}}
        board_util = BoardUtility(mocked_ref_dict)
        output = board_util.getBoardDict()
        expected_output = { 25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3, 0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4] }
        assert expected_output == output

    def testGetDistanceDict(self):
        mocked_ref_dict = {'boardDict': {25: [0, 0], 24: [0, 1], 23: [0, 2], 22: [0, 3], 21: [0, 4], 20: [1, 4], 19: [1, 3], 18: [1, 2], 17: [1, 1], 16: [1, 0], 15: [2, 0], 14: [2, 1], 13: [2, 2], 12: [2, 3], 11: [2, 4], 10: [3, 4], 9: [3, 3], 8: [3, 2], 7: [3, 1], 6: [3, 0], 5: [4, 0], 4: [4, 1], 3: [4, 2], 2: [4, 3], 1: [4, 4]}}
        board_util = BoardUtility(mocked_ref_dict)
        output = board_util.getDistanceDict()
        expected_output = { (0, 0): 25, (0, 1): 24, (0, 2): 23, (0, 3): 22, (0, 4): 21, (1, 4): 20, (1, 3): 19, (1, 2): 18, (1, 1): 17, (1, 0): 16, (2, 0): 15, (2, 1): 14, (2, 2): 13, (2, 3): 12, (2, 4): 11, (3, 4): 10, (3, 3): 9, (3, 2): 8, (3, 1): 7, (3, 0): 6, (4, 0): 5, (4, 1): 4, (4, 2): 3, (4, 3): 2, (4, 4): 1 }
        assert expected_output == output