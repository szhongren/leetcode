"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = [n + 1] * (n + 1)
        limit = int(math.sqrt(n)) + 1
        squares = [i * i for i in range(limit)]
        for i in range(len(results)):
            if i in squares:
                results[i] = 1
            else:
                for sq in squares:
                    if sq < i:
                        results[i] = min(results[i], 1 + results[i - sq])
                    else:
                        break
        return results[-1]

ans = Solution()
print(ans.numSquares(12))
print(ans.numSquares(4128))