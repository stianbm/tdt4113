"""The main file for the project"""

from ciphers.affine import Affine
from ciphers.caesar import Caesar
from ciphers.multiplication import Multiplication
from ciphers.rsa import RSA
from ciphers.unbreakable import Unbreakable


def main():
    """Main function to be run"""
    text = 'PYTHON IS NOT DA BEST'
    key = 15
    caesar = Caesar()
    caesar.verify(text, key)

    multiplication = Multiplication()
    key = multiplication.generate_keys()
    multiplication.verify(text, key)

    affine = Affine()
    key = (multiplication.generate_keys(), 5)
    print('Key: ', key)
    affine.verify(text, key)

    unbreakable = Unbreakable()
    key = 'PIZZA'
    unbreakable.verify(text, key)

    rsa = RSA()
    public_key, private_key = rsa.generate_keys()
    print('Public: ', public_key, ', Private: ', private_key)
    encoded = rsa.encode_int(5, public_key)
    print('Encoded: ', encoded)
    decoded = rsa.decode_int(encoded, private_key)
    print('Decoded: ', decoded)


if __name__ == "__main__":
    main()
