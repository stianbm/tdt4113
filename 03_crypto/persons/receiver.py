"""File contains Receiver class inheriting from Person"""

from persons.person import Person


class Receiver(Person):
    """The person who receives and decodes the message"""

    def __init__(self, cipher_key, cipher_algorithm):
        super().__init__(cipher_key, cipher_algorithm)
        self.type = 'sender'

    def operate_cipher(self, text):
        """Call the decode method of the algorithm"""
        return self._cipher_algorithm.decode(text, self._cipher_key)
