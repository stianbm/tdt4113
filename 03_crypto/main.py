"""The main file for the project"""

from ciphers.affine import Affine
from ciphers.caesar import Caesar
from ciphers.multiplication import Multiplication


def main():
    """Main function to be run"""
    text = 'PYTHON'
    key = 15
    caesar = Caesar()
    caesar.verify(text, key)

    multiplication = Multiplication()
    key1 = multiplication.generate_keys()
    multiplication.verify(text, key1)

    affine = Affine()
    key2 = (multiplication.generate_keys(), 5)
    print('Key: ', key2)
    affine.verify(text, key2)


if __name__ == "__main__":
    main()
