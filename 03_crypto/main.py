"""The main file for the project"""

from ciphers.affine import Affine
from ciphers.caesar import Caesar
from ciphers.multiplication import Multiplication
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

if __name__ == "__main__":
    main()
