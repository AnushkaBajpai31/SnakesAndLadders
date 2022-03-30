from unittest import TestCase, mock

import pytest

from bl.dice import Dice
from constants.errors import Error

class TestDice(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mock = mock

    def testRoll1(self):
        config = {'MIN': 1, 'MAX': 6}
        test_outputs = [1, 2, 3, 4, 5, 6]
        dice = Dice(config)
        output = dice.roll()
        assert output in test_outputs
    
    def testRoll2(self):
        config = {'MIN': 0, 'MAX': 5}
        test_outputs = [0, 1, 2, 3, 4, 5]
        dice = Dice(config)
        output = dice.roll()
        assert output in test_outputs

    def testRoll3(self):
        config = {'MIN': '0', 'MAX': '5'}
        dice = Dice(config)
        test_output = Error.ROLL_ERROR
        with pytest.raises(Exception) as exception:
            output = dice.roll()
        assert exception.value.args[0] == test_output
        assert str(exception.value) == test_output