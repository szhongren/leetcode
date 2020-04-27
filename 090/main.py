"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        else:
            prev = self.subsetsWithDup(nums[1:])
            new = prev + list(map(lambda x: sorted(x), list(map(lambda x: x + [nums[0]], prev))))
            seen = []
            res = []
            for l in new:
                if l not in seen:
                    res.append(l)
                    seen.append(l)
            return res

ans =  Solution()
print(ans.subsetsWithDup([4,4,4,1,4]))
print(ans.subsetsWithDup([1,2,2]))