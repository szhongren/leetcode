"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 0101
        # 1111
        while b != 0:
            c = a & b
            a = (a ^ b)
            b = c << 1
        return a # does not work for negative numbers in python because of the variable size of the int


ans = Solution()
print(ans.getSum(-1, 1))
print(ans.getSum(5, 15))