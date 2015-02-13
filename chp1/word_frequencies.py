import re

NON_WORDS = set(["the", "and", "of", "to", "a", "i",
                         "it", "in", "or", "is", "as", "so", "but"])


class FunList(object):

    def __init__(self, it):
        self.iter = it

    def __iter__(self):
        for x in self.iter:
            yield x

    def filter(self, f):
        return FunList(filter(f, self))

    def map(self, f):
        return FunList(map(f, self))

    def iterate(self, f):
        for k in self:
            f(k)

    def __str__(self):
        return str(list(self))


def word_freq(words):
    freq = {}

    def lower_f(x): return x.lower()

    def populate_freq(w): freq[w] = freq.get(w, 0) + 1

    # this is what you would do with std func only
    # map(populate_freq, filter(lambda w: w not in NON_WORDS,
    #                            map(lower_f, re.findall('\w+', words))))

    # this is a tail style functional version
    FunList(re.findall('\w+', words)).map(lower_f).filter(lambda w: w not in NON_WORDS).iterate(populate_freq)

    return freq
