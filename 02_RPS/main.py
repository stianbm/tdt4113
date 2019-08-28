"""The main file that starts it all..."""

from single_game import SingleGame
from players import RandomPlayer


def main():
    """Main method used to call the other classes"""
    print("START")

    player1 = RandomPlayer()
    player2 = RandomPlayer()
    game = SingleGame(player1, player2)
    game.execute_game()


if __name__ == "__main__":
    main()
