"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        power = 0
        while len(s) != 0:
            ch = s[-1]
            result += (ord(ch) - 64) * pow(26, power)
            power += 1
            s = s[:-1]
        return result

ans = Solution()
print(ans.titleToNumber("AA"))
print(ans.titleToNumber("D"))