from longest_peak.solution import longestPeak
import unittest


class LongestPeakTests(unittest.TestCase):
    def test_longest_peak2(self):
        peak = longestPeak([1, 3, 2])

        self.assertEqual(peak, 3)

    def test_longest_peak3(self):
        peak = longestPeak([1, 2, 3, 4, 5, 1])

        self.assertEqual(peak, 6)

    def test_longest_peak4(self):
        peak = longestPeak([5, 4, 3, 2, 1, 2, 1])

        self.assertEqual(peak, 3)

    def test_longest_peak5(self):
        peak = longestPeak([1, 1, 3, 2, 1])

        self.assertEqual(peak, 4)

    def test_longest_peak(self):
        peak = longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])

        self.assertEqual(peak, 6)


if __name__ == "__main__":
    unittest.main()
