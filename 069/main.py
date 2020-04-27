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
        root = 0
        while root * root <= x:
            root += 1
        return root - 1

    def mySqrtRecur(self, x, lo, hi):
        if lo * lo == x:
            return lo
        elif hi * hi == x:
            return hi
        else:
            if
        # else:
        #     root = 1
        #     while abs(root * root - x) > 0.000001:
        #         root = (root + x/root)/2
        #     return root

ans = Solution()

for i in range(20):
    print(i, ans.mySqrt(i))
