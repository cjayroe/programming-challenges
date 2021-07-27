import unittest
from .solution import run_length_encocding


class RunLengthEncodingTests(unittest.TestCase):
    def test_basic(self):
        answer = run_length_encocding('AAAAAAAAAAAAABBCCCCDD')
        self.assertEqual(answer, '9A4A2B4C2D')


if __name__ == "__main__":
    unittest.main()
