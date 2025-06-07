from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        approach
        go through the array and mark values as present
        go through from 0 to max and return first value that's not existing
        if all existing, return max + 1
        """
        present = set(nums)
        max_val = max(nums)
        if max_val <= 0:
            return 1
        for i in range(1, max_val):
            if i not in present:
                return i
        return max_val + 1
