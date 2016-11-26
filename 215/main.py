"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.l = len(nums)

        return self.partition(nums, self.l - k, 0, self.l)

    def partition(self, nums, target, start, end):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :type end: int
        """
        if start == target:
            return nums[start]
        elif target + 1 == end:
            return nums[end - 1]
        pivot = nums[end - 1]
        pass

ans = Solution()
print(ans.findKthLargest([3, 2, 1, 5, 6, 4], 2))