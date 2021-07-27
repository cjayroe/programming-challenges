import unittest
from .solution import two_sum

class TwoSumTest(unittest.TestCase):
    def test_basic(self):
        answer = two_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertEqual(answer, [-1, 11])

if __name__ == '__main__':
    unittest.main()