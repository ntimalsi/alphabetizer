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

    def test_special(self):
        string = "Py%%&*thon12Tech"
        result = alphabetizer.alphabetizer(string)
        self.assertEqual(result, "cehhnoPtTy")

    def test_empty(self):
        string = "             "
        result = alphabetizer.alphabetizer(string)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()