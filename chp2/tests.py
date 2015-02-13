import unittest
from .company_names import clean_names

class TestCleanNames(unittest.TestCase):

    def test_clean(self):
        names = clean_names(['john','s','calvin'])
        self.assertEqual("John,Calvin",names)
