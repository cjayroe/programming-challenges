from powerset.solution import powerset
import unittest


class PowersetTests(unittest.TestCase):
    def test_basic(self):
        answer = powerset([1, 2, 3])

        self.assertEqual(len(answer), len([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))



if __name__ == '__main__':
    unittest.main()