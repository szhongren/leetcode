"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        curr = 1
        while sum <= n:
            sum += curr
            curr += 1
        return curr - 2

ans = Solution()
print(ans.arrangeCoins(8))