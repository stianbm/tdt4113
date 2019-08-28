"""Contains the class for possible actions"""


class Action:
    """Class for an action that the different players can perform"""

    _ROCK = "ROCK"
    _PAPER = "PAPER"
    _SCISSORS = "SCISSORS"
    action_types = [_ROCK, _PAPER, _SCISSORS]

    def __init__(self, action_type):
        if action_type in self.action_types:
            self.action_type = action_type
        else:
            raise Exception(
                'action_type {} is not in action_types'.format(action_type))

    def __lt__(self, other):
        if self.action_type == self._ROCK:
            if other.actionType == self._PAPER:
                return True
        elif self.action_type == self._PAPER:
            if other.actionType == self._SCISSORS:
                return True
        elif self.action_type == self._SCISSORS:
            if other.actionType == self._ROCK:
                return True
        return False
