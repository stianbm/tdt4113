"""File contains the RSA encryption algorithm"""
from random import randint

from ciphers.cipher import Cipher
from crypto_utils import generate_random_prime, modular_inverse, blocks_from_text, text_from_blocks


class RSA(Cipher):
    """Use fancy math to encode and decode"""
    _n_bits = 8
    _block_length = 1
    _byte_size = 8

    def __init__(self):
        self._type = 'RSA'

    def encode(self, text, cipher_key):
        """Use blocks_from_text to make ints and decode them"""
        blocked_text = blocks_from_text(text, self._block_length)
        print('Blocked text: ', blocked_text)
        encoded_text = ''
        encoded_blocks = []
        for block in blocked_text:
            encoded_text += str(self.encode_int(block, cipher_key))
            encoded_blocks.append(self.encode_int(block, cipher_key))
        return encoded_blocks

    def decode(self, text, cipher_key):
        """Decode blocks and use text_from_blocks to fuse them together"""
        decoded_blocks = []
        for block in text:
            decoded_blocks.append(self.decode_int(block, cipher_key))
        return text_from_blocks(decoded_blocks, self._block_length * self._byte_size)

    def generate_keys(self):
        """Generate encryption keys"""
        prime1 = generate_random_prime(self._n_bits)
        while True:
            prime2 = generate_random_prime(self._n_bits)
            if prime1 != prime2:
                break
        print('Primes: ', prime1, ', ', prime2)

        prime_product = prime1 * prime2
        phi = (prime1 - 1) * (prime2 - 1)

        while True:
            random_int = randint(3, (phi - 1))
            inverse = modular_inverse(random_int, phi)
            if inverse:
                break

        return (prime_product, random_int), (prime_product, inverse)

    @staticmethod
    def encode_int(number, public_key):
        """Encodes an integer by using the public key"""
        return pow(number, public_key[1], public_key[0])

    @staticmethod
    def decode_int(number, private_key):
        """Decodes an integer by using the private key"""
        return pow(number, private_key[1], private_key[0])

    def verify(self, text, cipher_key):
        """Overload super method because cipher_key is tuple"""
        print('Type: ', self._type)
        print('Text: ', text)
        encoded = self.encode(text, cipher_key[0])
        print('Encoded: ', encoded)
        decoded = self.decode(encoded, cipher_key[1])
        print('Decoded: ', decoded)
        if text == decoded:
            print('VERIFIED')
            print()
            return True
        print('NOT VERIFIED')
        print()
        return False
