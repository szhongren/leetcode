"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

def recur_sum(nums, target, count):
    """
    :type nums: List[int]
    :type target: int
    :type count: int
    :rtype: List[List[int]]
    """
    for i in range(count, 0, -1):
        print(i)


ans = Solution()
ans.fourSum([1, 0, -1, 0, -2, 2], 0)
res = recur_sum([1, 0, -1, 0, -2, 2], 0, 1)
pass
