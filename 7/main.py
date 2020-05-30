"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        out = 0
        for i, v in enumerate(digits):
            out += pow(10, (len(digits) - i - 1)) * v
        if out > 2147483647:
            return 0
        return out


ans = Solution()
print(ans.reverse(123))
print(ans.reverse(-321))