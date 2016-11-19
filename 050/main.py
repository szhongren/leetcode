"""
Implement pow(x, n).
"""

import sys
sys.setrecursionlimit(1000000)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        recur = self.myPow(x, n // 2)
        if n % 2 == 0:
            return recur * recur
        else:
            return x * recur * recur

ans = Solution()
print(ans.myPow(8.88023, 3))