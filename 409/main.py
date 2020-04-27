"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for ch in s:
            if counts.__contains__(ch):
                counts[ch] += 1
            else:
                counts[ch] = 1
        found_odd = 0
        result = 0
        for (ch, c) in counts.items():
            result += (c // 2) * 2
            if c % 2 == 1:
                found_odd = 1
        return result + found_odd



ans = Solution()
print(ans.longestPalindrome("abccccdd"))