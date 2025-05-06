from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        approach
        DP
        for each position, for each position I can reach starting with the last
        if position == end, return true

        edge cases:
        [] -> not possible
        [1] -> True
        [0] -> True
        [0, 1] -> False
        """
        n = len(nums)
        can_reach = [False] * n
        can_reach[0] = True
        for i in range(n):
            if not can_reach[i]:
                continue
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                can_reach[j] = True
        return can_reach[-1]
