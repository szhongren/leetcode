"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        if target > nums[-1]:
            return end
        while start < end:
            mid = (end + start) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] >= target:
                end = mid
        return end

ans = Solution()
print(ans.searchInsert([1,3,5,6], 5))
print(ans.searchInsert([1,3,5,6], 2))
print(ans.searchInsert([1,3,5,6], 7))
print(ans.searchInsert([1,3,5,6], 0))