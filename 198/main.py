from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        approach
        dp
        each point is the max we can get up to that house
        for each house, we can have 2 cases, either we rob it or not
        if we rob it, our max is curr + dp[i - 2]
        if we don't rob it, our max is curr + dp[i - 1]
        return dp[-1]
        """
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-3]
