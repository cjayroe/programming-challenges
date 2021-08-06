import unittest
from .solution import three_sum


class ThreeSumTests(unittest.TestCase):
    def test_basic(self):
        answer = three_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
        self.assertEqual(answer, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])


if __name__ == "__main__":
    unittest.main()
