import sys
import unittest

class TestPython(unittest.TestCase):

    def test_version(self):
        self.assertGreaterEqual(
            sys.hexversion, 0x030400F0, "Python 3.4-3.6 is required")
        self.assertLess(
            sys.hexversion, 0x030700F0, "Python 3.4-3.6 is required")
