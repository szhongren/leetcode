"""
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).
"""

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = sum(A)
        l = len(A)
        curr_sum = 0
        max_sum = 0
        for (i, v) in enumerate(A):
            curr_sum += i * v
        max_sum = curr_sum
        for i in range(l):
            curr_sum += total - l * A[l - i - 1]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum




ans = Solution()
print(ans.maxRotateFunction([4, 3, 2, 6]))