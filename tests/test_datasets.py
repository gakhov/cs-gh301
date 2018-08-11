import os.path
import unittest

REQUIRED_DATASETS = [
    "alcoholic-drinks.csv",
    "avg-ukraine-EUR-cash.csv",
    "international-airline-passengers.csv",
    "monthly-reported-number-of-cases.csv",
    "os-visits-uk.csv",
    "visits-abroad-uk.csv",
    "wikipedia-en-timeseries-desktop.json",
    "wikipedia-en-homepage-desktop.json",
]

class TestDatasets(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dir = os.path.join(
            os.getcwd(),
            'cs-gh301',
            'data'
        )

    def test_files(self):
        for ds in REQUIRED_DATASETS:
            status = 'UNKN'
            if os.path.isfile(os.path.join(self.data_dir, ds)):
                status = 'SUCC'
            else:
                status = 'MISS'

            self.assertEqual(
                status, 'SUCC', 'Dataset {} is missing'.format(ds))
