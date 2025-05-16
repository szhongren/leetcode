from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        approach
        if len <= 2:
        return true
        while a == b:
        continue
        check to see if next pair holds the same direction as before
        """
        n = len(nums)
        if n <= 2:
            return True
        i = 0
        direction = None
        while i < n - 2:
            if nums[i] == nums[i + 1]:
                i += 1
                continue
            if nums[i] <= nums[i + 1]:
                if direction is None:
                    direction = 1
                if direction != 1:
                    return False
            if nums[i] >= nums[i + 1]:
                if direction is None:
                    direction = -1
                if direction != -1:
                    return False
            i += 1
        return True
