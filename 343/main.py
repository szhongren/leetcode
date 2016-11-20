"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Hint:

There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            result = 1
            for i in range(n // 3 - 1):
                result *= 3
            if n % 3 == 0:
                return result * 3
            elif n % 3 == 1:
                return result * 4
            elif n % 3 == 2:
                return result * 3 * 2

ans = Solution()
for i in range(20):
    print(i, ans.integerBreak(i))

"""
0 -> 0
1 -> 0
2 -> 1 * 1          = 1
3 -> 2 * 1          = 2
4 -> 2 * 2          = 4
5 -> 3 * 2          = 6
6 -> 3 * 3          = 9
7 -> 3 * 4          = 12
8 -> 3 * 3 * 2      = 18
9 -> 3 * 3 * 3      = 27
10 -> 3 * 3 * 4     = 36
11 -> 3 * 3 * 3 * 2 = 54
12
13
"""