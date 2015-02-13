import unittest
from .company_names import clean_names, clean_names_in_parallel


class TestCleanNames(unittest.TestCase):

    def test_clean(self):
        names = clean_names(['john', 's', 'calvin'])
        self.assertEqual("John,Calvin", names)

    def test_parallel_execution(self):
        names = clean_names_in_parallel(['john', 's', 'calvin'])
        self.assertEqual("John,Calvin", names)
