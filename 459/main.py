"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
"""
import sys
sys.setrecursionlimit(1000000)
class Solution(object):
    def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1

ans = Solution()
print(ans.repeatedSubstringPattern("abababab"))
print(ans.repeatedSubstringPattern("abcabcabcabc"))
print(ans.repeatedSubstringPattern("aba"))