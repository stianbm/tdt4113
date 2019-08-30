"""Contains the class for running a single game"""


class SingleGame:
    """Execute and represent a single game"""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.action1 = None
        self.action2 = None
        self.winner = None

    def execute_game(self):
        """Plays through one game and feeds the result back to the players"""
        self.action1 = self.player1.chose_action()
        self.action2 = self.player2.chose_action()

        value1 = 0
        value2 = 0

        if self.action1 < self.action2:
            value2 += 1
            self.winner = self.player2.get_name()
        elif self.action2 < self.action1:
            value1 += 1
            self.winner = self.player1.get_name()
        else:
            value1 += 0.5
            value2 += 0.5
            self.winner = "no-one"

        self.player1.receive_result(self.action1, self.action2)
        self.player2.receive_result(self.action2, self.action1)

        self.__str__()

        return value1

    def __str__(self):
        """Represents the single game as text"""
        print(
            self.player1.get_name() +
            ": " +
            self.action1.action_type +
            ".  " +
            self.player2.get_name() +
            ": " +
            self.action2.action_type +
            ".  " +
            self.winner +
            " wins")
