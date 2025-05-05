from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        binary search
        look for value, if not found, return +1 or -1

        edge cases:
        [] -> not possible
        [1] -> 0 if < 1, 1 if > 1, 0/1 if == 1
        [1, 3], 2 ->
        """
        start, end = 0, len(nums) - 1  # inclusive
        while start <= end:
            midpoint = (start + end) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                start = midpoint + 1
                if start > end:
                    return start
            elif nums[midpoint] > target:
                end = midpoint - 1
                if start > end:
                    return start
