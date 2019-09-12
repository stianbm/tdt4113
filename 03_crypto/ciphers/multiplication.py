"""File that contains the multiplication class"""

from random import randint

from ciphers.cipher import Cipher
from crypto_utils import modular_inverse


class Multiplication(Cipher):
    """Multiplies the numeral value of chars and reassigns"""

    def __init__(self):
        self._type = 'MULTIPLICATION'

    def encode(self, text, cipher_key):
        """Multiplies and reassigns characters"""
        encoded_text = ''
        for character in text:
            encoded_text += chr((((ord(character) -
                                   self._alphabet_start) *
                                  cipher_key) %
                                 self._alphabet_size) +
                                self._alphabet_start)
        return encoded_text

    def decode(self, text, cipher_key):
        """Shifts characters back to original place"""
        return self.encode(
            text, modular_inverse(
                cipher_key, self._alphabet_size))

    def generate_keys(self):
        """Generate valid keys"""
        while True:
            contestant = randint(0, self._alphabet_size)
            if modular_inverse(contestant, self._alphabet_size):
                break
        print("Key: ", contestant)
        return contestant

    def possible_keys(self):
        """Probably not necessary to use more than size of alphabet"""
        return [x for x in range(0, self._alphabet_size)]
