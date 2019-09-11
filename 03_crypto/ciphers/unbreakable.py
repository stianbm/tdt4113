"""File contains the Unbreakable encryption algorithm"""
from ciphers.caesar import Caesar
from ciphers.cipher import Cipher


class Unbreakable(Cipher):
    """Use word instead of value to shift character values"""

    def __init__(self):
        self._type = 'UNBREAKABLE'

    def encode(self, text, cipher_key):
        """Use keyword to shift characters by using Caesar"""
        encoded_text = ''
        caesar = Caesar()
        for i in range(0, len(text)):
            encoded_text += caesar.encode(text[i],
                                          ord(cipher_key[(i % len(cipher_key))]))
        return encoded_text

    def decode(self, text, cipher_key):
        """Use the same keyword to shift characters back using Caesar"""
        new_cipher_key = ''
        for character in cipher_key:
            #DUDE BRUK PARANTESER I OPPGAVETEKST PLS
            new_cipher_key += chr(((self._alphabet_size -
                                    ord(character) -
                                    self._alphabet_start) %
                                   self._alphabet_size) +
                                  self._alphabet_start)
        print("New cipher key: ", new_cipher_key)
        return self.encode(text, new_cipher_key)
