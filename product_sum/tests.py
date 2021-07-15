import unittest
from .solution import productSum

class ProductSumTests(unittest.TestCase):
    def test_basic(self):
        results = productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
        self.assertEqual(12, results)


if __name__ == '__main__':
    unittest.main()
