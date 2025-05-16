from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        approach
        prefix sum and suffix sum, keep running track
        then, iterate i
        if valid, result += 1
        """
        prefix_sum = 0
        suffix_sum = sum(nums)
        result = 0
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            suffix_sum -= nums[i]
            if prefix_sum >= suffix_sum:
                result += 1
        return result
