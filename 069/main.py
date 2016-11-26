"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        else:
            start = 0:

ans = Solution()
for i in range(10):
    print(ans.mySqrt(i))