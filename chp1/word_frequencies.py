from sets import ImmutableSet
import re

NON_WORDS = ImmutableSet(["the", "and", "of", "to", "a", "i",
                         "it", "in", "or", "is", "as", "so", "but"])


def word_freq(words):
    freq = {}

    def lower_f(x): return x.lower()

    def populate_freq(w): freq[w] = freq.get(w, 0) + 1

    map(populate_freq, filter(lambda w: w not in NON_WORDS,
                                map(lower_f, re.findall('\w+', words))))
    return freq
