"""Contains the class for possible actions"""


class Action:
    """Class for an action that the different players can perform"""

    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"
    action_types = [ROCK, PAPER, SCISSORS]

    def __init__(self, action_type):
        if action_type in self.action_types:
            self.action_type = action_type
        else:
            raise Exception(
                'action_type {} is not in action_types'.format(action_type))

    def __lt__(self, other):
        if self.action_type == self.ROCK:
            if other.actionType == self.PAPER:
                return True
        elif self.action_type == self.PAPER:
            if other.actionType == self.SCISSORS:
                return True
        elif self.action_type == self.SCISSORS:
            if other.actionType == self.ROCK:
                return True
        return False
