"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

def fact(n):
    results = [i for i in range(n + 1)]
    results[0] = 1
    for i in range(1, n + 1):
        results[i] *= results[i - 1]
    return results[-1]

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr_pow_5 = 5
        result = 0
        while curr_pow_5 <= n:
            result += (n // curr_pow_5)
            curr_pow_5 *= 5
        return result

ans = Solution()
for i in range(40, 60):
    print(i ,fact(i))
    print(ans.trailingZeroes(i))