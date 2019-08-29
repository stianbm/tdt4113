"""Holds class that can hold tournaments of single games"""

from single_game import SingleGame
import matplotlib.pyplot


class ManyGames:
    """Class that plays n single games and visualize the result"""

    def __init__(self, player1, player2, number_of_games):
        self.player1 = player1
        self.player2 = player2
        self.number_of_games = number_of_games
        self.x_axis = list(range(1, number_of_games + 1))
        self.player1_points = 0
        self.player1_points_mean = []

    def play_single_game(self):
        """Plays a game using SingleGame, updates player1_points"""
        single_game = SingleGame(self.player1, self.player2)
        player1_points = single_game.execute_game()
        self.player1_points += player1_points

    def play_tournament(self):
        """Plays as many games as requested"""
        i = 1
        while i <= self.number_of_games:
            self.play_single_game()
            self.player1_points_mean.append(self.player1_points / i)
            i += 1
        self.print_plot()

    def print_plot(self):
        """Prints result for player1 using matplot"""
        matplotlib.pyplot.plot(self.x_axis, self.player1_points_mean)
        matplotlib.pyplot.show()
