"""The file contains the parent class for different ciphers"""

from abc import abstractmethod


class Cipher:
    """The parent class for the different ciphers holding common attributes and abstract methods"""

    _alphabet_size = 95
    _alphabet_start = 32
    _type = ''

    @abstractmethod
    def encode(self, text, cipher_key):
        """Encode a text string using it's cipher and key and return encoded text"""
        return text

    @abstractmethod
    def decode(self, text, cipher_key):
        """Decode a text string using it's cipher and key and return decoded text"""
        return text

    def verify(self, text, cipher_key):
        """Check if the encoded - then decoded text is the same as original"""
        if text == self.decode(self.encode(text, cipher_key), cipher_key):
            print('VERIFIED')
            return True
        print('NOT VERIFIED')
        return False
