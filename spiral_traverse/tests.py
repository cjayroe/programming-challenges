import unittest
from .solution import spiral_traverse

class SpiralTraverseTests(unittest.TestCase):
    def test_spiral_traverse1(self):
        spiral = spiral_traverse([
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ])

        self.assertEqual(spiral, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    
    def test_spiral_traverse2(self):
        spiral = spiral_traverse([
            [1]
        ])

        self.assertEqual(spiral, [1])


if __name__ == '__main__':
    unittest.main()