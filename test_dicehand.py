import unittest
from unittest.mock import patch
from SDExamination2_piggame import Dice, DiceHand


class TestDiceHand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dicehand = DiceHand()

    def test_dicehand_has_two_dice(self):
        self.assertIsInstance(self.dicehand.dice1, Dice)
        self.assertIsInstance(self.dicehand.dice2, Dice)

    @patch.object(Dice, 'roll')
    def test_dicehand_roll_calls_roll_on_both_dice(self, mock_roll):
        # Test if roll method of both dice is called once
        self.dicehand.roll()
        mock_roll.assert_called_once_with()
        self.assertEqual(mock_roll.call_count, 2)

    def test_dicehand_get_value_returns_sum_of_dice_values(self):
        # Test get_value method returns sum of values of both dice
        self.dicehand.dice1.value = 2
        self.dicehand.dice2.value = 3
        self.assertEqual(self.dicehand.get_value(), 5)

    def test_dicehand_roll_sets_value_of_both_dice(self):
        # Test roll method sets value of both dice
        self.dicehand.roll()
        self.assertIsNotNone(self.dicehand.dice1.value)
        self.assertIsNotNone(self.dicehand.dice2.value)

    @patch.object(Dice, 'roll')
    def test_dicehand_roll_resets_value_of_both_dice(self, mock_roll):
        # Test roll method resets value of both dice
        self.dicehand.dice1.value = 2
        self.dicehand.dice2.value = 3
        self.dicehand.roll()
        self.assertIsNone(self.dicehand.dice1.value)
        self.assertIsNone(self.dicehand.dice2.value)

    @patch.object(Dice, 'roll')
    def test_dicehand_roll_updates_value_of_both_dice(self, mock_roll):
        # Test roll method updates value of both dice
        mock_roll.side_effect = [2, 3]
        self.dicehand.roll()
        self.assertEqual(self.dicehand.dice1.value, 2)
        self.assertEqual(self.dicehand.dice2.value, 3)

    def test_dicehand_get_value_returns_none_when_one_dice_value_is_none(self):
        # Test get_value method returns None when one of the dice values
        # is None (don't know if it's gonna work)
        self.dicehand.dice1.value = 2
        self.assertIsNone(self.dicehand.get_value())

    def test_dicehand_get_value_returns_none_when_both_dice_values_are_none(self):
        # Test get_value method returns None when both dice values are None
        self.assertIsNone(self.dicehand.get_value())

    def test_dicehand_roll_returns_tuple_of_both_dice_values(self):
        # Test roll method returns a tuple of both dice values
        self.dicehand.dice1.value = 2
        self.dicehand.dice2.value = 3
        self.assertEqual(self.dicehand.roll(), (2, 3))

    def test_dicehand_roll_returns_none_when_one_dice_value_is_none(self):
        # Test roll method returns None when one of the dice values is None
        self.dicehand.dice1.value = 2
        self.assertIsNone(self.dicehand.roll())

    def test_dicehand_roll_returns_none_when_both_dice_values_are_none(self):
        # Test roll method returns None when both dice values are None
        self.assertIsNone(self.dicehand.roll())


if __name__ == '__main__':
    unittest.main()
