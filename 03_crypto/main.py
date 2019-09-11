"""The main file for the project"""

from ciphers.caesar import Caesar
from ciphers.multiplication import Multiplication


def main():
    """Main function to be run"""
    text = 'PYTHON'
    key = 15
    caesar = Caesar()
    caesar.verify(text, key)

    multiplication = Multiplication()
    key = multiplication.generate_keys()
    multiplication.verify(text, key)



if __name__ == "__main__":
    main()
