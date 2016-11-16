"""
Given an array of integers, every element appears twice except for one. Find that single one.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for v in nums:
            result ^= v
        return result

ans = Solution()
print(ans.singleNumber([1, 3, 2, 2, 8, 9, 1, 3, 9]))