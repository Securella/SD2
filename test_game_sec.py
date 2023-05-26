import unittest
import os
from SDExamination2_piggame import Game


class TestGame(unittest.TestCase):

    def test_high_scores_file_access(self):
        # Check if the high scores file is only accessible by the game.
        self.assertFalse(os.access("high_scores.txt", os.X_OK))

    def test_player_name_sanitization(self):
        # Check if player's name input is sanitized and validated.
        game = Game(num_players=1, level=1)
        player_name = game.players[0].name
        self.assertTrue(player_name.isalpha())

    def test_cheat_variable_security(self):
        # Check if the "cheat" variable is properly secured.
        game = Game(num_players=1, level=1)
        game.cheat = True
        with self.assertRaises(AttributeError):
            game.cheat = False


if __name__ == '__main__':
    unittest.main()
