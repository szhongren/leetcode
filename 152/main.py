"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # l = len(nums)
        # dp = [[0 for _ in range(l)] for _ in range(l)]
        # max_val = -10000000
        # for i in range(l):
        #     for j in range(i, l):
        #         if i == 0:
        #             dp[i][j] = nums[j]
        #         else:
        #             dp[i][j] = dp[i-1][j-1] * nums[j]
        #         max_val = max(max_val, dp[i][j])
        # return max_val
        # above is O(n^2), below is O(n)
        l = len(nums)
        maxp = [0 for _ in range(l)]
        minp = [0 for _ in range(l)]

        maxp[0] = nums[0]
        minp[0] = nums[0]
        result = nums[0]

        for i in range(1, l):
            if nums[i] > 0:
                maxp[i] = max(nums[i], maxp[i-1] * nums[i])
                minp[i] = min(nums[i], minp[i-1] * nums[i])
            else:
                maxp[i] = max(nums[i], minp[i-1] * nums[i])
                minp[i] = min(nums[i], maxp[i-1] * nums[i])

            result = max(result, maxp[i])

        return result

ans = Solution()
print(ans.maxProduct([2, 3, -2, 4]))