"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

def isPalindrome(str):
    l = len(str)
    if l % 2 == 0:
        return reversed(str[:l // 2]) == str[l // 2:]
    else:
        return reversed(str[:l // 2]) == str[l // 2 + 1:]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        else:
            res = []
            res.append(list(s))
            return res

ans = Solution()
print(ans.partition("aab"))