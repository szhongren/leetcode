"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        else:
            prev = self.permute(nums[1:])
            new = prev + list(map(lambda x: x + [nums[0]], prev))
            return new

ans = Solution()
print(ans.permute([1, 2, 3]))