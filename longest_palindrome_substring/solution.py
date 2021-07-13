def longestPalindromicSubstring(string):
    palindrome = ''

    for index, letter in enumerate(string):
        odd_palindrome = find_palindrome(string, index, index)
        even_palindrome = find_palindrome(string, index, index + 1)

        if len(odd_palindrome) > len(palindrome):
            palindrome = odd_palindrome

        if len(even_palindrome) > len(palindrome):
            palindrome = even_palindrome
	
    return palindrome

def find_palindrome(string, left, right):
    palindrome = ''

    if right > len(string) - 1:
        return palindrome

    while string[left] == string[right]:
        palindrome = string[left:right+1]
        
        left -= 1
        right += 1
        
        if left < 0 or right > len(string) - 1:
            break
            
    return palindrome
		


if __name__ == '__main__':
    longestPalindromicSubstring("abaxyzzyxf")