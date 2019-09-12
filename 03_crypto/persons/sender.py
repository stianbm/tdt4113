"""File contains Sender class inheriting from Person"""

from persons.person import Person


class Sender(Person):
    """The Person who encodes and sends the message"""

    def __init__(self, cipher_key, cipher_algorithm):
        super().__init__(cipher_key, cipher_algorithm)
        self._type = 'Sender'

    def operate_cipher(self, text):
        """Call the encode method of the algorithm"""
        encoded = self._cipher_algorithm.encode(text, self._cipher_key)
        print('Encoded from sender: ', encoded)
        return encoded
