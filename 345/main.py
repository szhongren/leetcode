"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = -1
        end = len(s)
        vowels = "aeiouAEIOU"
        ls = list(s)
        while True:
            start += 1
            if start >= end:
                    break
            if ls[start] in vowels:
                while True:
                    end -= 1
                    if ls[end] in vowels:
                        ls[start], ls[end] = ls[end], ls[start]
                        break
        return ''.join(ls)


ans = Solution()
print(ans.reverseVowels("hello"))
print(ans.reverseVowels("leetcode"))