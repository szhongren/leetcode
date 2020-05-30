"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        max = nums[0]
        for i in range(l):
            if max >= l - 1:
                return True
            elif max <= i and nums[i] == 0:
                return False
            elif i + nums[i] > max:
                max = i + nums[i]
        return False

ans = Solution()
print(ans.canJump([2, 3, 1, 1, 4]))
print(ans.canJump([3, 2, 1, 0, 4]))
print(ans.canJump([2,5,0,0]))