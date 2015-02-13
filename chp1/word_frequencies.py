import re
from commons.structures import FunList

NON_WORDS = set(["the", "and", "of", "to", "a", "i",
                         "it", "in", "or", "is", "as", "so", "but"])


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
