"""File contains the Affine encryption class"""
from ciphers.caesar import Caesar
from ciphers.cipher import Cipher
from ciphers.multiplication import Multiplication


class Affine(Cipher):
    """Combination of Caesar and Multiplication"""

    def __init__(self):
        self._type = 'AFFINE'

    def encode(self, text, cipher_key):
        """Use Multiplication, then Caesar"""
        multiplication = Multiplication()
        encoded_text = multiplication.encode(text, cipher_key[0])
        print('Multiplied: ', encoded_text)
        caesar = Caesar()
        encoded_text = caesar.encode(encoded_text, cipher_key[1])
        print('Caesared: ', encoded_text)
        return encoded_text

    def decode(self, text, cipher_key):
        """Use decode from Caesar, then Multiplication"""
        caesar = Caesar()
        decoded_text = caesar.decode(text, cipher_key[1])
        print('DeCaesared: ', decoded_text)
        multiplication = Multiplication()
        decoded_text = multiplication.decode(decoded_text, cipher_key[0])
        print('DeMultiplied: ', decoded_text)
        return decoded_text
