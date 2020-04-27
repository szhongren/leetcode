"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        if target in nums:
            return True
        if max(nums) > target:
            return False
        number_vals = len(nums)
        dp = [[0 for _ in range(number_vals + 1)] for _ in range(target + 1)]

        for i in range(target + 1):
            dp[i][0] = 0
        for j in range(number_vals + 1):
            dp[0][j] = 1

        # for pos in range(1, number_vals + 1):
        #     for total in range(1, target + 1):
        print(dp)

        return dp[-1][-1]

ans = Solution()
print(ans.canPartition([1, 5, 11, 5]))
print()
print(ans.canPartition([1, 2, 3, 5]))
print()
print(ans.canPartition([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 97, 95]))
print()
print(ans.canPartition([3, 3, 3, 4, 5]))
