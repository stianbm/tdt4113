"""The main file that starts it all..."""

from many_games import ManyGames
from players import *


def main():
    """Main method used to call the other classes"""
    """
    player1 = Historian(2)
    player2 = MostCommon()
    game = ManyGames(player1, player2, 100)
    game.play_tournament()
    """
    menu()


def menu():
    players = [RandomPlayer(), SequentialPlayer(), MostCommon]
    print("WELCOME! Chose player 1")
    print_players()
    i = input()
    player1 = chose_player(i)
    print("Chose player 2")
    print_players()
    i = input()
    player2 = chose_player(i)
    print("Chose number of games")
    i = input()
    game = ManyGames(player1, player2, int(i))
    game.play_tournament()


def print_players():
    print("1 - Random")
    print("2 - Sequential")
    print("3 - Most common")
    print("4 - Historian")


def chose_player(choice):
    if choice == '1':
        return RandomPlayer()
    elif choice == '2':
        return SequentialPlayer()
    elif choice == '3':
        return MostCommon()
    elif choice == '4':
        print("Chose level")
        i = input()
        return Historian(int(i))


if __name__ == "__main__":
    main()
