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
        return Action(Action.action_types[random.randint(0, 2)])

    def receive_result(self, action1, action2):
        """Do nothing with given information"""


class SequentialPlayer(Player):
    """Runs through the options in a sequence"""

    def __init__(self):
        Player.__init__(self, "sequential")
        self.iterator = 0

    def chose_action(self):
        """Chose action by going through options in sequence"""
        if self.iterator > 1:
            self.iterator = 0
        else:
            self.iterator += 1
        return Action(Action.action_types[self.iterator])

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
        if action2.action_type == Action.ROCK:
            self.rock_counter += 1
        elif action2.action_type == Action.PAPER:
            self.paper_counter += 1
        elif action2.action_type == Action.SCISSORS:
            self.scissors_counter += 1
        else:
            raise Exception(
                'Invalid action {}'.format(action2.action_type))

    def chose_action(self):
        """Chose action based on most common opponent action"""
        if self.rock_counter > self.paper_counter:
            if self.rock_counter > self.scissors_counter:
                return Action(Action.PAPER)
            return Action(Action.ROCK)
        elif self.paper_counter > self.scissors_counter:
            return Action(Action.SCISSORS)
        return Action(Action.ROCK)


class Historian(Player):
    """Checks if the n last actions by opponents have been used before, if so choose
    counter action for what they didlast time"""

    def __init__(self, action_depth):
        Player.__init__(self, "historian")
        self.action_depth = action_depth
        self.actions = []
        self.all_actions = []

    def receive_result(self, action1, action2):
        """Add last action of opponent to string of actions"""
        self.all_actions.append(action2)
        if len(self.actions) > self.action_depth - 1:
            del self.actions[0]
        self.actions.append(action2)

    def chose_action(self):
        """Chose action based on if n last actions have been made before, and what usually comes after"""

        rock_vote = 0
        paper_vote = 0
        scissors_vote = 0

        # Find instances of last n actions in all actions
        i = 0
        while i < (len(self.all_actions) - (self.action_depth + 1)):
            for j in range(self.action_depth):
                if self.actions[j] == self.all_actions[i]:
                    if j == (self.action_depth - 1):
                        if self.all_actions[i + self.action_depth] == Action.ROCK:
                            paper_vote += 1
                        elif self.all_actions[i + self.action_depth] == Action.PAPER:
                            scissors_vote += 1
                        elif self.all_actions[i + self.action_depth] == Action.SCISSORS:
                            rock_vote += 1
                else:
                    break
            i += 1

        # If no instances are found, pick a random
        if rock_vote == 0 and paper_vote == 0 and scissors_vote == 0:
            return Action(Action.action_types[random.randint(0, 2)])

        # Chose most common of previous actions
        else:
            if rock_vote > paper_vote:
                if rock_vote > scissors_vote:
                    return Action(Action.ROCK)
                return Action(Action.SCISSORS)
            elif paper_vote > scissors_vote:
                return Action(Action.PAPER)
            return Action(Action.SCISSORS)
