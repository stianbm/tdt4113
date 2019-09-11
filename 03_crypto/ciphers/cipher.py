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
        print('Text: ', text)
        encoded = self.encode(text, cipher_key)
        print('Encoded: ', encoded)
        decoded = self.decode(encoded, cipher_key)
        print('Decoded: ', decoded)
        if text == decoded:
            print('VERIFIED')
            print()
            return True
        print('NOT VERIFIED')
        print()
        return False
