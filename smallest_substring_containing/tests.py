from smallest_substring_containing.solution import smallestSubstringContaining
import unittest


class SmallestsSubstringSolutionTest(unittest.TestCase):
    def test_basic(self):
        smallest_substring = smallestSubstringContaining("1456243561288281932363365412356789901!", "123!")
        self.assertEqual(smallest_substring, '2356789901!')

    def test_basic1(self):
        smallest_substring = smallestSubstringContaining("abcd$ef$axb$c$", "$$abf")
        self.assertEqual(smallest_substring, 'f$axb$')

if __name__ == '__main__':
    unittest.main()