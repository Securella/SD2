import unittest
from unittest.mock import patch
from SDExamination2_piggame import Game, Player


class TestGame(unittest.TestCase):
    """Unit tests for the Game class"""

    def test_start_game(self):
        """
        Test that the start_game method sets the game status to running.
        The start_game method should set the game status to running,
        indicating that the game is in progress.
        """
        game = Game()
        game.start_game()
        self.assertTrue(game.is_game_running())

    def test_end_game(self):
        """
        Test that the end_game method sets the game status to not running.
        The end_game method should set the game status to not running,
        indicating that the game is over.
        """
        game = Game()
        game.start_game()
        game.end_game()
        self.assertFalse(game.is_game_running())

    def test_add_player(self):
        """
        Test that the add_player method adds a player to the game.
        The add_player method should add a Player object to
        the game's list of players.
        This test will create a new player and add them to the game,
        then check that the player is in the game's list of players.
        """
        game = Game()
        player = Player("Jussi")
        game.add_player(player)
        self.assertIn(player, game.players)

    def test_remove_player(self):
        """
        Test that the remove_player method removes a player from the game.
        The remove_player method should remove a Player object from
        the game's list of players.
        This test will create a new player, add them to the game,
        remove them from the game, and then check that they are not
        in the game's list of players.
        """
        game = Game()
        player = Player("Pekka")
        game.add_player(player)
        game.remove_player(player)
        self.assertNotIn(player, game.players)

    @patch.object(Game, '_get_next_player')
    def test_play_round(self, mock_get_next_player):
        """
        Test that the play_round method advances the game to the next player.
        The play_round method should advance the game to the next player
        by calling the
        _get_next_player method. This test will mock the _get_next_player
        method and
        verify that it is called when the play_round method is called.
        """
        game = Game()
        player1 = Player("Jussi")
        player2 = Player("Pekka")
        game.add_player(player1)
        game.add_player(player2)
        game.start_game()
        mock_get_next_player.side_effect = [player2, player1]
        game.play_round()
        self.assertEqual(game.current_player, player2)
        game.play_round()
        self.assertEqual(game.current_player, player1)

    def test_get_winner(self):
        """
        Test that the get_winner method returns the player with
        the highest score.
        The get_winner method should return the Player object with
        the highest score.
        This test will create two players with different scores,
        add them to the game,
        and verify that the get_winner method returns the correct player.
        """
        game = Game()
        player1 = Player("Jussi")
        player2 = Player("Pekka")
        player1.score = 20
        player2.score = 30
        game.add_player(player1)
        game.add_player(player2)
        winner = game.get_winner()
        self.assertEqual(winner, player2)

    def test_is_game_over_returns_false_when_no_winner(self):
        """
        Test that the is_game_over method returns False when no winner
        has been reached.
        The is_game_over method should return False when
        no player's score reaches the
        winning score. This test will create a player with a score
        below the winning score,
        add them to the game, and verify that the is_game_over method
        returns False.
        """
        game = Game()
        player = Player("Pekka")
        player.score = game.WINNING_SCORE - 1
        game.add_player(player)
        self.assertFalse(game.is_game_over())

    def test_reset_game(self):
        """
        Test that the reset_game method resets the game.
        The reset_game method should reset the game's status, players,
        and scores.
        This test will create a game with players and scores, reset the game,
        and verify that the game's status, players, and scores have been reset.
        """
        game = Game()
        player1 = Player("Jussi")
        player2 = Player("Pekka")
        player1.score = 10
        player2.score = 20
        game.add_player(player1)
        game.add_player(player2)
        game.reset_game()
        self.assertFalse(game.is_game_running())
        self.assertEqual(len(game.players), 0)
        self.assertEqual(player1.score, 0)
        self.assertEqual(player2.score, 0)


if __name__ == '__main__':
    unittest.main()
