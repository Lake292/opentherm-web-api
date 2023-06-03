import unittest

from opentherm_web_api.opentherm_controller import OpenThermController


class TestSimple(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()