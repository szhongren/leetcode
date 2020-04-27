"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = 0
        p2 = len(nums)
        while p1 != p2:
            if nums[p1] == val:
                p2 -= 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
            else:
                p1 += 1
        return p2

ans = Solution()
print(ans.removeElement([3, 2, 2, 3], 3))