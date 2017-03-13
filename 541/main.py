"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:

    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        if length <= k:
            return s[::-1]
        if length <= 2 * k:
            return s[:k][::-1] + s[k:]
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k)

ans = Solution()
print(ans.reverseStr("abcdefg", 1))
