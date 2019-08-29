"""The main file that starts it all..."""

from many_games import ManyGames
from players import *


def main():
    """Main method used to call the other classes"""
    print("START")

    player1 = MostCommon()
    player2 = RandomPlayer()
    game = ManyGames(player1, player2, 100)
    game.play_tournament()

def menu():
    pass
    #TODO


if __name__ == "__main__":
    main()
