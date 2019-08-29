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

    def receive_result(self, action1, action2):
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

    def receive_result(self, action1, action2):
        """Do nothing with given information"""


class MostCommon(Player):
    """Chose action based on most used action made by opponent"""

    def __init__(self):
        Player.__init__(self, "most common")
        self.rock_counter = 0
        self.paper_counter = 0
        self.scissors_counter = 0

    def receive_result(self, action1, action2):
        """Add opponents action to memory"""
        if action2 == Action.ROCK:
            self.rock_counter += 1
        elif action2 == Action.PAPER:
            self.paper_counter += 1
        elif action2 == Action.SCISSORS:
            self.scissors_counter += 1
        else:
            raise Exception(
                'Invalid action {}'.format(action2))

    def chose_action(self):
        """Chose action based on most common opponent action"""
        if self.rock_counter > self.paper_counter:
            if self.rock_counter > self.scissors_counter:
                return Action.PAPER
            return Action.ROCK
        elif self.paper_counter > self.scissors_counter:
            return Action.SCISSORS
        return Action.ROCK


class Historian(Player):
    """Checks if the n last actions by opponents have been used before, if so choose counter action for what they did last time"""

    def __init__(self, action_depth):
        Player.__init__(self, "historian")
        self.action_depth = action_depth
        self.actions = []
        self.all_actions = []

    def receive_result(self, action1, action2):
        """Add last action of opponent to string of actions"""
        self.all_actions.append(action2)
        self.actions.pop()
        self.actions.append(action2)

    def chose_action(self):
        """Chose action based on if n last actions have been made before, and what usually comes after"""
        pass
        #TODO
