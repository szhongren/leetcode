"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""
import math

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # next_pow = 1
        # while next_pow <= n:
        #     next_pow *= 2
        # dp = [0] * (next_pow + 2)
        # dp[-1] = math.inf
        # for i in range(2, len(dp) - 1):
        #     base = i
        #     while True:
        #         if base > next_pow:
        #             break
        #         elif base % 2 == 0:
        #             if base // 2 != 1 and base // 2 % 2 != 0:
        #                 dp[base // 2] = 1 + min(dp[base // 2 - 1], dp[base // 2 + 1])
        #             dp[base] = 1 + dp[base // 2]
        #         base *= 2
        #     if dp[i] == 0:
        #         dp[i] = 1 + min(dp[i - 1], dp[i + 1])
        # return dp[n]
        if n < 4:
            return [0, 0, 1, 2][n]
        else:
            test = n % 4
            if test == 0 or test == 2:
                return self.integerReplacement(n // 2) + 1
            elif test == 1:
                return self.integerReplacement((n - 1) // 4) + 3
            else:
                return self.integerReplacement((n + 1) // 4) + 3

ans = Solution()
# for i in range(17):
#     print(ans.integerReplacement(i))
print(ans.integerReplacement(10000000))