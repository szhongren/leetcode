"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.
"""


class Solution(object):
    def twoSum(self, nums, target):
        found = {}
        res = []
        for (i, v) in enumerate(nums):
            if target - v in found:
                res.append(found[target - v])
                res.append(i)
                break
            else:
                found[v] = i
        return res

ans = Solution()
print(ans.twoSum([2, 7, 11, 15], 9))
