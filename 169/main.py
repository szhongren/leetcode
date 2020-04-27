"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = (0, 0)
        counts = {}
        for v in nums:
            if counts.__contains__(v):
                counts[v] += 1
            else:
                counts[v] = 1
            if counts[v] > curr_max[1]:
                curr_max = (v, counts[v])
        return curr_max[0]
