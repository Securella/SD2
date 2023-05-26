import unittest
from SDExamination2_piggame import Player


class TestPlayer(unittest.TestCase):

    def test_init(self):
        p = Player("Bob")
        self.assertEqual(p.name, "Bob")
        self.assertEqual(p.score, 0)

    def test_add_score(self):
        p = Player("Bob")
        p.add_score(10)
        self.assertEqual(p.score, 10)
        p.add_score(20)
        self.assertEqual(p.score, 30)

    def test_reset_score(self):
        p = Player("Bob")
        p.add_score(10)
        self.assertEqual(p.score, 10)
        p.reset_score()
        self.assertEqual(p.score, 0)

    def test_add_score_negative(self):
        p = Player("Bob")
        p.add_score(-10)
        self.assertEqual(p.score, -10)

    def test_add_score_zero(self):
        p = Player("Bob")
        p.add_score(0)
        self.assertEqual(p.score, 0)

    def test_add_score_float(self):
        p = Player("Bob")
        p.add_score(10.5)
        self.assertEqual(p.score, 10)

    def test_reset_score_negative(self):
        p = Player("Bob")
        p.add_score(10)
        self.assertEqual(p.score, 10)
        p.reset_score()
        p.add_score(-5)
        self.assertEqual(p.score, -5)

    def test_reset_score_float(self):
        p = Player("Bob")
        p.add_score(10)
        self.assertEqual(p.score, 10)
        p.reset_score()
        p.add_score(5.5)
        self.assertEqual(p.score, 5)

    def test_reset_score_zero(self):
        p = Player("Bob")
        p.add_score(10)
        self.assertEqual(p.score, 10)
        p.reset_score()
        p.add_score(0)
        self.assertEqual(p.score, 0)


if __name__ == '__main__':
    unittest.main()
