import unittest
from SDExamination2_piggame import Intelligence


class TestIntelligence(unittest.TestCase):
    """Unit tests for the Intelligence class"""

    def test_guess(self):
        """
        Test that the guess method returns a value between 1 and 6.

        The guess method should return a random value between
        1 and 6 inclusive, representing the Intelligence's guess
        for the player's roll.
        This test will call the guess method and ensure that
        the value returned is within the expected range.
        """
        intelligence = Intelligence()
        guess = intelligence.guess()
        self.assertGreaterEqual(guess, 1)
        self.assertLessEqual(guess, 6)

    def test_initial_score_is_zero(self):
        """
        Test that the initial score of the Intelligence is zero.
        """
        intelligence = Intelligence()
        self.assertEqual(intelligence.score, 0)

    def test_add_score_increases_score(self):
        """
        Test that the add_score method increases the Intelligence's score
        by the given amount.
        """
        intelligence = Intelligence()
        intelligence.add_score(5)
        self.assertEqual(intelligence.score, 5)

    def test_add_score_negative_value_raises_value_error(self):
        """
        Test that the add_score method raises a ValueError if
        a negative value is passed as argument.
        """
        intelligence = Intelligence()
        with self.assertRaises(ValueError):
            intelligence.add_score(-5)

    def test_add_score_non_integer_value_raises_type_error(self):
        """
        Test that the add_score method raises a TypeError if
        a non-integer value is passed as argument.
        """
        intelligence = Intelligence()
        with self.assertRaises(TypeError):
            intelligence.add_score(5.5)

    def test_reset_score_sets_score_to_zero(self):
        """
        Test that the reset_score method sets the Intelligence's score to zero.
        """
        intelligence = Intelligence()
        intelligence.add_score(5)
        intelligence.reset_score()
        self.assertEqual(intelligence.score, 0)

    def test_set_guess_sets_guess_to_given_value(self):
        """
        Test that the set_guess method sets the Intelligence's guess
        to the given value.
        """
        intelligence = Intelligence()
        intelligence.set_guess(3)
        self.assertEqual(intelligence.guess(), 3)

    def test_set_guess_outside_range_raises_value_error(self):
        """
        Test that the set_guess method raises a ValueError if the given value
        is outside the range of 1-6.
        """
        intelligence = Intelligence()
        with self.assertRaises(ValueError):
            intelligence.set_guess(7)

    def test_set_guess_non_integer_value_raises_type_error(self):
        """
        Test that the set_guess method raises a TypeError if a non-integer
        value is passed as argument.
        """
        intelligence = Intelligence()
        with self.assertRaises(TypeError):
            intelligence.set_guess(3.5)


if __name__ == "__main__":
    unittest.main()
