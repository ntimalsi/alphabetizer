import unittest
import alphabetizer

class TestAlphabetizer(unittest.TestCase):
    def test_string(self):
        string = "VirginiaTech"
        result = alphabetizer.alphabetizer(string)
        self.assertEqual(result, "aceghiiinrTV")

    def test_nonalpha(self):
        string = "3 Blind Mice"
        result = alphabetizer.alphabetizer(string)
        self.assertEqual(result, "BcdeiilMn")


if __name__ == '__main__':
    unittest.main()