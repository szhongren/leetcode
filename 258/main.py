"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        digit_sum = 0
        while num > 9:
            while num > 0:
                digit_sum += num % 10
                num //= 10
            num = digit_sum
            digit_sum = 0
        return num

ans = Solution()
print(ans.addDigits(38))