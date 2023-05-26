#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
from SDExamination2_piggame import Dice


class TestDice(unittest.TestCase):

    @patch('random.randint', return_value=1)
    def test_roll_one(self, mock_randint):
        """Test rolling the dice and getting the value when 1 is rolled"""
        dice = Dice()
        dice.roll()
        self.assertEqual(dice.value, 1)

    @patch('random.randint', return_value=6)
    def test_roll_six(self, mock_randint):
        """Test rolling the dice and getting the value when 6 is rolled"""
        dice = Dice()
        dice.roll()
        self.assertEqual(dice.value, 6)

    @patch('random.randint', return_value=3)
    def test_roll_three(self, mock_randint):
        """Test rolling the dice and getting the value when 3 is rolled"""
        dice = Dice()
        dice.roll()
        self.assertEqual(dice.value, 3)

    @patch('random.randint', return_value=2)
    def test_roll_two(self, mock_randint):
        """Test rolling the dice and getting the value when 2 is rolled"""
        dice = Dice()
        dice.roll()
        self.assertEqual(dice.value, 2)

    @patch('random.randint', return_value=4)
    def test_roll_four(self, mock_randint):
        """Test rolling the dice and getting the value when 4 is rolled"""
        dice = Dice()
        dice.roll()
        self.assertEqual(dice.value, 4)

    @patch('random.randint', return_value=5)
    def test_roll_five(self, mock_randint):
        """Test rolling the dice and getting the value when 5 is rolled"""
        dice = Dice()
        dice.roll()
        self.assertEqual(dice.value, 5)

    @patch('random.randint', return_value=1)
    def test_roll_twice(self, mock_randint):
        """Test rolling the dice twice and getting the value"""
        dice = Dice()
        dice.roll()
        first_roll = dice.value
        dice.roll()
        second_roll = dice.value
        self.assertNotEqual(first_roll, second_roll)

    def test_get_value(self):
        """Test getting the value of the dice after rolling"""
        dice = Dice()
        dice.value = 4
        self.assertEqual(dice.get_value(), 4)

    def test_get_value_before_roll(self):
        """Test getting the value of the dice before rolling"""
        dice = Dice()
        self.assertIsNone(dice.get_value())


if __name__ == '__main__':
    unittest.main()
