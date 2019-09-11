"""File contains the parent class 'Person' for the classes 'Sender', 'Receiver' and 'Hacker'"""

from abc import abstractmethod


class Person:
    """the parent class 'Person' for the classes 'Sender', 'Receiver' and 'Hacker'"""

    _cipher_key = None
    _cipher_algorithm = None

    def __init__(self, cipher_key, cipher_algorithm):
        self._cipher_key = cipher_key
        self._cipher_algorithm = cipher_algorithm

    def set_cipher_key(self, key):
        """Take a guess..."""
        self._cipher_key = key

    def get_cipher_key(self):
        """Take another guess..."""
        return self._cipher_key

    @abstractmethod
    def operate_cipher(self, text):
        """Use cipher_algorithm to either encode or decode message"""
        return text
