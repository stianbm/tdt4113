"""The general class for the different kinds of RPS players"""

from abc import abstractmethod


class Player:
    """Parent class for players with abstract methods that must be implemented"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def chose_action(self):
        """Chose the action, possibly based on history"""

    @abstractmethod
    def receive_result(self, value1, value2):
        """Receive result of game, possibly commit to memory"""

    def get_name(self):
        """get_name"""
        return self.name
