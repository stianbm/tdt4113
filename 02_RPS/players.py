"""Contains the different kinds of players"""

import random

from action import Action
from player import Player


class RandomPlayer(Player):
    """Chose action randomly"""

    def __init__(self):
        Player.__init__(self, "random")

    def chose_action(self):
        """Chose an action randomly from the possible"""
        return Action.action_types[random.randint(0, 2)]

    def receive_result(self, value1, value2):
        """Do nothing with given information"""


class SequentialPlayer(Player):
    """Runs through the options in a sequence"""

    def __init__(self):
        Player.__init__(self, "sequential")
        self.iterator = 0

    def chose_action(self):
        """Chose action by going through options in sequence"""
        if self.iterator > 2:
            self.iterator = 0
        else:
            self.iterator += 1
        return Action.action_types[self.iterator]

    def receive_result(self, value1, value2):
        """Do nothing with given information"""

    #TODO