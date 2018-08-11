import sys
import unittest

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

REQUIRED_PKGS = [
    "numpy",
    "pandas",
    "scipy",
    "sklearn.metrics",
    "statsmodels.tsa.statespace",
    "keras.layers",
    "sklearn",
    "keras",
]


class TestPackages(unittest.TestCase):

    def test_installed(self):
        for pkg in REQUIRED_PKGS:
            status = 'UNKN'
            try:
                __import__(pkg)
                status = 'SUCC'
            except ImportError:
                status = 'IERR'

            self.assertEqual(
                status, 'SUCC', 'Package {} is not installed'.format(pkg))

    def test_matplotlib(self):
        try:
            matplotlib = __import__('matplotlib')
            matplotlib.use('PS')
            plt = True
        except ImportError:
            plt = False

        self.assertTrue(plt, 'Package matplotlib is not installed')

        try:
            __import__('fbprophet')
            fbp = True
        except ImportError:
            fbp = False

        self.assertTrue(plt, 'Package fbprophet is not installed')
