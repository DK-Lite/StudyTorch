import os, sys
import collections

class Voacabulary():
    def __init__(self):
        self._voca = []
        pass
    
    def update(self):
        pass
    
    @property
    def data(self):
        return self._voca

    @data.setter
    def data(self, data):
        self._voca = data


class BytePairEncoding():
    
    def __init__(self):
        pass

    def get_state(self, dictionary: dict):
        pairs = collections.defaultdict(int)

        for word, freq in dictionary.items():
            symbols = word.split()
            for i in range(len(symbols)-1):
                pairs[symbols[i], symbols[i+1]] += freq

        return pairs

    def __call__(self, *arg, **kwargs) -> dict:
        return bpe


def main():
    iteration
    dict = BytePairEncoding(dict, iter=10)

if __name__ == "__main__":
    main()