from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        approach
        dp
        start with [False] * n
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for i in range(1, i + nums[i])
                    dp[i] = True
        return dp[-1]
        edge cases:
        0 -> impossible
        1 -> return True
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, min(n, i + nums[i] + 1)):
                    dp[j] = True
        return dp[-1]
