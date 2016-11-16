"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = {}
        for v in nums:
            if counts.__contains__(v):
                counts[v] += 1
            else:
                counts[v] = 1
        for (v, c) in counts.items():
            if c != 1:
                return True
        return False