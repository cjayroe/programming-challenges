import unittest
from .solution import non_change


class NonConstructibleChangeTests(unittest.TestCase):
    def test_basic(self):
        answer = non_change([5, 7, 1, 1, 2, 3, 22])
        self.assertEqual(20, 20)


if __name__ == "__main__":
    unittest.main()
