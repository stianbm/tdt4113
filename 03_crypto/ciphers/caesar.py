"""File that contains the Caesar encryption class"""

from ciphers.cipher import Cipher


class Caesar(Cipher):
    """Shifts all characters the value of cipher_key, which can be negative"""

    def __init__(self):
        self._type = 'CAESAR'

    def encode(self, text, cipher_key):
        """Shift all characters in text"""
        encoded_text = ''
        for character in text:
            encoded_text += (chr(((ord(character) -
                                   self._alphabet_start +
                                   cipher_key) %
                                  self._alphabet_size) +
                                 self._alphabet_start))
        return encoded_text

    def decode(self, text, cipher_key):
        """Shift all characters back to original place"""
        return self.encode(
            text, (self._alphabet_size - cipher_key) %
            self._alphabet_size)

    def possible_keys(self):
        """Possible keys are range(0, alphabet_length"""
        return [x for x in range(0, self._alphabet_size)]
