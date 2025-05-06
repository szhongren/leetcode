from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        look at midpoint
        if target == midpoint, return
        elif target < midpoint, search 0:midpoint
        elif target > midpoint, search midpoint:end
        edge cases:
        []
        ------
        [1]
        start, end = 0, 1
        mid = 0
        loop with exclusive end
        """
        start, end = 0, len(nums)
        while start < end:
            midpoint = (start + end) // 2
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] > target:
                end = midpoint
            elif nums[midpoint] < target:
                start = midpoint + 1
        return -1
