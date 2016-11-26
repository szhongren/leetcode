"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.l = len(nums)
        if self.l == 1:
            return 0
        elif self.l == 2:
            return nums.index(max(nums))
        else:
            return self.findPeakHelper(nums, 0, self.l)

    def findPeakHelper(self, nums, start, end):
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: int
        """
        if end - start <= 1 or start == self.l - 1:
            return start
        mid = (start + end) // 2
        if mid == 0 and nums[mid + 1] < nums[mid]:
            return mid
        elif mid == self.l - 1 and nums[mid - 1] < nums[mid]:
            return mid
        elif nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
            return mid
        elif nums[mid - 1] > nums[mid]:
            return self.findPeakHelper(nums, start, mid)
        elif nums[mid + 1] > nums[mid]:
            return self.findPeakHelper(nums, mid + 1, end)

ans = Solution()
print(ans.findPeakElement([1,2,3,4,3]))