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
        n = len(nums)
        if n == 0:
            return [[]]
        elif n == 1:
            return [[nums[0]]]
        else:
            prev = self.permute(nums[1:])
            for i in range(n - 1):
                prev.extend(self.permute(nums[1:]))
            prev.sort()
            prev_len = len(prev[0]) + 1
            for i in range(len(prev)):
                prev[i].insert(i % prev_len, nums[0])
            return prev

ans = Solution()
for v in ans.permute([1, 2, 3, 4]):
    print(v)