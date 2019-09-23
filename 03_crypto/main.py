"""The main file for the project"""

from ciphers.affine import Affine
from ciphers.caesar import Caesar
from ciphers.multiplication import Multiplication
from ciphers.rsa import RSA
from ciphers.unbreakable import Unbreakable
from persons.hacker import Hacker
from persons.receiver import Receiver
from persons.sender import Sender


def main():
    """Main function to be run"""

    test_ciphers()

    text = 'ENCODED'
    key = 3
    caesar = Caesar()

    sender = Sender(key, caesar)
    receiver = Receiver(key, caesar)
    encoded = sender.operate_cipher(text)
    receiver.operate_cipher(encoded)
    hacker = Hacker(caesar.possible_keys(), caesar)
    hacker.operate_cipher(encoded)
    print()

    multiplication = Multiplication()
    sender.set_cipher_algorithm(multiplication)
    receiver.set_cipher_algorithm(multiplication)
    encoded = sender.operate_cipher(text)
    receiver.operate_cipher(encoded)
    hacker.set_cipher_algorithm(multiplication)
    hacker.operate_cipher(encoded)
    print()

    affine = Affine()
    sender.set_cipher_algorithm(affine)
    receiver.set_cipher_algorithm(affine)
    key = (3, 3)
    sender.set_cipher_key(key)
    receiver.set_cipher_key(key)
    encoded = sender.operate_cipher(text)
    receiver.operate_cipher(encoded)
    hacker.set_cipher_key(affine.possible_keys())
    hacker.set_cipher_algorithm(affine)
    hacker.operate_cipher(encoded)
    print()

    unbreakable = Unbreakable()
    key = 'ABIDE'
    sender.set_cipher_algorithm(unbreakable)
    receiver.set_cipher_algorithm(unbreakable)
    sender.set_cipher_key(key)
    receiver.set_cipher_key(key)
    encoded = sender.operate_cipher(text)
    receiver.operate_cipher(encoded)
    hacker.set_cipher_algorithm(unbreakable)
    #hacker.set_cipher_key(unbreakable.possible_keys())
    #hacker.operate_cipher(encoded)
    hacker.crack_unbreakable(encoded)


def test_ciphers():
    """Runs verify of ciphers"""
    text = 'ENCODED'
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
    rsa.verify(text, (public_key, private_key))


if __name__ == "__main__":
    main()
