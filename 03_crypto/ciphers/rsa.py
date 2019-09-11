"""File contains the RSA encryption algorithm"""
from random import randint

from ciphers.cipher import Cipher
from crypto_utils import generate_random_prime, modular_inverse


class RSA(Cipher):
    """Use fancy math to encode and decode"""

    def __init__(self):
        self._type = 'RSA'

    def encode(self, text, cipher_key):
        pass

    def decode(self, text, cipher_key):
        pass

    @staticmethod
    def generate_keys():
        """Generate encryption keys"""
        n_bits = 8
        prime1 = generate_random_prime(n_bits)
        while True:
            prime2 = generate_random_prime(n_bits)
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
