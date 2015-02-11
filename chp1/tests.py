import unittest
from word_frequencies import word_freq
from first_index_of_any import first_index_of


class TestWordFreq(unittest.TestCase):

    def test_word_freq(self):
        count = word_freq("The quick red fox jumped the brown lazy dog." +
                            "Good fox!")
        self.assertTrue(len(count) > 0)
        self.assertEquals(1, count['red'])
        self.assertTrue('the' not in count)
        self.assertEquals(2, count['fox'])

class TestIndexOfAny(unittest.TestCase):

    def test_first_index_of(self):
        self.assertEqual(4,first_index_of("ala kazam","km"))
        self.assertIsNone(first_index_of("no la kazam","j"))



if __name__ == '__main__':
    unittest.main()
