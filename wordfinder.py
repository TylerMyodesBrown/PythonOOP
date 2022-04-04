"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self,a) -> None:
        self.a = a

    def __repr__(self) -> str:
        return f'Return Random line from {self.a}'

    def random(self):
        lines = open(self.a).read().splitlines()
        myline =random.choice(lines)
        print(myline)


class RandomWordFinder(WordFinder):
    def __init__(self, a) -> None:
        super().__init__(a)


    def rand_word(self):
        lines = open(self.a).read().split()
        myline =random.choice(lines)
        print(myline)