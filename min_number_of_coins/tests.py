from min_number_of_coins.solution import minNumberOfCoinsForChange
import unittest


class CoinsTests(unittest.TestCase):
    def test_basic(self):
        answer = minNumberOfCoinsForChange(10, [1, 3, 4])
        self.assertEqual(answer, 3)


if __name__ == '__main__':
    unittest.main()