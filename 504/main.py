"""
Given an integer, return its base 7 string representation.

Example 1:

Input: 100
Output: "202"

Example 2:

Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        res = ""
        if num < 0:
            return "-" + self.convertToBase7(-num)
        while num > 0:
            res = str(num % 7) + res
            num //= 7
        return res


ans = Solution()
print(ans.convertToBase7(100))
print(ans.convertToBase7(-7))
