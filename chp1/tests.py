import unittest
from word_frequencies import word_freq


class TestWordFreq(unittest.TestCase):

    def test_word_freq(self):
        count = word_freq("The quick red fox jumped the brown lazy dog." +
                            "Good fox!")
        self.assertTrue(len(count) > 0)
        self.assertEquals(1, count['red'])
        self.assertTrue('the' not in count)
        self.assertEquals(2, count['fox'])

if __name__ == '__main__':
    unittest.main()
