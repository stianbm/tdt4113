"""File contains hacker"""

from persons.person import Person


class Hacker(Person):
    """Brute force hacker"""

    def __init__(self, cipher_key, cipher_algorithm):
        super().__init__(cipher_key, cipher_algorithm)
        self.type = 'hacker'

    def operate_cipher(self, text):
        """Brute force the encryption"""
        for key in self._cipher_key:
            decoded_text = self._cipher_algorithm.decode(text, key)
            words = str(decoded_text).split()
            if self.checks_out(words):
                print('Hacker found: ', words)
                return
        print('Hacker failed')
        return

    @staticmethod
    def checks_out(words):
        """Checks if words are in the word list"""
        found = False
        with open('english_words.txt') as file:
            for word in words:
                if word.lower() not in file.read():
                    found = False
                    break
                else:
                    found = True
        if found:
            return True
        return False

    def crack_unbreakable(self, text):
        with open('english_words.txt') as file:
            for key in file:
                key = key.strip()
                if not key:
                    continue
                decoded_text = self._cipher_algorithm.decode(text, key.upper())
                words = str(decoded_text).split()
                if self.checks_out(words):
                    print('Hacker found: ', words)
                    return
            print('Hacker failed')
            return
