import random
import time


class Dice: 
    """The dice itself"""
    def __init__(self):
        """The dice self"""
        self.value = None

    def roll(self):
        """Defines rolling the dice"""
        self.value = random.randint(1, 6)


class DiceHand:
    """The dices that are thrown"""
    def __init__(self):
        """the dices that will be thrown"""
        self.dice1 = Dice()
        self.dice2 = Dice()

    def roll(self):
        "method for throwing them all at once"
        self.dice1.roll()
        self.dice2.roll()

    def get_value(self):
        """Returning value of the throw"""
        return self.dice1.value + self.dice2.value


class Player:
    """Class for the players"""
    def __init__(self, name):
        """the person info like name and score"""
        self.name = name
        self.score = 0

    def add_score(self, points):
        """adding score to the total"""
        self.score += points

    def reset_score(self):
        """Reseting score back to 0"""
        self.score = 0


class Intelligence:
    """Class for the AI"""
    def __init__(self, name="Jarvan"):
        """attributes of the AI"""
        self.name = name
        self.score = 0

    def add_score(self, points):
        """Adding AI's points"""
        self.score += points

    def reset_score(self):
        """Reseting score back to 0"""
        self.score = 0

    def rolls(self, turn_score, level=1):
        """AIs decision of rolling or passing"""
        time.sleep(1)
        if level == 1:
            if turn_score >= 2:
                return "h"
            else:
                return "r"
        elif level == 2:
            if turn_score >= 6:
                return "h"
            else:
                return "r"
        elif level == 3:
            if turn_score >= 8:
                return "h"
            else:
                return "r"
        elif level == 4:
            if turn_score >= 12:
                return "h"
            else:
                return "r"


class Game:
    """The main game itself"""
    def __init__(self, num_players=1, level=1):
        """Deciding players and their names and initiating their scores and
            all other info like attributes for whose turn it is"""
        self.players = []
        self.level = level
        for i in range(num_players):
            name = input(f"Enter the name of player {i + 1}: ")
            self.players.append(Player(name))
        if num_players == 1:
            if name == "Jarvis":
                self.players.append(Intelligence('Max'))
            else:
                self.players.append(Intelligence('Jarvis'))
        self.high_scores = {}
        self.load_high_scores()
        self.current_player = 0
        self.current_score = 0
        self.winner = None
        self.cheat = False

    def load_high_scores(self):
        """method for loading previous highscores"""
        try:
            with open("high_scores.txt", "r") as file:
                for line in file:
                    name, score = line.strip().split(",")
                    self.high_scores[name] = int(score)
        except FileNotFoundError:
            pass

    def save_high_scores(self):
        """method for saving new highscores"""
        with open("high_scores.txt", "w") as file:
            for name, score in self.high_scores.items():
                file.write(f"{name},{score}\n")

    def play(self):
        """The gameplay itself"""
        while not self.winner:
            player = self.players[self.current_player]
            print(f"It's {player.name}'s turn!")
            self.current_score = 0
            while True:
                if self.cheat:
                    self.current_score += 20

                if isinstance(player, Player): 
                    choice2 = input("Roll (r) or hold (h)? ")
                elif isinstance(player, Intelligence):
                    choice2 = Intelligence.rolls(self, self.current_score, self.level)
                if choice2.lower() == "r":
                    hand = DiceHand()
                    hand.roll()
                    if isinstance(player, Player):
                        print(f"You rolled a {hand.get_value()}!")
                    elif isinstance(player, Intelligence):
                        print(f"I rolled a {hand.get_value()}!")
                    if hand.get_value() == 2:
                        self.current_score = 0
                        print(f"{player.name} rolled snake eyes! Your turn is over.")
                        break
                    elif hand.dice1.value == 1 or hand.dice2.value == 1:
                        print(f"{player.name} rolled a 1. Your turn is over.")
                        break
                    else:
                        self.current_score += hand.get_value()
                        if self.current_score + player.score >= 100:
                            self.winner = player
                            break
                    if isinstance(player, Player):
                        print(f"Your turn score is {self.current_score}. Your total score is {player.score}.")
                    if isinstance(player, Intelligence):
                        print(f"My turn score is {self.current_score}. My total score is {player.score}.")

                elif choice2.lower() == "h":
                    if isinstance(player, Player):
                        print(f"Your total score is {player.score + self.current_score}.")
                    elif isinstance(player, Intelligence):
                        print(f"I hold, my total score is {player.score + self.current_score}")
                    player.add_score(self.current_score)
                    self.current_score = 0
                    break
                else:
                    print("Invalid choice. Please try again.")
            if not self.winner:
                self.current_player = (self.current_player + 1) % len(self.players)

        print(f"{self.winner.name} wins with a score of {self.winner.score}!")
        self.update_high_scores(self.winner)

    def update_high_scores(self, player):
        """Method for updating scores"""
        if player.name in self.high_scores:
            if player.score > self.high_scores[player.name]:
                self.high_scores[player.name] = player.score
                print("New high score!")
        else:
            self.high_scores[player.name] = player.score
            print("New high score!")
        self.save_high_scores()

    def print_high_scores(self):
        """Method for printing the scores"""
        print("High scores:")
        for name, score in sorted(self.high_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{name}: {score}")

    def set_computer_intelligence(self, level):
        """Setting the difficulty of AI"""
        self.level = level

    def toggle_cheat(self):
        """Gives cheats"""

        if self.cheat is False:
            print("You turned on cheats, you will get extra 20 points every round")
            self.cheat = True

        elif self.cheat is True:
            print("you turned off cheats")
            self.cheat = False

    def reset_game(self):
        """Method for reseting the game"""
        self.current_player = 0
        self.current_score = 0
        self.winner = None
        for player in self.players:
            player.reset_score()

    def print_rules(self):
        """Method for printing the rules of the game"""
        print("Welcome to Pig!")
        print("The goal of the game is to be the first player to reach 100 points.")
        print("On each turn, you can roll the dice as many times as you like.")
        print("Each roll adds to your turn score, but if you roll a 1, your turn is over and you score nothing.")
        print("If you roll snake eyes (two ones), your turn is over and you lose all your points for the round.")
        print("You can choose to hold at any time, which adds your turn score to your total score.")
        print("The computer will play with a configurable level of intelligence.")


if __name__ == "__main__":
    players_num = int(input("Hello, write Number of players and go to main menu: "))
    game = Game(num_players=players_num, level=1)
    game.print_rules()
    while True:
        choice = input("Enter choice (p)lay, set (i)ntelligence level, (t)oggle cheat, (r)eset game, (s)ee high scores, (q)uit: ")
        if choice.lower() == "p":
            game.play() 
        elif choice.lower() == "i":
            level = int(input("Enter intelligence level (1-4): "))
            game.set_computer_intelligence(level)
        elif choice.lower() == "t":
            game.toggle_cheat()
        elif choice.lower() == "r":
            game.reset_game()
        elif choice.lower() == "s":
            game.print_high_scores()
        elif choice.lower() == "q":
            break
        else:
            print("Invalid choice. Please try again.")
