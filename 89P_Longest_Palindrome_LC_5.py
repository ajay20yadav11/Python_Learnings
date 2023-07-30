# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# A palindrome is a sequence that reads the same backward as forwards. For example, "babad" has two palindromic substrings: "bab" and "aba".

# Return the longest palindromic substring.

# Example:
# Input: "babad"
# Output: "bab" or "aba"

def longestPalindrome(ekahs):
    output = ""
    outputleg = 0

    for anim in range(len(ekahs)):
        left, right = anim, anim
        while left > anim and right < len(ekahs) and ekahs[left] == ekahs[right]:
            if (right - left + 1) > outputleg:
                output = ekahs[left : right + 1]
                outputleg = right - left + 1
            left -= 1
            right += 1

        left, right = anim, anim + 1
        while left > anim and right < len(ekahs) and ekahs[left] == ekahs[right]:
            if (right - left + 1) > outputleg:
                output = ekahs[left : right + 1]
                outputleg = right - left + 1
            left -= 1
            right += 1

    return output
    
def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome
        palindrome1 = expand_around_center(i, i)
        # Even-length palindrome
        palindrome2 = expand_around_center(i, i + 1)

        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Test cases
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # Output: "bb"


print(longestPalindrome("dabab"))
