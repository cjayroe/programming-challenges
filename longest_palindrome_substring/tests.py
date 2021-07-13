from longest_palindrome_substring.solution import longestPalindromicSubstring
import unittest

class LongestPalindromeSubstringTest(unittest.TestCase):
    def test_basic(self):
        palindrome = longestPalindromicSubstring("abaxyzzyxf")

        self.assertEqual(palindrome, 'xyzzyx')


if __name__ == '__main__':
    unittest.main()