"""The general class for the different kinds of RPS players"""

class Player(object):

    def __init__(self, name):
        self.name = name


    def chose_action(self):
        return True

    def receive_result(self):
        return True

    def get_name(self):
        return self.name
